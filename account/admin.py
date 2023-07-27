from django.contrib import admin
from account.models import User
from django.contrib.auth.admin import UserAdmin as BasUserAdmin




# Register your models here.
class UserModelAdmin( BasUserAdmin):

    list_display = ['id',"email", "phone_number", "name","is_admin","photo"]
    list_filter = ["is_admin"]
    fieldsets = [
        ('User Credenatials', {"fields": ["email", "password",'password2']}),
        ("Personal info", {"fields": ["name","phone_number","photo"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "name","phone_number", "password1", "password2","photo"],
            },
        ),
    ]
    search_fields = ["phone_number"]
    ordering = ["email",'id']
    filter_horizontal = []


# Now register the new UserAdmin...
admin.site.register(User, UserModelAdmin)