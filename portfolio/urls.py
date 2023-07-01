from django.urls import path, include
from portfolio import views

urlpatterns = [
    path("portfolio/", views.portfolio, name="portfolio"),
]