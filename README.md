# KalOnline-Clientless-Bot
Kalonline clientless bot for private servers

current features: config md5 bypass, hwid block bypass.
proxy server commands:
-help \\shows in chat all proxy commands
-speed INTEGER \\speed hack
-fduel PLAYERNAME \\force duel
-fparty PLAYERNAME \\force party
-ftrade PLAYERNAME \\force trade
-stop \\clientless

how to set a proxy server -
1. get the kalonline server ip and port:
   run kalonline. open task manager -> performance -> open resource monitor -> TCP connections -> search for running engine.exe - remote address=ip , remote port=port

2. changes in 'src' folder:
   A. client.py - self.gameServerAddress = ("SERVERIP", SERVERPORT)  # SERVERNAME
   B. server.py - self.listenAddress = ("localhost", SERVERPORT) #"SERVERIP"

3. changes in kalonline (need to do only ONE of them):
   A. open config.pk with pkeditor -> change ip in xlate to 127.0.0.1
   B. run cheatengine -> search for string SERVERIP (ex. 185.244.194.237) -> change the address you got to 127.0.0.1
   C. if local server exists, no need to do A or B

4. run proxy server (main.py), run kalonline.

note:
evolved server connection is different - 
to connect (ONE of these options):
1. run notepad as administrator
   open through notepad hosts file from C:\Windows\System32\drivers\etc\hosts
   add this line 127.0.0.1 kalevolved.noip.me
   save the file as original hosts file (NOT AS TXT)

2. use cheatengine -> search string kalevolved.noip.me -> change to 127.0.0.1



PACKET SNIFFING:

fparty/fduel packet error in server:
need to change init_packet in network.py to 0xABCD
to find ABCD:
1. run wireshark
2. use filter:  ip.dst == SERVERIP


data contains 6200fd
3. send a skill in game
4. search for data with 0b and 0xfd. for example: 0b00fd5e000000c8200000
5. last 4 bytes will be our ABCD with this rule:
   9319==1993   c820==20c8
   7307== 0773
if you want to send a packet in kal it has to be through client.py. need to add a new -command
to send a skill:
1. search for the skill name in jobsystem.txt (for example "Spin Blade")
2. search for the skill action. (in the example above the action is 36)
3. open calculator and change to progammer mode
4. type the skill action (36 for the example)
5. hex number will complete the packet. DEC 36 = HEX 24 . so the spin packet is 0x24

to send an other packet:
1. open client.py
2. after this line: 
      if packet != None:   
   paste this three lines:
      packetType = unpack(packet, 2, 'B')
      packetLength = unpack(packet, 0, 'H')
      print("RECV -> Type: %d  Length:  %d" %(packetType, packetLength))   
3. run main.py and kal.
4. now every packet that sent will be shown on main.py with type and length
5. the type number is like the skill action number in the send skill explanation (number 4 and on)

