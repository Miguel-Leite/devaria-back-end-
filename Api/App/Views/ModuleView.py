from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.decorators import api_view
from rest_framework.response import Response

from Api.models import Module

from Api.App.Serializer.ModuleSerializer import ModuleSerializer


from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
def ModuleList(request):
	module = Module.objects.all()
	serializer = ModuleSerializer(module,many=True)
	return Response(serializer.data)


@api_view(['GET'])
def ModuleDetail(request, pk):
	module = Module.objects.filter(id=pk).values()
	serializer = ModuleSerializer(module, many=True)
	return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def ModuleCreate(request):
	try:
		serializer = ModuleSerializer(data=request.data)
		# authentication_classes = (PermitionAuthentication,) # especificando a classe de autenticação

		if serializer.is_valid():
			serializer.save()

		return Response(serializer.data)

	except Exception as e:
		return "Falha ao registar novo modulo!"

@api_view(['POST'])
def ModuleUpdate(request, pk):
	try:
		module = Module.objects.get(id=pk)
		serializer = ModuleSerializer(instance=module,data=request.data)
		
		if serializer.is_valid():
			serializer.save()

		return Response(serializer.data)

	except Exception as e:
		return "Falha ao actualizar o modulo!"

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def ModuleDelete(request, pk):
	try:
		module = Module.objects.get(id=pk)
		module.delete()
		if module:
			return Response({'deleted': True})
		return Response({'deleted': False})

	except Exception as e:
		return "Falha ao actualizar os dados!"