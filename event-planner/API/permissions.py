from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
	message = "You must be the owner of this Event"

	def has_object_permission(self, request, view, obj):
		if obj.owner == request.user:
			return True
		else:
			return False
