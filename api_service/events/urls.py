from django.urls import path

from events.views import *

urlpatterns = [
    path('', EventsView.as_view()),

    path('team/', TeamView.as_view()),
    path('teams/<int:pk>/', TeamViewList.as_view()),
    path('team/cat_ivents/<int:pk>/', ListEventsViewOfTeam.as_view()),

    path('regionalpartner/', RegionalPartnerView.as_view()),
    path('regionalpartners/<int:pk>/', RegionalPartnersView.as_view()),
]