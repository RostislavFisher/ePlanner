from django.http import FileResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from errorPages.views import onlyForLogginedChecker


@csrf_exempt
@api_view(['GET', 'POST'])
@onlyForLogginedChecker
def downloadFile(request, path):
    fileObject = open("media/" + path, 'rb')
    response = FileResponse(fileObject)
    return response

