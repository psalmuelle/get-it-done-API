from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken, TokenAuthentication
from .serializers import RegisterSerializer

def serialize_user(user):
    return {
       
        "username": user.username,
        "email": user.email
    }

@api_view(['POST'])
def login(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    _, token = AuthToken.objects.create(user)
    return Response({
        "username": user.username,
        "email": user.email,
        "user_id": user.id,
        'token': token
    })
        

@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        _, token = AuthToken.objects.create(user)
        return Response({
            "user_info": serialize_user(user),
            "user_id": user.id,
            "token": token
        })


@api_view(['GET'])
def get_user(request):
    token = request.META.get("HTTP_AUTHORIZATION", False)
    if token: 
        token = str(token).split()[1].encode("utf-8")
        knoxAuth = TokenAuthentication()
        user, auth_token = knoxAuth.authenticate_credentials(token)
        request.user = user
        return Response({
            'user_data': serialize_user(user),
            "user_id": user.id,
        })
    return Response({})


@api_view(['GET'])
def logout(request):
  user_token = request.META.get("HTTP_AUTHORIZATION", False)
  if user_token: 
    user_token = str(user_token).split()[1].encode("utf-8")
    knoxAuth = TokenAuthentication()
    user, auth_token = knoxAuth.authenticate_credentials(user_token)
    
    _, token = AuthToken.objects.all().delete()
    return Response({
    "Logged out successfully"
    })
  else:
    return Response({"invalid token"}, status=status.HTTP_401_UNAUTHORIZED)


