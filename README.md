# ihome_python04

##  项目工程结构搭建

1. 安装依赖包环境    
2. 配置相关文件    
3. 引入日志模块    

## 数据库的建立    
User表(一)：　主键(id);手机号(mobile),密码(password),名字(name),头像(avatar_url)  
认证相关:真实姓名(real_name),身份证号(real_id_card)    

House表(多):主键(id);外键(user_id),区域(area),价格(price),冗余字段(index_image_url,主要图片)--即以空间换取时间   

Area表(一):主键(area_id),名字(name)

House_image表(多)－－House(一):image_id,url,house_id     

Facility表:facility_id,name    
房屋和设施是多对多的关系
House_facility表:id,house_id,facility_id   
因此，需要在设施和房子之外单独建立一个房屋设施表,     

Comment表,因为评论在订单之后,因此评论可以放在订单表中    

Order表:order_id,user_id,house_id,create_time,start_time,end_time,price,amount(金额),days,status,comment,reject_reason

python manage.py db init    
python manage.py db migrate -m "init tables"    
python manage.py db upgrade

关于Flask使用mysql数据库:https://www.cnblogs.com/lonelyhiker/p/8486221.html    

## 静态文件蓝图    
由于自带的会显示127.0.0.1:5000/static/html/xx.html这样不好看,采用蓝图，然后自定义转换器，重新注册路由，使其路径变为127.0.0.1:5000/xx.html    

### CSRF防护机制   
Cookie和请求体中必须有值  
csrf的验证机制:从cookie中获取csrf_token的值,从请求体获取一个csrf_token的值,然后对两个值进行校验,如果这两个值相同,则校验通过,可以进入到视图函数中执行；如果两个值不同,则校验失败,会向前端返回400错误。    
请求中cookie的csrf_token和body的csrf_token需要我们自行进行设置,post,put,delete都会进行csrf验证     

CSRF机制原理    
同源策略:限制了不同源(IP地址和端口号)的网站不能相互操作资源
