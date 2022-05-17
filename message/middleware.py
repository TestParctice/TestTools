from utils.mylog import log
from django.http import HttpResponse, JsonResponse


class MessageMiddleWare(object):
    def __init__(self, get_response):
        self.mylog = log.logger(self)
        self.mylog.info("调用中间件方法__init__")
        self.get_response = get_response

    def __call__(self, request):
        self.process_request(request)
        # logging.Logger.log(self, str(time.time()) + request.get_host() + request.method() + request.get_full_path())
        # self.mylog.info(str(request.get_host()) + str(request.method()) + str(request.get_full_path()))
        # self.mylog.info(request.get_host)
        # self.mylog.info(request.method)
        self.mylog.info(request.get_full_path)
        response = self.get_response(request)
        self.process_response(request, response)
        return response

    def process_request(self, request):
        # 产生request对象之后，url匹配之前调用
        # print('----process_request----')
        return HttpResponse(request)

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        # url匹配之后，视图函数调用之前调用
        pass
        # return HttpResponse(request, view_func, *view_args, **view_kwargs)

    def process_response(self, request, response):
        # 视图函数调用之后，内容返回浏览器之前
        # print('----process_response----')
        return response
