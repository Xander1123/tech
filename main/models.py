from django.db import models
class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='services/' ,blank=True, null=True)

    def __str__(self):
        return self.name
# models.py

# main/models.py
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Feedback üçün əlavə sahə
    response = models.TextField(blank=True, null=True)
    responded_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.email}"



from django.db import models
from django.utils.translation import gettext_lazy as _

class FAQCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Category Name"))
    order = models.PositiveIntegerField(default=0, verbose_name=_("Display Order"))
    is_active = models.BooleanField(default=True, verbose_name=_("Active"))

    class Meta:
        verbose_name = _("FAQ Category")
        verbose_name_plural = _("FAQ Categories")
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

class FAQ(models.Model):
    question = models.CharField(max_length=255, verbose_name=_("Question"))
    answer = models.TextField(verbose_name=_("Answer"))
    category = models.ForeignKey(
        FAQCategory, 
        on_delete=models.CASCADE, 
        related_name='faqs',
        verbose_name=_("Category")
    )
    order = models.PositiveIntegerField(default=0, verbose_name=_("Display Order"))
    is_active = models.BooleanField(default=True, verbose_name=_("Active"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("FAQ")
        verbose_name_plural = _("FAQs")
        ordering = ['order', 'question']

    def __str__(self):
        return self.question
    # models.py


from django.db import models

class HeroSection(models.Model):
    title = models.CharField(max_length=200, verbose_name="Başlıq")
    description = models.TextField(verbose_name="Təsvir")
    button_text = models.CharField(max_length=100, verbose_name="Düymə Mətni", default="Ətraflı")
    button_url = models.CharField(max_length=200, default="#services", verbose_name="Düymə Linki")
    background_image = models.ImageField(upload_to='hero_images/', null=True, blank=True, verbose_name="Fon Şəkli")
    is_active = models.BooleanField(default=True, verbose_name="Aktivdir")

    class Meta:
        verbose_name = "Hero Section"
        verbose_name_plural = "Hero Sections"

    def __str__(self):
        return self.title
    

