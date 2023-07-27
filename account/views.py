from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from account.serializers import UserRegistrationSerializer,UserLoginSerializer,UserProfileSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
def get_tokens_for_user(user):
    refresh=RefreshToken.for_user(user)
    return{
        'refresh':str(refresh),
        'access':str(refresh.access_token)
    }






class UserRegistration(APIView):

    def post(self,request,format=None):
        
        data=UserRegistrationSerializer(data=request.data)

        if data.is_valid(raise_exception=True):
            user=data.save()
            token=get_tokens_for_user(user)
            return Response({'token':token,'msg':'Registration successful and now you can login'},
                            status=status.HTTP_201_CREATED)


   
        return Response(data.errors,status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    
    def post(self,request,format=None):
        datas=UserLoginSerializer(data=request.data)
        if datas.is_valid(raise_exception=True):
            
            phone_number=datas.data.get('phone_number')
            password=datas.data.get('password')
            user=authenticate(phone_number=phone_number,password=password)
            if user is not None:
                token=get_tokens_for_user(user)
                return Response({'token':token,'msg':'login successful'})
            else:
                return Response({'error':{'non_field_errors':["Email or Password is not valid"]}},status=status.HTTP_404_NOT_FOUND)
        return Response(datas.errors,stauts=status.HTTP_400_BAD_REQUEST)

class UserProfile(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def get(self,request,format=None):
        
        print(request.user)
        datas=UserProfileSerializer(request.user)
     
        return Response(datas.data,status=status.HTTP_200_OK)

