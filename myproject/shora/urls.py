from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'app1'
urlpatterns = [

                  path('pannel/council/<int:user_id>/', views.council, name='council'),
                  path('pannel/Assembly/<int:user_id>/', views.Assembly, name='assembly'),
                  path('pannel/council/success/', views.upload_document_success, name='upload_document_success')

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
