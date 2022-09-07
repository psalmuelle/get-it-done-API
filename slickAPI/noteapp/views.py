from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import NoteApp
from .serializers import NoteSerializer
from knox.auth import TokenAuthentication

@api_view(["POST", "GET"])
def note(request):
    token = request.META.get("HTTP_AUTHORIZATION", False)
    if token: 
        token = str(token).split()[1].encode("utf-8")
        knoxAuth = TokenAuthentication()
        user, auth_token = knoxAuth.authenticate_credentials(token)
        request.user = user
        if request.method == "POST":
            serializer = NoteSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user = request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == "GET":
            notes = NoteApp.objects.filter(user = request.user)
            serializer = NoteSerializer(notes, many=True)
            return Response(serializer.data)




@api_view(["DELETE"])
def delete_note(request, pk):
    try: 
        notes = NoteApp.objects.get(pk = pk)
    except NoteApp.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == "DELETE":
        notes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
