from django.urls import path
from .views import HomePageView, AboutPageView, PortPageView, ContPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(),name='about'),
    path('portfolio/', PortPageView.as_view(), name='portfolio'),
    path('contact/', ContPageView.as_view(), name='contact'),

]