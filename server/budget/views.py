from django.http import JsonResponse
from django.shortcuts import render

from accountOperations.models import Profile
from budget.models import budgetPlan, budgetItem
from file.models import Family
from errorPages.views import onlyForLogginedChecker
import json


@onlyForLogginedChecker
def budgetEdit(request):
    body = request.GET
    try:
        budget = Profile.objects.get(user=request.user).budget
        budget.totalBudget = body["roof"]
        budget.budgetItem.all().delete()
        for item in body.getlist("budgetItems[]"):
            item = json.loads(''.join(item))
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
