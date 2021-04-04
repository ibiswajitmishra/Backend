from rest_framework import serializers

from account.models import Account


class RegistrationSerializer(serializers.ModelSerializer):
    
	password2 		   = serializers.CharField(style={'input_type': 'password'}, write_only=True)
	name 		   = serializers.CharField(max_length=30,default='nan')
	class Meta:
		model = Account
		fields = ['name','email','username', 'password', 'password2']
		extra_kwargs = {
				'password': {'write_only': True},
		}	


	def	save(self):

            account = Account(
                        email=self.validated_data['email'],
                        username=self.validated_data['username']
                        )
            
            password = self.validated_data['password']
            password2 = self.validated_data['password2']
            name = self.validated_data['name']
            account.name = name
            account.username = str(account.email[:account.email.index('@')]) 

            if account.email.endswith("lpu.in"):
                account.is_collegeverified = True

            if password != password2:
                raise serializers.ValidationError({'password': 'Passwords must match.'})

            account.set_password(password)
            account.save()
            return account