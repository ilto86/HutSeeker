from django.contrib import admin

from HutSeeker.huts.models import Huts, HutsLike, HutsComment


# Register your models here.
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
        'approach',
        'weather_forecast',
        'opened_in',
        'services',
        'description',
        'website',
        'image',
        'longitude',
        'latitude',
        'publication_date_and_time',
        'user',
    )

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
        ('Huts info', {
            'fields': (
                'hut_name',
                'hut_owner',
                'hut_care_taker',
                'phone_contact',
                'hut_area',
                'altitude',
                'accommodation_beds',
                'approach',
                'weather_forecast',
                'opened_in',
                'services',
                'description',
                'website',
                'image',
                'longitude',
                'latitude',
                'publication_date_and_time',
                'user',
            )
        }),
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
                'weather_forecast',
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