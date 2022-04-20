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
    hana = Post.objects.filter(category="hana")
    science = Post.objects.filter(category="science")
    center = Post.objects.filter(category="center")
    square = Post.objects.filter(category="squre")
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

    
    """ post = Post.objects.get(pk=2)    
    end = post.time_end
    
    current = datetime.datetime.now().replace(microsecond=0)
    format_date = current.strftime("%Y-%m-%d %H:%M:%S")
    end = end.replace(' ', '')
    end = end.replace(':', '')
    end = end.replace('-', '')
    format_date = format_date.replace(' ', '')
    format_date = format_date.replace(':', '')
    format_date = format_date.replace('-', '')
    result = int(end) - int(format_date)
    print(str(result).zfill(6))
    print(int(end)-int(format_date))

    
    pdb.set_trace() """
    

    return render(request, 'home.html', {
        'posts': posts,
        'categorys': category,
        })



def new(request):

    start_time = datetime.datetime.now().replace(microsecond=0)
    end_time = start_time + datetime.timedelta(hours=4)

    if request.method == 'POST':
        Post.objects.create(
            title = request.POST['title'],
            category = request.POST['category'],
            content = request.POST['content'],
            date = request.POST['date'],
            time_start = start_time,
            time_end = end_time,
        )
        return redirect('home')
    return render(request, 'new.html')


# def detail(request, post_pk):
#     post = Post.objects.get(pk=post_pk)
    
#     return render(request, 'detail.html', {'post': post})


# def edit(request, post_pk):
#     post = Post.objects.get(pk=post_pk)

#     if request.method == 'POST':
#         Post.objects.filter(pk=post_pk).update(
#             title = request.POST['title'],
#             content = request.POST['content'],
#         )
#         return redirect('detail', post_pk)
    
#     return render(request, 'edit.html', {'post': post})


# def delete(request, post_pk):
#     post = Post.objects.get(pk=post_pk)
#     post.delete()

#     return redirect('home')





@csrf_exempt
def give(request):
    if request.method == 'POST':
    
        
        
        # data = json.loads(request.body)
        # print(data)
        # context = {
        #     'post':post,
        # }
        # print(context)
        post_pk = request.POST.get('tarData')  
        # p = get_object_or_404(Post, pk=post_pk)  
        # post = Post.objects.get(pk=post_pk)
        post = Post.objects.all()
        # post = Post.objects.get(pk=post_pk)
        # serialized_qs = serializers.serialize('json', post)

        name = Post.objects.get(pk=post_pk)
        content = name.content
        
  
        end = name.time_end
        
        current = datetime.datetime.now().replace(microsecond=0)
        format_date = current.strftime("%Y-%m-%d %H:%M:%S")
        # format_date = format_date.replaceAll("[^0-9]","*")
        end = end.replace(' ', '')
        end = end.replace(':', '')
        end = end.replace('-', '')
        format_date = format_date.replace(' ', '')
        format_date = format_date.replace(':', '')
        format_date = format_date.replace('-', '')
        hour = int(end[-6:-4]) - int(format_date[-6:-4])
        min = int(end[-4:-2]) - int(format_date[-4:-2])
        if min < 0:
            hour -= 1
            min += 60

        sec = int(end[-4:-2]) - int(format_date[-4:-2])
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
    
    # return JsonResponse("aa")


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
