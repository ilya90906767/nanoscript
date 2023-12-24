from rest_framework import serializers 
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            email = validated_data['email'],
            password = validated_data['password'],
            full_name = validated_data.get('full_name', ''),
            
        )
        return user
    
    class Meta:
        model = get_user_model()
        fields = ['email','password','full_name']
        extra_kwargs = {'password':{'write_only':True}}
        
class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    id = serializers.CharField(max_length=255, read_only = True)
    password = serializers.CharField(max_length=255, write_only = True)
    
    def validate(self, data): 
        email = data.get("email",None)
        password = data.get("password", None)
        
        if email is None: 
            raise serializers.ValidationError("Введите email для входа")
        if password is None: 
            raise serializers.ValidationError("Введите пароль для входа") 
        
        user = authenticate(username=email, password=password)
        
        if user is None: 
            raise serializers.ValidationError(
                "Вы ввели неверный email или пароль"
            )
        if not user.is_active:
            raise serializers.ValidationError(
                "Пользователь неактивен"
            )
        return {
            "email": user.email,
            "id" : user.id
        }
        
    class Meta:
        model = get_user_model()
        fields = ['email','password','id']