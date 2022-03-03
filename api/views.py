from ast import Not
from configparser import NoSectionError
import imp
from operator import imod
from select import select
from tkinter.messagebox import NO
from django.shortcuts import get_object_or_404, render
# Create your views here.
from django.http import JsonResponse
# 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer
from api import serializers


@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
           'Endpoint': '/notes/',
           'method': 'GET',
           'body': None,
           'description':'Returns an array of notes'
        },
         {
           'Endpoint': '/notes/id/',
           'method': 'GET',
           'body': None,
           'description':'Returns a single object of  notes'
        },
         {
           'Endpoint': '/notes/create/',
           'method': 'GET',
           'body': {"body" : ""},
           'description':'create a new note '
        },
         {
           'Endpoint': '/notes/id/update/',
           'method': 'GET',
           'body': {"body" : ""},
           'description':'update a note '
        },
        {
           'Endpoint': '/notes/id/delete/',
           'method': 'GET',
           'body': {"body" : ""},
           'description':'delete  a note '
        }

    ]

    return Response(routes)



@api_view(['GET'])
def getNotes(request):
   notes = Note.objects.all()
   serialzier = NoteSerializer(notes , many=True)
   return Response(serialzier.data)

@api_view(['GET'])
def getNote(request , pk):
   note =  get_object_or_404(Note , id=pk)
   serialzier = NoteSerializer(note , many=False)
   return Response(serialzier.data)


@api_view(['POST'])
def createNote(request):

   data = request.data 
   note = Note.objects.create(
      body = data['body']
   )
   serializer = NoteSerializer(note , many=False)
   return Response(serializer.data)



@api_view(['PUT'])
def updateNote(request , pk):

   data = request.data 

   note = get_object_or_404(Note , id=pk)
   serializer = NoteSerializer(note , data=request.data)

   if serializer.is_valid():
      serializer.save()

   return Response(serializer.data)



@api_view(['DELETE'])
def deleteNote(request, pk):

   note = get_object_or_404(Note, id=pk)
   note.delete()
   return Response('note has deleted ')