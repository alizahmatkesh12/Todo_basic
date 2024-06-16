from django.shortcuts import render, redirect
from .models import Post
from .forms import PostCreateForm, PostUpdateForm
from django.contrib import messages
def home(request):
    all = Post.objects.all()
    return render(request, "Home.html", {'all': all})

def detail(request, post_id):
    post = Post.objects.get(id = post_id)
    return render(request, 'detail.html', {'post': post})

def delete(request, post_id):
    Post.objects.get(id = post_id).delete()
    messages.success(request, 'Post deleted successfully', 'success')
    return redirect('home')

def create(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Post.objects.create(title=cd['title'], body=cd['body'], date_posted=cd['date_posted'])
            messages.success(request, 'Post created successfully', 'success')
            return redirect('home')
    else:
        form = PostCreateForm()
    return render(request, 'create.html', {'form':form})

def update(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostUpdateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully', 'success')
            return redirect('details', post_id)
    else:

        form = PostUpdateForm(instance=post)
    return render(request, 'update.html', {'form':form})


