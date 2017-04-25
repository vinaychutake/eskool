from django.shortcuts import render
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist

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
        pass

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

class GetMyNotices(View):
    """
    """

    def get(self, request):
        """
        """

        page_no = request.GET.get('page_no', 1)
        notices = notice_api.get_user_notices(request.user, page_no=page_no, paginate=False)
        return render(request, "my_notices.html", {'notices': notices})

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

class ListNotices(View):
    """
    """

    def get(self, request):
        """
        """
        #Return all notifications if user is admin of institute,
        #else only return notices created by logged in user

        user = User.objects.get(username=request.POST.get('user'))
        page_no = request.POST.get('page_no')
        paginate = request.POST.get('paginate')
        notice_api.get_user_notices(user, page_no, paginate)
        pass
