from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
import json
from .utils import run_code

# Definicion de las apis o rutas 
@api_view(['POST'])
def main(request):
    if request.method != 'POST':
        return JsonResponse(
            {'code':''}, status=405
        )
    

    try:
        body = request.body.decode('utf-8') if request.body else''
        data = json.loads(body) if body else {}
    except Exception:
        return JsonResponse({'code':'JsonInvalido'}, status=405)
    
    code = data.get('text','')
    output= run_code(code)


    return Response(
        {'output':output},
        status=status.HTTP_200_OK
    )
