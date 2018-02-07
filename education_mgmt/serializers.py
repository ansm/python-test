from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from school_mgmt.models import *

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    username = serializers.CharField(
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(min_length=8)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
             validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')




class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        


class SchoolListSerializer(serializers.ModelSerializer):
    class Meta:
        model = School


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student


# class universitiesListSerializer1(serializers.ModelSerializer):

#     School = SchoolListSerializer1(many=True)


#     class Meta:
#         model = Universities
#         fields = ('id', 'name',)
    

# class SchoolListSerializer1(serializers.ModelSerializer):
#      class Meta:
#         model = School
#         fields = ('id', 'name',)


class universitieslistcountSerializer(serializers.ModelSerializer):

    count_school = serializers.SerializerMethodField()
    
    class Meta:
        model = Universities
        fields = ('name','website','count_school')

    def get_count_school(self, obj):
        print obj.id
        return School.objects.filter(universities__id=obj.id).count()
        #School.objects.filter(Universities__id=obj.id).count()




class SchoolUniSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('id','name','universities')       
    

        
class UniversityListSerializer2(serializers.ModelSerializer):
     
    school_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Universities
        fields = ('id','name','school_name')

    def get_school_name(self, obj):
        print obj.id
        return SchoolUniSerializer(School.objects.filter(universities__id=obj.id),many=True).data