from django.conf import settings
import jwt
import datetime
from jwt import exceptions


def create_token(payload, timeout=60*24):
    headers = {
        'typ': 'jwt',
        'alg': 'HS256'
    }
    payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(minutes=timeout)
    result = jwt.encode(payload=payload, key=settings.SECRET_KEY, algorithm="HS256", headers=headers)
    return result


def parse_payload(token):
    result = {'status': False, 'data': None, 'error': None}
    try:
        verified_payload = jwt.decode(token, settings.SECRET_KEY, True)
        result['status'] = True
        result['data'] = verified_payload
    except exceptions.ExpiredSignatureError:
        result['error'] = '登录已过期,请重新登录!'
    except jwt.DecodeError:
        result['error'] = '认证失败,请检查配置!'
    except jwt.InvalidTokenError:
        result['error'] = '非法登录,请确认权限!'
    return result



