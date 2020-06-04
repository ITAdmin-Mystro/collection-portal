
from django.urls import path,include
from django.conf.urls import url
from . import views
from .views import add_rm, edit_details, send_SMS

urlpatterns = [
    path('',views.homepage,name='blog-homepage'),
    path('add/',views.add_rm,name='add-rm'),
    path('edit/<int:pk>/', views.edit_details, name='edit-details'),
#    path('customers/<str:risk_manager__firstname>/', views.customer_list, name="customer-list"),
    path('send_SMS/', views.send_SMS, name='send-SMS'),
    #path('send_SMS/', send_SMS.as_view(), name='send-SMS'),
    path('get_list/', views.get_list, name='get-list'),
 ]