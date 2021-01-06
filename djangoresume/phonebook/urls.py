from django.urls import path 
#from . import views 
from .views import HomeView , PhonebookDetailView , AddPostView , UpdatePostView , DeletePostView

urlpatterns = [
    #path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home') ,
    path('phonebook_number/<int:pk>', PhonebookDetailView.as_view(), name='phonebook-detail') ,
    path('add_post/', AddPostView.as_view(), name='add_post') ,
    path('phonebook_number/edit/<int:pk>', UpdatePostView.as_view(), name='update_post') ,
    path('phonebook_number/<int:pk>/delete', DeletePostView.as_view(), name='delete_post') ,
]