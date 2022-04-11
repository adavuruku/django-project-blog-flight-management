from django.shortcuts import render
from django.http import JsonResponse
from firstApp.models import Employee
from .models import Student, Course
from .serializers import StudentSerializer, CourseSerializer
from rest_framework.response import Response
from rest_framework import status, generics,mixins
from rest_framework.decorators import api_view

from rest_framework.views import APIView
from django.http import Http404
from rest_framework import viewsets

# Create your views here.

def employeeView(request):
    emp = {
        'id':123,
        'name':'John',
        'sal':1000000

    }
    data = Employee.objects.all()
    response = {'employees':list(data.values('name','sal'))}
    return JsonResponse(response)

"""
# FUNCTION BASE VIEW

# Create your views here.
@api_view(['GET','POST'])
def student_list(request):

    if request.method =='GET':
        students = Student.objects.all()
        serializer=StudentSerializer(students,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def student_detail(request,pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StudentList(APIView):

    def get(self,request):
        students = Student.objects.all()
        serializer = StudentSerializer(students,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

"""

# CLASS BASE VIEW

class StudentDetail(APIView):
    def get_object(self,pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self,request,pk):
        student=self.get_object(pk)
        serializer=StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StudentList(APIView):

    def get(self,request):
        students = Student.objects.all()
        serializer = StudentSerializer(students,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# Assignment solution

class CourseDetail(APIView):
    def get_object(self,pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        course = self.get_object(pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    def put(self,request,pk):
        course = self.get_object(pk)
        serializer=CourseSerializer(course,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        course = self.get_object(pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CourseList(APIView):

    def get(self,request):
        course = Course.objects.all()
        serializer = CourseSerializer(course,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# Mixing using view

class StudentListMixing(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class= StudentSerializer

    def get(self,request):
        return self.list(request)

    def post(self,request):
        return self.create(request)

class StudentDetailMixing(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class= StudentSerializer

    def get(self,request,pk):
        return self.retrieve(request,pk)

    def put(self,request,pk):
        return self.update(request,pk)

    def delete(self,request,pk):
        return self.destroy(request,pk)


# Mixing assignment using view

class CourseListMixing(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class= CourseSerializer

    def get(self,request):
        return self.list(request)

    def post(self,request):
        return self.create(request)

class CourseDetailMixing(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class= CourseSerializer

    def get(self,request,pk):
        return self.retrieve(request,pk)

    def put(self,request,pk):
        return self.update(request,pk)

    def delete(self,request,pk):
        return self.destroy(request,pk)


# Generic API View

class StudentListGeneric(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class= StudentSerializer

class StudentDetailGeneric(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class= StudentSerializer


# generic assignment

class CourseListGeneric(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class= CourseSerializer

class CourseDetailGeneric(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class= CourseSerializer

# Using Mixins

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # pagination_class = LimitOffsetPagination

# assignment

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer