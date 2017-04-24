from django.shortcuts import render
from django.views.generic import View
from notice_board.api import *
#TODO: All this view requires login required decorator

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
        create_notice(name, creator, group_names, text)
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
        update_notice(notice_id, group_names, text)
        pass

class DeleteNotice(View):
    """
    """

    def post(self, request, notice_id):
        """
        """
        delete_notice(notice_id)
        pass

class PublishNotice(View):
    """
    """

    def post(self, request, notice_id):
        """
        """
        publish_notice(notice_id)
        pass

class GetMyNotices(View):
    """
    """

    def get(self, request):
        """
        """
        user = request.user
        paginate = request.POST.get('paginate')
        page_no = request.POST.get('page_no')
        notice = get_user_notices(user, page_no, paginate)
        pass

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
        get_user_notices(user, page_no, paginate)
        pass
