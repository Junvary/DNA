from rest_framework.response import Response


class SuccessResponse(Response):

    def __init__(self, data=None, msg='操作成功', status=None, template_name=None, headers=None, exception=False,
                 content_type=None, page=1, limit=1, total=1):
        std_data = {
            "code": 1,
            "success": True,
            "data": {
                "page": page,
                "limit": limit,
                "total": total,
                "data": data
            },
            "message": msg
        }
        super().__init__(std_data, status, template_name, headers, exception, content_type)


class DetailResponse(Response):

    def __init__(self, data=None, msg='操作成功', status=None, template_name=None, headers=None, exception=False,
                 content_type=None, ):
        std_data = {
            "code": 1,
            "success": True,
            "data": data,
            "message": msg
        }
        super().__init__(std_data, status, template_name, headers, exception, content_type)


class ErrorResponse(Response):

    def __init__(self, data=None, msg='操作失败', code=0, status=None, template_name=None, headers=None,
                 exception=False, content_type=None):
        std_data = {
            "code": code,
            "success": False,
            "data": data,
            "message": msg
        }
        super().__init__(std_data, status, template_name, headers, exception, content_type)
