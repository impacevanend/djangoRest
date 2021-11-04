from rest_framework.views import APIView
from apps.users.models import User
from apps.users.api.serializers import UserSerializer


class UserAPIview(APIView):
    #REcive la petición get
    def get():