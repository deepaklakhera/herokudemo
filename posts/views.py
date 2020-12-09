from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from .forms import PostModelForm
from django.http import HttpResponseRedirect
# Create your views here.

def postDelete(request,pk):
    post=Post.objects.get(pk=pk)
    if request.method=='POST':
        print('post',post)
        post.delete()   
        return redirect('postList')
    return render(request,'posts/postdelete.html',{"post":post})


def postUpdate(request,pk):
    post=Post.objects.get(pk=pk)
    my_form=PostModelForm(instance=post)
    
    if request.method=='POST':
        my_form=PostModelForm(request.POST,request.FILES,instance=post)
        my_form.save()
        return redirect('postList')
    return render(request,'posts/postupdate.html',{"form":my_form})



def postCreate(request):
    print(request)
    my_form=PostModelForm()
    if request.method=='POST':

        my_form=PostModelForm(request.POST,request.FILES)
        my_form.save()
        return redirect('postList')
    return render(request,'posts/postcreate.html',{"form":my_form})



def postList(request):
    object_list=Post.objects.all()
    context={"object_list":object_list}
    return render(request,'posts/postlist.html',context)

def postDetail(request,pk):
    obj=Post.objects.get(pk=pk)
    context={
        "object":obj
    }
    return render(request,'posts/postdetail.html',context)