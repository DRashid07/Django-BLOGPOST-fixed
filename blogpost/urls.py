from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from posts.views import homepage, post, about, search, postlist, allposts, like_post, favourite_post, post_comment, tags_list, posts_by_tag, report_post,books

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name = 'homepage'),
    path('post/<slug>/', post, name = 'post'),
    path('about/', about,name = 'about' ),
    path('search/', search, name = 'search'),
    path('postlist/<slug>/', postlist, name = 'postlist'), 
    path('posts/', allposts, name = 'allposts'),
    path('post/like/<slug:slug>/',like_post, name='like_post'),
    path('post/favourite/<slug:slug>/', favourite_post, name='add_favourite'),
    path('post/comment/<slug:slug>/',post_comment, name='post_comment'),
    path('tags/',tags_list,name='tags_list'),
    path('tag/<int:tag_id>/', posts_by_tag,name='posts_by_tag'),
    path('post/report/<slug:slug>/',report_post, name='report_post'),
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
    path('books/', books, name = 'books'),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
