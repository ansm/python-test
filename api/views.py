from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from education_mgmt.serializers import UserSerializer, SchoolSerializer, SchoolListSerializer,  universitieslistcountSerializer,StudentSerializer, UniversityListSerializer2
from django.views.decorators.csrf import csrf_exempt
from school_mgmt.models import *
from rest_framework.authentication import TokenAuthentication
import random
from random import randint


# this is edit
@api_view(['POST'])
def user_login(request):
	serializer = UserSerializer(data=request.data)
	if serializer.is_valid():
		return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def user_Register(request):
	serializer = UserSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@csrf_exempt
@api_view(['GET'])
def universities_list(request):
	print "in list"
	print request.data
	universities = Universities.objects.all()
	print universities.count()
	serializer = universitieslistcountSerializer(universities, many=True)
	return Response(serializer.data, status=status.HTTP_200_OK)
	





@csrf_exempt
@api_view(['GET'])
def universities_list1(request): 
	universities = Universities.objects.all()
	serializer = UniversityListSerializer2(universities, many=True)
	print serializer.data
	return Response(serializer.data, status=status.HTTP_200_OK)



@csrf_exempt
@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
def school_create(request):
	if request.user.is_authenticated():
		owner = request.user
		data = request.data
		data['owner'] = owner.id
		serializer = SchoolSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	else:
		return Response({'error': 'You are not authenticated'}, status=status.HTTP_200_OK)



@csrf_exempt
@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
def school_list(request):
    if request.user.is_authenticated():
    	schools = School.objects.filter(is_active=True, owner=request.user)
    	serializer = SchoolListSerializer(schools, many=True)
    	return Response(serializer.data, status=status.HTTP_200_OK)
    else:
    	return Response({'error': 'You are not authenticated'}, status=status.HTTP_200_OK)





@csrf_exempt
@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
def school_details(request, pk):
	if request.user.is_authenticated():
		try:
			school = School.objects.get(id=pk, owner=request.user)
		except:
			return Response({'error': 'School id not found'}, status=status.HTTP_400_BAD_REQUEST)

		serializer = SchoolListSerializer(school, many=False)
		return Response(serializer.data, status=status.HTTP_200_OK)
	else:
		return Response({'error': 'You are not authenticated'}, status=status.HTTP_200_OK)



@csrf_exempt
@api_view(['PUT'])
@authentication_classes((TokenAuthentication,))
def school_update(request, pk):
    if request.user.is_authenticated():
	    try:
		    school = School.objects.get(id=pk)
	    except:
		    return Response({'error': 'school id not found'}, status=status.HTTP_400_BAD_REQUEST)

	    serializer = SchoolListSerializer(school, data=request.data, many=False)

	    if serializer.is_valid():
		    serializer.save()
		    return Response(serializer.data, status=status.HTTP_201_CREATED)
	    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'error': 'You are not authenticated'}, status=status.HTTP_200_OK)



@csrf_exempt
@api_view(['DELETE'])
@authentication_classes((TokenAuthentication,))
def school_delete(request, pk):
	if request.user.is_authenticated():
		try:
			school = School.objects.get(id=pk, owner=request.user)
		except:
			return Response({'error': 'School id not found'}, status=status.HTTP_400_BAD_REQUEST)

		school.delete()
		return Response({'success': 'School deleted successfully'}, status=status.HTTP_200_OK)
	else:
		return Response({'error': 'You are not authenticated'}, status=status.HTTP_200_OK)



    
    
@csrf_exempt
@api_view(['POST'])
def student_add(request):
	data = request.data
	serializer = StudentSerializer(data=data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	






@csrf_exempt
@api_view(['POST'])
def student_list(request):
   student = Student.objects.all()



# university name : M P Patel University
# school name : Mother Teresa World School
# student name : Maulik Patel
# date of birth : 05/07/1990

# 1) gerente a random number

   one = (random.randint(1,9999))

# 2) get a date from bday
   date = request.data['date_of_birth']
   two = date[8:10]

 # 3)get a first three character of universities
   
   schoolid =  request.data['school']
   school1 = School.objects.get(id=schoolid)
   universities1 = school1.universities.name
   three = universities1[:3]


 # 4)get a first three character of school
   
   schoolid = request.data['school']
   school1 = School.objects.get(id=schoolid)
   school1 = school.name
   four = school1[:3]


# 2) get a month from bday
   
   five = date[5:7]


# 2) get a year from bday
   six = date[0:4]

   one = str(one)
   two = str(two)
   three = str(three)
   four= str(four)
   five = str(five)
   six= str(six)


   smart_number= one + two + "_" + three + four + "_" + five + six
   print smart_number

   serializer = StudentSerializer(student, many=True)
   return Response({"Smart_number" : smart_number,"Data" : serializer.data}, status=status.HTTP_201_CREATED)
   
  
   









   




