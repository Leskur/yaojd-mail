import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

host = 'mail.gmx.com'
port = 587
user = 'tongren.yaojd@gmx.com'
password = 'tongren.yaojd'
message = MIMEText('药京采登录授权失败，请您及时处理。')

message['From'] = formataddr(('Tongren 药京采', user))
message['to'] = 'tongren.yaojd@gmx.com'
message['Subject'] = Header('药京采授权登录提醒')

try:
    smtp = smtplib.SMTP(host, port)
    smtp.starttls()
    smtp.login(user, password)
    smtp.sendmail(user, '173658141@qq.com', message.as_string())
    smtp.quit()
except smtplib.SMTPException as e:
    print(repr(e))
    print('邮件发送失败')
