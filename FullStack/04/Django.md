# Django2.0
原则：DRP：Don't repeat yourself
## 一 什么是web框架？ ##

框架，即framework，特指为解决一个开放性问题而设计的具有一定约束性的支撑结构，使用框架可以帮你快速开发特定的系统，简单地说，就是你用别人搭建好的舞台来做表演。

对于所有的Web应用，本质上其实就是一个socket服务端，用户的浏览器其实就是一个socket客户端。

	eg：server.py

## 接口就是WSGI：Web Server Gateway Interface ##
	
	eg:server-wsgi.py
	整个application()函数本身没有涉及到任何解析HTTP的部分，也就是说，底层代码不需要我们自己编写，
	我们只负责在更高层次上考虑如何响应请求就可以了。
	application()函数必须由WSGI服务器来调用。有很多符合WSGI规范的服务器，我们可以挑选一个来用。
	
	Python内置了一个WSGI服务器，这个模块叫wsgiref     
	application()函数就是符合WSGI标准的一个HTTP处理函数，它接收两个参数：
	
	        //environ：一个包含所有HTTP请求信息的dict对象；
	        
	        //start_response：一个发送HTTP响应的函数。
	
	在application()函数中，调用：
	
	start_response('200 OK', [('Content-Type', 'text/html')])
	
	就发送了HTTP响应的Header，注意Header只能发送一次，也就是只能调用一次start_response()函数。
	start_response()函数接收两个参数，一个是HTTP响应码，一个是一组list表示的HTTP Header，每
	个Header用一个包含两个str的tuple表示。
	
	通常情况下，都应该把Content-Type头发送给浏览器。其他很多常用的HTTP Header也应该发送。

	然后，函数的返回值b'<h1>Hello, web!</h1>'将作为HTTP响应的Body发送给浏览器。
	
	有了WSGI，我们关心的就是如何从environ这个dict对象拿到HTTP请求信息，然后构造HTML，
	通过start_response()发送Header，最后返回Body。


## 二 MVC和MTV模式 ##

	著名的MVC模式：所谓MVC就是把web应用分为模型(M),控制器(C),视图(V)三层；他们之间以一种插件似的，松耦合的方式连接在一起。

	模型负责业务对象与数据库的对象(ORM),视图负责与用户的交互(页面)，控制器(C)接受用户的输入调用模型和视图完成用户的请求。


	Django的MTV模式本质上与MVC模式没有什么差别，也是各组件之间为了保持松耦合关系，只是定义上有些许不同，Django的MTV分别代表：

       Model(模型)：负责业务对象与数据库的对象(ORM)

       Template(模版)：负责如何把页面展示给用户

       View(视图)：负责业务逻辑，并在适当的时候调用Model和Template

       此外，Django还有一个url分发器，它的作用是将一个个URL的页面请求分发给不同的view处理，view再调用相应的Model和Template

		   |----获取-----	
		   |			|
		   |			|	
		Models------> view-----> Template---->URL
		   |
		   |
	     数据库


## 三 django的流程和命令行工具 ##
	django
	安装 pip3 install django
	
	1 create project 
		django-admin startproject mysite
	
	---mysite
		---setings.py
		---url.py
		---wsgi.py
	---manage.py (启动文件)

	2 create APP
		python manage.py startapp blog

	3 settings config
		TEMPLATES
			'DIRS': [os.path.join(BASE_DIR,'templates')],   # 配置 模板路径
	4 add path in urls.py
		from blog import  views
		urlpatterns 中
			path('curtime/', views.curtime),
	5 start project 
		python manage.py runserver 127.0.0.1:8080
	6 produce databases 
		python manage.py makemigrations (生成同步数据库的脚本)
		python manage.py migrate  同步数据库
	注意：在开发过程中，数据库同步误操作之后，难免会遇到后面不能同步成功的情况，解决这个问题的一个简单粗暴方法是把migrations目录下的脚本（除__init__.py之外）全部删掉，再把数据库删掉之后创建一个新的数据库，数据库同步操作再重新做一遍。  
	7  setting user/passwd  
		python manage.py createsuperuser 
	8  clear databases
		python manage.py flush 
	9 select command 
		django-admin help startapp
		admin 是django自带的一个后台数据库管理系统
	10 	starting interface
		 python manage.py shell
		注释：这个命令和直接运行 python 进入 shell 的区别是：你可以在这个 shell 里面调用当前项目的 models.py 中的 API，对于操作数据，还有一些小测试非常方便。
	11 detailed list
		python manage.py

## 四 Django的配置文件(settings) ## 
	
	