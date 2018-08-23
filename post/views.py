from django.shortcuts import render,HttpResponse, get_list_or_404, HttpResponseRedirect, redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages

def post_index(request):
    posts = Post.objects.all() #veri tabanından getirdiğimiz değerler.
    return render(request,'post/index.html',{'posts':posts})


def post_detail(request,id):
    post = get_list_or_404(Post,id=id)
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
        form = PostForm(request.POST, request.FILES or None)
        if form.is_valid():
            post = form.save()
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

    post = get_list_or_404(Post, id=id)
    if request.method == "POST":
        # formdan gelen bilgileri kaydet
        form = PostForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(post.get_absolute_url())
    form =PostForm()
    context = {
             'form': form,
        }

    return render(request, 'post/form.html', context)

def post_delete(request, id):
    post = get_list_or_404(Post, id=id)
    post.delete()
    return redirect('post:index')
