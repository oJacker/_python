# AJAX

## 一、AJAX预备知识：json进阶

### 1.1 什么是JSON ###

	JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式。JSON是用字符串来表示Javascript对象；
	json字符串就是js对象的一种表现形式（字符串形式）

	JSON字符串的值：
		数字    （整数或浮点数）
		字符串  （在双引号中）
		逻辑值  （true 或 false）
		数组    （在方括号中）
		对象    （在花括号中，引号用双引）
		null     

### 1.2 python与json对象的对应： ###

		python         -->        json
        dict                      object
        list,tuple                array
        str,unicode               string
        int,long,float            number
        True                      true
        False                     false
        None  					  null

### 1.3 .parse()和.stringify() ###
	parse() 用于从一个json字符串中解析出json对象,如
		var str= '{"name":"oj","age":"23"}'
		JSON.parse(str)     ------>  Object  {age: "23",name: "yuan"}
	stringify()用于从一个json对象解析成json字符串，如
		结果：  JSON.stringify(c)     ------>      '{"a":1,"b":2}'
		注意1：单引号写在{}外，每个属性名都必须用双引号，否则会抛出异常。
		注意2:
			a={name:"yuan"};   //ok
			b={'name':'yuan'}; //ok
			c={"name":"yuan"}; //ok
			
			alert(a.name);  //ok
			alert(a[name]); //undefined
			alert(a['name']) //ok

### 1.4  django向js发送数据 ###
	def login(request):
    obj={'name':"alex111"}
    return render(request,'index.html',{"objs":json.dumps(obj)})
	#----------------------------------
	 <script>
	     var temp={{ objs|safe }}
	     alert(temp.name);
	     alert(temp['name'])
	 </script>

### 1.5 JSON与XML比较 ###	
    可读性：   XML胜出；
    解码难度： JSON本身就是JS对象（主场作战），所以简单很多；
    流行度：   XML已经流行好多年，但在AJAX领域，JSON更受欢迎。


## 二　什么是AJAX ##
	AJAX（Asynchronous Javascript And XML）翻译成中文就是“异步Javascript和XML”。即使用Javascript语言与服务器进行异步交互，传输的数据为XML（当然，传输的数据不只是XML）。

    	同步交互：客户端发出一个请求后，需要等待服务器响应结束后，才能发出第二个请求；
    	异步交互：客户端发出一个请求后，无需等待服务器响应结束，就可以发出第二个请求。

	AJAX除了异步的特点外，还有一个就是：浏览器页面局部刷新；（这一特点给用户的感受是在不知不觉中完成请求和响应过程）


## 三  AJAX常见应用情景 ##

## 四  AJAX的优缺点 ##
	优点：
	    AJAX使用Javascript技术向服务器发送异步请求；
	    AJAX无须刷新整个页面；
	    因为服务器响应内容不再是整个页面，而是页面中的局部，所以AJAX性能高；
	缺点：

	   	AJAX并不适合所有场景，很多时候还是要使用同步交互；
	    AJAX虽然提高了用户体验，但无形中向服务器发送的请求次数增多了，导致服务器压力增大；
	    因为AJAX是在浏览器中使用Javascript技术完成的，所以还需要处理浏览器兼容性问题；
## 五  AJAX技术 ##
	四步操作：
	    创建核心对象；
	    使用核心对象打开与服务器的连接；
	    发送请求
	    注册监听，监听服务器响应。
	XMLHTTPRequest		
	    open(请求方式, URL, 是否异步)
	    send(请求体)
	    onreadystatechange，指定监听函数，它会在xmlHttp对象的状态发生变化时被调用
	    readyState，当前xmlHttp对象的状态，其中4状态表示服务器响应结束
	    status：服务器响应的状态码，只有服务器响应结束时才有这个东东，200表示响应成功；
	    responseText：获取服务器的响应体

## 六  AJAX实现 ##
### 6.1 准备工作(后台设定)： ###
	def login(request):
    	print('hello ajax')
    	return render(request,'index.html') 
	def ajax_get(request):
    	return HttpResponse('helloyuanhao')

### 6.2 AJAX核心（XMLHttpRequest） ###
	其实AJAX就是在Javascript中多添加了一个对象：XMLHttpRequest对象。所有的异步交互都是使用XMLHttpServlet对象完成
	var xmlHttp = new XMLHttpRequest()；（大多数浏览器都支持DOM2规范）

		function createXMLHttpRequest() {
	        var xmlHttp;
	        // 适用于大多数浏览器，以及IE7和IE更高版本
	        try{
	            xmlHttp = new XMLHttpRequest();
	        } catch (e) {
	            // 适用于IE6
	            try {
	                xmlHttp = new ActiveXObject("Msxml2.XMLHTTP");
	            } catch (e) {
	                // 适用于IE5.5，以及IE更早版本
	                try{
	                    xmlHttp = new ActiveXObject("Microsoft.XMLHTTP");
	                } catch (e){}
	            }
	        }            
	        return xmlHttp;
	    }

