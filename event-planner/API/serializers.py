from rest_framework import serializers
from events.models import Booking, Event
from django.contrib.auth.models import User


class EventListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Event
		fields = ['title', ]

class BookingListSerializer(serializers.ModelSerializer):
	event = EventListSerializer()
	class Meta:
		model = Booking
		fields = ['event', 'num_seats', ]

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        new_user = User(username=username, first_name=first_name, last_name=last_name)
        new_user.set_password(password)
        new_user.save()
        return validated_data


class CreateEventSerializer(serializers.ModelSerializer):
	class Meta:
		model = Event
		exclude = ['owner']


class Userinfo(serializers.ModelSerializer):
	# user = serializers.SlugRelatedField(
	# 	slug_field= 'username',
	# 	read_only=True,	
	# 	)
	class Meta:
		# model = Booking
		model = User
		fields = ['first_name', 'last_name']


class EventDetailSerializer(serializers.ModelSerializer):
	user = Userinfo()
	class Meta:
		model = Booking
		fields = ['user', 'num_seats', ]

class BookEventSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['num_seats', ]








