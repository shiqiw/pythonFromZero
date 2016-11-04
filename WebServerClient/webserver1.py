# 编程语言、编译器和解释器、数据库和操作系统、WEB服务器和WEB框架。
# 从重建不同的软件系统来开始来学习它们是如何工作的，是一个好主意。

import socket
 
HOST, PORT = '', 8888
 
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print('Serving HTTP on port %s ...' % PORT)
while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print request
 
    http_response = """
HTTP/1.1 200 OK
 
Hello, World!
"""
    client_connection.sendall(http_response)
    client_connection.close()

# protocol://host:port/path
# 查找和连接的WEB服务器地址，和你要获取的服务器上的路径
# 浏览器需要先和WEB服务器建立TCP连接，然后浏览器在TCP连接上发送HTTP请求，然后等待服务器回发HTTP响应

# telnet localhost 8888
# GET /hello HTTP/1.1
# HTTP method + path + HTTP version

# HTTP/1.1 200 OK
#
# body
# HTTP version + status code + status explanation
# newline
# response body
