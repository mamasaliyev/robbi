from django.contrib import admin
# Import models from all apps
from clinic_and_sanatorium.models import clinic, clinic_and_sanatorium
from hotels.models import Hotels, Hotel_information
from mosques.models import Mosques, Mosques_info
from parks.models import Parks, Parks_info
from restaruants.models import Restaurants, Restaurant_info, Menu
from registers.models import CustomUser, Language

# Register models from each app

# CustomUser and Language admin
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass

# Hotels admin
@admin.register(Hotels)
class HotelsAdmin(admin.ModelAdmin):
    list_display = ('title', 'job_time', 'address', 'image')
    search_fields = ('title', 'address')
    list_filter = ('job_time',)

@admin.register(Hotel_information)
class HotelInformationAdmin(admin.ModelAdmin):
    list_display = ('title', 'job_time', 'address', 'star_rating', 'tel', 'image')
    search_fields = ('title', 'address', 'tel')
    list_filter = ('job_time', 'star_rating')

    def star_rating_display(self, obj):
        return f"{obj.get_star_rating_display()}"
    star_rating_display.short_description = 'Star Rating'

# Clinic admin
@admin.register(clinic)
class ClinicAdmin(admin.ModelAdmin):
    list_display = ('title', 'jop_time', 'address', 'image')
    search_fields = ('title', 'address')
    list_filter = ('jop_time',)

@admin.register(clinic_and_sanatorium)
class ClinicAndSanatoriumAdmin(admin.ModelAdmin):
    list_display = ('title', 'jop_time', 'address', 'tier', 'image')
    search_fields = ('title', 'address')
    list_filter = ('tier', 'jop_time')

# Restaurants admin
@admin.register(Restaurants)
class RestaurantsAdmin(admin.ModelAdmin):
    list_display = ('title', 'jop_time', 'address')
    search_fields = ('title', 'address')
    list_filter = ('jop_time',)

@admin.register(Restaurant_info)
class RestaurantInfoAdmin(admin.ModelAdmin):
    list_display = ('address', 'tel', 'latitude', 'longitude')
    search_fields = ('address', 'tel')
    list_filter = ('latitude', 'longitude')

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')
    search_fields = ('title',)
    list_filter = ('price',)

# Parks admin
@admin.register(Parks)
class ParksAdmin(admin.ModelAdmin):
    list_display = ('title', 'jop_time', 'address', 'image')
    search_fields = ('title', 'address')
    list_filter = ('jop_time',)

@admin.register(Parks_info)
class ParksInfoAdmin(admin.ModelAdmin):
    list_display = ('address', 'jop_time', 'latitude', 'longitude', 'tel')
    search_fields = ('address', 'tel')
    list_filter = ('jop_time',)

# Mosques admin
@admin.register(Mosques)
class MosquesAdmin(admin.ModelAdmin):
    list_display = ('title', 'jop_time', 'address', 'image')
    search_fields = ('title', 'address')
    list_filter = ('jop_time',)

@admin.register(Mosques_info)
class MosquesInfoAdmin(admin.ModelAdmin):
    list_display = ('address', 'jop_time', 'latitude', 'longitude', 'tel')
    search_fields = ('address', 'tel')
    list_filter = ('jop_time',)
