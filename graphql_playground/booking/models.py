from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Room(models.Model):
    ROOM_TYPES = (
        ('SGL', 'Single'),
        ('DBL', 'Double'),
        ('TPL', 'Triple'),
        ('QD', 'Quad'),
        ('QN', 'Queen'),
        ('KG', 'King'),
        ('TWN', 'Twin'),
        ('ST', 'Studio'),
    )
    number = models.CharField(max_length=10, unique=True)
    room_type = models.CharField(max_length=3, choices=ROOM_TYPES)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.number} - {self.get_room_type_display()}"

class Booking(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f"{self.client} - Room: {self.room.number}"

class Review(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.PositiveIntegerField()

    def __str__(self):
        return f"Review by {self.client} for Room {self.room.number}"
