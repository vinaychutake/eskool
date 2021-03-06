from django.contrib import messages
from django.shortcuts import render
from django.views.generic import View
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.humanize.templatetags.humanize import naturaltime

from academics_management.api import year_api
from academics_management.forms import AcademicYearForm

class AcademicYearManagement(View):
    """
    """

    def get(self, request):
        """
        """

        return render(request, "acadamic_year_management.html")

class GetAcademicYears(View):
    """
    """

    def get(self, request):
        """
        """
        page_no =  int(request.GET.get('start'))
        records_per_page = int(request.GET.get('length'))
        page_no = page_no / records_per_page + 1

        years = year_api.get_academic_years(page_no=page_no,
                                            paginate=True,
                                            records_per_page=records_per_page)
        data = []

        for index, year in enumerate(years.get('years', [])):
            year = [index+1,
            year.name,
            year.get_status_display(),
            """<a href={0}> <span class='fa fa-pencil'>
            </span></a>""".format(reverse('update_academic_year',
                                           kwargs={'year_id': year.id})),
            """<button class="btn btn-default delete_year mb-control"
            data-box="#mb-delete"id="{0}"><span class="fa fa-trash-o">
            </span></button>""".format(year.id)]
            data.append(year)

        response = {'recordsTotal': years.get('count'),
        'data': data, 'recordsFiltered': years.get('count')}

        return JsonResponse(response)

class CreateAcademicYear(View):
    """
    """

    def get(self, request):
        """
        """

        form = AcademicYearForm()
        return render(request, 'academic_year.html',
                      {'form': form, 'heading': _('Add')})

    def post(self, request):
        """
        """

        form = AcademicYearForm(request.POST)
        if form.is_valid():
            try:
                name = form.cleaned_data.get('name')
                status = form.cleaned_data.get('status')
                year_id = year_api.create_academics_year(name, status)
                messages.success(request, _('Academic year created successfully.'))
                if 'save_continue' in request.POST:
                    return HttpResponseRedirect(reverse('update_academic_year',
                                                        kwargs={'year_id': year_id}))
                elif 'add_another' in request.POST:    
                    return HttpResponseRedirect(reverse('create_academic_year'))

                else:
                    return HttpResponseRedirect(reverse('academic_year_management'))
            except ValidationError as e:
                for error,msgs in e:
                    for msg in msgs:
                        messages.error(request,msg)
        else:
            messages.error(request, _('Please correct the errors below.'))

        return render(request, 'academic_year.html',
                      {'form': form, 'heading': _('Add')})

class UpdateYear(View):

    def get(self, request, year_id):

        year = year_api.get_academic_year_obj(year_id)
        form = AcademicYearForm({'name':year.name, 'status': year.status})
        return render(request, 'academic_year.html',
                      {'form': form, 'heading': _('Edit'), 'year_id':year_id})

    def post(self, request, year_id):

        form = AcademicYearForm(request.POST)
        if form.is_valid():
            try:
                name = form.cleaned_data.get('name')
                status = form.cleaned_data.get('status')
                year_api.update_year(year_id, name, status)
                messages.success(request, _('Academic year updated successfully.'))
                if 'save_continue' in request.POST:
                    return HttpResponseRedirect(reverse('update_academic_year',
                                                        kwargs={'year_id': year_id}))
                elif 'add_another' in request.POST:    
                    return HttpResponseRedirect(reverse('create_academic_year'))

                else:
                    return HttpResponseRedirect(reverse('academic_year_management'))
            except ValidationError as e:
                for error,msgs in e:
                    for msg in msgs:
                        messages.error(request,msg)

        else:
            return render(request, 'academic_year.html',
                          {'form': form, 'heading': _('Edit'), 'year_id':year_id})

        return render(request, 'academic_year.html',
                      {'form': form, 'heading': _('Edit'), 'year_id':year_id})

class DeleteYear(View):

    def get(self, request, year_id):
        """
        """
        year_api.delete_year(year_id)
        messages.success(request, _('Academic year deleted successfully.'))
        return HttpResponseRedirect(reverse('academic_year_management'))