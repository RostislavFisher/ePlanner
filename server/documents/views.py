from datetime import datetime

from django.conf import settings
from django.http import JsonResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from accountOperations.models import Profile
from documents.models import Tag, File

from errorPages.views import onlyForStaffChecker, onlyForLogginedChecker
from product.models import Product


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
def getListOfDocuments(request):
    body = request.data["params"]
    response = JsonResponse({
        "dataf": body["amountOfDocuments"] if body["amountOfDocuments"] is not None else -1,
        # "tags": [for tag in Profile.objects.get(user=request.user)],
        "result": "GotOut",
        "data": [{"id": i.id, "textTitle": i.textTitle, "text": i.text, "price": i.price,
                  "images": [j.file.url for j in i.files.filter()], "tags" : [tag.tag for tag in i.tags.all()]} for i in
                 Profile.objects.get(user=request.user).products.all()[::-1][:body["amountOfDocuments"] if
                 body["amountOfDocuments"] is not None else -1]],
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


@csrf_exempt
@api_view(['GET', 'POST'])
@onlyForStaffChecker
def deleteDocument(request):
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
def createDocument(request):
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
    print(body)
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
def getInformationOfDocumentByID(request, num):
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
