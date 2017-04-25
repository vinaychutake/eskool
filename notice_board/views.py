from django.shortcuts import render
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.core.urlresolvers import reverse

from notice_board import api as notice_api

class CreateNotice(View):
    """
    """

    def post(self, request):
        """
        """
        name = request.POST.get('name')
        creator = request.POST.get('creator')
        group_names = request.POST.get('group_names')
        text = request.POST.get('text')
        notice_api.create_notice(name, creator, group_names, text)

class UpdateNotice(View):
    """
    """

    def get(self, request, notice_id):
        """
        """

        pass

    def post(self, request, notice_id):
        """
        """
        text = request.GET.get('text')
        group_names = request.GET.get('name')
        notice_api.update_notice(notice_id, group_names, text)
        pass

class DeleteNotice(View):
    """
    """

    def post(self, request, notice_id):
        """
        """
        notice_api.delete_notice(notice_id)
        pass

class PublishNotice(View):
    """
    """

    def post(self, request, notice_id):
        """
        """
        notice_api.publish_notice(notice_id)
        pass

class ViewNotice(View):
    """
    """

    def get(self, request, notice_id):
        """
        """

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

class NoticeBoard(View):
    """
    """

    def get(self, request):
        """
        """

        return render(request, "notice_base.html")