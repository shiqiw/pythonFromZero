from pyramid.config import Configurator
from pyramid.response import Response
 
def hello_world(request):
    return Response(
        'Hello world from Pyramid!n',
        content_type='text/plain',
    )
 
config = Configurator()
config.add_route('hello', '/hello')
config.add_view(hello_world, route_name='hello')
app = config.make_wsgi_app()

# (lsbaws) $ python webserver2.py pyramidapp:app
# WSGIServer: Serving HTTP on port 8888 ...

# $ curl -v http://localhost:8888/hello

# flask and Django are similar

# 1.框架提供一个可调用的’应用’（WSGI规格并没有要求如何实现）
# 2.服务器每次接收到HTTP客户端请求后，执行可调用的’应用’。服务器把一个包含了WSGI/CGI变量的字典和一个可调
# 用的’start_response’做为参数给可调用的’application’。
# 3.框架/应用生成HTTP状态和HTTP响应头，然后把它们传给可调用的’start_response’，让服务器保存它们。
# 框架/应用也返回一个响应体。
# 4.服务器把状态，响应头，响应体合并到HTTP响应里，然后传给（HTTP）客户端（这步不是（WSGI）规格里的一部分，
# 但它是后面流程中的一步，为了解释清楚我加上了这步）