# CMDB 介绍（Configuration Management Database）
	CMDB存储与管理企业IT架构中设备的各种配置信息，它与所有服务支持和服务交付流程都紧密相联，支持这些流程的运转、发挥配置信息的价值，同时依赖于相关流程保证数据的准确性。

在实际的项目中，CMDB常常被认为是构建其它ITIL流程的基础而优先考虑，ITIL项目的成败与是否成功建立CMDB有非常大的关系。
70%～80%的IT相关问题与环境的变更有着直接的关系。实施变更管理的难点和重点并不是工具，而是流程。即通过一个自动化的、可重复的流程管理变更，使得当变更发生的时候，有一个标准化的流程去执行，能够预测到这个变更对整个系统管理产生的影响，并对这些影响进行评估和控制。而变更管理流程自动化的实现关键就是CMDB。
CMDB工具中至少包含这几种关键的功能：整合、调和、同步、映射和可视化。

	整合是指能够充分利用来自其他数据源的信息，对CMDB中包含的记录源属性进行存取，将多个数据源合并至一个视图中，生成连同来自CMDB和其他数据源信息在内的报告；
	调和能力是指通过对来自每个数据源的匹配字段进行对比，保证CMDB中的记录在多个数据源中没有重复现象，维持CMDB中每个配置项目数据源的完整性；自动调整流程使得初始实施、数据库管理员的手动运作和现场维护支持工作降至最低；
	同步指确保CMDB中的信息能够反映联合数据源的更新情况，在联合数据源更新频率的基础上确定CMDB更新日程，按照经过批准的变更来更新 CMDB，找出未被批准的变更；
	应用映射与可视化，说明应用间的关系并反应应用和其他组件之间的依存关系，了解变更造成的影响并帮助诊断问题。


## CMDB建模思路

    配置管理面向消费，发挥数据价值
    配置管理以数据和模型为核心
    配置管理以整合的思路推进
    配置元模型和分视角模型相结合


www.cnblogs.com/alex3714/articles/5420433.html

# 浅谈ITIL
TIL即IT基础架构库(Information Technology Infrastructure Library, ITIL，信息技术基础架构库)由英国政府部门CCTA(Central Computing and Telecommunications Agency)在20世纪80年代末制订，现由英国商务部OGC(Office of Government Commerce)负责管理，主要适用于IT服务管理（ITSM）。ITIL为企业的IT服务管理实践提供了一个客观、严谨、可量化的标准和规范。

1、事件管理（Incident Management）

事故管理负责记录、归类和安排专家处理事故并监督整个处理过程直至事故得到解决和终止。事故管理的目的是在尽可能最小地影响客户和用户业务的情况下使IT系统恢复到服务级别协议所定义的服务级别。

2、问题管理（Problem Management）

问题管理是指通过调查和分析IT基础架构的薄弱环节、查明事故产生的潜在原因，并制定解决事故的方案和防止事故再次发生的措施，将由于问题和事故对业务产生的负面影响减小到最低的服务管理流程。与事故管理强调事故恢复的速度不同，问题管理强调的是找出事故产生的根源，从而制定恰当的解决方案或防止其再次发生的预防措施。

3、配置管理（Configuration Management）

配置管理是识别和确认系统的配置项，记录和报告配置项状态和变更请求，检验配置项的正确性和完整性等活动构成的过程，其目的是提供IT基础架构的逻辑模型，支持其它服务管理流程特别是变更管理和发布管理的运作。

4、变更管理（Change Management）

变更管理是指为在最短的中断时间内完成基础架构或服务的任一方面的变更而对其进行控制的服务管理流程。变更管理的目标是确保在变更实施过程中使用标准的方法和步骤，尽快地实施变更，以将由变更所导致的业务中断对业务的影响减小到最低。

5、发布管理（Release Management）

 发布管理是指对经过测试后导入实际应用的新增或修改后的配置项进行分发和宣传的管理流程。发布管理以前又称为软件控制与分发

事件管理的目标是在不影响业务的情况下，尽可能快速的恢复服务，从而保证最佳的效率和服务的可持续性。事件管理流程的建立包括事件分类，确定事件的优先级和建立事件的升级机制。

问题管理是调查基础设施和所有可用信息，包括事件数据库，来确定引起事件发生的真正潜在原因，一起提供的服务中可能存在的故障。

配置管理的目标是：定义和控制服务与基础设施的部件，并保持准确的配置信息。

变更管理的目标是：以受控的方式，确保所有变更得到评估、批准、实施和评审。

发布管理的目标是：在实际运行环境的发布中，交付、分发并跟踪一个或多个变更。

服务台：服务台是IT部门和IT服务用户之间的单一联系点。它通过提供一个集中和专职的服务联系点促进了组织业务流程与服务管理基础架构集成。服务台的主要目标是协调客户（用户）和IT部门之间的联系，为IT服务运作提供支持，从而提高客户的满意度。


# CMDB 资产管理部分实现 

## 需求

    •存储所有IT资产信息
    •数据可手动添加
    •硬件信息可自动收集
    •硬件信息可自动变更
    •可对其它系统灵活开放API
    •API接口安全认证

## 配置项分析
	

每个配置项需存储的属性信息分析

## 立业之本：定义表结构

    各种硬件都能存
    资产变更有纪录
    资产ID永不变
    资产要有状态机

## 重中之重：接口设计好 

    可对内外灵活开放接口
    接口定义要标准化
    一定要提供排错依据
    数据返回要标准
    要能增删改查
    所有异常要抓住
    接口安全要注意

## 表结构设计　






## CMDB资产数据自动汇报及更新流程图

	https://www.processon.com/view/link/571b4b2ce4b049474cc87feb 
	自定义用户认证
	
	https://docs.djangoproject.com/en/1.9/topics/auth/customizing/#django.contrib.auth.models.PermissionsMixin.has_perms 
	浅谈Restful API
	
	理解RESTful架构 :http://www.ruanyifeng.com/blog/2011/09/restful 

RESTful API 设计指南 :http://www.ruanyifeng.com/blog/2014/05/restful_api.html　