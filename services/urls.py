from django.urls import path
from . import views
urlpatterns=[
    path('electrician',views.electrician,name='electrician'),
    path('plumber',views.plumber,name='plumber'),
    path('cleaner',views.cleaner,name='cleaner'),
    path('booking',views.booking,name='booking'),
    path('cancelBooking',views.cancelBooking,name='cancelBooking'),
]