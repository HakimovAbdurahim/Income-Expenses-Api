from django.urls import path

# Project
from .views import IncomeListAPIView, IncomeDetailAPIView

urlpatterns = [
    path('', IncomeListAPIView.as_view(), name='incomes'),
    path('<int:pk>', IncomeDetailAPIView.as_view(), name='income'),
]