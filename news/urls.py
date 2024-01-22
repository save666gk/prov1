from django.urls import path
# Импортируем созданное нами представление
from .views import PostList, PostDetail, PostCreate, PostUpdate, PostDelete, authorized_page, become_author_view

urlpatterns = [

   path('', PostList.as_view(),name='post_list'),
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('authorized_page/', authorized_page, name='authorized_page'),
   path('become_author/', become_author_view, name='become_author')
]
