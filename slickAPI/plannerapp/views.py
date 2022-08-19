from email import message
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import PlannerApp
from .serializers import PlannerSerializer


@api_view(["POST"])
def create_plan(request):
   
    if request.method == "POST":
        serializer = PlannerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(["GET"])
def get_plan(request,pk):
    userId = pk 
    if request.method == "GET":
        plans= PlannerApp.objects.filter(generated_by=userId)
        serializer = PlannerSerializer(plans, many=True)
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
        
