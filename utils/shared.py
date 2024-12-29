from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
def swagerHeaders():
    menualParams = openapi.Parameter(
                  name='Authorization',
                  in_=openapi.IN_HEADER,
                  description='Bearer token for authentication',
                  type=openapi.TYPE_STRING,
                  required=True
              )
    return [menualParams]
    
