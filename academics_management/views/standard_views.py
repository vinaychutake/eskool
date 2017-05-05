from django.contrib import messages
from django.shortcuts import render
from django.views.generic import View
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext_lazy as _
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.humanize.templatetags.humanize import naturaltime

from academics_management.api import standard_api
from academics_management.forms import StandardForm

class StandardManagement(View):
    """
    """

    def get(self, request):
        """
        """

        return render(request, "standard_management.html")

class CreateStandard(View):
    """
    """

    def get(self, request):
        """
        """

        form = StandardForm(initial={'standard': ' '})
        return render(request, 'standard.html', {'form': form, 'heading': _('Add')})

    def post(self, request):
        """
        """
        form = StandardForm(request.POST)
        if form.is_valid():
            try:
                template = form.cleaned_data.get('template')
                year = form.cleaned_data.get('year')
                status = form.cleaned_data.get('status')
                standard_api.create_standard(template, year, status)
                messages.success(request, _('Standard created successfully.'))

                if 'save_continue' in request.POST:
                    return HttpResponseRedirect(reverse('update_standard',
                                                        kwargs={'standard_id': subject_id}))
                elif 'add_another' in request.POST:    
                    return HttpResponseRedirect(reverse('create_standard'))

                else:
                    return HttpResponseRedirect(reverse('standard_management'))

            except ValidationError as e:
                for error,msgs in e:
                    for msg in msgs:
                        messages.error(request,msg)
        else:
            messages.error(request, _('Please correct the errors below.'))
                        
        return render(request, 'standard.html', {'form': form, 'heading': _('Add')})


class GetStandards(View):
    """
    """

    def get(self, request):
        """
        """
        page_no = int(request.GET.get('start'))
        records_per_page = int(request.GET.get('length'))
        page_no = page_no / records_per_page + 1

        standards = standard_api.get_standards(page_no=page_no,
                                            paginate=True,
                                            records_per_page=records_per_page)

        data = []
        for index, standard in enumerate(standards.get('standards', [])):
            standard = [index+1,
                      standard.name,
                      str(standard.standard_template),
                      str(standard.academic_year),
                      standard.get_status_display(),
                      """<button class="btn btn-default delete_notice mb-control" data-box="#mb-delete" id="{0}">
                         <span class="fa fa-trash-o"></span></button>""".format(standard.id)]
            data.append(standard)

        response = {'recordsTotal': standards.get('count'),
                    'data': data, 'recordsFiltered': standards.get('count')}

        return JsonResponse(response)


class DeleteStandard(View):
    """
    """

    def get(self, request, standard_id):
        """
        """
        standard_api.delete_standard(standard_id)
        messages.success(request, _('Standard deleted successfully.'))
        return HttpResponseRedirect(reverse('standard_management'))   
