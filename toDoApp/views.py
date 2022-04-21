from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
import datetime
import pdb
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import json
# from django.core import serializer
from django.utils import timezone


# Create your views here.
def home(request):
    posts = Post.objects.all()
    for post in posts:
        end = post.time_end
        current = datetime.datetime.now().replace(microsecond=0)
        current = current.strftime("%Y-%m-%d %H:%M:%S")
        end = end.replace(' ', '')
        end = end.replace(':', '')
        end = end.replace('-', '')
        current = current.replace(' ', '')
        current = current.replace(':', '')
        current = current.replace('-', '')
        if int(end) <= int(current):
            post.delete()


    hana = Post.objects.filter(category="hana")
    science = Post.objects.filter(category="science")
    center = Post.objects.filter(category="center")
    square = Post.objects.filter(category="square")
    one = Post.objects.filter(category="one")
    cafe = Post.objects.filter(category="cafe")
    home = Post.objects.filter(category="home")
    etc = Post.objects.filter(category="etc")
    
    category = {
        'hana': hana,
        'science': science,
        'square': square,
        'center': center,
        'one': one,
        'cafe':cafe,
        'home': home,
        'etc':etc,
    }

    return render(request, 'home.html', {
        'posts': posts,
        'categorys': category,
        })



def new(request):
    if request.method == 'POST':
        
        start_time = datetime.datetime.now().replace(microsecond=0)
        date = request.POST['date']
        date = int(date)
        end_time = start_time + datetime.timedelta(hours=1)

    
        Post.objects.create(
            title = request.POST['title'],
            category = request.POST['category'],
            content = request.POST['content'],
            date = date,
            time_start = start_time,
            time_end = end_time,
            active = request.POST['with'],
        )
        return redirect('home')
    return render(request, 'new.html')


# def detail(request, post_pk):
#     post = Post.objects.get(pk=post_pk)
    
#     return render(request, 'detail.html', {'post': post})


def change(request, post_pk):
    post = Post.objects.get(pk=post_pk)

  

    if request.method == 'POST':
        start_time = datetime.datetime.now().replace(microsecond=0)
        date = request.POST['date']
        date = int(date)
        end_time = start_time + datetime.timedelta(hours=date)
        Post.objects.filter(pk=post_pk).update(
            title = request.POST['title'],
            category = request.POST['category'],
            content = request.POST['content'],
            date = date,
            time_start = start_time,
            time_end = end_time,
            active = request.POST['with'],
        )
        return redirect('home')
    
    return render(request, 'change.html', {'post': post})


# def delete(request, post_pk):
#     post = Post.objects.get(pk=post_pk)
#     post.delete()

#     return redirect('home')





@csrf_exempt
def give(request):
    if request.method == 'POST':
    
        post_pk = request.POST.get('tarData')  
        post = Post.objects.all()

        name = Post.objects.get(pk=post_pk)
        content = name.content
        
        end = name.time_end
        
        current = datetime.datetime.now().replace(microsecond=0)
        format_date = current.strftime("%Y-%m-%d %H:%M:%S")
    

        end = end.replace(' ', '')
        end = end.replace(':', '')
        end = end.replace('-', '')
        format_date = format_date.replace(' ', '')
        format_date = format_date.replace(':', '')
        format_date = format_date.replace('-', '')

        end_hour = end[-6:-4]
        for_hour = format_date[-6:-4]
        
        end_min = end[-4:-2]
        for_min = format_date[-4:-2]

        end_sec = end[-4:-2]
        for_sec = format_date[-4:-2]

        hour = int(end[-6:-4]) - int(format_date[-6:-4])
        hour = int(end[-6:-4]) - int(format_date[-6:-4])
        if int(end[6:8]) > int(format_date[6:8]):
            hour += 24
        min = int(end[-4:-2]) - int(format_date[-4:-2])
        if min < 0:
            hour -= 1
            min += 60

        sec = int(end[-2:]) - int(format_date[-2:])
        if sec < 0:
            min -= 1
            sec += 60
        result = str(hour).zfill(2)+str(min).zfill(2)+str(sec).zfill(2)
    
         
        context = {
            'point': 'point',
            'post_pk': post_pk,
            'name':str(name),
            'content':str(content),
            'time': result,
        }
        return JsonResponse(context)
    return render(request, 'home.html')
    


    # def detail(request, post_pk):
    # post = Post.objects.get(pk=post_pk)
    
    # return render(request, 'detail.html', {'post': post})


@csrf_exempt
def delete(request):
    if request.method == 'POST':
        post_pk = request.POST.get('tarData')  
        post = Post.objects.get(pk=post_pk)
        post.delete()
        return redirect('home')
    return redirect('home')


@csrf_exempt
def edit(request):
    if request.method == 'POST':
        post_pk = request.POST.get('tarData')
        start_time = datetime.datetime.now().replace(microsecond=0)
        end_time = start_time + datetime.timedelta(hours=4)

        name = Post.objects.get(pk=post_pk)
        end = name.time_end

        cha = str(int(end[-8:-6]) + 4)
        temp = list(end)
        temp[-8] = cha[0]
        temp[-7] = cha[1]
        stra = ''.join(temp)

        Post.objects.filter(pk=post_pk).update(
            time_start = start_time,
            time_end = stra,
        )
        return redirect('home')
    
    return render(request, 'home.html')
