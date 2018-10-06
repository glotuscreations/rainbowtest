from django.shortcuts import render
from django.views.generic import UpdateView, FormView, DetailView, ListView, DeleteView
from userprofile.forms import UserProfileForm, ContactForm
from userprofile.models import UserProfiles
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from userprofile.filters import UserProfilesFilter
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import redirect

# Create your views here.

class NewUserProfileView(FormView,LoginRequiredMixin):
    template_name = "userprofile/user_profile.html"
    form_class = UserProfileForm

    def form_valid(self, form):
        try:
            form.save(self.request.user)
            return super(NewUserProfileView, self).form_valid(form)
        except IntegrityError:
            return HttpResponse("You have already created a profile, please click back and click on My Profile.")

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy("home:index")


class EditUserProfileView(UpdateView, LoginRequiredMixin):

    model = UserProfiles
    form_class = UserProfileForm
    template_name = "userprofile/user_profile.html"
    slug_field = 'slug'

    def get_object(self, *args, **kwargs):

        user = get_object_or_404(User, pk=self.kwargs['pk'])
        return user.userprofiles

        def form_valid(self, form):
            print(form.cleaned_data)
            return super().form_valid(form)

    def get_success_url(self, *args, **kwargs):
         return reverse_lazy('home:index')


@login_required
def profiles_list(request):
    filter = UserProfilesFilter(request.GET, queryset = UserProfiles.objects.all().order_by('-pub_date'))
    return render(request,"userprofile/user_list.html", {'filter': filter})

@login_required
def profile_details(request,slug):
    profile = get_object_or_404(UserProfiles, slug=slug)
    return render(request, 'userprofile/profile_detail.html', {'profile': profile})

class UserProfileDelete(DeleteView, LoginRequiredMixin):
    model = UserProfiles
    success_url = reverse_lazy('home:index')
    template_name = "userprofile/profile_delete.html"

     # override the delete function to check for a user match
    def delete(self, request, *args, **kwargs):
        # the Post object
        self.object = self.get_object()
        if self.object.user == request.user:
            success_url = self.get_success_url()
            self.object.delete()
            return HttpResponseRedirect(success_url)
        else:
            return HttpResponse("Cannot delete other's profiles")


def contact(request, slug):

    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            Username = form.cleaned_data['Username']
            Reason = form.cleaned_data['Reason']
            Explanation = form.cleaned_data['Explanation']
            try:
                send_mail(Username,Explanation, 'report@rainbowsaathimail.com', ['rainbowsaathimail@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('home:success')
    return render(request, "userprofile/report.html", {'form': form})
