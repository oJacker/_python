## Base Introduction ##

###Coding###
	ASSIC 字符统都由8个bit来存储

### Computer capacity
	位 bit (比特)(Binary Digits)：存放一位二进制数，即 0 或 1，最小的存储单位。
	字节 byte：8个二进制位为一个字节(B)，最常用的单位。
	1B（bytes） = 8bit
	1KB (Kilobyte 千字节)=1024B，
	1MB (Megabyte 兆字节 简称“兆”)=1024KB，
	1GB (Gigabyte 吉字节 又称“千兆”)=1024MB，
	1TB(Trillionbyte 万亿字节 太字节)=1024GB，
	1PB（Petabyte 千万亿字节 拍字节）=1024TB，
	1EB（Exabyte 百亿亿字节 艾字节）=1024PB，
	1ZB (Zettabyte 十万亿亿字节 泽字节)= 1024 EB,
	1YB (Yottabyte 一亿亿亿字节 尧字节)= 1024 ZB,
	1BB (Brontobyte 一千亿亿亿字节)= 1024 YB

### eg. 硬盘空间少比买的时候要少？是因为 换算时他们将 1024 按照 1000来算###
	256G的硬盘： 256G= ？ Bytes：按1000来算
	256G 硬盘
	1K = 1000B
	1M = 1000K
	1G = 1000M = 1000*1000*1000B =1000000000B
	256G = 256000000000B
	256000000000/1024/1024/1024 B = 238.4185791015625 G
	500GB*1000*1000*1000/1024/1024/1024=465.66	

### Binary 二进制
	1024 516 256 128 64 32 16 8 4 2 1
	 1    1   1   1  1   1  1 1 1 1 1
	 2 ** 4 = 16
	 2 ** 5 = 32
	 2 ** 6 = 64
	 逢二进一
### ASCII table totel（127）
	001 = 1 -> a
	010 = 2 -> b
	011 = 3 -> c
	100 = 4 -> d
	001010011100 = abc
### Octonary 八进制
	逢八进一
	01234567
	作用： 在某些编程语言里提供了使用八进制符号来表示数字的能力，而且还是有一些比较古老的Unix应用在使用八进制。
	和二进制之间的转换：
	2-->8 :  取三合一     8-->2 ： 取一分三
**注释** 二进制使用起来很不方便， 16进制或8进制可以解决这个问题。因为，进制越大，数的表达长度也就越短。不过，为什么偏偏是16或8进制，而不其它的?2、8、16，分别是2的1次方、3次方、4次方。这一点使得三种进制之间可以非常直接地互相转换。8进制或16进制缩短了二进制数，但保持了二进制数的表达特点

### Hexadecimal  十六进制
	逢十六进一
	01234567ABCDEF 
### Decimal 十进制
	 逢十进一
	 表示数字： 0123456789	


