from datetime import datetime

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login, authenticate
from django.http import JsonResponse, FileResponse
import json

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from accountOperations.models import Profile
from django.contrib.auth import logout

from budget.models import budgetPlan
from documents.models import Product, File, Tag
from errorPages.views import onlyForStaffChecker, onlyForLogginedChecker


@csrf_exempt
@api_view(['GET', 'POST'])
def logOut_view(request):
    try:
        logout(request)
        response = JsonResponse({
            "result": "IsLoggedOut"
        })
        response.status_code = 200
        return response
    except:
        response = JsonResponse({
            "result": "ERROR"
        })
        response.status_code = 404
        return response


@csrf_exempt
@api_view(['GET', 'POST'])
@onlyForLogginedChecker
def checkIfHasItExpired(request):
    if Profile.objects.get(user=request.user).expire_date > datetime.now().date():
        response = JsonResponse({
            "result": "currentlyWorks"
        })
    else:
        response = JsonResponse({
            "result": "currentlyDoesNotWorks"
        })
    response.status_code = 200
    return response


@csrf_exempt
@api_view(['GET', 'POST'])
@onlyForStaffChecker
def deleteAccount(request):
    if request.user.is_authenticated:
        body = request.data["params"]
        print(body)
        User.objects.get(id=body["id"]).delete()
        response = JsonResponse({
            "result": "GotOut"
        })
    else:
        response = JsonResponse({
            "result": "Error",
            "cause": "notAdmin"
        })
    response.status_code = 200
    return response


def checkifLogged(request):
    print("isStaff" if request.user.is_staff else "isLoggined" if request.user.is_authenticated else "isNotLoggined")
    return JsonResponse({
        'userStatus': "isStaff" if request.user.is_staff else "isLoginned" if request.user.is_authenticated else "isNotLoggined"})


@csrf_exempt
@api_view(['GET', 'POST'])
@onlyForLogginedChecker
def returnUserInformation(request):
        return JsonResponse({
            'userStatus': "isStaff" if request.user.is_staff else "isLoginned" if request.user.is_authenticated else "isNotLoggined",
            'username': request.user.username,
            'icon': Profile.objects.get(user=request.user).icon,
            'fullName': "{0} {1}".format(request.user.first_name, request.user.last_name),
            'email': request.user.email,
            'expire_date': Profile.objects.get(user=request.user).expire_date,
            'firstConnection_date': Profile.objects.get(user=request.user).firstConnection_date,
        })


@csrf_exempt
@api_view(['GET', 'POST'])
@onlyForStaffChecker
def getUserListInformation(request):
    listOfUsers = {"data": []}
    for userFromList in User.objects.all(): listOfUsers["data"].append({
        'id': userFromList.id,
        'userStatus': "isStaff" if userFromList.is_staff else "user",
        'username': userFromList.username,
        'fullName': "{0} {1}".format(userFromList.first_name, userFromList.last_name),
        'email': userFromList.email,
        'expire_date': Profile.objects.get(user=userFromList).expire_date,
        'firstConnection_date': Profile.objects.get(user=userFromList).firstConnection_date,

    })
    print(User.objects.all())
    return JsonResponse(listOfUsers, safe=False)


@csrf_exempt
@api_view(['GET', 'POST'])
def register(request):
    print(json.loads(request.body.decode('utf8')))
    body = json.loads(request.body.decode('utf8'))["params"]
    if body['password'] == body['confirm']:
        print("registered")
        user = User.objects.create_user(username=body['username'], email=body['email'],
                                        password=body['password'])
        budget = budgetPlan.objects.create(totalBudget=0)
        budget.save()
        Profile.createCell(user=user, expire_date=datetime.now(), firstConnection_date=datetime.now(), budget=budget)
        if user.is_active:
            login(request, user)
            return Response("Success", status=202)
        else:
            return Response("loginError", status=202)
    else:
        return Response("Passwords don't match", status=401)


@csrf_exempt
@api_view(['GET', 'POST'])
def loginUser(request):
    body = json.loads(request.body.decode('utf8'))["params"]
    try:

        if request.method == "POST":
            username = body['username']
            password = body['password']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return Response("Success", status=202)
    except:
        print("Error")
        return Response("Error!!!", status=202)


@csrf_exempt
@api_view(['GET', 'POST'])
def getUserProductInfromation(request):
    body = request.GET
    try:
        budget = Profile.objects.get(user=request.user).budget
        response = JsonResponse({
            "result": "successfully",
            "listOfTags": [x for x in budget.budgetItem],
            "families": [x for x in budget.budgetItem],
        })
        response.status_code = 200
    except:
        response = JsonResponse({
            "result": "error"
        })
        response.status_code = 200
    return response
