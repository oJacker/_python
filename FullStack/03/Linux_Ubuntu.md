## Ubuntu ## 

### 语言环境
### 查看是否安装了中文支持

	locale -a 
如果有 zh_CN.utf8 则表示系统已经安装了中文locale，如果没有则需要安装相应的软件包。安装方式如下：

sudo apt-get install language-pack-zh-hans language-pack-zh-hans-base

软件管理 apt ( Advanced Packaging Tool ) , 他可以自动下载、配置、安装软件包；简化了Linux系统上的。Debian及衍生版中都包含了apt ， RedHat系列的linux的则使用yum来进行管理，其中Fedora22中Centos7中开始使用dnf 来替代yum。

	apt-cache search package 搜索包
	apt-cache show package 获取包的相关信息，如说明、大小、版本等
	sudo apt-get install package 安装包
	sudo apt-get install package –reinstall 重新安装包
	sudo apt-get -f install 强制安装
	sudo apt-get remove package 删除包
	sudo apt-get remove package –purge 删除包，包括删除配置文件等
	sudo apt-get autoremove 自动删除不需要的包
	sudo apt-get update 更新源
	sudo apt-get upgrade 更新已安装的包
	sudo apt-get dist-upgrade 升级系统
	sudo apt-get dselect-upgrade 使用 dselect 升级
	apt-cache depends package 了解使用依赖
	apt-cache rdepends package 了解某个具体的依赖
	sudo apt-get build-dep package 安装相关的编译环境
	apt-get source package 下载该包的源代码
	sudo apt-get clean && sudo apt-get autoclean 清理下载文件的存档
	sudo apt-get check 检查是否有损坏的依赖
### apt的配置文件

	/etc/apt/sources.list 设置软件包的获取来源
	/etc/apt/apt.conf apt配置文件
	/etc/apt/apt.conf.d apt的零碎配置文件
	/etc/apt/preferences 版本参数
	/var/cache/apt/archives/partial 存放正在下载的软件包
	/var/cache/apt/archives 存放已经下载的软件包
	/var/lib/apt/lists 存放已经下载的软件包详细信息
	/var/lib/apt/lists/partial 存放正在下载的软件包详细信息

### 软件源配置文件格式： 
	deb http://security.ubuntu.com/ubuntu xenial-security main restricted
	# deb-src http://security.ubuntu.com/ubuntu xenial-security main restricted
	deb http://security.ubuntu.com/ubuntu xenial-security universe
	# deb-src http://security.ubuntu.com/ubuntu xenial-security universe
	deb http://security.ubuntu.com/ubuntu xenial-security multiverse
	# deb-src http://security.ubuntu.com/ubuntu xenial-security multiverse

Ubuntu 软件仓库被分为四个部分:main（主要的）, restricted（受限的）, universe（广泛的） ， multiverse（多元的），这主要根据我们对软件的支持能力，以及软件的目的是否符合我们的 自由软件哲学。 

先看了一下配置文件的一段内容：

第一个deb表示软件包的格式，可以是 deb 或 deb-src，前者表示所指向的存放 binary 格式(已编译)，后者为 sources 格式(原代码)。
第二个URI，即 Universal Resource Identifier，通用资源标识符，可以是以：file(系统) 、 cdrom(光驱) 、 http 、 ftp、copy 、rsh 、ssh 等几个参数开头的软件包所在位置。
第三个Distribution 指发行版本号，可以是：stable，testing，unstable，sarge，etch，sid 等，具体可参考Debian文档。

后面的几个component表示具体的软件包分类：
	main：完全遵循 Debian  自由软件准则 即DFSG的软件包；
	contrib：软件包均遵循DFSG自由使用原则，但是其使用了某些不符合DFSG的第三方库；
	non-free：不符合DFSG的软件包。

dpkg是Debian软件包管理器的基础，被用于安装、卸载和供给和.deb软件包相关的信息。dpkg本身是一个底层的工具，本身并不能从远程包仓库下载包以及处理包的依赖的关系，需要将包从远程下载后再安装。DPKG常用命令：

	dpkg -i package.deb 安装包
	dpkg -r package 删除包
	dpkg -P package 删除包（包括配置文件）
	dpkg -L package 列出与该包关联的文件
	dpkg -l package 显示该包的版本
	dpkg –unpack package.deb 解开 deb 包的内容
	dpkg -S keyword 搜索所属的包内容
	dpkg -l 列出当前已安装的包
	dpkg -c package.deb 列出 deb 包的内容
	dpkg –configure package 配置包


