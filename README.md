# Remote Keyboard

â­ Use a the client on a Raspberry pi or a PC to send keyboard input to a host PC



## Usage

âšī¸ Find the local IP address of the host PC and enter it in the IP field in Client.py
Run Host.py first and only then run Client.py.  
![Screenshot](https://i.imgur.com/lgvaWu9.png)


## Known Issues

đ´ Right shift doesnt work.  
đ´ Struggles to send or receive too frequent consecutive inputs (such as holding down a key)  
đ´ Key combos dont work (such as ctrl+c, shift+alt etc.)đ  
đ´ Tried using it in a game (Age of empires 4) and that doesnt work. :/


## TODO

đĄ Fix Known Issues above  
đĄ Add some logic to automatically find an IP address with the needed port open so that its easier to connect if the host IP changes frequently.đ¤
