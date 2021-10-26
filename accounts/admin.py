from django.contrib import admin

from accounts.models import BookForm, NewUser

# Register your models here.


admin.site.site_header="MADURAINEEDS ADMINISTRATION PAGE"
class NewUserAdmin(admin.ModelAdmin):
    list_display= ("username","email","pwd","gender")

class BookFormAdmin(admin.ModelAdmin):
    list_display=("name","specialisation","phnno","addressline1","mainarea","pincode")

admin.site.register(NewUser,NewUserAdmin)
admin.site.register(BookForm,BookFormAdmin)