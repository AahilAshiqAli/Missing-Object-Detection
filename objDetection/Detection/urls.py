from django.urls import path
from django.contrib import admin
from Detection import views

admin.site.site_header = "Elite Estate Royce | Admin"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Hello"

urlpatterns = [
    path("", views.index, name="index"),
    path('contact',views.contact,name='contact'),
    path('login',views.loginUser,name = 'login'),
    path('logout',views.logoutUser,name = 'logout'),
    path('dashboard',views.user_dashboard,name = "dashboard"),
    path('details/<str:name>/',views.details,name = "details")
]