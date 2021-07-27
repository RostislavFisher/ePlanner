from django.http import JsonResponse
from django.shortcuts import render

from budget.models import budgetPlan
from documents.models import Family
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
