from django.contrib import admin
from .models import Post, Profile, Resort, Follower

# Registration.
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    fields = ('published', 'title', 'slug', 'content', 'image', 'author')
    list_display = ['published', 'title', 'created_at', 'updated_at']
    list_display_links = ['title']
    list_editable = ['published']
    list_filter = ['published', 'updated_at', 'author']
    prepopulated_fields = {"slug" : ("title",)}

# Profile Administration
class ProfileAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    fields = ('username', 'firstname', 'lastname', 'contact_phone', 'contact_email', 'slug', 'country', 'resort', 'markdown_description')
    list_display = ['username', 'firstname', 'lastname', 'resort']
    list_display_links = ['username']
    list_filter = ['resort', 'country', 'firstname', 'lastname']
    prepopulated_fields = {"slug" : ("firstname", "lastname", "resort",)}
    
# Resort administration
class ResortAdmin(admin.ModelAdmin):
    fields = ('country', 'state', 'name')
    list_display = ['name', 'country', 'state']
    list_display_links = ['name']
    list_filter = ['country']
    
# Mailing list administration    
class FollowerAdmin(admin.ModelAdmin):
    fields = ('email', 'firstname', 'lastname', 'active')
    list_display = ['active', 'email', 'follow_date']
    list_display_links = ['email']
    list_filter = ['active']
    list_editable = ['active']
    

admin.site.register(Post, PostAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Resort, ResortAdmin)
admin.site.register(Follower, FollowerAdmin)
