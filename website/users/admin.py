from django.contrib import admin

# Register your models here.
from .models import Post, Messages, encMessages

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["postname", "Content", "timestamp", "file", "owner"]
    list_display_links = ["postname", "Content", "timestamp"]
    list_filter = ["postname", "timestamp"]

    class Meta:
        model = Post

admin.site.register(Post, PostModelAdmin)

class MsgModelAdmin(admin.ModelAdmin):
    list_display = ["title", "message", "timestamp", "owner", ]
    list_display_links = ["message"]

    class Meta:
        model = Messages

admin.site.register(Messages, MsgModelAdmin)

class encMsgModelAdmin(admin.ModelAdmin):
    list_display = ["title", "encrypted_message", "timestamp", "owner", ]
    list_display_links = ["encrypted_message"]

    class Meta:
        model = encMessages

admin.site.register(encMessages, encMsgModelAdmin)