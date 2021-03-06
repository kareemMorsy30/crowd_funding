from django.urls import path
from .views import index,launch_project,reply,show,comment,rate,admin_reported_projects

urlpatterns = [
    path('<int:project_id>', show ,name="project_show_url"),
    path('launch',launch_project,name="launch"),
    path('index', index,name="index"),
    path('<int:project_id>/rate', rate,name="rate"),
    path('comment', comment,name="comment_url"),
    path('reply', reply,name="reply_url"),
    # path('reported_project/<int:project_id>',admin_delete_reported_projects,name="delete_reported_projects"),

]


