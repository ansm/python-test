@csrf_exempt
@api_view(['GET'])
def universities_list(request):
	print "in list"
	print request.data
	universities = Universities.objects.all()
	serializer = universitiesSerializer(universities, many=True)
	return Response(serializer.data, status=status.HTTP_200_OK)