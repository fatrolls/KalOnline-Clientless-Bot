import sys
import socket
import time
import threading
import struct
import random
import logging
import math
import ast
from .network import Network, unpack, decompile
from .network_enum import C2S, S2C
from .player_enum import SkillID, SkillTIME, SkillMP, SkillCD, ClassID, SkillUSE, PimpTYPE
from .misc import RandomString, Rectangle, GetValueFromKey


class Client():
    """This class 
    """
    MAX_ENTITYS = 500
    END_HASH = 0x1c99

    def __init__(self, clientSocket, clientAddress):
        self.nearPlayers = [Entity() for _ in range(self.MAX_ENTITYS)] # Entitys
        self.countNearPlayers = 0
        self.chatEnabled = True
        self.id = 0
        self.enabledTeleport = False  # when disabled(False), any teleportation packets are not forwarded to the game server

        self.clientConnected = True  

        # game client
        self.gameClientSocket = clientSocket
        self.gameClientSocket.setblocking(0)
        self.gameClientAddress = clientAddress
        self.gameClientNetwork = Network(clientSocket, clientAddress)
        # game server
        self.gameServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.gameServerAddress = ("51.77.57.38", 33332)  # violent
        self.gameServerNetwork = Network(self.gameServerSocket, self.gameServerAddress)
        try:
            self.gameServerSocket.connect(self.gameServerAddress)
            self.gameServerSocket.setblocking(0)
        except:
            print("Cannot establish connection to game server. program stopped.")
            sys.exit()

        threading.Thread(target=self.recv_gameclient).start()        
        threading.Thread(target=self.recv_gameserver).start()

        # chat name
        self.botname = "Zona"      


    def recv_gameclient(self):
        print("Started receiving from gameclient.")
        while True:            
            packet = self.gameClientNetwork.recv_packet()
            if packet is None:
                time.sleep(0.01)
            if packet != None:
                packetType = unpack(packet, 2, 'B')
                packetLength = unpack(packet, 0, 'H')
                # do something with packets being sent from the client
                if packetType == C2S.LOGIN:
                    accId, accPw, Mac = decompile(packet, "sss")                    
                    newMac = RandomString(0, 2) + "-" +  RandomString(0, 2) + "-" + RandomString(0, 2) + "-" + RandomString(0, 2) + "-" + RandomString(0, 2) + "-" + RandomString(0, 2)
                    print("oldMac=[%s]" % (Mac))
                    print("newMac=[%s]" % (newMac))
                    self.gameServerNetwork.send_packet(C2S.LOGIN, "sssH", [accId, accPw, newMac, self.END_HASH]) #old value 0x12d4
                    continue
                elif packetType == 0xfe:
                    if unpack(packet, 3, "H") == 0x09fb:
                        user_names = ["user", "User", "USER"]
                        os_names = ["Windows 7 Service Pack 1 x64", "Windows 7 Service Pack 1 x32", "Windows 7 Service Pack 2 x64", "Windows 7 Service Pack 2 x32", "Windows 10 x64", "Windows 10 x32"]

                        self.gameServerNetwork.send_packet(0xfe, "LBssssssssssH", 
                                             [0x09fb, 
                                              0x01,
                                              RandomString(1, 25), 
                                              "DESKTOP-" + RandomString(2,7), 
                                              user_names[random.randint(0,len(user_names)-1)], 
                                              os_names[random.randint(0,len(os_names)-1)],
                                              RandomString(1, 20), 
                                              RandomString(1, 32), 
                                              RandomString(0, 4) + "-" + RandomString(0, 4),
                                              "GenuntelineI",
                                              RandomString(0, 2) + ":" + RandomString(0, 2) + ":" + RandomString(0, 2) + ":" + RandomString(0, 2) + ":" + RandomString(0, 2) + ":" + RandomString(0, 2),
                                              "null",
                                              self.END_HASH], 
                                              init=False)
                        continue
                if packetType == C2S.CHAT:
                    message = decompile(packet, "s")
                    message = str(message).strip(chr(0x20))
                    print("chat=[%s]" % (message))
                    if message == "-help":
                        self.SendChatMessageToGameClient("Command List:")
                        self.SendChatMessageToGameClient("-speed <speedValue,int>")
                        self.SendChatMessageToGameClient("e.g. -speed 500")
                        self.SendChatMessageToGameClient("-fduel <playerName,string>")
                        self.SendChatMessageToGameClient("e.g. -fduel FixWithLeave")
                        self.SendChatMessageToGameClient("-fparty <playerName,string>")
                        self.SendChatMessageToGameClient("e.g. -fparty FixWithLeave")
                        self.SendChatMessageToGameClient("-teleport")
                        self.SendChatMessageToGameClient("-stop")
                        continue
                    elif message.startswith("-speed"):
                        command_args = message.split(' ')
                        if len(command_args) != 2:
                            self.SendChatMessageToGameClient("Invalid command. Type \"-help\" to get usage information")
                        else:
                            try:
                                speed = int(command_args[1])
                            except ValueError:
                                self.SendChatMessageToGameClient("ValueError in -speed")
                                continue
                            self.gameClientNetwork.send_packet(S2C.UPDATE_MPROPERTY, "LBH", [self.id, 32, speed])
                            continue
                    elif message.startswith("-fduel"):
                        command_args = message.split(' ')
                        if len(command_args) != 2:
                            self.SendChatMessageToGameClient("Invalid amount of arguments")
                        else:
                            player = self.GetNearPlayerFromName(command_args[1])
                            if player is not None:
                                self.gameServerNetwork.send_packet(0x1e, "BL", [0x01, player.id])
                                self.SendChatMessageToGameClient("Duel forced")
                        continue
                    elif message.startswith("-fparty"):
                        command_args = message.split(' ')
                        if len(command_args) != 2:
                            self.SendChatMessageToGameClient("Invalid amount of arguments")
                        else:
                            player = self.GetNearPlayerFromName(command_args[1])
                            if player is not None:
                                self.gameServerNetwork.send_packet(0x11, "BL", [0x01, player.id])
                                self.SendChatMessageToGameClient("Party forced")
                        continue
                    elif message == "-teleport":
                        if self.enabledTeleport:
                            self.enabledTeleport = False
                            self.SendChatMessageToGameClient("Teleport disabled")
                        else:
                            self.enabledTeleport = True
                            self.SendChatMessageToGameClient("Teleport enabled")
                        continue
                    elif message == "-stop":
                        self.clientConnected = False
                        self.gameClientNetwork.send_packet(0x1d, "B", [1])
                        self.gameClientNetwork.send_bytes(b'\x09\x00\x11\x00\x00\x00\x00\x00\x00')  # playerinfo packet
                    elif str(message).startswith("-"):  # even if chat is enabled dont allow messages starting with "-" to pass to server
                        self.SendChatMessageToGameClient("Message blocked! Startswith \"-\"")
                        continue
                elif packetType == C2S.TELEPORT_SEND_Z:
                    if not self.enabledTeleport:
                        continue                
                # forward the packet
                if self.clientConnected:
                    self.gameServerNetwork.send_bytes(packet)
                else:
                    return  # stop this thread


    def SendChatMessageToGameClient(self, text):
        """Sends a text message to the game self. 

        """
        self.gameClientNetwork.send_packet(S2C.CHAT, "ss", [self.botname, "*" + text])


    def recv_gameserver(self):
        print("Started receiving from gameserver.")
        while True:            
            packet = self.gameServerNetwork.recv_packet()    
            if packet is None:
                time.sleep(0.01)
            if packet != None:
                packetType = unpack(packet, 2, 'B')
                packetLength = unpack(packet, 0, 'H')
                # do something with packets being sent from game server                                 
                if packetType == S2C.MD5_PACKET:
                    indicator = unpack(packet, 3, 'B')
                    if indicator == 0xff:
                        continue  # this is indeed the md5 protection packet, dont forward         
                elif packetType == S2C.PLAYER_APPEAR:  # player_appear
                    player_id = unpack(packet, 3, 'L')
                    name_end = packet.find(0x00, 7)
                    player_name = packet[7:name_end].decode('utf-8')
                    player_class = unpack(packet, name_end + 1, 'B')
                    x = unpack(packet, name_end + 2, 'L')
                    y = unpack(packet, name_end + 6, 'L')
                    z = unpack(packet, name_end + 10, 'L')
                    print("R_PLAYER_APPEAR: id=%d, name=%s, class=%d, x=%d, y=%d, z=%d" %(player_id, player_name, player_class, x, y, z))     
                    for i in range(self.MAX_ENTITYS):
                        if self.nearPlayers[i].id == 0:
                            self.nearPlayers[i].id = player_id
                            self.nearPlayers[i].name = player_name
                            self.nearPlayers[i].x = x
                            self.nearPlayers[i].y = y
                            self.nearPlayers[i].z = z
                            self.countNearPlayers += 1
                            break
                    if player_class & 0x80 > 0:
                        self.id = player_id
                elif packetType == S2C.PLAYER_DISAPPEAR:  # player_disappear
                    player_id = unpack(packet, 3, 'L')
                    disappear_player_name = ""
                    for i in range(self.MAX_ENTITYS):
                        if self.nearPlayers[i].id == player_id:
                            disappear_player_name = self.nearPlayers[i].name
                            self.nearPlayers[i].name = ""
                            self.nearPlayers[i].id = 0
                            self.countNearPlayers -= 1
                            break
                    print("R_PLAYER_DISAPPEAR: id=%d" % (player_id))
                elif packetType == S2C.PLAYER_MOVE:  # player_move
                    player_id = unpack(packet, 3, 'L')
                    x = unpack(packet, 7, 'b')
                    y = unpack(packet, 8, 'b')
                    z = unpack(packet, 9, 'b')
                    for i in range(self.MAX_ENTITYS):
                        if self.nearPlayers[i].id == player_id:
                            self.nearPlayers[i].x += x
                            self.nearPlayers[i].y += y
                            self.nearPlayers[i].z += z
                            break                              
                    # print("R_PLAYER_MOVE: id=%d, x=%d, y=%d, z=%d" %(player_id, x, y, z))
                elif packetType == S2C.PLAYER_MOVE_STOP:  # player_move_stop
                    player_id = unpack(packet, 3, 'L')
                    x = unpack(packet, 7, 'b')
                    y = unpack(packet, 8, 'b')
                    z = unpack(packet, 9, 'b')
                    for i in range(self.MAX_ENTITYS):
                        if self.nearPlayers[i].id == player_id:
                            self.nearPlayers[i].x += x
                            self.nearPlayers[i].y += y
                            self.nearPlayers[i].z += z
                            break
                elif packetType == S2C.PING:
                    if not self.clientConnected:  # not connected so we must imitate the heartbeat
                        self.gameServerNetwork.send_packet(C2S.HEART_BEAT, "L", [random.randint(1,10000)], init=False)
                        continue
                if self.clientConnected:  # client is connected so forward it
                    self.gameClientNetwork.send_bytes(packet)  



    def SendChatMessageToGameClient(self, text):
        """Sends a text message to the game self. 
        Color depending on if chatting enabled or disabled
        """
        if self.chatEnabled:
            color = "&"
        else:
            color = "*"
        self.gameClientNetwork.send_packet(S2C.CHAT, "ss", [self.botname, color + text])


    def GetNearPlayerFromId(self, player_id):
        for i in range(self.MAX_ENTITYS):
            if self.nearPlayers[i].id == player_id:
                return self.nearPlayers[i]
        return None


    def GetNearPlayerFromName(self, player_name):
        for i in range(self.MAX_ENTITYS):
            if self.nearPlayers[i].name == player_name:
                return self.nearPlayers[i]
        return None


class Entity():
    def __init__(self):
        self.name = 0
        self.id = 0
        self.x = 0
        self.y = 0
        self.z = 0
        self.type = 0
        self.hp = 0
        self.time = 0
        self.marked = False

    def __repr__(self):
        return "Entity: name=%s, id=%d, x=%d, y=%d, z=%d, type=%d, hp=%d, time=%d" % (self.name, self.id, self.x, self.y, self.z, self.type, self.hp, self.time)
