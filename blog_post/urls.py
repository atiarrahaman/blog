from django.urls import path 
from . import views

urlpatterns = [
    path('',views.Blog_Post , name='post'),
    path('post-details/<int:id>',views.Post_details , name='post_details'),
    path('add-post',views.Add_Post , name='add_post'),
    path('login',views.Login , name='login'),
    path('logout',views.Logut , name='logout'),
    path('signup-user',views.SignupUser , name='signup'),
    path('profile',views.Profile , name='profile'),
    path('change-password-with-old-password',views.Cahnge_passwords , name='cng_pass_with_old_pass'),
    path('change-password-with-out-old-password',views.Cahnge_passwords_without_old_pass , name='cng_pass_with_out_old_pass'),

    path('catagory-filter/<slug:catagory_slug>',views.Blog_Post ,name='catagory_filter'),
 
   

]
