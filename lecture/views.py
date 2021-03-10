from django.shortcuts import reverse, render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from .models import Event,applications
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin




class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # context['book_list'] = Book.objects.all()
        return context

def appliedEvents(request,username):
    apps = applications.objects.filter(student=username)
    eventobj_list = []
    for app in apps:
        eventobj = Event.objects.get(event_name=app.event)
        eventobj_list.append(eventobj)
    return render(request,'appliedEvents.html',{'events':eventobj_list})

# @login_required()
# def home_view(request, username):
#     user = CustomUser.objects.get(username = username)

#     return render(request, 'stud_app/home.html', context={
#         'username': username,
#         'student' : student,
#         'name': student.get_name(),
#         'current_page': 'home',
        
#     })