### Introduction to programming language
What is a programming language
	
	1：与计算机交互的语法规则，这套规则 就可称为一门编程语言

	C 语言，各个操作系统的开发语言1973 C++ = C++是C语言的加强版，1983年，贝尔实验室的Bjarne Stroustrup在C语言基础上推出了C++[1]  。 C++进一步扩充和完善了C语言，是一种面向对象的程序设计语言
	
	java ： 1995 由sun 公司开发出来，java 虚拟机 支持跨平台 
	
	php ： 1994, 纯web开发语言， 1994 Netscape 浏览器诞生了
	
	python ：  1989年诞生， 刚开始被做为脚本语言， 开发小任务， 跟linux同年诞生，89，1991,苏联解体， 1991年正式版本
	
	C#、csharpe  C#是微软公司发布的一种面向对象的、运行于.NET Framework之上的高级程序设计语言。并定于在微软职业开发者论坛(PDC)上登台亮相。C#是微软公司研究员Anders Hejlsberg的最新成果。C#看起来与Java有着惊人的相似；它包括了诸如单一继承、接口、与Java几乎同样的语法和编译成中间代码再运行的过程。但是C#与Java有着明显的不同，它借鉴了Delphi的一个特点，与COM（组件对象模型）是直接集成的，而且它是微软公司 .NET windows网络框架的主角。

	Ruby 一种简单快捷的面向对象（面向对象程序设计）脚本语言，在20世纪90年代由日本人松本行弘(Yukihiro Matsumoto)开发，遵守GPL协议和Ruby License。它的灵感与特性来自于 Perl、Smalltalk、Eiffel、Ada以及 Lisp 语言。由 Ruby 语言本身还发展出了JRuby（Java平台）、IronRuby（.NET平台）等其他平台的 Ruby 语言替代品。Ruby的作者于1993年2月24日开始编写Ruby，直至1995年12月才正式公开发布于fj（新闻组）。因为Perl发音与6月诞生石pearl（珍珠）相同，因此Ruby以7月诞生石ruby（红宝石）命名。
	Ruby on rails web框架
	perl ： Unix平台上开发出来的语言，做文字处理非常强大， 可以写出没人能看懂的代码
	
	Scala 是一门多范式的编程语言，一种类似java的编程语言[1] ,大数据开发

	erlang 是一种通用的面向并发的编程语言，它由瑞典电信设备制造商爱立信，函数式编程
	
	Go语言是谷歌2009发布的第二款开源编程语言。Go语言专门针对多处理器系统应用程序的编程进行了优化，使用Go编译的程序可以媲美C或C++代码的速度，而且更加安全、支持并行进程

	javascript 是当下使用最为广泛的语言，主要写前端的语言，nodejs  后端 全栈式的语言

	vb  微软的脚本语言，bat脚本

	lua  nginx 的脚本语言， ngnix 是时下最nb web服务器

### Python Introduction
	目前Python主要应用领域：
    云计算: 云计算最火的语言， 典型应用OpenStack
    WEB开发: 众多优秀的WEB框架，众多大型网站均为Python开发，Youtube, Dropbox,
    豆瓣。。。， 典型WEB框架有Django
    科学运算、人工智能: 典型库NumPy, SciPy, Matplotlib, Enthought librarys,pandas
    系统运维: 运维人员必备语言
    金融：量化交易，金融分析，在金融工程领域，Python不但在用，且用的最多，
	而且重要性逐年提高。原因：作为动态语言的Python，语言结构清晰简单，库丰富，
	成熟稳定，科学计算和统计分析都很牛逼，生产效率远远高于c,c++,java,
	尤其擅长策略回测 图形GUI: PyQT, WxPython,TkInter
	Python在一些公司的应用： 

    谷歌：Google App Engine 、code.google.com 、Google earth 、谷歌爬虫、Google广告等项目都在大量使用Python开发
    CIA: 美国中情局网站就是用Python开发的
    NASA: 美国航天局(NASA)大量使用Python进行数据分析和运算
    YouTube:世界上最大的视频网站YouTube就是用Python开发的
    Dropbox:美国最大的在线云存储网站，全部用Python实现，每天网站处理10亿个文件的上传和下载
    Instagram:美国最大的图片分享社交网站，每天超过3千万张照片被分享，全部用python开发
    Facebook:大量的基础库均通过Python实现的
    Redhat: 世界上最流行的Linux发行版本中的yum包管理工具就是用python开发的
    豆瓣: 公司几乎所有的业务均是通过Python开发的
    知乎: 国内最大的问答社区，通过Python开发(国外Quora)
    春雨医生：国内知名的在线医疗网站是用Python开发的
    除上面之外，还有搜狐、金山、腾讯、盛大、网易、百度、阿里、淘宝 、土豆、新浪、果壳等公司都在使用Python完成各种各样的任务。
	
###按编译分类###
	编译型 = 全部翻译，再执行  ，翻译=编译  ，c,c++
	解释型 = 边执行边翻译， python php java c# 
	perl ruby javascript 	

 [详情](http://www.cnblogs.com/resn/p/5775378.html)