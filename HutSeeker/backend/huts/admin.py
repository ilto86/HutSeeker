from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from backend.huts.models import Approach, Huts, HutsLike, HutsComment, Month, Services, WeatherCondition


@admin.register(Huts)
class HutsAdmin(admin.ModelAdmin):
    readonly_fields = ('publication_date_and_time',)

    list_display = (
        'hut_name',
        'hut_owner',
        'hut_care_taker',
        'phone_contact',
        'hut_area',
        'altitude',
        'accommodation_beds',
        'display_approach',
        'display_weather_condition',
        'display_opened_in',
        'display_services',
        'description',
        'website',
        'image',
        'longitude',
        'latitude',
        'publication_date_and_time',
        'user',
    )

    def display_approach(self, obj):
        return ', '.join([str(approach) for approach in obj.approach.all()])
    display_approach.short_description = 'Approach'

    def display_weather_condition(self, obj):
        return ', '.join([str(condition) for condition in obj.weather_condition.all()])
    display_weather_condition.short_description = 'Weather Condition'

    def display_opened_in(self, obj):
        return ', '.join([str(month) for month in obj.opened_in.all()])
    display_opened_in.short_description = 'Opened In'

    def display_services(self, obj):
        return ', '.join([str(service) for service in obj.services.all()])
    display_services.short_description = 'Services'

    search_fields = (
        'hut_name',
        'hut_area',
        'altitude',
        'accommodation_beds',
        'approach',
        'opened_in',
        'website',
        'publication_date_and_time',
    )

    list_filter = (
        'publication_date_and_time',
        'hut_name',
        'hut_area',
        'altitude',
        'approach',
        'opened_in',
        'user',
    )

    fieldsets = (
        ('Contact Information', {
            'fields': ('hut_name', 'hut_owner', 'hut_care_taker', 'phone_contact')
        }),
        ('Location Information', {
            'fields': ('hut_area', 'altitude', 'longitude', 'latitude')
        }),
        ('Accommodation Information', {
            'fields': ('accommodation_beds',)
        }),
        ('Many-to-Many Fields', {
            'fields': ('approach', 'weather_condition', 'opened_in', 'services')
        }),
        ('Additional Information', {
            'fields': ('description', 'website', 'image', 'publication_date_and_time', 'user')
        }),
    )

    filter_horizontal = (
        'approach',
        'weather_condition',
        'opened_in',
        'services'
    )

    add_fieldsets = (
        ('Huts', {
            'classes': (
                'wide',
            ),
            'fields': (
                'hut_name',
                'hut_owner',
                'hut_care_taker',
                'phone_contact',
                'hut_area',
                'altitude',
                'accommodation_beds',
                'approach',
                'weather_condition',
                'opened_in',
                'services',
                'description',
                'website',
                'image',
                'longitude',
                'latitude',
                'publication_date_and_time',
                'user',
            ),
        }),
    )

    @staticmethod
    def product_image(obj):
        return mark_safe('<img src="{url}" width="{width}"/>'.format(
            url=obj.image.url,
            width=200,
        )
        )

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

    fieldsets = (
        ('Services', {
            'fields': (
                'name',
            )
        }),
    )

    search_fields = (
        'name',
    )

    list_filter =(
        'name',
    )

@admin.register(Approach)
class ApproachAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

    fieldsets = (
        ('Services', {
            'fields': (
                'name',
            )
        }),
    )

    search_fields = (
        'name',
    )

    list_filter =(
        'name',
    )

@admin.register(Month)
class MonthAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

    fieldsets = (
        ('Services', {
            'fields': (
                'name',
            )
        }),
    )

    search_fields = (
        'name',
    )

    list_filter =(
        'name',
    )

@admin.register(WeatherCondition)
class WeatherConditionAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

    fieldsets = (
        ('Services', {
            'fields': (
                'name',
            )
        }),
    )

    search_fields = (
        'name',
    )

    list_filter =(
        'name',
    )

@admin.register(HutsLike)
class HutsLikeAdmin(admin.ModelAdmin):
    list_display = (
        'huts',
        'user',
    )

    search_fields = (
        'huts',
    )

    list_filter = (
        'huts',
        'user',
    )

    fieldsets = (
        ('Huts like', {
            'fields': (
                'huts',
                'user',
            )
        }),
    )

    add_fieldsets = (
        ('Huts like', {
            'classes': (
                'wide',
            ),
            'fields': (
                'huts',
                'user',
            ),
        }),
    )

@admin.register(HutsComment)
class HutsCommentAdmin(admin.ModelAdmin):
    list_display = (
        'comment',
        'huts',
        'user',
    )

    search_fields = (
        'huts',
    )

    list_filter = (
        'huts',
        'user',
    )

    fieldsets = (
        ('Huts comments', {
            'fields': (
                'comment',
                'huts',
                'user',
            )
        }),
    )

    add_fieldsets = (
        ('Huts comments', {
            'classes': (
                'wide',
            ),
            'fields': (
                'comment',
                'huts',
                'user',
            )
        }),
    )