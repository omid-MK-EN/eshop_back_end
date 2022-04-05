from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import User

# is_new_active = User.is_new_active
# is_accounting_manager = User.is_accounting_manager
# is_sales_manager = User.is_sales_manager
# bio  = User.bio
# UserAdmin.fieldsets +=(
#     ("is_new_active",{"fields":("is_new_active",)}),
#     ("is_accounting_manager",{"fields":("is_accounting_manager",)}),
#     ("is_sales_manager",{"fields":("is_sales_manager",)}),
#     ("bio",{"fields":("bio",)}),
# )
admin.site.register(User)
