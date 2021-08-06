from django.urls import path
from .views import render_pdf_view,CustomerListView,crpv
app_name='customers'
urlpatterns=[
    path('',CustomerListView.as_view(),name='customer-listview'),
    path('test/',render_pdf_view,name='test-view'),
    path('pdf/<pk>/',crpv,name='cprv'),
]