from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="livestock-index"),
    path("about/", views.about, name="livestock-about"),
    path("shop/", views.shop, name="livestock-shop"),
    path("cows/", views.cows, name="livestock-cows"),
    path("cows/<int:id>/", views.cow, name="livestock-cow")
]

