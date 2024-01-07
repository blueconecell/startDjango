from django.urls import path
from . import views

urlpatterns = [
    path('',views.Users.as_view()),
    path('@<str:username>',views.PublicUser.as_view()),
    path('@<str:username>/reviews',views.PublicUserReviews.as_view()),
    path('@<str:username>/rooms',views.PublicUserRooms.as_view()),
    path('change-password',views.ChangePassword.as_view()),
    path('me',views.Me.as_view()),
    
    
    
    
]
