from rest_framework import serializers
import re

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id", "name", "phone", "message", "brand", "model", "year"]

    def validate_phone(self, value):
        """
        Check that phone number in post
        """
        if not value:
            raise serializers.ValidationError("Phone number is required")

        phone_re = re.compile('^((\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?)?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$')

        if not phone_re.match(value):
            raise serializers.ValidationError("Number is not valid")

        return value