from django.contrib.auth.decorators import user_passes_test
from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
def handler403(request, *args, **argv):
    response = JsonResponse({
        "error": "csrfTokenError"
    })
    response.status_code = 404
    return response


def onlyForStaffChecker(function):
    def decorator(request):
        if request.user.is_staff:
            return function(request)
        else:
            response = JsonResponse({
                "error": "isNotStaff"
            })
            response.status_code = 404
            return response

    return decorator


def onlyForLogginedChecker(function):
    def decorator(request):
        if request.user:
            return function(request)
        else:
            response = JsonResponse({
                "error": "isNotLoggined"
            })
            response.status_code = 404
            return response

    return decorator
