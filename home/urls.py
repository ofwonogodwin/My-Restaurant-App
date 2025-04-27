from django.urls import path
from.import views

# these are the Url Patterns
urlpatterns = [
    path('',views.home, name = 'homepage'),
    path('about/',views.about, name = 'aboutpage'),
    path('contact/',views.contact, name = 'contactpage'),
]
