from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.core.urlresolvers import reverse
from django.contrib.humanize.templatetags.humanize import naturalday

from staff_management import api as sm_api
from staff_management.forms import UserForm

class CreateTeacher(View):
    """
    """

    def get(self, request):
        """
        """
        form = UserForm()
        return render(request, 'create_teacher.html',
                      {'form': form})

    def post(self, request):
        """
        """

        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            middle_name = form.cleaned_data['middle_name']
            last_name = form.cleaned_data['last_name']
            print username
            print first_name
            print middle_name
            print last_name

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

        else:
            print form.errors
            return render(request, 'create_teacher.html',
                      {'form': form})


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


class CreateStaff(View):
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

class StaffManagement(View):
    """
    """

    def get(self, request):
        """
        """
        return render(request, 'staff_management.html')

class GetNonTeachingStaff(View):
    """
    """

    def get(self, request):
        """
        """
        page_no = int(request.GET.get('start'))
        records_per_page = int(request.GET.get('length'))
        page_no = page_no / records_per_page + 1

        staff = sm_api.get_non_teaching_staff(page_no=page_no,
                                              paginate=True,
                                              records_per_page=records_per_page)

        data = []
        for index, staff_user in enumerate(staff.get('staff', [])):
            staff_user = [index+1,
                          "<a href=%s>%s</a>" %(reverse('view_notice',
                                                kwargs={'notice_id': staff_user.id}),
                                                staff_user.user.get_full_name()),
                          staff_user.staff_type.name,
                          naturalday(staff_user.joining_date)]
            data.append(staff_user)

        response = {'recordsTotal': staff.get('count'),
                    'data': data, 'recordsFiltered': staff.get('count')}

        return JsonResponse(response)

class GetTeachers(View):
    """
    """

    def get(self, request):
        """
        """
        page_no = int(request.GET.get('start'))
        records_per_page = int(request.GET.get('length'))
        page_no = page_no / records_per_page + 1

        teachers = sm_api.get_teachers(page_no=page_no,
                                       paginate=True,
                                       records_per_page=records_per_page)

        data = []
        for index, teacher in enumerate(teachers.get('teachers', [])):
            teacher = [index+1,
                       "<a href=%s>%s</a>" %(reverse('view_notice',
                                                kwargs={'notice_id': teacher.id}),
                                                teacher.staff.user.get_full_name()),
                       ", ".join([subject.name for subject in teacher.subjects.all()]),
                       naturalday(teacher.staff.joining_date)]
            data.append(teacher)

        response = {'recordsTotal': teachers.get('count'),
                    'data': data, 'recordsFiltered': teachers.get('count')}

        return JsonResponse(response)