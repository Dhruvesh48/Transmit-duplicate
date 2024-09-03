from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post, Community

# Create your views here.
def community_detail(request, name):
    """
    Display an individual :model:`blog.Community`.

    **Context**

    ``post``
        An instance of :model:`blog.Community`.

    **Template:**

    :template:`blog/community_detail.html`
    """

    community_profile = get_object_or_404(Community, name=name)
    community_posts = Post.objects.filter(status=1, community=community_profile)

    return render(
        request,
        "blog/community_detail.html",
        {
            "community_profile": community_profile,
            "community_posts": community_posts
        },
    )

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/post_detail.html",
        {"post": post},
    )

