from django.urls import path
from . import views
urlpatterns = [
    path('userlogin/',views.userLogin),
    path('userlogout/',views.userLogout),
    path('searching/',views.search),
    path('search/',views.searchBook),
    path('delete/',views.deleteBook),
    path('edit/',views.editBook),
    path('update/',views.edit),
    path('view/',views.viewBooks),
    path('insert/', views.insertBook ),
    path('save/',views.insert),

]
