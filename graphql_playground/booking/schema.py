from graphene_django import DjangoObjectType
from .models import Client, Room, Booking, Review
import graphene

class ClientType(DjangoObjectType):
    class Meta:
        model = Client
        fields = "__all__"

class RoomType(DjangoObjectType):
    class Meta:
        model = Room
        fields = "__all__"

class BookingType(DjangoObjectType):
    class Meta:
        model = Booking
        fields = "__all__"

class ReviewType(DjangoObjectType):
    class Meta:
        model = Review
        fields = "__all__"


import graphene

class Query(graphene.ObjectType):
    all_clients = graphene.List(ClientType)
    all_rooms = graphene.List(RoomType)
    all_bookings = graphene.List(BookingType)
    all_reviews = graphene.List(ReviewType)

    def resolve_all_clients(root, info):
        return Client.objects.all()

    def resolve_all_rooms(root, info):
        return Room.objects.all()

    def resolve_all_bookings(root, info):
        return Booking.objects.all()

    def resolve_all_reviews(root, info):
        return Review.objects.all()



class ClientInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    email = graphene.String(required=True)
    phone = graphene.String(required=True)

class CreateClient(graphene.Mutation):
    class Arguments:
        input = ClientInput(required=True)

    client = graphene.Field(ClientType)

    @staticmethod
    def mutate(root, info, input):
        client = Client(
            name=input.name,
            email=input.email,
            phone=input.phone
        )
        client.save()
        return CreateClient(client=client)


class RoomInput(graphene.InputObjectType):
    number = graphene.String(required=True)
    room_type = graphene.String(required=True)
    price = graphene.Float(required=True)
    available = graphene.Boolean(required=True)

class CreateRoom(graphene.Mutation):
    class Arguments:
        input = RoomInput(required=True)

    room = graphene.Field(RoomType)

    @staticmethod
    def mutate(root, info, input):
        room = Room(
            number=input.number,
            room_type=input.room_type,
            price=input.price,
            available=input.available
        )
        room.save()
        return CreateRoom(room=room)
class Mutation(graphene.ObjectType):
    create_client = CreateClient.Field()
    create_room = CreateRoom.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
# schema = graphene.Schema(query=Query)
