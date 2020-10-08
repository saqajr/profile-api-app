from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_Api import serializers

class HelloApi(APIView):
    """
    Test Api View
    """

    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """
        Returns Api Features
        """

        APi_Feat = [ 'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
            ]

        return Response({'message':'HelloWorld','List':APi_Feat})


    def post(self , request):

        """
        Create hello message with your name
        """
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('inputname')
            message = f'Hello {name}'
            return Response({'mess':message})
        else:
            return Response(serializer.errors ,
            status= status.HTTP_400_BAD_REQUEST
            )


    def put(self, request, pk=None):
        """
        Handle updating an object
        """
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """
        Handle partial update of object
        """
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """
        Delete an object
        """
        return Response({'method': 'DELETE'})
