"""
Portal views
"""

from django.shortcuts import render
from django.views.generic import View

class LandingView(View):
    """
    """
    def get(self, request):
        """
        """

        return render(request, "{0}.html".format(request.tenant.code))
