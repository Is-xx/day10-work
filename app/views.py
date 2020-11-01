from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins

from app.models import User
from app.serializers import UserModelSerializer


class UserLogin(viewsets.GenericViewSet):
    queryset = User.objects.filter(is_delete=False)
    serializer_class = UserModelSerializer
    lookup_field = 'id'

    def login(self, request, *args, **kwargs):
        data = request.data
        username = data.get('username')
        pwd = data.get('password')
        user = User.objects.filter(username=username, is_delete=False)
        if user:
            if user[0].password == pwd:
                return Response({
                    'status': 200,
                    'message': '登陆成功',
                    'result': '用户为：' + user[0].username
                })
        return Response({
            'status': 404,
            'message': '用户名或密码错误'
        })


class UserInfo(generics.GenericAPIView, mixins.CreateModelMixin,
               mixins.DestroyModelMixin, mixins.ListModelMixin,
               mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    queryset = User.objects.filter(is_delete=False)
    serializer_class = UserModelSerializer
    lookup_field = 'id'

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        if id:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
