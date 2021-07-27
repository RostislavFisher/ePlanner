import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from accountOperations.models import Profile
from budget.models import budgetPlan
from documents.models import Family, Product
from errorPages.views import onlyForLogginedChecker


@onlyForLogginedChecker
def createFamily(request):
    body = request.GET
    print(body["Title"])
    try:
        Family.objects.create(title=body["Title"], budget=budgetPlan.objects.create()).users.add(request.user)
        response = JsonResponse({
            "result": "successfully"
        })
        response.status_code = 200
    except:
        response = JsonResponse({
            "result": "error"
        })
        response.status_code = 500
    return response


@csrf_exempt
@api_view(['GET', 'POST'])
@onlyForLogginedChecker
def getProductsInfoByFamily(request):
    body = request.GET
    listOfTags = dict.fromkeys(
        set([x.tags.all()[0].tag for x in Product.objects.filter(family=Family.objects.get(id=body["familyID"]))]))
    for object in Product.objects.filter(family=Family.objects.get(id=body["familyID"])):
        try:
            listOfTags[object.tags.all()[0].tag] = listOfTags[object.tags.all()[0].tag] + object.price
        except:
            listOfTags[object.tags.all()[0].tag] = 0 + object.price
    response = JsonResponse({
        "result": listOfTags,
        "keys": list(listOfTags.keys()),
        "values": list(listOfTags.values()),
        "budget": {"roof": Family.objects.get(id=body["familyID"]).budget.totalBudget,
                   "current": sum(list(listOfTags.values()))}
    })
    response.status_code = 200
    return response


@csrf_exempt
@api_view(['GET', 'POST'])
def getListOfFamilyDocuments(request):
    body = request.GET
    response = JsonResponse({
        "result": "GotOut",
        "data": [{"id": i.id, "textTitle": i.textTitle, "text": i.text, "price": i.price,
                  "images": [j.file.url for j in i.files.filter()], "tags": [tag.tag for tag in i.tags.all()]} for i in
                 Product.objects.filter(family=Family.objects.get(id=body["familyID"]))]
    })
    response.status_code = 200
    return response


@onlyForLogginedChecker
def returnBudgetOfFamily(request):
    body = request.GET
    try:
        budget = Family.objects.get(id=body["familyID"]).budget
        response = JsonResponse({
            "result": "successfully",
            "totalBudget": budget.totalBudget,
            "budgetItems": [[x.title, x.budget] for x in budget.budgetItem.all()]
        })
        response.status_code = 200
    except:
        response = JsonResponse({
            "result": "error"
        })
        response.status_code = 500
    return response


@onlyForLogginedChecker
def budgetEdit(request):
    body = request.GET
    try:
        budget = Family.objects.get(id=body["familyID"])
        budget.totalBudget = body["totalBudget"]
        budget.budgetItem.all().delete()
        for item in body.getlist("budgetList[]"):
            item = json.loads(''.join(item))
            budgetItemObject = budget.budgetItem.get_or_create(title=item["Type"])[0]
            budgetItemObject.budget = item["Limit"]
            budgetItemObject.save()
            budget.budgetItem.add(budgetItemObject)
        budget.save()
        response = JsonResponse({
            "result": "successfully"
        })
        response.status_code = 200
    except:
        response = JsonResponse({
            "result": "error"
        })
        response.status_code = 200
    return response


@onlyForLogginedChecker
def budgetFamilyEdit(request):
    body = request.GET
    try:
        budget = Family.objects.get(id=body["familyID"]).budget
        budget.totalBudget = body["totalBudget"]
        budget.budgetItem.all().delete()
        for item in body.getlist("budgetList[]"):
            item = json.loads(''.join(item))
            budgetItemObject = budget.budgetItem.get_or_create(title=item["Type"])[0]
            budgetItemObject.budget = item["Limit"]
            budgetItemObject.save()
            budget.budgetItem.add(budgetItemObject)
        budget.save()
        response = JsonResponse({
            "result": "successfully"
        })
        response.status_code = 200
    except:
        response = JsonResponse({
            "result": "error"
        })
        response.status_code = 200
    return response
