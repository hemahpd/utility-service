from django.contrib import admin

from accounts.models import BookForm, NewUser

# Register your models here.
admin.site.register(NewUser)
admin.site.register(BookForm)


