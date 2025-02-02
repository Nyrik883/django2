from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .From import FeedBlogForm

def alist(request):
    model = Blog.objects.all()
    return render(request,'list.html',{'model':model})

def feedblog(request):
    if request.method == 'POST':
        form = FeedBlogForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'form_end.html')
    else:
        form = FeedBlogForm()  # Instantiate an empty form for GET requests

    return render(request, 'form.html', {'form': form})

def deta_blog(request, pk):
    model = get_object_or_404(Blog,pk=pk)
    return render(request,'detail.html',{'model':model})

def edit_blog(request, pk):
    blog = get_object_or_404(Blog,pk=pk)
    if request.method == 'POST':
        form = FeedBlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('list.html')   
    else:
        form = FeedBlogForm(instance=Blog)
    return render(request, 'update.html', {'form':form})

def delete_blog(request, pk):
    blog = get_object_or_404(Blog,pk=pk)
    if request.method == 'POST':
        blog.delete()
        return redirect('alist')
    return render(request , 'delete.html', {'blog':blog})
    