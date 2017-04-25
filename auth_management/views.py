from django.shortcuts import render
from django.views.generic import View
from django.core.mail import send_mail
from django.contrib import messages

from auth_management import models as auth_models
from common.utils import check_email_validity

class ForgotPassword(View):
    """
    """

    def get(self, request):
        """
        """

        return render(request, 'forgot_password.html')

    def post(self, request):
        """
        """
        is_valid = check_email_validity(request.POST['email'])
        if not is_valid:
            messages.error(request, 'Provided email is in invalid format.')
        else:
            try:
                user = auth_models.User.objects.get(email = request.POST['email'])
                subject = 'Password reset for eskool'
                content = '''
Hi,

email content yet to be addded

Thanks,
Team eSkool
        '''
                send_mail(subject, content, 'support@eskool.com', [user.email])
                messages.success(request, 'Email sent successfuly.')
            except auth_models.User.DoesNotExist:
                messages.error(request, 'User with provided email does not exists.')
            except:
                messages.error(request, 'Error occured while processing your request.')

        return render(request, 'forgot_password.html')

