from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from dna_utils.page import MyPageNumber
from dna_system.models.role import Role
from dna_utils.response import SuccessResponse, ErrorResponse
from rest_framework import serializers


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['role_code', 'role_name']


class GetRoleListView(ListModelMixin, GenericAPIView):
    authentication_classes = []
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    pagination_class = MyPageNumber

    def post(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return SuccessResponse(data=serializer.data, total=len(serializer.data))
        serializer = self.get_serializer(queryset, many=True)
        return SuccessResponse(serializer.data)
