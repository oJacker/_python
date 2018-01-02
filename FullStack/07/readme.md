Admin Management

	1: login and register
	2: teacher
	3: scdu

#### developer: ####
	1:定义数据库表结构
		表结构关系
			学员班级多对一
		class Classes(models.Model):
			caption = models.CharField(max_length=32)
		class Student(models.Model):
			name = models.CharField(max_lenth=32)
			cls = models.ForignKey('Classes',on_delete=)

			username = models.CharField(max_length=32)
			password = models.CharField(max_length=32)
		
		class Teacher(model.Model):
			name = models.CharFiled(max_length= 32)
			cls = models.ManytoMany('Classes')
			
			username = models.CharField(max_length=32)
			password = models.CharField(max_length=32)
		# 第三张
		#第四张
	2:登录、注册
		-登录
			- Form
			- Ajax
			- 成功： 记住状态 ，保存回话
			- 失败   错误提示 