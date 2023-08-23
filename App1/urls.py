from django.urls import path
from . import views
urlpatterns=[
    path("login/",views.login,name='login'),
    path("signup/",views.signup,name='signup'),
    path("content/",views.content,name='content'),
    path("crowd/",views.crowd,name='crowd'),
    path("graphic/",views.graphic,name='graphic'),
    path("Home/",views.Home,name='Home'),
    path("post/",views.post,name='post'),
    path("thankyou/",views.thankyou,name='thankyou'),
    path("translate/",views.translate,name='translate'),
    path("work/",views.work,name='work'),
    path("write/",views.write,name='write'),
]