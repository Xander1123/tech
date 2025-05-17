from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.utils.timezone import now
from .models import HeroSection
from .models import Service, FAQCategory
from .forms import ContactMessage
from django.http import Http404
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags



def home(request):
    hero_section = HeroSection.objects.filter(is_active=True).first()
    background_image_url = hero_section.background_image.url if hero_section and hero_section.background_image else None

    services = Service.objects.all()
    faq_categories = FAQCategory.objects.filter(is_active=True).prefetch_related('faqs').order_by('order', 'name')

    for category in faq_categories:
        category.active_faqs = category.faqs.filter(is_active=True).order_by('order', 'question')

    return render(request, 'index.html', {
        'hero_section': hero_section,
        'background_image_url': background_image_url,
        'services': services,
        'faq_categories': faq_categories,
    })

def services_view(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})

def send_feedback_email(contact_message):
    send_mail(
        'Cavabınız haqqında məlumat',
        contact_message.response,
        settings.DEFAULT_FROM_EMAIL,
        [contact_message.email],
    )

def contact_message(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Verilənləri bazaya yaz
        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message,
            created_at=now()
        )

        # 🔧 Bura saytın domenini əlavə et — localhost üçün bu olar:

        # HTML cavab üçün template yığırıq
        html_content = render_to_string('auto_reply.html', {
            'name': name,
        })
        text_content = strip_tags(html_content)

        # Avtomatik cavab göndər
        msg = EmailMultiAlternatives(
            subject="Fixbit ilə əlaqə saxladığınız üçün təşəkkür edirik!",
            body=text_content,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[email]
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        # Əvvəlki səhifəyə yönləndir
        referer = request.META.get('HTTP_REFERER')
        return redirect(referer) if referer else redirect('home')

    return redirect('home')

def questions_view(request):
    # Aktiv olan FAQ kateqoriyalarını alırıq və hər kateqoriya üçün aktiv olan FAQ-ları da çəkirik
    faq_categories = FAQCategory.objects.filter(is_active=True).prefetch_related('faqs')
    
    for category in faq_categories:
        category.active_faqs = category.faqs.filter(is_active=True).order_by('order', 'question')

    return render(request, 'questions.html', {'faq_categories': faq_categories})

def contact_view(request):
    return render(request, 'contact.html')
# views.py


def test_404_view(request):
    return render(request, '404.html')  # Öz şablonunu göstər


from .models import TranslatableText
from django.utils.translation import get_language

def get_text(key):
    lang = get_language()[:2]
    try:
        return TranslatableText.objects.get(key=key, lang=lang).text
    except TranslatableText.DoesNotExist:
        return key  # Fallback
