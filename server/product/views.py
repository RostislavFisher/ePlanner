from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from accountOperations.models import Profile
from file.models import File
from errorPages.views import onlyForLogginedChecker, onlyForStaffChecker
from product.models import Product
from tag.models import Tag


@csrf_exempt
@api_view(['GET', 'POST'])
@onlyForStaffChecker
def deleteProduct(request):
    body = request.data["params"]
    Product.remove(id=body["id"])
    response = JsonResponse({
        "result": "OK",
    })
    response.status_code = 200
    return response


@csrf_exempt
@api_view(['GET', 'POST'])
@onlyForStaffChecker
def deleteTag(request, id):
    Tag.remove(id=id)
    response = JsonResponse({
        "result": "OK",
    })
    response.status_code = 200
    return response


@csrf_exempt
@api_view(['GET', 'POST'])
@onlyForLogginedChecker
def createProduct(request):
    body = request.data
    Profile.objects.get(user=request.user).products.add(
    Product.init(textTitle=body["Title"], text=body["Text"], dateAdded=datetime.now(),
                 files=[File.objects.create(file=x) for x in request.FILES.getlist("file")],
                 tags=[Tag.objects.get_or_create(tag=x) for x in body["tags"].split(",")], price=body["Price"],
                 family=body["family"])
    )
    response = JsonResponse({
        "result": "OK",
    })
    response.status_code = 200
    return response


@csrf_exempt
@api_view(['GET', 'POST'])
def search(request):
    body = request.data["params"]
    response = JsonResponse({
        "result": "GotOut",
        "data": [{"id": x.id, "textTitle": x.textTitle, "text": x.text} for x in
                 Product.objects.filter(textTitle__contains=body["search"])[::-1]],
    })
    response.status_code = 200
    return response


@csrf_exempt
@api_view(['GET', 'POST'])
@onlyForLogginedChecker
def getInformationOfProductByID(request, num):
    response = JsonResponse({
        "result": "GotOut",
        "data": {"textTitle": Product.objects.get(id=num).textTitle, "text": Product.objects.get(id=num).text,
                 "dateAdded": Product.objects.get(id=num).dateAdded,
                 "files": [x.file.name for x in Product.objects.get(id=num).files.all()],
                 "tags": [x.tag for x in Product.objects.get(id=num).tags.all()],
                 },
    })
    response.status_code = 200
    return response

@csrf_exempt
@api_view(['GET', 'POST'])
@onlyForLogginedChecker
def getProductsInfo(request):
    listOfTags = dict.fromkeys(set([x.tags.all()[0].tag for x in Profile.objects.get(user=request.user).products.all()]))
    for object in Profile.objects.get(user=request.user).products.all():
        try:
            listOfTags[object.tags.all()[0].tag] = listOfTags[object.tags.all()[0].tag] + object.price
        except:
            listOfTags[object.tags.all()[0].tag] = 0 + object.price
    response = JsonResponse({
        "result": listOfTags,
        "keys": list(listOfTags.keys()),
        "values": list(listOfTags.values()),
        "budget": {"roof": Profile.objects.get(user=request.user).budget.totalBudget,
                   "current": sum(list(listOfTags.values()))}
    })
    response.status_code = 200
    return response


@csrf_exempt
@api_view(['GET', 'POST'])
def getListOfProducts(request):
    body = request.data["params"]
    response = JsonResponse({
        "dataf": body["amountOfDocuments"] if body["amountOfDocuments"] is not None else -1,
        "result": "GotOut",
        "data": [{"id": i.id, "textTitle": i.textTitle, "text": i.text, "price": i.price,
                  "images": [j.file.url for j in i.files.filter()], "tags" : [tag.tag for tag in i.tags.all()]} for i in
                 Profile.objects.get(user=request.user).products.all()[::-1][:body["amountOfDocuments"] if
                 body["amountOfDocuments"] is not None else -1]],
    })
    response.status_code = 200
    return response
