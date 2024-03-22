from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Post
from .forms import CommentForm

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "organic_eire/index.html"
    paginate_by = 4


def post_detail(request, slug):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.filter(approved=True).order_by("-created_on")
    comment_count = comments.count()
    comment_form = CommentForm(request.POST or None)

    if request.method == "POST" and comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()
        messages.add_message(
            request, messages.SUCCESS,
            'Comment submitted and awaiting approval'
        )
        comment_form = CommentForm()  # Reinitialize the form for a fresh instance

    return render(
        request,
        "organic_eire/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form  # Add this to the context
        },
    )
    