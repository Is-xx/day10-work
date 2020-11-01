from rest_framework import serializers
from rest_framework.response import Response

from app.models import User


class UserListSerializer(serializers.ListSerializer):
    def update(self, instance, validated_data):
        for index, obj in enumerate(instance):
            self.child.update(obj, validated_data[index])
            return instance


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'user_info', 'get_pic',
                  'get_gender', 'age', 'pic', 'gender')
        extra_kwargs = {
            'username': {
                'required': True,
                'min_length': 1,
                'max_length': 6,
                'error_messages': {
                    'required': '请输入用户名',
                    'min_length': '用户名字数不能少于一个字',
                    'max_length': '用户名字数不能超过六个字',
                }
            },
            'password': {
                'required': True,
                'error_messages': {
                    'required': '请输入密码',
                }
            },
            'user_info': {
                'read_only': True
            },
            'get_gender': {
                'read_only': True
            },
            'get_pic': {
                'read_only': True
            },
            'pic': {
                'write_only': True
            },
            'gender': {
                'write_only': True
            },
        }

    def validate(self, attrs):
        return attrs

    def validated_password(self, pwd):
        return pwd

    def validated_username(self, username):
        user = User.objects.filter(username=username)
        if not user:
            return username
        else:
            return Response({
                'error_message': '用户名已存在',
            })

    list_serializer_class = UserListSerializer
