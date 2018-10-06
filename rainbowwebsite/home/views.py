from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from home.forms import SignUpForm

# Create your views here.
def index(request):
    return render(request, "home/index.html", {"index": index})

def aboutus(request):
    return render(request, "home/aboutus.html", {"aboutus": aboutus})

class SignUpFormView(View):
    form_class = SignUpForm
    template_name = 'home/signup.html'

    #if there is no sign up yet
    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    #if going to sig up
    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            #it takes information but does save it
            user = form.save(commit = False)
            #cleaned normalized data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #returns if it is all correct

            user = authenticate(username = username, password = password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect("userprofile:newprofile")

        return render(request, self.template_name, {'form': form})

def success(request):
    return render(request, "home/successreport.html", {'success': success})

def terms(request):
    return render(request, "home/terms.html", {'terms': terms})
