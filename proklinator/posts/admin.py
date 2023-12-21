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

    def get_form(self, request, obj=None, **kwargs):
        form = super(AccountAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['link'].required = False
        form.base_fields['comment'].required = False
        return form