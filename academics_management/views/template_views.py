from django.contrib import messages
from django.shortcuts import render
from django.views.generic import View
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext_lazy as _
from django.http import JsonResponse, HttpResponseRedirect

from academics_management.api import template_api
from academics_management.forms import STDTemplateForm

class StandardTemplateManagement(View):
    """
    """

    def get(self, request):
        """
        """

        return render(request, "standard_template_management.html")


class STDTemplates(View):
    """
    """

    def get(self, request):
        """
        """

        page_no = int(request.GET.get('start'))
        records_per_page = int(request.GET.get('length'))
        page_no = page_no / records_per_page + 1

        std_templates = template_api.get_std_templates(page_no=page_no,
                                                       paginate=True,
                                                       records_per_page=records_per_page)

        data = []
        for index, std_template in enumerate(std_templates.get('std_templates', []), 1):
            
            std_template_data = [index,
                      "%s" %(std_template.name),

                      "%s"%(std_template.code),

                      """<a href={0}> <span class='fa fa-pencil'>
                      </span></a>""".format(reverse('update_std_template', kwargs={'std_template_id': std_template.id})),

                      """<button class="btn btn-default delete_notice mb-control" data-box="#mb-delete" id="{0}">
                         <span class="fa fa-trash-o"></span></button>""".format(std_template.id)]

            data.append(std_template_data)

        response = {'recordsTotal': std_templates.get('count'),
                    'data': data, 'recordsFiltered': std_templates.get('count')}

        return JsonResponse(response)


class UpdateSTDTemplate(View):
    """
    """

    def get(self, request, std_template_id):
        """
        """
        std_template = template_api.get_std_template_obj(std_template_id)
        form = STDTemplateForm({'name': std_template.name,
                                'code': std_template.code,
                                'subjects': std_template.subjects.all()})
        return render(request, 'standard_template.html',
                      {'form': form, 'heading': _('Edit'),
                      'template_id': std_template_id})

    def post(self, request, std_template_id):
        """
        """

        form = STDTemplateForm(request.POST)
        if form.is_valid():
            try:
                code = form.cleaned_data.get('code')
                name = form.cleaned_data.get('name')
                subjects = form.cleaned_data.get('subjects')
                template_api.update_std_template(std_template_id, name, code, subjects)
                messages.success(request, _('Template updated successfully.'))
                if 'save_continue' in request.POST:
                    return HttpResponseRedirect(reverse('update_std_template',
                                                        kwargs={'std_template_id': std_template_id}))
                elif 'add_another' in request.POST:    
                    return HttpResponseRedirect(reverse('create_std_template'))
                else:
                    return HttpResponseRedirect(reverse('standard_template_management'))

            except ValidationError as e:
                for error,msgs in e:
                    for msg in msgs:
                        messages.error(request,msg)

        else:
            messages.error(request, _('Please correct the errors below.'))
        return render(request, 'standard_template.html',
                      {'form': form, 'heading': _('Edit'),
                      'template_id': std_template_id})

class CreateSTDTemplate(View):
    """
    """

    def get(self, request):
        """
        """

        form = STDTemplateForm()
        return render(request, 'standard_template.html',
                      {'form': form, 'heading': _('Add')})

    def post(self, request):
        """
        """

        form = STDTemplateForm(request.POST)
        if form.is_valid():
            try:
                code = form.cleaned_data.get('code')
                name = form.cleaned_data.get('name')
                subjects = form.cleaned_data.get('subjects')
                std_template_id = template_api.create_std_template(name, code, subjects)
                messages.success(request, _('Template created successfully.'))
                if 'save_continue' in request.POST:
                    return HttpResponseRedirect(reverse('update_std_template',
                                                        kwargs={'std_template_id': std_template_id}))
                elif 'add_another' in request.POST:    
                    return HttpResponseRedirect(reverse('create_std_template'))
                else:
                    return HttpResponseRedirect(reverse('standard_template_management'))

            except ValidationError as e:
                for error,msgs in e:
                    for msg in msgs:
                        messages.error(request,msg)
        else:
            messages.error(request, _('Please correct the errors below.'))
        return render(request, 'standard_template.html',
                      {'form': form, 'heading': _('Add')})

class DeleteSTDTemplate(View):
    """
    """

    def get(self, request, std_template_id):
        """
        """
        template_api.delete_std_template(std_template_id)
        messages.success(request, _('Template deleted successfully.'))
        return HttpResponseRedirect(reverse('standard_template_management'))
