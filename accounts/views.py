from django.http import HttpResponse, HttpResponseRedirect
from django.urls.base import reverse_lazy

from django.conf import settings
from django.views.generic import CreateView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import authenticate, get_user_model, login
from django.shortcuts import reverse, render

# from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CustomUserCreationForm


CustomUser = get_user_model()


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy(settings.LOGIN_URL)

def login_view(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = CustomUser.objects.get(username = username)
        except CustomUser.DoesNotExist:
            context = { 
                'no_user' : True,
                'first_render' : False,
                'wrong_password' : False,
            } 
            return render(request, 'registration/login.html', context)
        else:
            if user.check_password(password):
                # if student.user.is_authenticated:
                #     return HttpResponseRedirect(reverse('lecture_app:home', args=[username,]))
                # else:
                #     return HttpResponse('not authenticated')
                account = authenticate(username=username, password=password)
                login(request, account)
                # if not request.POST.get('remember_me', None):
                #     request.session.set_expiry(0)

                context = {
                    'user': user,
                }
                return HttpResponseRedirect(reverse(settings.LOGIN_REDIRECT_URL), context)

            else:
                context = { 
                'wrong_password' : True,
                'no_user' : False,
                'first_render' : False,
                } 
                return render(request, 'registration/login.html', context)
    else:
        context = { 
                'first_render' : True,
                'wrong_password' : False,
                'no_user' : False,
            } 
        return render(request, 'registration/login.html', context)

class CustomLogOutView(LogoutView):
    template_name = 'registration/logout.html'