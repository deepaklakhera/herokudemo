from django.urls import path
from . views import postList,postDetail,postCreate,postUpdate,postDelete
urlpatterns=[
    path('',postList,name="postList"),
    path('<int:pk>',postDetail,name="postDetail"),
    path('create',postCreate,name="postCreate"),
    path('update/<int:pk>',postUpdate,name="postUpdate"),
    path('delete/<int:pk>',postDelete,name="postDelete"),
]