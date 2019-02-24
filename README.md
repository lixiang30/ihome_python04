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


