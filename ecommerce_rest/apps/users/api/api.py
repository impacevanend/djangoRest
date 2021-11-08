import re
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.users.models import User
from apps.users.api.serializers import UserSerializer

#*Clase
# class UserAPIview(APIView):
#     #REcive la petición get
#     def get(self, request):
#         users = User.objects.all()

#         #*pasando la consulta a un serializador

#         users_serializer = UserSerializer(users, many = True)
#         #*Información enviada en data
#         return Response(users_serializer.data)




#Todo decorador
@api_view(['GET','POST'])#*metodos [get, post, put, delete]
def user_api_view(request):
    
    if request.method == 'GET':
        users = User.objects.all()

        #*pasando la consulta a un serializador

        users_serializer = UserSerializer(users, many = True)
        #*Información enviada en data
        return Response(users_serializer.data)

    elif request.method == 'POST':
        users_serializer = UserSerializer(data = request.data)
        if users_serializer.is_valid():
            users_serializer.save()
            """
            Guarda la información serlializada cuando se envia una serie de parametros para GET
            Y la información de una creación serializada
            """
            return Response(users_serializer.data)
        return Response(users_serializer.errors)


@api_view(['GET','PUT','DELETE'])
def user_detail_api_view(request,pk=None):
    if request.method == 'GET':
        user = User.objects.filter(id = pk).first()
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data)

    elif request.method == 'PUT':
        user = User.objects.filter(id = pk).first()
        user_serializer = UserSerializer(user, data = request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)
        return Response(user_serializer.errors)

    elif request.method == 'DELETE':
        user = User.objects.filter(id = pk).first()
        user.delete()
        return Response("Eliminado")