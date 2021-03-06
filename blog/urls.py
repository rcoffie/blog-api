from django.urls import path  
from .import views 
from .feeds import LatestPostFeed
# from . views import PostListView


app_name = 'blog'


urlpatterns = [
  #post views  
  path('',views.post_list, name="post_list"),
  # path('',views.PostListView.as_view(), name="post_list"),
  path('detailt',views.detailt, name="detailt"),
  path('tag/<slug:tag_slug>', views.post_list,name='post_list_by_tag'),
  path('search/', views.post_search,name="post_search"),
  path('<int:year>/<int:month>/<int:day>/<slug:post>/',views.post_detail,name="post_detail"),
  path('<int:year>/<int:month>/<int:day>/<slug:post>/',views.post_detail,name="post_detail2"),
  path('<int:post_id>/share/', views.post_share,name="post_share"),
  path('feed/', LatestPostFeed(), name="post_feed"),


  ##
  path('list2',views.post_list2,name="post_list2"),
]