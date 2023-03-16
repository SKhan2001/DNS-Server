import socket 
import select 
import sys
import time

def ls_server(ls_port, ts1Hostname, ts1_port, ts2Hostname, ts2_port):
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       # print("[S]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()
    server_binding = ('', int(ls_port))
    ss.bind(server_binding)
    ss.listen(1)
    host = socket.gethostname()
    print(host)
    print("[S]: Server host name is {}".format(host))
    csockid, addr = ss.accept()
    print ("[S]: Got a connection request from a client at {}".format(addr))

    ##creating a socket for ts1 and connecting it 
    try:
        ts1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_binding = (ts1Hostname, int(ts1_port))
        ts1.connect(server_binding)
        
        #print("[C]: Client socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()
    ##creating a socket for ts2 and connecting it 
    try:
        ts2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_binding = (ts2Hostname, int(ts2_port))
        ts2.connect(server_binding)
       # print("[C]: Client socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()
    
    # connect to the server on local machine
    ts2.settimeout(2.5)
    ts1.settimeout(2.5)
  
    while True:
        data = csockid.recv(200)
        if not data:
            break
        ts1.send(data)
        ts2.send(data)
        
        try:
            ts1_msg = ts1.recv(200)
            ts1_msg_data = ts1_msg.decode('utf-8')
            #print("[LS]: The data received from [TS1] -> " , ts1_msg)
            csockid.send(ts1_msg_data.encode('utf-8'))
        except socket.timeout:
            try:
                ts2_msg = ts2.recv(200)
                ts2_msg_data = ts2_msg.decode('utf-8')
                #print("[LS]: The data received from [TS2] -> " , ts2_msg)
                csockid.send(ts2_msg_data.encode('utf-8'))
            except socket.timeout:
                data = format(data.decode('utf-8'))
                error_code = data + ' - TIMED OUT\n'
                csockid.send(error_code.encode('utf-8'))
       

if __name__ == "__main__":
    args = sys.argv
    ls_server(args[1], args[2], args[3], args[4], args[5])
    #python3 ls.py 50001 ts1 50007 ts2 50006 