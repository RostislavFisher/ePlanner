"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token

from budget.views import budgetEdit, returnUserInfo, returnBudgetOfUser
from accountOperations.views import checkifLogged, loginUser, returnUserInformation, logOut_view, \
     getUserListInformation, deleteAccount,  checkIfHasItExpired
from accountOperations.views import register
from documents.views import getListOfDocuments, getListOfTags, search, createDocument, createTags, deleteTag, \
    deleteDocument, getInformationOfDocumentByID, downloadFile, getProductsInfo
from family.views import createFamily, getProductsInfoByFamily, getListOfFamilyDocuments, returnBudgetOfFamily, \
    budgetFamilyEdit
from tariff.views import tariffs, deleteTariff, createTariff

urlpatterns = [
    # path('admin', admin.site.urls),
    path('api-token-auth', obtain_auth_token, name='api_token_auth'),

    path('checkIfLogged', checkifLogged),
    path('registerUser', register, name='registerUser'),
    path('loginUser', loginUser, name='loginUser'),
    path('logOut', logOut_view, name='logOut'),
    path('getUserListInformation', getUserListInformation, name='getUserListInformation'),
    path('returnUserInformation', returnUserInformation, name='returnUserInformation'),
    path('checkIfHasItExpired', checkIfHasItExpired, name='checkIfHasItExpired'),
    path('deleteAccount', deleteAccount, name='deleteAccount'),
    path('returnUserInfo', returnUserInfo, name='returnUserInfo'),

    path('getInformationOfDocumentByID/<int:num>/', getInformationOfDocumentByID, name='getInformationOfDocumentByID'),
    path('getListOfDocuments', getListOfDocuments, name='getListOfDocuments'),
    path('createDocument', createDocument, name='createDocument'),
    path('deleteDocument', deleteDocument, name='deleteDocument'),
    path('downloadFile/<path:path>', downloadFile, name='downloadFile'),

    path('getListOfTags', getListOfTags, name='getListOfTags'),
    path('search', search, name='search'),
    path('createTags', createTags, name='createTags'),
    path('deleteTag/<int:id>/', deleteTag, name='deleteTag'),


    path('budgetEdit', budgetEdit, name='budgetEdit'),
    path('returnBudgetOfUser', returnBudgetOfUser, name='returnBudgetOfUser'),
    path('getProductsInfo', getProductsInfo, name='getProductsInfo'),


    path('deleteTariff/<int:id>/', deleteTariff, name='deleteTariff'),
    path('getTariffsList', tariffs, name='tariffs'),
    path('getTariffInformation/<int:id>/', tariffs, name='tariffs'),
    path('createTariff', createTariff, name='createTariff'),


    path('createFamily', createFamily, name='createFamily'),
    path('getProductsInfoByFamily', getProductsInfoByFamily, name='getProductsInfoByFamily'),
    path('getListOfFamilyDocuments', getListOfFamilyDocuments, name='getListOfFamilyDocuments'),
    path('returnBudgetOfFamily', returnBudgetOfFamily, name='returnBudgetOfFamily'),
    path('budgetFamilyEdit', budgetFamilyEdit, name='budgetFamilyEdit'),
]
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns +=[re_path(r'^.*$', TemplateView.as_view(template_name='index.html'), name='index')]