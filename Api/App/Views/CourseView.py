from django.db import connection
from rest_framework.decorators import api_view
from rest_framework.response import Response


from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response

from Api.models import Courses

from Api.App.Serializer.CoursesSerializer import CoursesSerializer


@api_view(['GET'])
def CourseList(request):
	course = Courses.objects.all()
	serializer = CoursesSerializer(course,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def getCourseAndModule_view(request):
    sql = "SELECT C.id, C.course, M.module FROM Api_courses AS C INNER JOIN Api_module AS M ON C.module_id = M.id "
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    data = [{
        'id': result[0][0],
        'course': result[0][1],
        'module': result[0][2],
    }]
    return Response(data)


@api_view(['GET'])
def CourseDetail(request, pk):
	course = Courses.objects.filter(id=pk).values()
	serializer = CoursesSerializer(course, many=True)
	return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CourseCreate(request):
	try:
		serializer = CoursesSerializer(data=request.data)

		if serializer.is_valid():
			serializer.save()

		return Response(serializer.data)

	except Exception as e:
		return None

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CourseUpdate(request, pk):
	try:
		course = Courses.objects.get(id=pk)
		serializer = CoursesSerializer(instance=course,data=request.data)
		
		if serializer.is_valid():
			serializer.save()

		return Response(serializer.data)

	except Exception as e:
		return None

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def CourseDelete(request, pk):
	try:
		course = Courses.objects.get(id=pk)
		course.delete()
		if course:
			return Response({'deleted': True})
		return Response({'deleted': False})

	except Exception as e:
		return None
