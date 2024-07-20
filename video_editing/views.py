from django.shortcuts import render
from .serializers import PostSerializer
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


# This is the view that will allow you to upload video 
class PostFileView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = PostSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)