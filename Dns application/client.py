import socket
import sys
import threading
import time
def client_server (lshostname,port):
    #create a socket 
    try:
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()
        
    # Define the port on which you want to connect to the server

    # connect to the server on local machine
    server_binding = (lshostname, port)
    cs.connect(server_binding)
    #send file line by line to ls 
    file_path = './PROJ2-HNS.txt'
    with open(file_path, 'r') as f:
        data = f.readlines()
        clean_data = [i.replace('\n', '') for i in data]
    r = open('./RESOLVED.txt','a')
    for l in clean_data:
        cs.send(l.encode('utf-8'))
        time.sleep(5)
        dns_res = cs.recv(200)
        res = format(dns_res.decode('utf-8'))
        r.write(res)
    
if __name__ == "__main__":
    client_server(sys.argv[1], int(sys.argv[2]))
    #python3 client.py 50001