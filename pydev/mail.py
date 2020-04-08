import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
def mail_send(receiver_mail_address):
    mail_host="smtp.163.com"
    mail_user="dustinduan2010"
    mail_pass="acdd1234"
    
    sender="dustinduan2010@163.com"
    receivers=receiver_mail_address
    
    mail_text=input("请输入右键正文内容:")
    message = MIMEText(mail_text, 'plain', 'utf-8')
    sender_name=input("请输入发件人的名称：")
    message['From'] = Header(sender_name, 'utf-8')
    to_name=input("请输入收件人的称呼：")
    message['To'] =  Header(to_name, 'utf-8')
    
    subject=input('请输入右键标题:')
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host,25)# 25 为 SMTP 端口号
        smtpObj.login(mail_user,mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print ("邮件发送成功")
    except smtplib.SMTPException:
        print ("Error: 无法发送邮件")

mail_send("15952415736@139.com")
