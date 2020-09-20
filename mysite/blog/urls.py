from django.urls import path
from blog import views


urlpatterns = [
    path('home/',views.PostListView.as_view,name='post_list'),
    path('about/',views.AboutView.as_view,name='about'),
    path('post/<int:pk>',views.PostDetailView.as_view,name='post_detail'),
    path('post/new/',views.CreatePostView.as_view,name='post_create'),
    path('post/<int:pk>/edit/',views.PostUpdateView.as_view,name='post_edit'),
    path('post/<int:pk>/delete/',views.PostDetailView.as_view,name='post_delete'),
    path('post/drafts/',views.DraftListView,name='post_draft_list'),
]
