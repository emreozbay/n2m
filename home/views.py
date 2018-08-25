from django.shortcuts import render,HttpResponse


def home_view(request):
    if request.user.is_authenticated:
        context = {
            'isim':'Emre',
        }
    else:
        context ={
            'isim':'Misafir'
        }


    return render(request,'home.html',context)
