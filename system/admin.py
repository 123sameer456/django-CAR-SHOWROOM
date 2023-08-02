from django.contrib import admin
from .models import ShowRoom , Staff , Brand , Modell , Engine , Feature
# Register your models here.


@admin.register(ShowRoom)
class ShowRoomAdmin(admin.ModelAdmin):
    list_display = ['id' , 'name' , 'location' , 'contact' , 'email' , 'capacity']
    list_display_links = ['name']
    list_filter = ['name']
    search_fields = ['name']

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['id' , 'first_name' , 'last_name' , 'designation' , 'contact' ,
                     'email' , 'join_date' , 'image' ]
    list_display_links = ['first_name' , 'last_name']
    search_fields  =[ 'first_name' , 'last_name' , 'designation' ]
 
    
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['id' , 'brand_name' , 'brand_image' ]
    list_display_links = ['brand_name']
    search_fields  =[ 'brand_name']
    list_filter = ['brand_name']
@admin.register(Modell)
class ModellAdmin(admin.ModelAdmin):
    list_display = ['id' , 'model_name' , 'brand' , 'year' , 'price'   ]
    list_display_links = ['model_name']
    search_fields  =[ 'model_name' , 'year' , 'price']
    list_filter = ['model_name' , 'year' , 'price']
@admin.register(Engine)
class EngineAdmin(admin.ModelAdmin):
    list_display = ['id' , 'engine_type' , 'horse_power' , 'fuel_type']
    search_fields  =['engine_type','horse_power']
    list_display_links = ['engine_type']
    list_filter = ['engine_type','horse_power']
@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ['id' , 'feature_name' , 'description' ]
    list_display_links = ['feature_name']
    list_filter = ['feature_name' ]
    search_fields = ['features_name']
    