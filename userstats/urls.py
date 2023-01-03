from django.urls import path
# Project
from .views import ExpenseSummaryStats, IncomeSummaryStats

urlpatterns = [
    path('expense_category_date/', ExpenseSummaryStats.as_view(), name='expense-category-summary'),
    path('income_category_date/', IncomeSummaryStats.as_view(), name='income-category-summary'),
]