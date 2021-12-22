from django.db import connection
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from Api.App.Serializer.UserSerializer import RegisterSerializer
from Api.App.Serializer.UserSerializer import UserSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from Api.models import User


@api_view(['GET'])
def getusers_view(request):
    users = User.objects.all()
    serializer = UserSerializer(users,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def userDetail(request, id):
	user = User.objects.filter(id=id).values()
	serializer = UserSerializer(user, many=True)
	return Response(serializer.data)

@api_view(['POST'])
def userUpdate(request, id):
	try:
		user = User.objects.get(id=id)
		serializer = UserSerializer(instance=user,data=request.data)
		
		if serializer.is_valid():
			serializer.save()

		return Response(serializer.data)

	except Exception as e:
		return "Falha ao actualizar o modulo!"

@api_view(['POST'])
def registration_view(request):    
    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        data ={}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = True
            data['email'] = account.email
            data['username'] = account.username
            return Response({'response': True})
        else:
            data['response'] = False
            data = serializer.errors
        return Response(data)
    
@api_view(['DELETE'])
def delete_view(request,id):
    try:
        user = User.objects.get(pk=id)
        user.delete()
        return Response({'response': True})
    except User.DoesNotExist:
        return Response({'response': None})
    