### 6.3　打开与服务器的连接（open方法） ###
	当得到XMLHttpRequest对象后，就可以调用该对象的open()方法打开与服务器的连接了。open()方法的参数如下：

	open(method, url, async)：
	
	    method：请求方式，通常为GET或POST；
	    url：请求的服务器地址，例如：/ajaxdemo1/AServlet，若为GET请求，还可以在URL后追加参数；
	    async：这个参数可以不给，默认值为true，表示异步请求；
			var xmlHttp = createXMLHttpRequest();
			xmlHttp.open("GET", "/ajax_get/", true);　
### 6.5　接收服务器响应 ###
	当请求发送出去后，服务器端Servlet就开始执行了，但服务器端的响应还没有接收到。接下来我们来接收服务器的响应。

	XMLHttpRequest对象有一个onreadystatechange事件，它会在XMLHttpRequest对象的状态发生变化时被调用。下面介绍一下XMLHttpRequest对象的5种状态：

    0：初始化未完成状态，只是创建了XMLHttpRequest对象，还未调用open()方法；
    1：请求已开始，open()方法已调用，但还没调用send()方法；
    2：请求发送完成状态，send()方法已调用；
    3：开始读取服务器响应；
    4：读取服务器响应结束。 
		onreadystatechange事件会在状态为1、2、3、4时引发。

### 6.6  if 发送POST请求： ###
	 <1>需要设置请求头：xmlHttp.setRequestHeader(“Content-Type”, “application/x-www-form-urlencoded”)；
            注意 :form表单会默认这个键值对;不设定，Web服务器会忽略请求体的内容。
      <2>在发送时可以指定请求体了：xmlHttp.send(“username=yuan&password=123”)

### 6.7　AJAX实现小结 ###
	创建XMLHttpRequest对象；
    调用open()方法打开与服务器的连接；
    调用send()方法发送请求；
    为XMLHttpRequest对象指定onreadystatechange事件函数，这个函数会在

    XMLHttpRequest的1、2、3、4，四种状态时被调用；

    XMLHttpRequest对象的5种状态，通常我们只关心4状态。

    XMLHttpRequest对象的status属性表示服务器状态码，它只有在readyState为4时才
    能获取到。

     XMLHttpRequest对象的responseText属性表示服务器响应内容，它只有在
     readyState为4时才能获取到！

### 6.8  请求完整代码： ###

	<h1>AJAX</h1>
	<button onclick="send()">测试</button>
	<div id="div1"></div>
	<script>
	       function createXMLHttpRequest() {
	            try {
	                return new XMLHttpRequest();//大多数浏览器
	            } catch (e) {
	                try {
	                    return new ActiveXObject("Msxml2.XMLHTTP");
	                } catch (e) {
	                    return new ActiveXObject("Microsoft.XMLHTTP");
	                }
	            }
	        }
	
	        function send() {
	            var xmlHttp = createXMLHttpRequest();
	            xmlHttp.onreadystatechange = function() {
	                if(xmlHttp.readyState == 4 && xmlHttp.status == 200) {
	                    var div = document.getElementById("div1");
	                    div.innerText = xmlHttp.responseText;
	                    div.textContent = xmlHttp.responseText;
	                }
	            };
	
	            xmlHttp.open("POST", "/ajax_post/", true);
	            //post: xmlHttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
	            xmlHttp.send(null);  //post: xmlHttp.send("b=B");
	        }
	
	
	</script>
       
	#--------------------------------views.py 
	from django.views.decorators.csrf import csrf_exempt
	
	def login(request):
	    print('hello ajax')
	    return render(request,'index.html')
	
	@csrf_exempt   ＃csrf防御
	def ajax_post(request):
	    print('ok')
	    return HttpResponse('helloyuanhao') 


## 七　AJAX实例（用户名是否已被注册） ##
### 7.1　功能介绍 ###

	在注册表单中，当用户填写了用户名后，把光标移开后，会自动向服务器发送异步请求。服务器返回true或false，返回true表示这个用户名已经被注册过，返回false表示没有注册过。
	
	客户端得到服务器返回的结果后，确定是否在用户名文本框后显示“用户名已被注册”的错误信息！
### 7.2　案例分析###

    页面中给出注册表单；
    在username表单字段中添加onblur事件，调用send()方法；
    send()方法获取username表单字段的内容，向服务器发送异步请求，参数为username；
    django 的视图函数：获取username参数，判断是否为“yuan”，如果是响应true，否则响应false View Code

