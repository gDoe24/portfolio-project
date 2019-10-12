from django.shortcuts import render,get_object_or_404,redirect

from .models import Blog

from .forms import CommentForm
# Create your views here.
def allblogs(request):
	blogs = Blog.objects
	return render(request, 'blog/allblogs.html', {'blogs':blogs})

def detail(request, blog_id):

	detail_blog = get_object_or_404(Blog, pk=blog_id)
	return render(request, 'blog/detail.html', {'blog':detail_blog})

def add_comment(request, pk):
	post= get_object_or_404(Blog, pk=pk)

	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post=post
			comment.save()
			response = detail(request, pk)
			return response
		else:
			form=CommentForm()
	return render(request, 'blog/add_comment.html', {'form':CommentForm})