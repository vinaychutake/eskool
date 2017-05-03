from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class AcademicsManagement(View):
    """
    """

    def get(self, request):
        """
        """

        return render(request, "academic_management.html")
