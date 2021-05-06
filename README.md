# KalOnline-Clientless-Bot
Kalonline clientless bot for private servers

PK Password: EV)O8@BL$3O2E
2006 Config.pk crypt

current features: config md5 bypass, hwid block bypass.<br/>
proxy server commands:<br/>
-help \\shows in chat all proxy commands<br/>
-speed INTEGER \\speed hack<br/>
-fduel PLAYERNAME \\force duel<br/>
-fparty PLAYERNAME \\force party<br/>
-ftrade PLAYERNAME \\force trade<br/>
-stop \\clientless<br/>

how to set a proxy server -<br/>
1. get the kalonline server ip and port:<br/>
   run kalonline. open task manager -> performance -> open resource monitor -> TCP connections -> search for running engine.exe - remote address=ip , remote port=port

2. changes in 'src' folder:<br/>
   A. client.py - self.gameServerAddress = ("SERVERIP", SERVERPORT)  # SERVERNAME<br/>
   B. server.py - self.listenAddress = ("localhost", SERVERPORT) #"SERVERIP"<br/>

3. changes in kalonline (need to do only ONE of them):<br/>
   A. open config.pk with pkeditor -> change ip in xlate to 127.0.0.1<br/>
   B. run cheatengine -> search for string SERVERIP (ex. 185.244.194.237) -> change the address you got to 127.0.0.1<br/>
   C. if local server exists, no need to do A or B<br/>

4. run proxy server (main.py), run kalonline.<br/>

note:<br/>
evolved server connection is different - <br/>
to connect (ONE of these options):<br/>
1. run notepad as administrator<br/>
   open through notepad hosts file from C:\Windows\System32\drivers\etc\hosts<br/>
   add this line 127.0.0.1 kalevolved.noip.me<br/>
   save the file as original hosts file (NOT AS TXT)<br/>

2. use cheatengine -> search string kalevolved.noip.me -> change to 127.0.0.1<br/>



PACKET SNIFFING:<br/>

fparty/fduel packet error in server:<br/>
need to change init_packet in network.py to 0xABCD<br/>
to find ABCD:<br/>
1. run wireshark<br/>
2. use filter:  ip.dst == SERVERIP<br/>


data contains 6200fd<br/>
3. send a skill in game<br/>
4. search for data with 0b and 0xfd. for example: 0b00fd5e000000c8200000<br/>
5. last 4 bytes will be our ABCD with this rule:<br/>
   9319==1993   c820==20c8<br/>
   7307== 0773<br/>
if you want to send a packet in kal it has to be through client.py. need to add a new -command<br/>
to send a skill:<br/>
1. search for the skill name in jobsystem.txt (for example "Spin Blade")<br/>
2. search for the skill action. (in the example above the action is 36)<br/>
3. open calculator and change to progammer mode<br/>
4. type the skill action (36 for the example)<br/>
5. hex number will complete the packet. DEC 36 = HEX 24 . so the spin packet is 0x24<br/>

to send an other packet:<br/>
1. open client.py<br/>
2. after this line: <br/>
      if packet != None:   <br/>
   paste this three lines:<br/>
      packetType = unpack(packet, 2, 'B')<br/>
      packetLength = unpack(packet, 0, 'H')<br/>
      print("RECV -> Type: %d  Length:  %d" %(packetType, packetLength)) <br/>  
3. run main.py and kal.<br/>
4. now every packet that sent will be shown on main.py with type and length<br/>
5. the type number is like the skill action number in the send skill explanation (number 4 and on)<br/>

