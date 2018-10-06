from django.shortcuts import render, redirect
from django.utils import timezone
from posts.models import Post
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from posts.forms import PostForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

# Create your views here.

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(reverse_lazy('posts:postshome'))
    else:
        form = PostForm()
    return render(request, 'posts/create.html', {'form': form})


def postshome(request):
    posts = Post.objects.order_by('-pub_date')
    return render(request, 'posts/posthome.html', {'posts':posts})


class PostDelete(DeleteView, LoginRequiredMixin):
    model = Post
    success_url = reverse_lazy('posts:postshome')
    template_name = "posts/post_delete.html"

     # override the delete function to check for a user match
    def delete(self, request, *args, **kwargs):
        # the Post object
        self.object = self.get_object()
        if self.object.author == request.user:
            success_url = self.get_success_url()
            self.object.delete()
            return HttpResponseRedirect(success_url)
        else:
            return HttpResponse("Cannot delete other's profiles")