### 7.3 代码 ###
	<script type="text/javascript">
        function createXMLHttpRequest() {
            try {
                return new XMLHttpRequest();
            } catch (e) {
                try {
                    return new ActiveXObject("Msxml2.XMLHTTP");
                } catch (e) {
                    return new ActiveXObject("Microsoft.XMLHTTP");
                }
            }
        }

        function send() {
            var xmlHttp = createXMLHttpRequest();
            xmlHttp.onreadystatechange = function() {
                if(xmlHttp.readyState == 4 && xmlHttp.status == 200) {
                    if(xmlHttp.responseText == "true") {
                        document.getElementById("error").innerText = "用户名已被注册！";
                        document.getElementById("error").textContent = "用户名已被注册！";
                    } else {
                        document.getElementById("error").innerText = "";
                        document.getElementById("error").textContent = "";
                    }
                }
            };
            xmlHttp.open("POST", "/ajax_check/", true, "json");
            xmlHttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
            var username = document.getElementById("username").value;
            xmlHttp.send("username=" + username);
        }
	</script>

		//--------------------------------------------------index.html
		
		<h1>注册</h1>
		<form action="" method="post">
		用户名：<input id="username" type="text" name="username" onblur="send()"/><span id="error"></span><br/>
		密　码：<input type="text" name="password"/><br/>
		<input type="submit" value="注册"/>
		</form>
		
		
		//--------------------------------------------------views.py
		from django.views.decorators.csrf import csrf_exempt
		
		def login(request):
		    print('hello ajax')
		    return render(request,'index.html')
		    # return HttpResponse('helloyuanhao')
		
		@csrf_exempt
		def ajax_check(request):
		    print('ok')
		
		    username=request.POST.get('username',None)
		    if username=='yuan':
		        return HttpResponse('true')
		    return HttpResponse('false')

## 八 jquery实现的ajax ##



## 九 跨域请求 ##

### 9.1 同源策略机制 ###
	浏览器有一个很重要的概念——同源策略(Same-Origin Policy)。所谓同源是指，域名，协议，端口相同。不同源的客户端脚本(javascript、ActionScript)在没明确授权的情况下，不能读写对方的资源。

	简单的来说，浏览器允许包含在页面A的脚本访问第二个页面B的数据资源，这一切是建立在A和B页面是同源的基础上。
	如果Web世界没有同源策略，当你登录淘宝账号并打开另一个站点时，这个站点上的JavaScript可以跨域读取你的淘宝账号数据，这样整个Web世界就无隐私可言了。
### 9.2  jsonp的js实现 ###
	JSONP是JSON with Padding的略称。可以让网页从别的域名（网站）那获取资料，即跨域读取数据。

	它是一个非官方的协议，它允许在服务器端集成Script tags返回至客户端，通过javascript callback的形式实现跨域访问（这仅仅是JSONP简单的实现形式）。

	JSONP就像是JSON+Padding一样(Padding这里我们理解为填充)
	#---------------------------http://127.0.0.1:8001/login
	
		 def login(request):
		    print('hello ajax')
		    return render(request,'index.html')
		 #---------------------------返回用户的index.html
		 <h1>发送JSONP数据</h1>
		
		
		<script>
		    function fun1(arg){
		        alert("hello"+arg)
		    }
		</script>
		<script src="http://127.0.0.1:8002/get_byjsonp/"></script>  //返回：<script>fun1("yuan")</script>
	#-----------------------------http://127.0.0.1:8002/get_byjsonp
	
		def get_byjsonp(req):
		    print('8002...')
		    return HttpResponse('fun1("yuan")')

	这其实就是JSONP的简单实现模式，或者说是JSONP的原型：创建一个回调函数，然后在远程服务上调用这个函数并且将JSON 数据形式作为参数传递，完成回调。

	将JSON数据填充进回调函数，这应该就是JSONP的JSON+Padding的含义吧。

      一般情况下，我们希望这个script标签能够动态的调用，而不是像上面因为固定在html里面所以没等页面显示就执行了，很不灵活。我们可以通过javascript动态的创建script标签，这样我们就可以灵活调用远程服务了。
	<button onclick="f()">submit</button>
	<script>
	    function addScriptTag(src){
	     var script = document.createElement('script');
	         script.setAttribute("type","text/javascript");
	         script.src = src;
	         document.body.appendChild(script);
	         document.body.removeChild(script);
	    }
	    function fun1(arg){
	        alert("hello"+arg)
	    }
	    
	    function f(){
	         addScriptTag("http://127.0.0.1:8002/get_byjsonp/")
	    }
	</script>

	 为了更加灵活，现在将你自己在客户端定义的回调函数的函数名传送给服务端，服务端则会返回以你定义的回调函数名的方法，将获取的json数据传入这个方法完成回调：
	<button onclick="f()">submit</button>

	<script>
	    function addScriptTag(src){
	     var script = document.createElement('script');
	         script.setAttribute("type","text/javascript");
	         script.src = src;
	         document.body.appendChild(script);
	         document.body.removeChild(script);
	    }
	    function SayHi(arg){
	        alert("Hello "+arg)
	    }
	
	    function f(){
	         addScriptTag("http://127.0.0.1:8002/get_byjsonp/?callbacks=SayHi")
	    }
	</script>


	----------------------views.py
	def get_byjsonp(req):

    func=req.GET.get("callbacks")

    return HttpResponse("%s('yuan')"%func)