### data: 用来显示或设定系统的日期和与时间 ###

	date //显示当前日期
	# 日期格式化
	#       %Y     year
	#       %m     month (01..12)
	#       %d     day of month (e.g., 01)
	#       %H     hour (00..23)
	#       %I     hour (01..12)
	#       %M     minute (00..59)
	#       %S     second (00..60)
	date +"%Y%m%d %H%M%S"
	    20160824 223856
	date +"%Y-%m-%d %H:%M:%S"
	    2016-08-24 22:39:07
	
	date -s //设置当前时间，只有root权限才能设置，其他只能查看。
	date -s 20061010 //设置成20061010，这样会把具体时间设置成空00:00:00
	date -s 12:23:23 //设置具体时间，不会对日期做更改
	date -s “12:12:23 2006-10-10″ //这样可以设置全部时间
	
	# 注意： 重新设置时间后需要将时间捅不到硬件时钟。方式如下：
	hwclock -w    

### cal : 显示一个日历 ###

	cal  #  现实当前月份的日历
	cal -y  # 显示当年的日历
	cal 2016 #  # 显示指定年份的日历

### 设置时区 ### 
	tzselect
	
	# 或者
	
	cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime 

### 修改密码：  ###
	# 修改密码的命令
	passwd # 默认修改当前用户的密码
	
	passwd username # 修改指定用户的密码，需要管理员权限

### 忘记密码 ###

	开始时长按shift键，进入grub菜单-->  按字母e 进入编辑模式 --> 编辑内容--> 启动 进入但用户模式 ，重新设置用户密码，-->  按照F10重启 -- >  使用新密码进入系统
	修改内容 linux ro***  为 rw single init=/bin/bash

### 注销/重启/关机 ###
	logout  # 注销

	reboot  # 重启系统： 需要管理员全新啊
	
	shutdown # 关机： 需要管理员权限
	shutdown -r now # 现在立即重启
		shutdown -r +5  # 三分钟后重启
		shutdown -r 12:12    #在12:12时将重启计算机		
		shutdown -h now # 现在立即关机
		shutdown -h +5  “The System will shutdown after 3 minutes”   # 提示使用者将在三分钟后关机
		shutdown -h +5   #  5分钟后关机
		shutdown -h 12:00  # 12点钟关机
		shutdown -c   # 取消关机操作
### cd  ： 切换目录 ###
	cd  # 回到当前用户的家目录
	# ～  可用于表示用户家目录
	cd  /etc # 切换到/etc目录
	cd - 
	# 切换到上一次的目录
### pwd ： 查看当前的工作路径 ###

###创建目录： ###

	# mkdir 目录名
	mkdir my_dir
	
	# - p 参数 : 递归创建目录，用于同时创建多级目录
	mkdir   a/b/c/d   

### 获取帮助 ###
	-h  --help  info  man 
	man man  # 查看man命令的手册  
	man  cd 
	man  pwd 
	man 5 passwd
	man -k passwd # 模糊查找
	man -f  passwd  # 精确查找 
### 创建文件 ###
touch ： 改变文件或目录的时间，文件不存在时会创建一个空文件。

	touch file1 # file1 不存在时被创建
	touch -c file1 # 不创建文件
	touch -r ref_file file1  更新file1.txt的时间戳和ref+file相同
	touch -t 201210120505.25 file1
	#  -t  time 使用指定的时间值 time 作为指定文件相应时间戳记的新值．此处的 # # time规定为如下形式的十进制数:      
	#  [[CC]YY]MMDDhhmm[.SS]     
	#   这里，CC为年数中的前两位，即”世纪数”；YY为年数的后两位，即某世纪中的年数．如果不给出CC的值，则touch   将把年数CCYY限定在1969--2068之内．MM为月数，DD为天将把年数CCYY限定在1969--2068之内．MM为月数，DD为天数，hh 为小时数(几点)，mm为分钟数，SS为秒数．此处秒的设定范围是0--61，这样可以处理闰秒．这些数字组成的时间是环境变量TZ指定的时区中的一个时 间．由于系统的限制，早于1970年1月1日的时间是错误的

注意： 如果文件以 ”.“ 开头，则表示文件是隐藏文件。 

### rm ： 删除命令


	rm -f  file1 # 强制删除文件
	rm -r  a/b/file1  # 删除指定目录及其下的所有文件和目录
	rm -rf  a/b/file1  #  强制删除指定目录及其下的所有文件和目录
	# rm 命令太危险，不建议使用

### mv  ： 移动或重命令文件或目录 
	mv SOURCE DEST  # 
	mv test.log test.txt  # 文件改名
	mv test1.txt dir1/      #移动文件
	mv test1.txt  test2.tx  test3.tx dir1/      #移动多个文件
### cp ： 复制 
	cp SOURCE DEST # 复制文件
	cp -i  SOURCE DEST  #   如果遇到需要覆盖的情况，则提示
	cp -r  dir1  dir2  # 若给出的源文件是一目录文件，此时cp将递归复制该目录下所有的子目录和文件。此时目标文件必须为一个目录名
	cp -p  file1 file2  #  此时cp除复制源文件的内容外，还将把其修改时间和访问权限也复制到新文件中。
	
	cp -rp dir1  dir2