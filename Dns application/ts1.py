import socket 
import threading
import sys
import time

def ts1_search(url):
    for i in ls:
        s = i.split()
        clean_data = s[0].lower()
        clean_url = url.lower()
        if clean_data == clean_url:
            i = i.strip()
            i = i + ' IN'

            return i 
    return 0
    

def ts_server(port): 
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()
    server_binding = ('', int(port))
    ss.bind(server_binding)
    ss.listen(1)
    host = socket.gethostname()
    print("[S]: Server host name is {}".format(host))
    localhost_ip = (socket.gethostbyname(host))
    print("[S]: Server IP address is {}".format(localhost_ip))
    csockid, addr = ss.accept()
    print ("[S]: Got a connection request from a client at {}".format(addr))
    
    while True:
        data = csockid.recv(200)
        if not data:
            break
        result_search = ts1_search(format(data.decode('utf-8')))
        if result_search != 0:
            result_search += '\n'
            csockid.send(result_search.encode('utf'))
        #csockid.send(result_search.encode('utf-8'))
if __name__ == "__main__":
    with open('PROJ2-DNSTS1.txt', 'r') as f:
        ls = f.readlines()
    ts_server(sys.argv[1])
    #python3 ts1.py 50007

    
