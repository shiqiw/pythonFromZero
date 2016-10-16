# socket就是通信终端的一种抽象，它允许你的程序使用文件描述符和别的程序通信。
# TCP的socket对是一个4元组，标识着TCP连接的两个终端：本地IP地址、本地端口、远程IP地址、远程端口。
# 一个socket对唯一地标识着网络上的TCP连接。标识着每个终端的两个值，IP地址和端口号，通常被称为socket。

# create TCP/IP socket
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# set option
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# bind address / port, both optional
listen_socket.bind(SERVER_ADDRESS)
# on server side, set the socket to listen
listen_socket.listen(REQUEST_QUEUE_SIZE)

# client side
import socket
 
 # create a socket and connect to a server
 sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 # connect to server
 # 客户端不用调用bind和accept。
 # 客户端没必要调用bind，是因为客户端不关心本地IP地址和本地端口号。
 # 当客户端调用connect时内核的TCP/IP栈自动分配一个本地IP址地和本地端口。
 # 本地端口被称为暂时端口（ ephemeral port），也就是，short-lived 端口。
 sock.connect(('localhost', 8888))
 # host, port = sock.getsockname()[:2]
 
 # send and receive some data
 sock.sendall(b'test')
 data = sock.recv(1024)
 print(data.decode())

 # related, what is process
 # os.getppid() and os.getpid()

# related, file descriptor
# 当打开一个存在的文件，创建一个文件，或者创建一个socket时，内核返回的非负整数。
# 在UNIX里一切皆文件。
# 内核使用文件描述符来追踪进程打开的文件。
# 当你需要读或写文件时，你就用文件描述符标识它。P
# 在底层，UNIX中是这样标识文件和socket的：通过它们的整数文件描述符。
# STD in/out/err

# socket is an object, which has file descriptor

# 当父进程fork了一个新的子进程，子进程就获取了父进程文件描述符的拷贝
# 内核使用描述符引用计数来决定是否关闭文件/socket。

# 终止数据包（在TCP/IP说法中叫做FIN）没有发送给客户端，客户端就保持在线
# ulimit -a