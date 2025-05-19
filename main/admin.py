from django.contrib import admin
from .models import Service, ContactMessage
from django.utils.timezone import now
from django.core.mail import send_mail
from .models import FAQCategory, FAQ
from .models import HeroSection




# Service model üçün admin tənzimləməsi
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image')  # Göstəriləcək sahələr
    search_fields = ('name',)  # Axtarış üçün istifadə ediləcək sahə

# main/admin.py


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at', 'responded_at']
    readonly_fields = ['name', 'email', 'message', 'created_at']
    fields = ('name', 'email', 'message', 'created_at', 'response', 'responded_at')

    def save_model(self, request, obj, form, change):
        if obj.response and not obj.responded_at:
            obj.responded_at = now()

            # Əgər SMTP işləyirsə, istifadəçiyə cavab göndər
            try:
                send_mail(
                    subject='Fixbit: Mesajınıza cavab',
                    message=obj.response,
                    from_email='your_email@gmail.com',
                    recipient_list=[obj.email],
                )
            except:
                pass  # SMTP problemi varsa, sus

        super().save_model(request, obj, form, change)

#from django.contrib import admin

from django.contrib import admin
from .models import FAQCategory, FAQ

@admin.register(FAQCategory)
class FAQCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('name',)
    ordering = ('order', 'name')

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'category', 'order', 'is_active')
    list_filter = ('category', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('question', 'answer')
    ordering = ('category__order', 'order', 'question')
    # admin.py




@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    list_filter = ('is_active',)

# admin.py
