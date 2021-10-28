from django.db import models
import string
import random


def generate_unique_code():
    '''
    Input: None
    Output: code, string of size defined by length that is unique
            in the set of Room models
    '''
    length = 10
    while True:
        # Creates a code with length k using only upper case ascii letters
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        # Calculates the number of Room models that contain the generated code
        if Room.objects.filter(code=code).count == 0:
            break

        return code


class Room(models.Model):
    code = models.CharField(max_length=8, default="", unique=True)
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
