from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status 

from todo.serializers import TodoSerializer 
from todo.models import Todo

from django.http import Http404

class TodoList(APIView):

    def get(self,request):
        todo = Todo.objects.all()
        serializer = TodoSerializer(todo,many=True)
        return Response(serializer.data)

    
    def post(self,request):
        serializer = TodoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)


class TodoDetail(APIView):
    
    def get_object(self,pk):
        try:
            return Todo.objects.get(pk=pk)
        except:
            return Http404

    def put(self,request,pk):
        todo = self.get_object(pk)
        serializer = TodoSerializer(todo,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return TodoSerializer(serializer.data,status=status.HTTP_201_CREATED)
        return TodoSerializer(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,pk):
        todo = self.get_object(pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def delete(self,request,pk):
        todo = self.get_object(pk)
        todo.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

