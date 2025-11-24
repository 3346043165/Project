import yagmail
def fs(a):
    ele=yagmail.SMTP(user='3346043165@qq.com',password='nfmqstiuaooscjfe',host='smtp.qq.com')
    ele.send(to='3346043165@qq.com',subject="练习",contents='任务',attachments=a)