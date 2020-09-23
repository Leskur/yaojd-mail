from http.server import BaseHTTPRequestHandler
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
from datetime import datetime


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        host = 'mail.gmx.com'
        port = 587
        user = 'tongren.yaojd@gmx.com'
        password = 'tongren.yaojd'
        message = MIMEText('药京采登录授权失败，请您及时处理。')

        message['From'] = formataddr(('Tongren 药京采', user))
        message['to'] = '466923681@qq.com'
        message['Subject'] = Header('药京采授权登录提醒')

        message['From'] = formataddr(('Tongren', user))
        message['to'] = '173658141@qq.com'
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

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')).encode())
        return
