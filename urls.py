from django.urls import path
from . import views
urlpatterns = [ 
    path('edit_user/', views.edit_user, name='edit_user'),
    path('edit_user_data/', views.edit_user_data, name='edit_user_data'),
    path('delete_user/', views.delete_user, name='delete_user'),
]
