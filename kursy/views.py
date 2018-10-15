from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models  import Course
from .serializers import CourseSerializer 


class Courselist(APIView):
	
	def get(self, request):
		courses=Course.objects.all()
		serializer=CourseSerializer(courses,many=True)
		return Response(serializer.data)



	def post(self):
		pass
