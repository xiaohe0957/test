import os
from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

if __name__ == '__main__':
    send_mail(
        '测试邮件',
        '测试',
        '1192309555@qq.com',
        ['656086914@qq.com'],
    )