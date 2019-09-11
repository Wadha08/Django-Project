from django.shortcuts import render
from rest_framework.generics import ListAPIView, DestroyAPIView, RetrieveUpdateAPIView, RetrieveAPIView,CreateAPIView
from datetime import datetime
from events.models import Event,Booking
from .serializers import (EventListSerializer, BookingListSerializer,RegisterSerializer, BookEventSerializer,
	CreateEventSerializer, EventDetailSerializer)
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner
from django.contrib import messages



class EventList(ListAPIView):
	queryset = Event.objects.filter(date__gte=datetime.today())
	serializer_class = EventListSerializer


class OrgList(ListAPIView):
	queryset = Event.objects.all()
	serializer_class = EventListSerializer
	
	def get_queryset(self):
		return Event.objects.filter(owner__id= self.kwargs['owner_id'])


class BookingList(ListAPIView):
	serializer_class = BookingListSerializer
	permission_classes = [IsAuthenticated]

	def get_queryset(self):
		return self.request.user.attended.all()


class Register(CreateAPIView):
	serializer_class = RegisterSerializer

class CreateEvent(CreateAPIView):
	serializer_class = CreateEventSerializer
	permission_classes = [IsAuthenticated]
	
	def perform_create(self,serializer):
		serializer.save(owner=self.request.user)


class UpdateEvent(RetrieveUpdateAPIView):
	queryset = Event.objects.all()
	serializer_class = CreateEventSerializer
	permission_classes = [IsAuthenticated,IsOwner]
	lookup_field = 'id'
	lookup_url_kwarg = 'event_id'



class EventDetails(ListAPIView):
	serializer_class = EventDetailSerializer
	permission_classes = [IsAuthenticated, IsOwner]

	def get_queryset(self):
		return Booking.objects.filter(event__id=self.kwargs['event_id'])



class BookEvent(CreateAPIView):
	queryset = Event.objects.all()
	serializer_class = BookEventSerializer
	permission_classes = [IsAuthenticated]
	lookup_url_kwarg = 'event_id'


	def perform_create(self,serializer):
		valid_data = serializer.validated_data

		if valid_data['num_seats'] <= self.get_object().get_seats_left():
			return serializer.save(user=self.request.user, event_id=self.kwargs['event_id'])
		else:
			return messages.warning(self.request, "You are excedding the limits!.")

