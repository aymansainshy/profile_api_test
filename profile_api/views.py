from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profile_api import serializers


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


