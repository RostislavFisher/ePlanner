import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from budget.models import budgetPlan
from file.models import Family
from errorPages.views import onlyForLogginedChecker
from product.models import Product


@onlyForLogginedChecker
def createFamily(request):
    body = request.GET
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
    for product in Product.objects.filter(family=Family.objects.get(id=body["familyID"])):
        try:
            listOfTags[product.tags.all()[0].tag] = listOfTags[product.tags.all()[0].tag] + product.price
        except:
            listOfTags[product.tags.all()[0].tag] = 0 + product.price
    response = JsonResponse({
        "result": listOfTags,
        "keys": list(listOfTags.keys()),
        "values": list(listOfTags.values()),
        "budget": {"roof": Family.objects.get(id=body["familyID"]).budget.totalBudget,
                   "current": sum(list(listOfTags.values()))},
        "data": [{"id": i.id, "textTitle": i.textTitle, "text": i.text, "price": i.price,
                  "images": [j.file.url for j in i.files.filter()], "tags": [tag.tag for tag in i.tags.all()]} for i in
                 Product.objects.filter(family=Family.objects.get(id=body["familyID"]))]

    })
    response.status_code = 200
    return response


@csrf_exempt
@api_view(['GET', 'POST'])
def getListOfFamilyProducts(request):
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
            "budgetItems": [{"id": x.id, "title": x.title, "budget": x.budget} for x in budget.budgetItem.all()],

        })
        response.status_code = 200
    except:
        response = JsonResponse({
            "result": "error"
        })
        response.status_code = 500
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
            print(item["title"], item["budget"])
            budgetItemObject = budget.budgetItem.get_or_create(title=item["title"])[0]
            budgetItemObject.budget = item["budget"]
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
