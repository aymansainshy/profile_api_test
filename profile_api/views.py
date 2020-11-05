from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test HelloApiView"""

    def get(self, request, format=None):
        an_apiView = [ 'ayman','mohammed','Seddig', 'ayman sainshy # gmail.com']
        return Response({'message' : 'Hello', 'an_apiView':an_apiView})

