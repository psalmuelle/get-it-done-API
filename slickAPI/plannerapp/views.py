
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import PlannerApp
from .serializers import PlannerSerializer
from knox.auth import TokenAuthentication

@api_view(["POST", "GET"])
def plan(request):
    token = request.META.get("HTTP_AUTHORIZATION", False)
    if token: 
        token = str(token).split()[1].encode("utf-8")
        knoxAuth = TokenAuthentication()
        user, auth_token = knoxAuth.authenticate_credentials(token)
        request.user = user
        if request.method == "POST":
            serializer = PlannerSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user = request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == "GET":
            notes = PlannerApp.objects.filter(user = request.user)
            serializer = PlannerSerializer(notes, many=True)
            return Response(serializer.data)


@api_view(["DELETE"])
def delete_plan(request, pk):
    try: 
        plans = PlannerApp.objects.get(pk= pk)
    except PlannerApp.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == "DELETE":
        plans.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
