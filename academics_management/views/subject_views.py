from django.contrib import messages
from django.shortcuts import render
from django.views.generic import View
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext_lazy as _
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.humanize.templatetags.humanize import naturaltime

from academics_management.api import subject_api
from academics_management.forms import SubjectForm

class SubjectManagement(View):
    """
    """

    def get(self, request):
        """
        """

        return render(request, "subject_management.html")

class CreateSubject(View):
    """
    """

    def get(self, request):
        """
        """

        form = SubjectForm(initial={'subject': ' '})
        return render(request, 'subject.html', {'form': form, 'heading': _('Add')})

    def post(self, request):
        """
        """
        form = SubjectForm(request.POST)
        if form.is_valid():
            try:
                name = form.cleaned_data.get('name')
                status = form.cleaned_data.get('status')
                code = form.cleaned_data.get('code')
                subject_api.create_subject(name, status, code)
                messages.success(request, _('Subject created successfully.'))

                if 'save_continue' in request.POST:
                    return HttpResponseRedirect(reverse('update_subject',
                                                        kwargs={'subject_id': subject_id}))
                elif 'add_another' in request.POST:    
                    return HttpResponseRedirect(reverse('create_subject'))

                else:
                    return HttpResponseRedirect(reverse('subject_management'))

            except ValidationError as e:
                for error,msgs in e:
                    for msg in msgs:
                        messages.error(request,msg)
        else:
            messages.error(request, _('Please correct the errors below.'))
                        
        return render(request, 'subject.html', {'form': form, 'heading': _('Add')})


class GetSubjects(View):
    """
    """

    def get(self, request):
        """
        """
        page_no = int(request.GET.get('start'))
        records_per_page = int(request.GET.get('length'))
        page_no = page_no / records_per_page + 1

        subjects = subject_api.get_subjects(page_no=page_no,
                                            paginate=True,
                                            records_per_page=records_per_page)

        data = []
        for index, subject in enumerate(subjects.get('subjects', [])):
            subject = [index+1,
                      subject.name,
                      subject.code,
                      naturaltime(subject.creted_on),
                      subject.get_status_display(),
                      """<a href={0}> <span class='fa fa-pencil'>
                      </span></a>""".format(reverse('update_subject', kwargs={'subject_id': subject.id})),
                      """<button class="btn btn-default delete_notice mb-control" data-box="#mb-delete" id="{0}">
                         <span class="fa fa-trash-o"></span></button>""".format(subject.id)]
            data.append(subject)

        response = {'recordsTotal': subjects.get('count'),
                    'data': data, 'recordsFiltered': subjects.get('count')}

        return JsonResponse(response)

class UpdateSubject(View):
    """
    """
    
    def get(self, request, subject_id):
        """
        """
        subject = subject_api.get_subject_obj(subject_id)
        form = SubjectForm({'name': subject.name,
                            'status':subject.status,
                            'code':subject.code})
        return render(request, 'subject.html',
                      {'form': form, 'heading': _('Edit'),
                       'subject_id': subject_id})

    def post(self, request, subject_id):
        """
        """

        form = SubjectForm(request.POST)
        if form.is_valid():
            try:
                name = form.cleaned_data.get('name')
                status = form.cleaned_data.get('status')
                code = form.cleaned_data.get('code')
                subject_api.update_subject(subject_id, name, status, code)
                messages.success(request, _('Subject updated successfully.'))
                if 'save_continue' in request.POST:
                    return HttpResponseRedirect(reverse('update_subject',
                                                        kwargs={'subject_id': subject_id}))
                elif 'add_another' in request.POST:    
                    return HttpResponseRedirect(reverse('create_subject'))

                else:
                    return HttpResponseRedirect(reverse('subject_management'))

                return HttpResponseRedirect(reverse('subject_management'))
            except ValidationError as e:
                for error,msgs in e:
                    for msg in msgs:
                        messages.error(request,msg)
        else:
            messages.error(request, _('Please correct the errors below.'))
        return render(request, 'subject.html',
                      {'form': form, 'heading': _('Edit'),
                      'subject_id': subject_id})

class DeleteSubject(View):
    """
    """

    def get(self, request, subject_id):
        """
        """
        subject_api.delete_subject(subject_id)
        messages.success(request, _('Subject deleted successfully.'))
        return HttpResponseRedirect(reverse('subject_management'))   
