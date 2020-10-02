from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApi(APIView):
    """Test Api View"""
    def get(self,request,format=None):
        """Returns Api Features """
        APi_Feat = [ 'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
            ]

        return Response({'message':'HelloWorld','List':APi_Feat})
