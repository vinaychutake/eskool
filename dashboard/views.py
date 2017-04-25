from django.shortcuts import render
from django.views.generic import View
from communication_management.api import get_user_notifications

class IndexView(View):

	def get(self, request):
		context = {}
		user = request.user
		notifications = get_user_notifications(user, paginate=False)
		print 'notification',notifications
		return render(request, 'dashboard.html', {'user_notification':notifications})