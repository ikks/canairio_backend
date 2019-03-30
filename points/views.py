# Create your views here.
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from points.influx_settings import influx_client


@authentication_classes((JWTAuthentication, BasicAuthentication))
@api_view(['POST'])
def save_points(request):
    point_data = request.data
    write = influx_client.write_points(point_data)
    return Response(write)
