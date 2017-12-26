from wsgiref.simple_server import make_server


def f1(req):
    return [b'<h1>Hello, book!</h1>']
def f2(req):
    return [b'<h1>Hello, web!</h1>']
import time
def f3(req):
    f = open('curtime.html','rb')
    data =f.read()
    cur_time= time.ctime(time.time())
    data = str(data,'utf8').replace('!time!',str(cur_time))
    return [data.encode('utf8')]

def routers():
    urlpatterns =(
        ('/book',f1),
        ('/web',f2),
        ('/curtime', f3),
    )
    return  urlpatterns



def application(environ, start_response):
    #通过environ封装成一个所有请求信息的对象
    #start_response 可以很方便的设置响应头
    #print("environ=",environ)
    #print("environ=",environ['PATH_INFO'])
    path = environ['PATH_INFO']
    start_response('200 OK',[('Content-Type','text/html')])
    urlpatterns = routers()
    func = None
    for itme in urlpatterns:
        if itme[0] == path:
            func = itme[1]
            break

    if func:
        return func(environ)
    else:
        return [b'<h1>404</h1>']

#封装socket对象以及准备过程，(socket,bind,listen)

httpd = make_server('127.0.0.1',8002, application)
print('Serving HTTP on port 8002')

# # 开始监听HTTP请求:
httpd.serve_forever()