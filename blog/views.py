from django.shortcuts import render,get_object_or_404
from .models import Blog
import operator
def allblog(request):
    blogs=Blog.objects
    #blogs=sorted(blogs.items(), key=operator.itemgetter(1), reverse=True)
    return render(request,'blog/allblog.html',{'blogs':blogs})

def detail(request,blog_id):
    detailblog=get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':detailblog})
