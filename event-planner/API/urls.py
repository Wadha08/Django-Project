
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView

from API import views 

app_name = 'API'

urlpatterns = [
 
    path('list/', views.EventList.as_view(), name='API_list'), 
    path('org_list/<int:owner_id>/', views.OrgList.as_view(), name='API_org_list'),
    path('booking/list/', views.BookingList.as_view(), name='API_booking_list'),
    path('create/', views.CreateEvent.as_view(), name='API_create'),
    path('update/<int:event_id>/', views.UpdateEvent.as_view(), name='API_update'),
    path('detail/<int:event_id>/', views.EventDetails.as_view(), name='API_detail'),
    path('book/<int:event_id>/', views.BookEvent.as_view(), name='API_book'),

    path('register/', views.Register.as_view(), name="register"),
    path('login/', TokenObtainPairView.as_view(), name='login'),

]