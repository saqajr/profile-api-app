from rest_framework import serializers


class HelloSerializer(serializers.Serializer):

    """ Serializer a name field for testing our APi View """

    inputname = serializers.CharField(max_length=10)