### jQuery对JSONP的实现 ### 
	jQuery框架也当然支持JSONP，可以使用$.getJSON(url,[data],[callback])方法
	<script type="text/javascript">
	    $.getJSON("http://127.0.0.1:8002/get_byjsonp?callback=?",function(arg){
	        alert("hello"+arg)
	    });
	</script>
	结果是一样的，要注意的是在url的后面必须添加一个callback参数，这样getJSON方法才会知道是用JSONP方式去访问服务，callback后面的那个问号是内部自动生成的一个回调函数名。

  	此外，如果说我们想指定自己的回调函数名，或者说服务上规定了固定回调函数名该怎么办呢？我们可以使用$.ajax方法来实现
	<script type="text/javascript" src="/static/jquery-2.2.3.js"></script>

	<script type="text/javascript">
	   $.ajax({
	        url:"http://127.0.0.1:8002/get_byjsonp",
	        dataType:"jsonp",
	        jsonp: 'callbacks',
	        jsonpCallback:"SayHi"
	   });
	    function SayHi(arg){
	        alert(arg);
	    }
	</script>
	#--------------------------------- http://127.0.0.1:8002/get_byjsonp
 	def get_byjsonp(req):

	    callback=req.GET.get('callbacks')
	    print(callback)
	    return HttpResponse('%s("yuan")'%callback)

	当然，最简单的形式还是通过回调函数来处理：
	<script type="text/javascript" src="/static/jquery-2.2.3.js"></script>

	<script type="text/javascript">
	   $.ajax({
	        url:"http://127.0.0.1:8002/get_byjsonp",
	        dataType:"jsonp",            //必须有，告诉server，这次访问要的是一个jsonp的结果。
	        jsonp: 'callbacks',          //jQuery帮助随机生成的：callbacks="wner"
	        success:function(data){
	            alert(data)
	        }
	   });
	
	</script>
 	#-------------------------------------http://127.0.0.1:8002/get_byjsonp
	def get_byjsonp(req):
	
	    callbacks=req.GET.get('callbacks')
	    print(callbacks)                 #wner  
	
	return HttpResponse("%s('yuan')"%callbacks)

 	jsonp: 'callbacks'就是定义一个存放回调函数的键，	jsonpCallback是前端定义好的回调函数方法名'SayHi'，server端接受callback键对应值后就可以在其中填充数据打包返回了; 
   	jsonpCallback参数可以不定义，jquery会自动定义一个随机名发过去，那前端就得用回调函数来处理对应数据了。

　   利用jQuery可以很方便的实现JSONP来进行跨域访问。　　
	<button onclick="f()">submit</button>

	<script src="/static/jquery-1.8.2.min.js"></script>
	<script type="text/javascript">
	    function f(){
	        $.ajax({
	        url:"http://127.0.0.1:8002/get_byjsonp",
	        dataType:"jsonp",
	        jsonp: 'callbacks',
	        success :function(data){        //传过来的数据会被转换成js对象
	            console.log(data);          //Object {name: Array[2]}
	            console.log(typeof data);   //object
	            console.log(data.name)      //["alex", "alvin"]
	        }
	   });
	    }
	</script>
	------------------------------------views.py
	def get_byjsonp(req):
	
	    func=req.GET.get("callbacks")
	
	    a=json.dumps({'name':('alex','alvin')})
	    return HttpResponse("%s(%s)"%(func,a))
	
	
	    #return HttpResponse("%s({'name':('alex','alvin')})"%func)
	
	    #return HttpResponse("%s('hello')"%func)
	    #return HttpResponse("%s([12,34])"%func)
	    #return HttpResponse("%s(5)"%func)

		#views.py 中可以用  request.is_ajax() 方法判断是否是 ajax 请求，需要添加一个 HTTP 请求头：

		#原生javascript：
		#xmlhttp.setRequestHeader("X-Requested-With", "XMLHttpRequest");
		#用 jQuery：
		#用 $.ajax 方法代替 $.get，因为 $.get 在 IE 中不会发送 ajax header
		
		#注意：is_ajax()在跨域ajax请求时不好使