from datetime import datetime
from django.http import JsonResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from accountOperations.models import Profile
from documents.models import Tag
from errorPages.views import onlyForStaffChecker, onlyForLogginedChecker


@csrf_exempt
@api_view(['GET', 'POST'])
@onlyForStaffChecker
def createTags(request):
    body = request.data
    print(body)
    for x in body["params"]["tags"]:
        Tag.init(tag=x)
    response = JsonResponse({
        "result": "OK",
    })
    response.status_code = 200
    return response



@csrf_exempt
@api_view(['GET', 'POST'])
@onlyForStaffChecker
def getListOfTags(request):
    response = JsonResponse({
        "result": "GotOut",
        "data": [{"id": x.id, "tag": x.tag} for x in Tag.objects.filter()[::-1]],
    })
    response.status_code = 200
    return response


@csrf_exempt
@api_view(['GET', 'POST'])
@onlyForLogginedChecker
def downloadFile(request, path):
    fileObject = open("media/" + path, 'rb')
    response = FileResponse(fileObject)
    return response

