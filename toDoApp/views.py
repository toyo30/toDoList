from django.shortcuts import render, redirect
from .models import Post
from datetime import date
# Create your views here.
def home(request):
    posts = Post.objects.all()
    # today = datetime.datetime.today().replace(microsecond=0)
    today = date.today().isoformat()
    return render(request, 'home.html', {
        'posts': posts,
        'today' : today,
        })



def new(request):
    if request.method == 'POST':
        Post.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            date = request.POST['date'],
        )
        return redirect('home')
    return render(request, 'new.html')


def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    
    return render(request, 'detail.html', {'post': post})


def edit(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == 'POST':
        Post.objects.filter(pk=post_pk).update(
            title = request.POST['title'],
            content = request.POST['content'],
        )
        return redirect('detail', post_pk)
    
    return render(request, 'edit.html', {'post': post})


def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()

    return redirect('home')