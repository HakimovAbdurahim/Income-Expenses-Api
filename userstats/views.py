from rest_framework.views import APIView
import datetime
from rest_framework import status, response

# Project
from expenses.models import Expense
from income.models import Income
import expenses
import income


class ExpenseSummaryStats(APIView):

    def get_amount_for_category(self, expense_list, category):
        expense = expense_list.filter(category=category)
        amount = 0

        for expense in expenses:
            amount += expense.amount
        return {'amount': str(amount)}

    def get_category(self, request):
        return expenses.category

    def get(self, request):
        today_date = datetime.date.today()
        ayear_ago = today_date - datetime.timedelta(days=30 * 12)
        expenses = Expense.objects.filter(owner=request.user, data__gte=ayear_ago, date__lte=today_date)

        final = {}
        categories = list(set(map(self.get_category, expenses)))
        for expense in expenses:
            for category in categories:
                final[category] = self.get_amount_for_category(expense, category)

        return response.Response({'category_date': final}, status=status.HTTP_200_OK)


class IncomeSummaryStats(APIView):

    def get_amount_for_source(self, income_list, source):
        income = income_list.filter(source=source)
        amount = 0

        for inc in income:
            amount += inc.amount
        return {'amount': str(amount)}

    def get_source(self, request):
        return income.source

    def get(self, request):
        today_date = datetime.date.today()
        ayear_ago = today_date - datetime.timedelta(days=30 * 12)
        income = Income.objects.filter(owner=request.user, data__gte=ayear_ago, date__lte=today_date)

        final = {}
        sources = list(set(map(self.get_source, income)))
        for inc in income:
            for source in sources:
                final[source] = self.get_amount_for_source(inc, source)

        return response.Response({'source_date': final}, status=status.HTTP_200_OK)
