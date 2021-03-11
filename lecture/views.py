from django.db import models
from django.shortcuts import reverse, render, redirect

# from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from datetime import datetime
from .models import Event, applications


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # context['book_list'] = Book.objects.all()
        return context


def appliedEvents(request, user_pk):
    apps = applications.objects.filter(student=user_pk)
    eventobj_list = []
    for app in apps:
        eventobj = Event.objects.get(event_name=app.event)
        eventobj_list.append(eventobj)
    return render(request, "appliedEvents.html", {"events": eventobj_list})


def upcomingEvents(request, user_pk):
    eventobj_list = Event.objects.filter(status=Event.EventStatus.ON_SCHEDULE)
    eventobj_list = list(eventobj_list)
    apps = applications.objects.filter(student=user_pk)
    eventobj_lists = []
    print(eventobj_list)
    for app in apps:
        eventobj = Event.objects.get(event_name=app.event)
        eventobj_lists.append(eventobj)
    for eventobj in eventobj_lists:
        eventobj_list.remove(eventobj)
    print(eventobj_list)
    return render(request, "upcomingEvents.html", {"events": eventobj_list})


def pastEvents(request, user_pk):
    apps = applications.objects.filter(student=user_pk)
    eventobj_list = []
    for app in apps:
        eventobj = Event.objects.get(event_name=app.event)
        if eventobj.end_date > datetime.now():
            eventobj_list.append(eventobj)
    return render(request, "pastEvents.html", {"events": eventobj_list})


class EventView(DetailView):
    template_name = "event.html"
    model = Event
    context_object_name = "event"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['already_applied'] = applications.has_applied(user_pk=self.kwargs["user_pk"], event_pk=context['event'].pk)
        
        return context



def eventRegistrationView(request, user_pk, pk):
    event = Event.objects.get(pk=pk)
    event.register_to_event(user=request.user)
    return redirect(reverse('lecture_app:event', kwargs=dict(user_pk=user_pk,pk=pk)))


# @login_required()
# def home_view(request, username):
#     user = CustomUser.objects.get(username = username)

#     return render(request, 'stud_app/home.html', context={
#         'username': username,
#         'student' : student,
#         'name': student.get_name(),
#         'current_page': 'home',

#     })
