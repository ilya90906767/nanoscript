from rest_framework.request import Request
from rest_framework.response import Response
from users.serializers import UserSerializer

from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from users.serializers import UserSerializer, IssueTokenRequestSerializer, TokenSeriazliser
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate



@api_view(['POST'])
@permission_classes([AllowAny])
def issue_token(request: Request):
    serializer = IssueTokenRequestSerializer(data=request.data)
    if serializer.is_valid():
        authenticated_user = authenticate(**serializer.validated_data)
        try: 
            token = Token.objects.get(user=authenticated_user)
        except Token.DoesNotExist:
            token = Token.objects.create(user=authenticated_user)
        return Response(TokenSeriazliser(token).data)
    else:
        return Response(serializer.errors, status=400)
    

@api_view()
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def user(request: Request):
    return Response({
        'data': UserSerializer(request.user).data
    })
    