from django.urls import path

# Project
from .views import ExpenseListAPIView, ExpenseDetailAPIView

urlpatterns = [
    path('', ExpenseListAPIView.as_view(), name='expenses'),
    path('<int:pk>', ExpenseDetailAPIView.as_view(), name='expense'),
]