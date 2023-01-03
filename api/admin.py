from django.contrib import admin
from .models import Usermodel, Postmodel, Likemodel

# Register your models here.

"""admin side view for user table"""
@admin.register(Usermodel)
class Useradmin(admin.ModelAdmin):
    filelds = ['id','username','created_at']


"""admin side view for post table """
@admin.register(Postmodel)
class Useradmin(admin.ModelAdmin):
    filelds = ['text','post_id','created_at','user_id']


"""admin side view for like table"""
@admin.register(Likemodel)
class Useradmin(admin.ModelAdmin):
    filelds = ['resp_id','post_id','user_id','like','updated_at']    