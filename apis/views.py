from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from apis.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class Apiiii(APIView):
    def get(self, request):
        return Response({"message": "Hey I'm a GET Method"}, status=status.HTTP_200_OK)

    def post(self, request):
        return Response(
            {"message": "Hey I'm a POST Method"}, status=status.HTTP_201_CREATED
        )

    def put(self, request):
        return Response(
            {"message": "Hey I'm a PUT Method"}, status=status.HTTP_201_CREATED
        )

    def patch(self, request):
        return Response(
            {"message": "Hey I'm a PATCH Method"}, status=status.HTTP_201_CREATED
        )

    def delete(self, request):
        return Response(
            {"message": "Hey I'm a DELETE Method"}, status=status.HTTP_201_CREATED
        )


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt

# # Create your views here.
# @csrf_exempt
# def index(request):
#     try:
#         if request.method == "GET":
#             return HttpResponse("Hey I'm a GET")

#         if request.method == "POST":
#             byte_str = request.body
#             dict_str = byte_str.decode('UTF-8')
#             _dict = ast.literal_eval(dict_str)

#             print("Hello, POST!!!")
#             return HttpResponse(f"Hey I'm a POST, Dict: {_dict}")
#     except Exception as e:
#         print(e)
#         return HttpResponse(f"Hey, Error occured :: {e}")
