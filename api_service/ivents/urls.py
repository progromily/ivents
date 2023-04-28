from django.urls import path

from ivents.views import *

urlpatterns = [
    path('', IventsView.as_view()),

    path('team/', TeamView.as_view()),
    path('teams/<int:pk>/', TeamViewList.as_view()),
    path('team/cat_ivents/<int:pk>/', ListIventsViewOfTeam.as_view()),

    path('regionalpartner/', RegionalPartnerView.as_view()),
    path('regionalpartners/<int:pk>/', RegionalPartnersView.as_view()),
]