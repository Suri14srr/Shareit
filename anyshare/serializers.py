from rest_framework import serializers

class InviteSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    message = serializers.CharField(max_length=255, required=False)
    name = serializers.CharField(required=False)

    def validate_email(self, value):
        if not value.endswith("@example.com"):
            raise serializers.ValidationError("Email domain must be '@example.com'.")
        return value



    
