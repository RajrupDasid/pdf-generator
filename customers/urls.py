from django.urls import path
from .views import render_pdf_view
app_name='customers'
urlpatterns=[
    path('',render_pdf_view,name='test-view'),
]