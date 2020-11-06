from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from profile_api import serializers
from profile_api import models
from profile_api import permissions

""" ////////////////////////////////////////////// [ ApiView ] //////////////////////////////////////////////// """
class HelloApiView(APIView):
    """Test HelloApiView"""
    serializers_calss = serializers.HelloSerializer

    def get(self, request, format=None):
        an_apiView = [ 'ayman','mohammed','Seddig', 'ayman sainshy # gmail.com']
        return Response({'message' : 'Hello', 'an_apiView':an_apiView})

    def post(self, request):
        """Create Hello message with our name """ 
        serializer = self.serializers_calss(data=request.data)    

        if serializer.is_valid():
            name    = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message' : message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            ) 

    def put(self,request,pk=None):          
         """Hendel updating an Object"""
         return Response({'method':'PUT'})

    def patch(self,request,pk=None):          
         """Hendel updating partial an Object"""
         return Response({'method':'PATCH'})

    def delet(self,request,pk=None):          
         """Delete an Object"""
         return Response({'method':'DELETE'})


""" ////////////////////////////////////////////// [ ViewSet ] //////////////////////////////////////////////// """
class HelloViewSet(viewsets.ViewSet):
    """Test ApiviewSet """
    serializers_calss = serializers.HelloSerializer 

    def list(self,request):
        """Return Hello message"""
        a_viewSet = [ 'ayman','mohammed','Seddig', 'ayman sainshy # gmail.com' ,'Adam', 'i am actually working at BDC as a mobile app Developer !']
        return Response({'message':'Hello !' ,'a_viewSet':a_viewSet})
  
    def create(self,request):
        """Create a new hello message """
        serializer = self.serializers_calss(data=request.data)

        if serializer.is_valid():
            name    = serializer.validated_data.get('name')
            message = f'Hello {name} !'
            return Response({'message' : message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )   

    def retrieve(self, request, pk=None):
        """Hendel getting an Object by it's Id """
        return Response({'http_Method' : 'GET'})         
   
    def update(self, request, pk=None):
        """Hendel Updating an Object by it's Id """
        return Response({'http_Method' : 'PUT'})         
   
    def partial_update(self, request, pk=None):
        """Hendel Updating part of an Object by it's Id """
        return Response({'http_Method' : 'PATCH'})         
    
    def destroy(self, request, pk=None):
        """Hendel deleting an Object by it's Id """
        return Response({'http_Method' : 'DELETE'})         

""" ////////////////////////////////////////////// [ UserProfileViewSet ] //////////////////////////////////////////////// """
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handel creating and updating profile"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()    
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)
 