#if判断



test1=['username:','password:']
test1[0]=input('Please input your username:')
test1[1]=input('Please input your password:')
if test1[0] == 'root' and  test1[1] =='admin':
       print("欢迎登陆!")
while test1[0] =='root':
       print('1.查看日志')
       print('2.进入应用目录')
       print('3.爱睡懒觉')
       print('4.主程序')
       print('5.能够恢复')
       print('0.退出')
       num=input('请选择功能:')
       if num == '1':
           print('tail -1000f /webservers/server/tomcat7a/logs/catalina.out')
       elif num == '2':
           print("22222222")
       elif num == '3':
           print("3333333")
       elif num == '4':
           print("444444")
       elif num == '5':
           print("5555555")
       elif num == '0':
           exit(2)
       elif num != [1|2|3|4|5]:
           print('请正确输入！')
else:
      print("用户名或密码错误，请重试！")

