# 当一个子进程终止了，内核发送SIGCHLD信号。
# 父进程可以设置一个信号处理器来异步地被通知，然后就能wait子进程获取它的终止状态，因此阻止了僵尸进程出现。
# 异步事件意味着父进程不会提前知道事件发生的时间。
###########################################################################
# Concurrent server - webserver3e.py                                      #
#                                                                         #
# Tested with Python 2.7.9 & Python 3.4 on Ubuntu 14.04 & Mac OS X        #
###########################################################################
import os
import signal
import socket
import time
 
SERVER_ADDRESS = (HOST, PORT) = '', 8888
REQUEST_QUEUE_SIZE = 5
 
def grim_reaper(signum, frame):
    pid, status = os.wait()
    print(
        'Child {pid} terminated with status {status}'
        'n'.format(pid=pid, status=status)
    )
 
def handle_request(client_connection):
    request = client_connection.recv(1024)
    print(request.decode())
    http_response = b"""
HTTP/1.1 200 OK
 
Hello, World!
"""
    client_connection.sendall(http_response)
    # sleep to allow the parent to loop over to 'accept' and block there
    time.sleep(3)
 
def serve_forever():
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind(SERVER_ADDRESS)
    listen_socket.listen(REQUEST_QUEUE_SIZE)
    print('Serving HTTP on port {port} ...'.format(port=PORT))
 
    signal.signal(signal.SIGCHLD, grim_reaper)
 
    while True:
        client_connection, client_address = listen_socket.accept()
        pid = os.fork()
        if pid == 0:  # child
            listen_socket.close()  # close child copy
            handle_request(client_connection)
            client_connection.close()
            os._exit(0)
        else:  # parent
            client_connection.close()
 
if __name__ == '__main__':
    serve_forever()