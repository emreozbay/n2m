from django.shortcuts import render,HttpResponse, get_list_or_404, HttpResponseRedirect, redirect, Http404,get_object_or_404
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.http import JsonResponse

def post_index(request):
    posts = Post.objects.all() #veri tabanından getirdiğimiz değerler.
    return render(request,'post/index.html',{'posts':posts})


def post_detail(request,id):
    post = get_object_or_404(Post, id=id)


        # formdan gelen bilgileri kaydet

    context = {
        'post': post,

    }
    return render(request, 'post/detail.html', context)


def post_create(request):
    form =PostForm()
    context = {
        'form': form,
    }

    #if request.method == "POST":
    #   print(request.POST)

    if request.method == "POST":
        # formdan gelen bilgileri kaydet
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            post.user = request.user
            messages.success(request, 'Başarılı bir şekilde oluşturdunuz....', extra_tags='mesaj-basarili')
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        #formu kullanıcıya göster
        form = PostForm()
        context = {
             'form' :form,
        }

    #form = PostForm(request.POST or None)
    #if form.is_valid():
    #   form.save()
    #context = {
    #         'form' :form,
   #     }
    return render(request, 'post/form.html', context)


def post_update(request, id):

    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        messages.success(request, "Başarılı bir şekilde güncellediniz.")
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
             'form': form
        }

    return render(request, 'post/form.html', context)

def post_delete(request, id=None):

    post = get_object_or_404(Post, id=id)
    if request.method=='POST':
        post.delete()
        return JsonResponse(data={'success':'silindi'})










