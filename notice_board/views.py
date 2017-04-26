from django.shortcuts import render
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages

from notice_board import api as notice_api
from notice_board.forms import NoticeForm

class CreateNotice(View):
    """
    """

    def get(self, request):
        """
        """

        form = NoticeForm()
        return render(request, 'notice.html', {'form': form, 'heading': _('Add')})

    def post(self, request):
        """
        """

        form = NoticeForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('notice')
            name = form.cleaned_data.get('title')
            groups = form.cleaned_data.get('to')
            notice_api.create_notice(name, request.user, groups, text)
            messages.success(request, _('Notice created successfully.'))
            return HttpResponseRedirect(reverse('notice_board'))
        else:
            messages.error(request, _('Please correct the errors below.'))
        return render(request, 'notice.html', {'form': form, 'heading': _('Add')})

class UpdateNotice(View):
    """
    """

    def get(self, request, notice_id):
        """
        """
        try:
            notice = notice_api.get_notice_obj(notice_id)
            form = NoticeForm({'title': notice.name,
                               'notice': notice.text,
                               'to': notice.groups.all()})
            return render(request, 'notice.html', {'form': form, 'heading': _('Edit')})
        except ObjectDoesNotExist:
            raise Http404

    def post(self, request, notice_id):
        """
        """

        form = NoticeForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('notice')
            name = form.cleaned_data.get('title')
            groups = form.cleaned_data.get('to')
            notice_api.update_notice(notice_id, name, groups, text)
            messages.success(request, _('Notice updated successfully.'))
            return HttpResponseRedirect(reverse('notice_board'))
        else:
            messages.error(request, _('Please correct the errors below.'))
        return render(request, 'notice.html', {'form': form, 'heading': _('Edit')})

class DeleteNotice(View):
    """
    """

    def get(self, request, notice_id):
        """
        """
        notice_api.delete_notice(notice_id)
        response = {'success':'true'}
        return JsonResponse(response)
 

class PublishNotice(View):
    """
    """

    def get(self, request, notice_id):
        """
        """
        notice_api.publish_notice(notice_id)
        response = {'success':'true'}
        return JsonResponse(response)

class ViewNotice(View):
    """
    """

    def get(self, request, notice_id):
        """
        """
        print '******here************'
        try:
            notice = notice_api.get_notice_obj(notice_id)
            return render(request, 'view_notice.html', {'notice': notice})
        except ObjectDoesNotExist:
            raise Http404

class GetMyNotices(View):
    """
    """

    def get(self, request):
        """
        """
        page_no = int(request.GET.get('start'))
        records_per_page = int(request.GET.get('length'))
        page_no = page_no / records_per_page + 1

        notices = notice_api.get_user_notices(request.user,
                                              page_no=page_no,
                                              paginate=True,
                                              records_per_page=records_per_page)

        data = []
        for index, notice in enumerate(notices.get('notices', [])):
            notice = [index+1,
                      "<a href=%s>%s</a>" %(reverse('view_notice',
                                                    kwargs={'notice_id': notice.id}),
                                            notice.name),
                      "%s ..." %(notice.text[:30]),
                      naturaltime(notice.creted_on)]
            data.append(notice)

        response = {'recordsTotal': notices.get('count'),
                    'data': data, 'recordsFiltered': notices.get('count')}

        return JsonResponse(response)

class ListNotices(View):
    """
    """

    def get(self, request):
        """
        """

        page_no = int(request.GET.get('start'))
        records_per_page = int(request.GET.get('length'))
        page_no = page_no / records_per_page + 1

        notices = notice_api.get_notices(request.user,
                                         page_no=page_no,
                                         paginate=True,
                                         records_per_page=records_per_page)

        data = []
        for index, notice in enumerate(notices.get('notices', [])):
            if notice.is_published:
                    published = """<label class="switch">
                         <input type="checkbox" class="switch publish_notice" checked value="True" id="{1}"/>
                       <span></span>
                       </label>
                       """.format(notice.is_published, notice.id)
            else:
                published = """<label class="switch">
                         <input type="checkbox" class="switch publish_notice" value="False" id="{1}"/>
                       <span></span>
                       </label>
                       """.format(notice.is_published, notice.id)
                       

            notice = [index+1,
                      """<a href=%s class="ls-modal" data-target="#myModal" data-toggle="modal">%s</a>""" %(reverse('view_notice', kwargs={'notice_id': notice.id}), notice.name),
                      "%s ..." %(notice.text[:30]), naturaltime(notice.creted_on),

                      """<a href={0}> <span class='fa fa-pencil'>
                      </span></a>""".format(reverse('update_notice', kwargs={'notice_id': notice.id})),

                      published,
                       """<button class="btn btn-default delete_notice" id="{0}">
                       <span class="fa fa-trash-o"></span></button>""".format(notice.id)]
            data.append(notice)

        response = {'recordsTotal': notices.get('count'),
                    'data': data, 'recordsFiltered': notices.get('count')}

        return JsonResponse(response)

class NoticeBoard(View):
    """
    """

    def get(self, request):
        """
        """

        return render(request, "notice_base.html")