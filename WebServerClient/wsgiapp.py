def app(environ, start_response):
    """A barebones WSGI application.
 
    This is a starting point for your own Web framework :)
    """
    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain')]
    start_response(status, response_headers)
    return ['Hello world from a simple WSGI application!n']

# 首先，服务器启动并加载一个由Web框架/应用提供的可调用的’application’
# 然后，服务器读取请求
# 然后，服务器解析它
# 然后，服务器使用请求的数据创建了一个’environ’字典
# 然后，服务器使用’environ’字典和’start_response’做为参数调用’application’，并拿到返回的响应体。
# 然后，服务器使用调用’application’返回的数据，由’start_response’设置的状态和响应头，来构造HTTP响应。
# 最终，服务器把HTTP响应传回给户端。