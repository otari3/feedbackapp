from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from utils.shared import swagerHeaders
from drf_yasg.utils import swagger_auto_schema
from utils import custom_erros,shared
import json

# Create your views here.

@swagger_auto_schema(method='get',manual_parameters=swagerHeaders())
@api_view(['get'])
def testingSwager(request):
  header = request.headers.get('Authorization')
  return Response(header)

@swagger_auto_schema(method='post',request_body=shared.swager_body()['register_componey'])
@api_view(['post'])
def register_compony(request):
  parsed_json = json.loads(request.body)
  return Response(parsed_json)