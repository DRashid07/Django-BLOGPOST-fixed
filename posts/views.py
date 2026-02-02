from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q 
from .models import Category, Post, Author, About, Comment, Tag, Book

def get_author(user):
    qs = Author.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None

def homepage (request):
    categories = Category.objects.all()[0:3]
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-timestamp')[0:3]
    context= {
        'object_list': featured,
        'latest': latest,
        'categories':categories,
    }
    return render(request, 'homepage.html',context)

def post (request,slug):
    post = Post.objects.get(slug = slug)
    post.view_count+=1
    post.save()
    comments=post.comments.all()
    latest = Post.objects.order_by('-timestamp')[:3]
    context = {
        'post': post,
        'latest': latest,
        'comments':comments
    }
    return render(request, 'post.html', context)

def about (request):
    about= About.objects.first()
    context={
        'about':about,
        }
    return render(request, 'about_page.html',{'about':about})

def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()

        
    context = {
        'object_list': queryset
        
    }
    return render(request, 'search_bar.html', context)


def postlist (request,slug):
    category = Category.objects.get(slug = slug)
    posts = Post.objects.filter(categories__in=[category])

    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'post_list.html', context)

def allposts(request):
    posts = Post.objects.order_by('-timestamp')

    context = {
        'posts': posts,
    }
    return render(request, 'all_posts.html', context)

def like_post(request,slug):
    post=get_object_or_404(Post,slug=slug)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect("post",slug=slug)

def favourite_post(request,slug):
    post=get_object_or_404(Post,slug=slug)
    if request.user in post.favourites.all():
        post.favourites.remove(request.user)
    else:
        post.favourites.add(request.user)
    return redirect ("post", slug=slug)

def post_comment(request,slug):
    post=get_object_or_404(Post,slug=slug)
    if request.method == 'POST' and request.user.is_authenticated:
        Comment.objects.create(
        post=post, user=request.user, text=request.POST.get('comment')
        )
    return redirect ('post',slug=slug)

def tags_list(request):
    tags= Tag.objects.all().order_by('name')
    posts=Post.objects.all().order_by('-timestamp')
    context={
        'tags':tags,
        'posts':posts,
        }
    return render(request,'tags_posts.html',context)

def posts_by_tag(request, tag_id):
    
    tag= Tag.objects.get(id=tag_id)
    posts= Post.objects.filter(tags=tag).order_by('-timestamp')
    context={
        'posts':posts,
        'tag':tag,
    }
    return render(request,'tag_posts.html', context)

def report_post(request,slug):
    post=get_object_or_404(Post,slug=slug)
    if request.user in post.reports.all():
        post.reports.remove(request.user)
    else:
        post.reports.add(request.user)
    return redirect("post",slug=slug)

def books(request):
    books=Book.objects.all()
    return render(request, 'book.html',{'books': books})