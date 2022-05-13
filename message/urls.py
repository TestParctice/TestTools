from django.conf.urls import url
from message import views

app_name = 'message'

urlpatterns = [
    url("login$", views.login, name='login'),
    url("login_check$", views.login_check, name='login_check'),
    url("index$", views.index, name='index'),
    url("verify_code$", views.verify_code, name='verify_code'),
    url("getmsg$", views.getmsg, name='getmsg'),
    url("getall$", views.getall, name='getall'),
    url("getidCard", views.getidCard, name='getidCard'),
    url("getvin", views.getvin, name='getvin'),
    url("getname", views.getname, name='getname'),
    url("getphone", views.getphone, name='getphone'),
    url("getorganization", views.getorganization, name='getorganization'),
    url("getsocial_credit", views.getsocial_credit, name='getsocial_credit'),
    url("getzzm", views.getzzm, name='getzzm'),
    url("getgonghang", views.getgonghang, name='getgonghang'),
    url("getnonghang", views.getnonghang, name='getnonghang'),
    url("getjianshe", views.getjianshe, name='getjianshe'),
    url("getzhongguo", views.getzhongguo, name='getzhongguo'),
    url("getjiaotong", views.getjiaotong, name='getjiaotong'),
]
