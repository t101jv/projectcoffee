import datetime

from django.db import models
from django.utils import timezone
import json

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date > timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Company(models.Model):
    PUBLIC_TRANSIT_COMPANY = 'public_transit_company'
    CHARTER = 'charter'
    AIRPORTER = 'airporter'
    PUBLIC_FERRY = 'public_ferry'
    PRIVATE_FERRY = 'private_ferry'
    COACH_BUS = 'coach_bus'
    PARTY_BUS = 'party_bus'
    HOP_ON_HOP_OFF = 'hop_on_hop_off'
    RIDESHARE = 'rideshare'
    CARPOOL = 'carpool'
    SCOOTER = 'scooter'
    RENTAL_CAR = 'rental_car'
    BIKE_SHARE = 'bike_share'

    TRANSIT_TYPES = (
        (PUBLIC_TRANSIT_COMPANY, 'Public Transit Company'),
        (CHARTER, 'Charter'),
        (AIRPORTER, 'Airporter'),
        (PUBLIC_FERRY, 'Public Ferry'),
        (PRIVATE_FERRY, 'Private Ferry'),
        (COACH_BUS, 'Coach Bus'),
        (PARTY_BUS, 'Party Bus'),
        (HOP_ON_HOP_OFF, 'Hop On Hop Off'),
        (RIDESHARE, 'Rideshare'),
        (CARPOOL, 'Carpool'),
        (SCOOTER, 'Scooter'),
        (RENTAL_CAR, 'Rental Car'),
        (BIKE_SHARE, 'Bike Share'),
    )

    PUBLIC = 'public'
    PRIVATE = 'private'

    COMPANY_TYPES = (
        (PUBLIC, 'Public'),
        (PRIVATE, 'Private')
    )

    name = models.CharField(max_length=200)
    transit_type = models.CharField(max_length=200, choices=TRANSIT_TYPES)
    headquarters_location = models.CharField(max_length=200)
    company_type = models.CharField(max_length=200, choices=COMPANY_TYPES)
    area_served = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    logo = models.ImageField()

class Route(models.Model):
    PASSENGER_TRAIN = 'passenger_train'
    LIGHT_RAIL = 'light_rail'
    BUS = 'bus'
    FERRY = 'ferry'
    GONDOLA = 'gondola'
    STREETCAR = 'streetcar'
    RIDESHARE = 'rideshare'
    BIKE = 'bike'
    SCOOTER = 'scooter'
    CARPOOL = 'carpool'
    AIRPORTER = 'airporter'
    MODE = (
        (PASSENGER_TRAIN, 'Passenger Train'),
        (LIGHT_RAIL, 'Light Rail'),
        (BUS, 'Bus'),
        (FERRY, 'Ferry'),
        (GONDOLA, 'Gondola'),
        (STREETCAR, 'Streetcar'),
        (RIDESHARE, 'Rideshare'),
        (BIKE, 'Bike'),
        (SCOOTER, 'Scooter'),
        (CARPOOL, 'Carpool'),
        (AIRPORTER, 'Airporter'),
    )

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    mode = models.CharField(max_length=200, choices=MODE)
    start_address = models.CharField(max_length=200)
    end_address = models.CharField(max_length=200)
    amenities = models.CharField(max_length=200)


    def set_amenities(self, amenities):
        self.amenities = json.dumps(amenities)

    def get_amenities(self):
        return json.loads(self.amenities)

