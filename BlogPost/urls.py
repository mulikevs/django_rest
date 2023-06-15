from django.urls import path
from BlogPost import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('blog/', views.blogApiGet),
     path('addblog/', views.blogApiPost),
    path('blog/<slug:slug>/', views.blogDetailApi),
    path('blog/<int:id>/like/', views.blogLikeApi),
    path('blogs/<slug:slug>/comments/', views.add_comment),
    path('blogs/<slug:slug>/comment/', views.get_comments),
    path('savefile/', views.SaveFile),
     path('getuser/', views.UsersAPIView),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
