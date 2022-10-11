from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from dna_utils.page import MyPageNumber
from dna_system.models.user import User
from dna_utils.jwt_auth import create_token
from dna_utils.response import SuccessResponse, ErrorResponse
from rest_framework import serializers
from dna_system.views.role import RoleSerializer
from dna_utils.jwt_auth import parse_payload


class LoginView(APIView):
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                token = create_token(payload={'username': username})
                return SuccessResponse(data=token)
            else:
                raise Exception
        except Exception as e:
            print(e)
            return ErrorResponse(data='用户名或密码错误')


class UserSerializer(serializers.ModelSerializer):
    role = RoleSerializer(label='角色', many=True)

    class Meta:
        model = User
        exclude = ["password"]


class GetUserListView(ListModelMixin, GenericAPIView):
    authentication_classes = []
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = MyPageNumber

    def post(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return SuccessResponse(data=serializer.data, total=len(serializer.data))
        serializer = self.get_serializer(queryset, many=True)
        return SuccessResponse(serializer.data)


class GetUserMenuView(APIView):
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        print(request.headers.get('Content-Type'))
        # token = request.headers
        # result = parse_payload()
        return SuccessResponse(1)
