from django.shortcuts import render
from django.views.generic import View

class ForgotPassword(View):
    """
    """

    def get(self, request):
        """
        """

        return render(request, 'forgot_password.html')

    def post(self, request):
        """
        """

        return render(request, 'forgot_password.html')