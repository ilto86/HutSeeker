from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.text import slugify

from django.core import validators
# from backend.utils.model_mixins import ChoicesEnumMixin

UserModel = get_user_model()


# class ApproachTypes(ChoicesEnumMixin, Enum):
#     PEDESTRIAN = "Pedestrian"
#     WHEEL = "Wheel"
#     CAR = "Car"
#     BUS = "Bus"
#     LIFT = "Lift"
#     CAMPER = "Camper"


# class WeatherCondition(ChoicesEnumMixin, Enum):
#     SUNNY = "Sunny"
#     CLOUDY = "Cloudy"
#     RAINY = "Rainy"
#     SNOWY = "Snowy"


# class Month(ChoicesEnumMixin, Enum):
#     JANUARY = "January"
#     FEBRUARY = "February"
#     MARCH = "March"
#     APRIL = "April"
#     MAY = "May"
#     JUNE = "June"
#     JULY = "July"
#     AUGUST = "August"
#     SEPTEMBER = "September"
#     OCTOBER = "October"
#     NOVEMBER = "November"
#     DECEMBER = "December"


# class Services(ChoicesEnumMixin, Enum):
#     KITCHEN = "Kitchen"
#     CENTRAL_HEATING = "Central Heating"
#     FIREPLACE = "Fireplace"
#     WIFI = "WiFi"
#     TV = "TV"
#     ROOM_WITH_BATHROOM = "Room with Bathroom"
#     SHARED_BATHROOM = "Shared Bathroom"
#     ROOM_WITH_TOILET = "Room with Toilet"
#     SHARED_TOILET = "Shared Toilet"
#     SAUNA = "Sauna"
#     BBQ_AREA = "BBQ Area"
#     PLAYGROUND = "Playground"
#     LAUNDRY_FACILITIES = "Laundry Facilities"
#     BALCONY = "Balcony"


class Approach(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Approach"

    def __str__(self):
        return self.name


class Month(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Month"
    
    def __str__(self):
        return self.name


class Services(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Services"

    def __str__(self):
        return self.name


class WeatherCondition(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Weather Condition"

    def __str__(self):
        return self.name


class Huts(models.Model):
    MAX_NAME_LENGTH = 40
    MAX_OWNER_LENGTH = 80
    MAX_MANAGER_LENGTH = 40
    MAX_AREA_LENGTH = 60
    MAX_ALTITUDE_LENGTH = 5
    MAX_LODGING_DIGITS_LENGTH = 9
    MAX_LODGING_DIGITS_PLACES_LENGTH = 4
    MAX_DESCRIPTION_LENGTH = 1000
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

    approach = models.ManyToManyField(Approach)

    weather_condition = models.ManyToManyField(WeatherCondition)

    opened_in = models.ManyToManyField(Month)

    services = models.ManyToManyField(Services)

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

    def __str__(self):
        return self.hut_name

    def get_absolute_url(self):
        return reverse('hut-details', args=[self.pk, slugify(self.hut_name)])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.pk}-{self.hut_name}')

        return super().save(*args, **kwargs)


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
