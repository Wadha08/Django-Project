from django.urls import path

from events import views

app_name = 'events'

urlpatterns = [

	path('home/', views.home, name='home'),

	path('create/', views.create_event, name='create'),
	path('list/', views.event_list, name='list'),
	path('detail/<int:event_id>/', views.event_detail, name='detail'),
	path('edit/<int:event_id>/', views.event_edit, name='edit'),
	path('booking/<int:event_id>/', views.booking, name='booking'),
	path('cancel/<int:booking_id>/', views.cancel_booking, name='cancel'),

	path('dashboard/', views.dashboard, name='dashboard'),

    path('signup/', views.Signup.as_view(), name='signup'),
    path('login/', views.Login.as_view(), name= 'login'),
    path('logout/', views.Logout.as_view(), name='logout'),

]