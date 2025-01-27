from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from utils.shared import swagerHeaders
from drf_yasg.utils import swagger_auto_schema
from utils import custom_erros

# Create your views here.

@swagger_auto_schema(method='get',manual_parameters=swagerHeaders())
@api_view(['get'])
def testingSwager(request):
  test = {'swagger':True}
  raise custom_erros.APIException('hello')
  return Response(test)
