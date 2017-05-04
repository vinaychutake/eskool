from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages

# Create your views here.
class AcademicsManagement(View):
    """
    """

    def get(self, request):
        """
        """

        return render(request, "academic_management.html")

