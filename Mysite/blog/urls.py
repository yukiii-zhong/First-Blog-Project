from django.urls import include, path
from . import views

urlpatterns = [
    path('about/',views.AboutView.as_view(),name='about'),
    path('',views.PostListView.as_view(),name='post_list'),
    path('<int:pk>/',views.PostDetailView.as_view(),name='post_detail'),
    path('new/',views.CreatePostView.as_view, name='post_new'),
    path('<int:pk>/edit/',views.PostUpdateView.as_view(),name = 'post_edit'),
    path('<int:pk>/remove/',views.PostDeleteView.as_view(),name='post_remove'),
    path('drafts/',views.DraftListView.as_view(),name = 'post_draft_list'),
]
