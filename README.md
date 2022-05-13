# TestTools
测试工具
Django版本：Django:3.2.13
使用时需要在TestTools下增加config文件，用来保存数据库信息，
例如：
config.py:
mysql_message = {'ENGINE': 'django.db.backends.mysql',
                 'NAME': '***',
                 'USER': '***',
                 'PASSWORD': '***',
                 'HOST': '***',
                 'PORT': '***'}
