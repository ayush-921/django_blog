from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
)
from .models import Post  # importing post model


# def home(request):
#     context = {
#         "blog_posts": Post.objects.all(),  # querying all the post model
#     }
#     return render(request, "blog/home.html", context)


class PostListView(ListView):
    # PostListView is class based view which inherits from generic CBV ListView
    # Reason we are using ListView is home page shows list of Posts

    model = Post
    # model attribute take the model for which we are making the ListView

    template_name = "blog/home.html"
    # <app>/<model>_<viewtype>.html this is the default template name the ListView look for
    # but we have different template name available therefore in order to use that we use template_name attribute

    context_object_name = "blog_posts"
    # context_object_name attribute contains the context for the ListView inorder to generate the required lists
    # defualt context list is 'object_list'

    ordering = ["-date_posted"]
    # ordering show the list according to specified field here we are using -date_posted so that newest post is at the top


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    # CBV for create forms
    model = Post
    fields = ["title", "content"]
    # this will show a form with following fields

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})
