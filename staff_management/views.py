from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.humanize.templatetags.humanize import naturalday
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
from django.db import IntegrityError, transaction

from staff_management import api as sm_api
from staff_management.forms import StaffForm

class StaffManagement(View):
    """
    """

    def get(self, request):
        """
        """

        page_no = int(request.GET.get('page', 1))

        staff = sm_api.get_staff(page_no=page_no,
                                 paginate=True,
                                 records_per_page=10)

        return render(request, 'staff_management.html', {'staff': staff})

class CreateStaff(View):
    """
    """

    def get(self, request):
        """
        """
        form  = StaffForm()
        return render(request, "staff.html", {'form': form, 'heading': _('Add')})

    def post(self, request):
        """
        """
        form  = StaffForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            middle_name = form.cleaned_data.get('middle_name')
            last_name = form.cleaned_data.get('last_name')
            date_of_birth = form.cleaned_data.get('date_of_birth')
            email = form.cleaned_data.get('email')
            profile_pic = form.cleaned_data.get('profile_pic')
            gender = form.cleaned_data.get('gender')
            staff_type = form.cleaned_data.get('staff_type')
            joining_date = form.cleaned_data.get('joining_date')
            city = form.cleaned_data.get('city')
            address1 = form.cleaned_data.get('address1')
            address2 = form.cleaned_data.get('address2')
            address3 = form.cleaned_data.get('address3')
            contact_number = form.cleaned_data.get('contact_num')
            reporting_to = form.cleaned_data.get('reporting_to')

            with transaction.atomic():

                user = sm_api.create_user(username, first_name, middle_name,
                                          last_name, date_of_birth,
                                          email, profile_pic, gender)

                sm_api.add_user_address(user, address1, address2, address3, city)

                sm_api.add_user_contactnumber(user, contact_number)

                sm_api.create_staff(user, staff_type, joining_date, reporting_to)

            messages.success(request, _('New staff user created successfully.'))
            return HttpResponseRedirect(reverse('staff_management'))
        else:
            messages.error(request, _('Please correct the errors below.'))
            return render(request, "staff.html", {'form': form, 'heading': _('Add')})

class UpdateStaff(View):
    """
    """

    def get(self, request, staff_id):
        """
        """
        pass

    def post(self, request, staff_id):
        """
        """
        pass

class DeleteStaff(View):
    """
    """

    def get(self, request, staff_id):
        """
        """
        pass

    def post(self, request, staff_id):
        """
        """
        pass

class UploadStaff(View):
    """
    """

    def get(self, request):
        """
        """
        pass

    def post(self, request):
        """
        """
        pass

class ViewStaffProfile(View):
    """
    """

    def get(self, request, staff_id):
        """
        """
        pass

class CreateTeacher(View):
    """
    """

    def get(self, request):
        """
        """
        # form = UserForm()
        # return render(request, 'create_teacher.html',
        #               {'form': form})
        pass

    def post(self, request):
        """
        """

        pass

        # form = UserForm(request.POST)
        # if form.is_valid():
        #     username = form.cleaned_data['username']
        #     first_name = form.cleaned_data['first_name']
        #     middle_name = form.cleaned_data['middle_name']
        #     last_name = form.cleaned_data['last_name']
        #     print username
        #     print first_name
        #     print middle_name
        #     print last_name

            # date_of_birth = form.cleaned_data['date_of_birth']
            # email = form.cleaned_data['email']
            # profile_pic = form.cleaned_data['profile_pic']
            # gender = form.cleaned_data['gender']
            # contact_number = form.cleaned_data['contact_number']
            # state = form.cleaned_data['state']
            # city = form.cleaned_data['city']
            # address1 = form.cleaned_data['address1']
            # address2 = form.cleaned_data['address2']
            # address3 = form.cleaned_data['address3']
            # subjects = form.cleaned_data['subjects']

        # else:
        #     print form.errors
        #     return render(request, 'create_teacher.html',
        #               {'form': form})


class UpdateTeacher(View):
    """
    """

    def get(self, request, teacher_id):
        """
        """
        pass

    def post(self, request, teacher_id):
        """
        """
        pass

class DeleteTeacher(View):
    """
    """

    def get(self, request, teacher_id):
        """
        """
        pass

    def post(self, request, teacher_id):
        """
        """
        pass

class UploadTeachers(View):
    """
    """

    def get(self, request):
        """
        """
        pass

    def post(self, request):
        """
        """
        pass

class ViewTeacherProfile(View):
    """
    """

    def get(self, request, teacher_id):
        """
        """
        pass