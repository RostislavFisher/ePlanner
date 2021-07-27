from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from errorPages.views import onlyForStaffChecker
from tariff.models import Tariff


@csrf_exempt
@api_view(['GET'])
def tariffs(request, *args):
    response = JsonResponse({
        "tariffs": [{"id": x.id, "title": x.title, "subTitle": x.subTitle, "time": x.time} for x in Tariff.objects.filter()]
    })
    response.status_code = 200
    return response

@csrf_exempt
@api_view(['GET'])
def getInformationTariff(request, id):
    tariffObject = Tariff.objects.get(id=id)
    response = JsonResponse({
        "tariff": [{"id": tariffObject.id, "time": tariffObject.time,
                    "title": tariffObject.title, "subTitle": tariffObject.subTitle}]
    })
    response.status_code = 200
    return response

@csrf_exempt
@api_view(['POST'])
@onlyForStaffChecker
def createTariff(request, *args):
    body = request.data["params"]
    Tariff.objects.create(title=body["title"], subTitle=body["subTitle"], time=body["time"])
    response = JsonResponse({
        "tariffs": "OK"
    })
    response.status_code = 200
    return response


@csrf_exempt
@api_view(['DELETE'])
@onlyForStaffChecker
def deleteTariff(request, id):
    body = request.data["params"]
    Tariff.objects.get(id=id).delete()
    response = JsonResponse({
        "result": "OK"
    })
    response.status_code = 200
    return response

