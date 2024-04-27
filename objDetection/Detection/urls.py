from django.urls import path
from django.contrib import admin
from Detection import views
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = "Elite Estate Royce | Admin"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Hello"

urlpatterns = [
    path("", views.index, name="index"),
    path('contact',views.contact,name='contact'),
    path('login',views.loginUser,name = 'login'),
    path('logout',views.logoutUser,name = 'logout'),
    path('dashboard',views.user_dashboard,name = "dashboard"),
    path('details/<str:name>/',views.details,name = "details_withname"),
    path('details',views.details,name = "details_withoutname"),
    path('help',views.document,name='help')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)