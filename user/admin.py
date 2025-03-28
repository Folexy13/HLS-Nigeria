from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from user.models import UserProfile, Basic, Lifestyle, HealthCondition, Preference
from .models import Notification,Message

# @admin.register(Notification)
# class NotificationAdmin(admin.ModelAdmin):
#     list_display = ('user', 'message', 'created_at', 'is_read')

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    extra = 1

class BasicInline(admin.StackedInline):
    model = Basic
    extra = 1

class LifestyleInline(admin.StackedInline):
    model = Lifestyle
    extra = 1

class HealthConditionInline(admin.StackedInline):
    model = HealthCondition
    extra = 1

class PreferenceInline(admin.StackedInline):
    model = Preference
    extra = 1

# UserProfileAdmin now inherits from InlineModelAdmin
class UserProfileAdmin(admin.ModelAdmin):
    inlines = [BasicInline, LifestyleInline, HealthConditionInline, PreferenceInline]

# Register the UserProfile model and its inlines
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Notification)
admin.site.register(Message)

# Add UserProfileInline to the UserAdmin
UserAdmin.inlines = [UserProfileInline]
admin.site.unregister(User)  # Unregister the default UserAdmin to register a customized one
admin.site.register(User, UserAdmin)  # Register the customized UserAdmin
