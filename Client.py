import socket
from pynput.keyboard import Key, Listener


host = socket.gethostname()  # as both code is running on same pc
port = 5969  # socket server port number

client_socket = socket.socket()  # instantiate
client_socket.connect((host, port))  # connect to the server

def on_press(key):
    print(format(key))
    prKey = str(format(key)).strip("'")
    if len(prKey) != 1:
        prKey = str(format(key)).strip('"')
    #client_socket.send(("PRESSED~" +  prKey).encode())
    client_socket.send(prKey.encode())

def on_release(key):
    #print('{0} release'.format(key))
    '''reKey = str(format(key)).strip("'")
    if len(reKey) != 1:
        reKey = str(format(key)).strip('"')
    client_socket.send(("RELEASED~" +  reKey).encode())'''
    
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

client_socket.close()  # close the connection

