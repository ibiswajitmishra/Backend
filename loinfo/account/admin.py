
from django.contrib import admin
from account.models import Account

class AccountAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','username','date_joined', 'last_login', 'is_admin','is_staff','is_collegeverified')
    search_fields = ('email','username',)
    readonly_fields=('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
admin.site.register(Account, AccountAdmin)
