'''下载器'''

import requests
from elegance_spider.http.response import Response


class Downloader(object):
    def get_response(self, request):
        if request.method.upper() == 'GET':
            resp = requests.get(request.url, headers=request.headers, params=request.params)
        elif request.method.upper() == 'POST':
            resp = requests.post(request.url, headers=request.headers, params=request.param, data=request.data)
        else:
            raise Exception('不支持的请求方法')

        return Response(resp.url, resp.status_code, resp.headers, resp.content)