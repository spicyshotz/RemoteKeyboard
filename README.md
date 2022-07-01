# Remote Keyboard

⭐ Use a the client on a Raspberry pi or a PC to send keyboard input to a host PC



## Usage

ℹ️ Find the local IP address of the host PC and enter it in the IP field in Client.py
Run Host.py first and only then run Client.py.


## Known Issues

🔴 Right shift doesnt work.  
🔴 Struggles to send or receive too frequent consecutive inputs (such as holding down a key)  
🔴 Key combos dont work (such as ctrl+c, shift+alt etc.)😔  


## TODO

💡 Fix Known Issues above  
💡 Add some logic to automatically find an IP address with the needed port open so that its easier to connect if the host IP changes frequently.🤓
