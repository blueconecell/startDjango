from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from users.serializer import TinyUserSerializer
from categories.serializers import CategorySerializer
from reviews.serializers import ReviewSerializer

from .models import Room, Amenity

class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = ("name","description",)


class RoomDetailSerializer(ModelSerializer):
    owner = TinyUserSerializer(read_only=True)
    amenities = AmenitySerializer(many=True,read_only=True)
    category = CategorySerializer(read_only=True)

    rating = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField()
    # reviews = ReviewSerializer(many=True, read_only=True)

    def get_rating(self, room):
        return room.rating()
    def get_is_owner(self,room):
        request = self.context["request"]
        return room.owner == request.user

    class Meta:
        model = Room
        fields = "__all__"




class RoomListSerializer(ModelSerializer):
    rating = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField()
    def get_rating(self, room):
        return room.rating()
    def get_is_owner(self,room):
        request = self.context["request"]
        return room.owner == request.user
    class Meta:
        model = Room
        fields = ("pk","name","country","city","price","rating","is_owner",)