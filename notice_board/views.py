from django.shortcuts import render
from django.views.generic import View

#TODO: All this view requires login required decorator

class CreateNotice(View):
    """
    """

    def post(self, request):
        """
        """
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
        pass

class DeleteNotice(View):
    """
    """

    def post(self, request, notice_id):
        """
        """
        pass

class PublishNotice(View):
    """
    """

    def post(self, request, notice_id):
        """
        """
        pass

class GetMyNotices(View):
    """
    """

    def get(self, request):
        """
        """
        pass

class ListNotices(View):
    """
    """

    def get(self, request):
        """
        """
        #Return all notifications if user is admin of institute,
        #else only return notices created by logged in user

        pass
