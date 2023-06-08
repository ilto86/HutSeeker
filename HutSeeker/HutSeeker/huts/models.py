from django.db import models
from multiselectfield import MultiSelectField
from enum import Enum
from django.contrib.auth import get_user_model

from django.core import validators
from HutSeeker.utils.model_mixins import ChoicesEnumMixin

UserModel = get_user_model()


class Approach(ChoicesEnumMixin, Enum):
    PEDESTRIAN = "Pedestrian"
    WHEEL = "Wheel"
    CAR = "Car"
    BUS = "Bus"
    LIFT = "Lift"
    CAMPER = "Camper"


class WeatherCondition(ChoicesEnumMixin, Enum):
    SUNNY = "Sunny"
    CLOUDY = "Cloudy"
    RAINY = "Rainy"
    SNOWY = "Snowy"


class Month(ChoicesEnumMixin, Enum):
    JANUARY = "Jan"
    FEBRUARY = "Feb"
    MARCH = "Mar"
    APRIL = "Apr"
    MAY = "May"
    JUNE = "Jun"
    JULY = "Jul"
    AUGUST = "Aug"
    SEPTEMBER = "Sep"
    OCTOBER = "Oct"
    NOVEMBER = "Nov"
    DECEMBER = "Dec"


class Services(ChoicesEnumMixin, Enum):
    KITCHEN = "Kitchen"
    CENTRAL_HEATING = "Central Heating"
    FIREPLACE = "Fireplace"
    WIFI = "WiFi"
    TV = "TV"
    ROOM_WITH_BATHROOM = "Room with Bathroom"
    SHARED_BATHROOM = "Shared Bathroom"
    ROOM_WITH_TOILET = "Room with Toilet"
    SHARED_TOILET = "Shared Toilet"
    SAUNA = "Sauna"
    BBQ_AREA = "BBQ Area"
    PLAYGROUND = "Playground"
    LAUNDRY_FACILITIES = "Laundry Facilities"
    BALCONY = "Balcony"


class Huts(models.Model):
    MAX_NAME_LENGTH = 40
    MAX_OWNER_LENGTH = 80
    MAX_MANAGER_LENGTH = 40
    MAX_AREA_LENGTH = 60
    MAX_ALTITUDE_LENGTH = 5
    MAX_LODGING_DIGITS_LENGTH = 9
    MAX_LODGING_DIGITS_PLACES_LENGTH = 4
    MAX_DESCRIPTION_LENGTH = 150
    MAX_DIGITS_LENGTH = 9
    MAX_DECIMAL_PLACES_LENGTH = 6

    hut_name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        blank=False,
        null=False,
    )

    hut_owner = models.CharField(
        max_length=MAX_OWNER_LENGTH,
        blank=False,
        null=False,
    )

    hut_care_taker = models.CharField(
        max_length=MAX_MANAGER_LENGTH,
        blank=False,
        null=False,
    )

    phone_contact = models.CharField(
        max_length=20,
        blank=False,
        null=False,
    )

    hut_area = models.CharField(
        max_length=MAX_AREA_LENGTH,
        blank=True,
        null=True,
    )

    altitude = models.CharField(
        max_length=MAX_ALTITUDE_LENGTH,
        blank=True,
        null=True,
    )

    accommodation_beds = models.DecimalField(
        max_digits=MAX_LODGING_DIGITS_LENGTH,
        decimal_places=MAX_LODGING_DIGITS_PLACES_LENGTH,
        blank=True,
        null=True,
    )

    approach = MultiSelectField(
        choices=Approach.choices(),
        max_length=Approach.max_length(),
        blank=True,
        null=True,
    )

    weather_forecast = MultiSelectField(
        choices=WeatherCondition.choices(),
        max_length=WeatherCondition.max_length(),
        blank=True,
        null=True,
    )

    opened_in = MultiSelectField(
        choices=Month.choices(),
        max_length=Month.max_length(),
        blank=True,
        null=True,
    )

    services = MultiSelectField(
        choices=Services.choices(),
        max_length=Services.max_length(),
        blank=True,
        null=True,
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
    )

    description = models.TextField(
        max_length=MAX_DESCRIPTION_LENGTH,
        blank=True,
        null=True,
    )

    website = models.URLField(
        blank=True,
        null=True,
    )

    image = models.ImageField(
        upload_to='huts',
        blank=True,
        null=True,
    )

    longitude = models.DecimalField(
        max_digits=MAX_DIGITS_LENGTH,
        decimal_places=MAX_DECIMAL_PLACES_LENGTH,
        blank=True,
        null=True,
    )

    latitude = models.DecimalField(
        max_digits=MAX_DIGITS_LENGTH,
        decimal_places=MAX_DECIMAL_PLACES_LENGTH,
        blank=True,
        null=True,
    )

    publication_date_and_time = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=False,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name_plural = "Huts"  # Specify the plural name explicitly


class HutsLike(models.Model):
    huts = models.ForeignKey(
        Huts,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class HutsComment(models.Model):
    MAX_COMMENT_LENGTH = 180
    MIN_COMMENT_LENGTH = 5

    comment = models.TextField(
        max_length=MAX_COMMENT_LENGTH,
        validators=(
            validators.MinLengthValidator(MIN_COMMENT_LENGTH),
        ),
        blank=True,
        null=True,
    )

    huts = models.ForeignKey(
        Huts,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
