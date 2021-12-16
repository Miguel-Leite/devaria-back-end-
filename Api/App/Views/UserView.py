from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.decorators import api_view
from rest_framework.response import Response

from Api.models import CustomUser

from Api.App.Serializer.UserSerializer import UserSerializer


@api_view(['GET'])
def UserList(request):
	user = CustomUser.objects.all()
	serializer = UserSerializer(user,many=True)
	return Response(serializer.data)