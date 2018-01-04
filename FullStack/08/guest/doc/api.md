# Web 接口文档
#
## 添加发布会接口 ##


<table cellspacing="0" align='left' >
	<tr >
		<th>名称</th>
		<th>添加发布会</th>
	</tr>
	<tr>
		<th>描述</th>
		<th>添加发布会</th>
	</tr>
	<tr>
		<th>URL</th>
		<th>http://127.0.0.1:8000/api/add_event/</th>
	</tr>
	<tr>
		<th>调用方式</th>
		<th>POST</th>
	</tr>
	<tr>
		<th  rowspan='6'>传入参数</th>
		<th>eid # 发布会 id	</th>

	</tr>
	<tr>	
		<th>name # 发布会标题	</th></tr>
	<tr>
		<th>limit # 限制人数	</th>
	</tr>
	<tr>
		<th>status # 状态	</th>
	</tr>
	<tr>
		<th>address # 地址	</th>
	</tr>
	<tr>
		<th>start_time # 发布会时间 （ 2016-08-10 12:00:00）</th>
	</tr>
	<tr>
		<th>返回值</th>
		<th>
		{'status':200,'message':'add event success'}
		</th>
	</tr>
	<tr>
		<th rowspan='7'>状态码</th>
		<th>start_time # 发布会时间 （ 2016-08-10 12:00:00）</th>
	</tr>
	<tr>
		<th>每一个状态码要有一条用例。</th>
	</tr>
	<tr>
		<th>{'status':10021,'message':'parameter error'}</th>
	</tr>
	<tr>
		<th>{'status':10022,'message':'event id already exists'}</th>
	</tr>
	<tr>
		<th>{'status':10023,'message':'event name already exists'}</th>
	</tr>
	<tr>
		<th>{'status':10024,'message':'start_time format error. It must be in
			YYYY-MM-DD HH:MM:SS format.'}</th>
	</tr>
	<tr>
		<th>{'status':200,'message':'add event success'}</th>
	</tr>
	<tr>
		<th>说明</th>
		<th></th>
	</tr>
</table>

#------


## 添加嘉宾接口 ##
<table cellspacing="0" align='left' >
	<tr >
		<th>名称</th>
		<th>添加嘉宾接口</th>
	</tr>
	<tr>
		<th>描述</th>
		<th>添加嘉宾接口</th>
	</tr>
	<tr>
		<th>URL</th>
		<th>http://127.0.0.1:8000/api/add_guest/</th>
	</tr>
	<tr>
		<th>调用方式</th>
		<th>POST</th>
	</tr>
	<tr>
		<th  rowspan='4'>传入参数</th>
		<th>id # 关联发布会 id</th>

	</tr>
	<tr>	
		<th>realname # 姓名	</th></tr>
	<tr>
		<th>phone # 手机号</th>
	</tr>
	<tr>
		<th>email # 邮箱</th>
	</tr>
	<tr>
		<th>返回值</th>
		<th>
		{'status':200,'message':'add guest success'}
		</th>
	</tr>
	<tr>
		<th rowspan='7'>状态码</th>
		<th>{'status':10021,'message':'parameter error'}</th>
	</tr>
	<tr>
		<th>{'status':10022,'message':'event id null'}</th>
	</tr>
	<tr>
		<th>{'status':10023,'message':'event status is not available'}</th>
	</tr>
	<tr>
		<th>{'status':10024,'message':'event number is full'}</th>
	</tr>
	<tr>
		<th>{'status':10025,'message':'event has started'}</th>
	</tr>
	<tr>
		<th>{'status':10026,'message':'the event guest phone number repeat'}</th>
	</tr>
	<tr>
		<th>{'status':200,'message':'add guest success'}</th>
	</tr>
	<tr>
		<th>说明</th>
		<th></th>
	</tr>
</table>


## 3、 查询发布会接口 ##
<table cellspacing="0" align='left' >
	<tr >
		<th>名称</th>
		<th>查询发布会接口</th>
	</tr>
	<tr>
		<th>描述</th>
		<th>查询发布会接口</th>
	</tr>
	<tr>
		<th>URL</th>
		<th>http://127.0.0.1:8000/api/get_event_list/</th>
	</tr>
	<tr>
		<th>调用方式</th>
		<th>GET</th>
	</tr>
	<tr>
		<th  rowspan='2'>传入参数</th>
		<th>id #发布会 id</th>

	</tr>
	<tr>	
		<th>name #发布会名称</th></tr>
	<tr>
		<th>返回值</th>
		<th>
			{
			"data": {
			"start_time": "2016-12-10T14:00:00",
			"name": "小米手机 6 发布会",
			"limit": 2000,
			"address": "北京水立方",
			"status": true
			},
			"message": "success",
			"status": 200
			}
		</th>
	</tr>
	<tr>
		<th rowspan='3'>状态码</th>
		<th>{'status':10021,'message':'parameter error'}</th>
	</tr>
	<tr>
		<th>{'status':10022, 'message':'query result is empty'}</th>
	</tr>
	<tr>
		<th>{'status':200, 'message':'success', 'data':datas}</th>
	</tr>
	<tr>
		<th>说明</th>
		<th> id 或 name 两个参数二选一</th>
	</tr>
</table>


## 4、 查询嘉宾接口 ##
<table cellspacing="0" align='left' >
	<tr >
		<th>名称</th>
		<th>查询嘉宾接口</th>
	</tr>
	<tr>
		<th>描述</th>
		<th>查询嘉宾接口</th>
	</tr>
	<tr>
		<th>URL</th>
		<th>http://127.0.0.1:8000/api/get_guest_list/</th>
	</tr>
	<tr>
		<th>调用方式</th>
		<th>GET</th>
	</tr>
	<tr>
		<th  rowspan='2'>传入参数</th>
		<th>id # 关联发布会 id</th>

	</tr>
	<tr>	
		<th>phone # 嘉宾手机号</th></tr>
	<tr>
		<th>返回值</th>
		<th>
			{
				"data": [
				{
				"email": "david@mail.com",
				"phone": "13800110005",
				"realname": "david",
				"sign": false
				},
				{
				"email": "david@mail.com",
				"phone": "13800110005",
				"realname": "david",
				"sign": false
				},
				{
				"email": "david@mail.com",
				"phone": "13800110005",
				"realname": "david",
				"sign": false
				}
				],
				"message": "success",
				"status": 200
			}
		</th>
	</tr>
	<tr>
		<th rowspan='3'>状态码</th>
		<th>{'status':10021,'message':'eid cannot be empty'}</th>
	</tr>
	<tr>
		<th>{'status':10022, 'message':'query result is empty'}</th>
	</tr>
	<tr>
		<th>{'status':200, 'message':'success', 'data':datas}</th>
	</tr>
	<tr>
		<th>说明</th>
		<th></th>
	</tr>
</table>


## 5、 嘉宾签到接口

<table cellspacing="0" align='left' >
	<tr >
		<th>名称</th>
		<th>嘉宾签到接口</th>
	</tr>
	<tr>
		<th>描述</th>
		<th>嘉宾签到接口</th>
	</tr>
	<tr>
		<th>URL</th>
		<th>http://127.0.0.1:8000/api/user_sign/</th>
	</tr>
	<tr>
		<th>调用方式</th>
		<th>GET</th>
	</tr>
	<tr>
		<th  rowspan='2'>传入参数</th>
		<th>id # 发布会 id</th>

	</tr>
	<tr>	
		<th>phone # 嘉宾手机号</th></tr>
	<tr>
		<th>返回值</th>
		<th>
			{'status':200,
			'message':'sign success'
			}
		</th>
	</tr>
	<tr>
		<th rowspan='3'>状态码</th>
		<th>{'status':10021,'message':'parameter error'}</th>
	</tr>
	<tr>
		<th>{'status':10022,'message':'event id null'}</th>
	</tr>
	<tr>
		<th>{'status':10023,'message':'event status is not available'}</th>
	</tr>
	<tr>
		<th>{'status':10024,'message':'user phone null'}</th>
	</tr>
	<tr>
		<th>{'status':10025,'message':'user did not participate in the conference'}</th>
	</tr>
	<tr>
		<th>{'status':10026,'message':'user has sign in'}</th>
	</tr>
	<tr>
		<th>{'status':200,'message':'sign success'}</th>
	</tr>
	<tr>
		<th>说明</th>
		<th></th>
	</tr>
</table>