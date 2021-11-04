from rest_framework.response import Response
from rest_framework.views import APIView
from apps.users.models import User
from apps.users.api.serializers import UserSerializer


class UserAPIview(APIView):
    #REcive la petición get
    def get(self, request):
        users = User.objects.all()

        #*pasando la consulta a un serializador

        users_serializer = UserSerializer(users, many = True)
        #*Información enviada en data
        return Response(users_serializer.data)