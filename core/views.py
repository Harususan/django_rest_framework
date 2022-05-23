from django.shortcuts import render
from django.http import JsonResponse

# Third party imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer,RegisterSerializer
from .models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics

class UserDetailAPI(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = (TokenAuthentication,)
    def get(self,request,*args,**kwargs):
        '''
        This api endpoint gives us the details of the user.

        Args: request.
        Returns: serializer data.
        '''
        qs = User.objects.get(id = request.user.id)
        serializer = UserSerializer(qs)
        return Response(serializer.data)

    # def post(self,request,*args,**kwargs):
    #     serializer = PostSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors)

class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
