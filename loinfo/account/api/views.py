from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from account.api.serializers import RegistrationSerializer
from account.models import Account

@api_view(['POST', ])
def registration_view(request):

	if request.method == 'POST':
		serializer = RegistrationSerializer(data=request.data)
		data = {}
		if serializer.is_valid():
            
			account = serializer.save()
			data['response'] = 'successfully new user created'
			data['email'] = account.email
			data['username'] = account.username
			data['name'] = account.name

		else:
			data = serializer.errors
		return Response(data)

