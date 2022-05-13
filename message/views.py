from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from utils.method_public import nowTime, verify_code_way, ident_generator, random_vin, random_name, phone_num, \
    create_organization, create_social_credit, ZZM, gen_bank_card_gonghang, gen_bank_card_nonghang, \
    gen_bank_card_jainshe, gen_bank_card_zhongguo, gen_bank_card_jiaotong
from message.models import UserInfo
from django.urls import reverse


# Create your views here.

def login(request):
    """
        登录，如果cookie中有登录信息，则自动填充用户名
        :param request:
        :return:
        """
    # if request.session['islogin'] == True:
    #     username = request.COOKIES['username']
    #     return render(request, template_name='message/index.html', context={"username": username})
    if 'username' in request.COOKIES:
        username = request.COOKIES['username']
    else:
        username = ""
    return render(request, template_name='message/login.html', context={"username": username})


def login_check(request):
    """
    检查登录状态是否正确
    :param request:
    :return:
    """
    username = request.POST.get('username')
    password = request.POST.get('password')
    remember = request.POST.get('remember')
    vcode = request.POST.get('vcode')
    userinfo = UserInfo.objects.filter(username=username).filter(isDel=0)
    if password == userinfo[0].password and vcode == request.session['verifycode']:
        response = redirect(reverse("message:index"))
        if remember == 'on':
            request.session['islogin'] = True
            request.session['username'] = username
            response.set_cookie('username', username, max_age=30 * 24 * 3600)
            return response
        request.session['username'] = username
        return response
    return redirect(reverse("message:login"))


def index(request):
    username = request.session['username']
    return render(request, template_name='message/index.html', context={"username": username})


def verify_code(request):
    """
    获取当前验证码
    :param request:
    :return:
    """
    return verify_code_way(request)


def getmsg(request):
    return render(request, template_name='message/test_msg.html')


def getall(request):
    idCard = ident_generator()  # 身份证号码
    vin = random_vin()  # 车辆车架号
    name = random_name()  # 姓名
    phone = phone_num()  # 电话
    organization = create_organization()  # 组织机构代码
    social_credit = create_social_credit()  # 统一社会信用代码
    zzm = ZZM()  # 中征码
    gonghang = gen_bank_card_gonghang()  # 工商银行卡
    nonghang = gen_bank_card_nonghang()  # 农行
    jianshe = gen_bank_card_jainshe()  # 建设
    zhongguo = gen_bank_card_zhongguo()  # 中国
    jiaotong = gen_bank_card_jiaotong()  # 交通
    list = [name, idCard, phone, social_credit, organization, vin, zzm, gonghang, nonghang, jiaotong, zhongguo, jianshe]
    return JsonResponse({"allMsg": list})


def getidCard(request):
    idCard = ident_generator()  # 身份证号码
    list = [idCard]
    return JsonResponse({"idCard": list})


def getvin(request):
    vin = random_vin()  # 车辆车架号
    list = [vin]
    return JsonResponse({"vin": list})


def getname(request):
    name = random_name()  # 姓名
    list = [name]
    return JsonResponse({"name": list})


def getphone(request):
    phone = phone_num()  # 电话
    list = [phone]
    return JsonResponse({"phone": list})


def getorganization(request):
    organization = create_organization()  # 组织机构代码
    list = [organization]
    return JsonResponse({"organization": list})


def getsocial_credit(request):
    social_credit = create_social_credit()  # 统一社会信用代码
    list = [social_credit]
    return JsonResponse({"social_credit": list})


def getzzm(request):
    zzm = ZZM()  # 中征码
    list = [zzm]
    return JsonResponse({"zzm": list})


def getgonghang(request):
    gonghang = gen_bank_card_gonghang()  # 工商银行卡
    list = [gonghang]
    return JsonResponse({"gonghang": list})


def getnonghang(request):
    nonghang = gen_bank_card_nonghang()  # 农行
    list = [nonghang]
    return JsonResponse({"nonghang": list})


def getjianshe(request):
    jianshe = gen_bank_card_jainshe()  # 建设
    list = [jianshe]
    return JsonResponse({"jianshe": list})


def getzhongguo(request):
    zhongguo = gen_bank_card_zhongguo()  # 中国
    list = [zhongguo]
    return JsonResponse({"zhongguo": list})


def getjiaotong(request):
    jiaotong = gen_bank_card_jiaotong()  # 交通
    list = [jiaotong]
    return JsonResponse({"jiaotong": list})
