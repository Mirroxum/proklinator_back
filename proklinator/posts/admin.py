from django.contrib import admin

from posts.models import Post

@admin.register(Post)
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'curse',
        'comment',
        'duration',
        'likes',
        'link',
        'created_at',
        'updated_at',
        'is_active'
    )

    search_fields = ('id',)
