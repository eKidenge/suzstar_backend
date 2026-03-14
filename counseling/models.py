from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone

class Service(models.Model):
    """Model for counseling services"""
    icon_choices = [
        ('MessageCircle', 'Message Circle'),
        ('Users', 'Users'),
        ('BookOpen', 'Book Open'),
        ('Heart', 'Heart'),
        ('Shield', 'Shield'),
        ('Clock', 'Clock'),
        ('CheckCircle', 'Check Circle'),
        ('Phone', 'Phone'),
        ('Sparkles', 'Sparkles'),
        ('Star', 'Star'),
        ('Award', 'Award'),
    ]
    
    icon = models.CharField(max_length=50, choices=icon_choices, default='Heart')
    title = models.CharField(max_length=200, default="Untitled Service")
    description = models.TextField()
    short_description = models.CharField(max_length=100, blank=True)
    image_url = models.URLField(blank=True, help_text='URL to service image')
    video_url = models.URLField(blank=True, help_text='URL to service video')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    duration = models.CharField(max_length=50, blank=True, help_text='e.g., "60 minutes"')
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'title']

    def __str__(self):
        return self.title

class Value(models.Model):
    """Model for company values/why choose us section"""
    icon_choices = [
        ('Heart', 'Heart'),
        ('Shield', 'Shield'),
        ('Users', 'Users'),
        ('BookOpen', 'Book Open'),
        ('TrendingUp', 'Trending Up'),
        ('Star', 'Star'),
        ('Award', 'Award'),
        ('Sparkles', 'Sparkles'),
    ]
    
    icon = models.CharField(max_length=50, choices=icon_choices, default='Heart')
    title = models.CharField(max_length=200, default="Untitled Value")
    description = models.TextField(blank=True)
    text = models.CharField(max_length=200)  # For backward compatibility
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.text

class HeroSlider(models.Model):
    """Model for hero slider images and content - multiple slides supported"""
    title = models.CharField(max_length=200, default="Untitled Slide")
    title_highlight = models.CharField(max_length=100, blank=True, help_text='Text to highlight in title')
    subtitle = models.CharField(max_length=300, blank=True)
    description = models.TextField()
    badge_text = models.CharField(max_length=200, blank=True)
    primary_button_text = models.CharField(max_length=100, default='Book Now')
    primary_button_link = models.CharField(max_length=200, default='contact')
    secondary_button_text = models.CharField(max_length=100, blank=True)
    secondary_button_link = models.CharField(max_length=200, blank=True)
    background_image_url = models.URLField(blank=True, help_text='URL to background image')
    background_video_url = models.URLField(blank=True, help_text='URL to background video')
    overlay_opacity = models.FloatField(default=0.5, help_text='Overlay opacity (0-1)')
    overlay_color = models.CharField(max_length=20, default='#000000')
    text_color = models.CharField(max_length=20, default='#FFFFFF')
    animation_type = models.CharField(max_length=50, choices=[
        ('fade', 'Fade'),
        ('slide', 'Slide'),
        ('zoom', 'Zoom'),
    ], default='fade')
    slide_duration = models.IntegerField(default=5000, help_text='Duration in milliseconds')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class HeroSection(models.Model):
    """Model for homepage hero section content - legacy support"""
    badge_text = models.CharField(max_length=200, default='Compassionate Mental Health Support')
    title = models.CharField(max_length=500, default="Untitled HeroSection")
    title_highlight = models.CharField(max_length=100, default='Alone')
    description = models.TextField()
    button_text = models.CharField(max_length=100, default='Book an Appointment')
    button_link = models.CharField(max_length=200, default='contact')
    phone_number = models.CharField(max_length=20, default='0799240254')
    background_image_url = models.URLField(blank=True)
    background_video_url = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Hero Section (Legacy)'
        verbose_name_plural = 'Hero Section (Legacy)'

    def save(self, *args, **kwargs):
        if self.is_active:
            HeroSection.objects.exclude(pk=self.pk).update(is_active=False)
        super().save(*args, **kwargs)

class Feature(models.Model):
    """Model for features displayed in hero section sidebar"""
    icon = models.CharField(max_length=50, choices=Service.icon_choices)
    title = models.CharField(max_length=200, default="Untitled Feature")
    description = models.CharField(max_length=300)
    icon_color = models.CharField(max_length=20, default='teal', choices=[
        ('teal', 'Teal'),
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('orange', 'Orange'),
        ('purple', 'Purple'),
        ('pink', 'Pink'),
    ])
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    """Model for client testimonials"""
    quote = models.TextField()
    author_name = models.CharField(max_length=200)
    author_title = models.CharField(max_length=200, blank=True)
    author_image_url = models.URLField(blank=True)
    rating = models.IntegerField(default=5, choices=[(i, i) for i in range(1, 6)])
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return f"Testimonial by {self.author_name}"

class Stat(models.Model):
    """Model for statistics/counters"""
    icon_choices = [
        ('Heart', 'Heart'),
        ('Users', 'Users'),
        ('Shield', 'Shield'),
        ('TrendingUp', 'Trending Up'),
        ('BookOpen', 'Book Open'),
        ('Calendar', 'Calendar'),
        ('Clock', 'Clock'),
        ('Award', 'Award'),
    ]
    
    icon = models.CharField(max_length=50, choices=icon_choices, default='Heart')
    title = models.CharField(max_length=200)
    value = models.CharField(max_length=100)
    suffix = models.CharField(max_length=20, blank=True, help_text='e.g., "+", "%", "k"')
    prefix = models.CharField(max_length=20, blank=True, help_text='e.g., "$"')
    description = models.CharField(max_length=300)
    animation_duration = models.IntegerField(default=2000, help_text='Duration in milliseconds')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title

class TeamMember(models.Model):
    """Model for counselor profiles"""
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    bio = models.TextField()
    image_url = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    specialties = models.JSONField(default=list, help_text='List of specialties')
    education = models.JSONField(default=list, help_text='List of education credentials')
    languages = models.JSONField(default=list, help_text='List of languages spoken')
    years_experience = models.IntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

class FAQ(models.Model):
    """Model for frequently asked questions"""
    question = models.CharField(max_length=500)
    answer = models.TextField()
    category = models.CharField(max_length=100, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'

    def __str__(self):
        return self.question

class BlogPost(models.Model):
    """Model for blog/articles"""
    title = models.CharField(max_length=500, default="Untitled BlogPost")
    slug = models.SlugField(unique=True)
    excerpt = models.TextField(max_length=500)
    content = models.TextField()
    author = models.CharField(max_length=200)
    author_image_url = models.URLField(blank=True)
    featured_image_url = models.URLField(blank=True)
    category = models.CharField(max_length=100, blank=True)
    tags = models.JSONField(default=list)
    read_time = models.IntegerField(default=5, help_text='Reading time in minutes')
    is_featured = models.BooleanField(default=False)
    views_count = models.IntegerField(default=0)
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title

class Event(models.Model):
    """Model for workshops and events"""
    title = models.CharField(max_length=500, default="Untitled Event")
    description = models.TextField()
    event_type = models.CharField(max_length=100, choices=[
        ('workshop', 'Workshop'),
        ('support_group', 'Support Group'),
        ('seminar', 'Seminar'),
        ('webinar', 'Webinar'),
    ])
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=500, blank=True)
    is_online = models.BooleanField(default=False)
    meeting_link = models.URLField(blank=True, help_text='For online events')
    capacity = models.IntegerField(null=True, blank=True)
    registered_count = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_free = models.BooleanField(default=False)
    featured_image_url = models.URLField(blank=True)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['start_date']

    def __str__(self):
        return self.title

class Partner(models.Model):
    """Model for partners and affiliates"""
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    logo_url = models.URLField(blank=True)
    website_url = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

class CallToAction(models.Model):
    """Model for CTA sections"""
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True)
    primary_button_text = models.CharField(max_length=100)
    primary_button_link = models.CharField(max_length=200)
    secondary_button_text = models.CharField(max_length=100, blank=True)
    secondary_button_link = models.CharField(max_length=200, blank=True)
    background_color = models.CharField(max_length=20, default='teal-600')
    text_color = models.CharField(max_length=20, default='white')
    background_image_url = models.URLField(blank=True)
    section_type = models.CharField(max_length=50, choices=[
        ('standard', 'Standard'),
        ('split', 'Split Screen'),
        ('full_width', 'Full Width'),
    ], default='standard')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class SupportOption(models.Model):
    """Model for support options (online, in-person, groups)"""
    icon_choices = [
        ('Video', 'Video'),
        ('Users', 'Users'),
        ('Calendar', 'Calendar'),
    ]
    
    icon = models.CharField(max_length=50, choices=icon_choices, default='Users')
    title = models.CharField(max_length=200)
    description = models.TextField()
    features = models.JSONField(default=list)
    color = models.CharField(max_length=20, choices=[
        ('teal', 'Teal'),
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('orange', 'Orange'),
        ('red', 'Red'),
    ], default='teal')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title

class WellnessTip(models.Model):
    """Model for mental wellness tips"""
    icon_choices = [
        ('Heart', 'Heart'),
        ('Users', 'Users'),
        ('Lightbulb', 'Lightbulb'),
        ('BookOpen', 'Book Open'),
        ('Phone', 'Phone'),
    ]
    
    icon = models.CharField(max_length=50, choices=icon_choices, default='Heart')
    title = models.CharField(max_length=200)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title

class EducationalResource(models.Model):
    """Model for educational resources"""
    icon_choices = [
        ('FileText', 'File Text'),
        ('BookOpen', 'Book Open'),
        ('Calendar', 'Calendar'),
        ('Lightbulb', 'Lightbulb'),
    ]
    
    icon = models.CharField(max_length=50, choices=icon_choices, default='FileText')
    title = models.CharField(max_length=200)
    description = models.TextField()
    button_text = models.CharField(max_length=100)
    button_action = models.CharField(max_length=200, help_text='URL, "contact", or "tel:number"')
    color = models.CharField(max_length=20, choices=[
        ('teal', 'Teal'),
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('orange', 'Orange'),
    ], default='teal')
    is_coming_soon = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title

class EmergencyContact(models.Model):
    """Model for emergency contacts"""
    title = models.CharField(max_length=200)
    contact = models.CharField(max_length=100)
    description = models.TextField()
    action = models.CharField(max_length=200, help_text='e.g., "tel:0799240254"')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title

class MissionVision(models.Model):
    """Model for mission and vision section"""
    mission_badge = models.CharField(max_length=100, default='Our Mission')
    mission_title = models.CharField(max_length=200, default='Why We Exist')
    mission_description = models.TextField()
    vision_badge = models.CharField(max_length=100, default='Our Vision')
    vision_title = models.CharField(max_length=200, default="The Future We're Building")
    vision_description = models.TextField()
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Mission & Vision'
        verbose_name_plural = 'Mission & Vision'

    def save(self, *args, **kwargs):
        if self.is_active:
            MissionVision.objects.exclude(pk=self.pk).update(is_active=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return "Mission & Vision"

class WhoWeServe(models.Model):
    """Model for who we serve section"""
    title = models.CharField(max_length=200, default='Who We Serve')
    description = models.TextField()
    items = models.JSONField(default=list)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Who We Serve'
        verbose_name_plural = 'Who We Serve'

    def save(self, *args, **kwargs):
        if self.is_active:
            WhoWeServe.objects.exclude(pk=self.pk).update(is_active=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Appointment(models.Model):
    """Model for appointment bookings"""
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
        ('rescheduled', 'Rescheduled'),
    ]
    
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    preferred_date = models.DateField()
    preferred_time = models.TimeField()
    preferred_contact_method = models.CharField(max_length=50, choices=[
        ('phone', 'Phone'),
        ('email', 'Email'),
        ('whatsapp', 'WhatsApp'),
    ], default='phone')
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True)
    counselor = models.ForeignKey(TeamMember, on_delete=models.SET_NULL, null=True, blank=True)
    message = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    is_urgent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Appointment - {self.name} - {self.preferred_date}"

class ContactMessage(models.Model):
    """Model for contact form submissions"""
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    is_replied = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"

class SiteSettings(models.Model):
    """Model for site-wide settings"""
    site_name = models.CharField(max_length=200, default='Suzstar Counseling')
    site_description = models.TextField(blank=True, help_text='Meta description for SEO')
    contact_email = models.EmailField(default='info@suzstarcounseling.com')
    contact_phone = models.CharField(max_length=20, default='0799240254')
    whatsapp_number = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    google_maps_url = models.URLField(blank=True)
    facebook_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)
    tiktok_url = models.URLField(blank=True)
    working_hours = models.TextField(default='Monday - Saturday: 9:00 AM - 6:00 PM')
    footer_text = models.TextField(default='© 2024 Suzstar Counseling. All rights reserved.')
    logo_url = models.URLField(blank=True)
    favicon_url = models.URLField(blank=True)
    primary_color = models.CharField(max_length=20, default='teal-600')
    secondary_color = models.CharField(max_length=20, default='blue-600')
    accent_color = models.CharField(max_length=20, default='orange-500')
    google_analytics_id = models.CharField(max_length=50, blank=True)
    
    class Meta:
        verbose_name = 'Site Settings'
        verbose_name_plural = 'Site Settings'

    def save(self, *args, **kwargs):
        SiteSettings.objects.exclude(pk=self.pk).delete()
        super().save(*args, **kwargs)

class TherapeuticApproach(models.Model):
    """Model for therapeutic approaches"""
    icon_choices = [
        ('Brain', 'Brain'),
        ('Lightbulb', 'Lightbulb'),
        ('Target', 'Target'),
        ('Sparkles', 'Sparkles'),
        ('BookOpen', 'Book Open'),
        ('Heart', 'Heart'),
        ('Users', 'Users'),
        ('Shield', 'Shield'),
    ]
    
    icon = models.CharField(max_length=50, choices=icon_choices, default='Brain')
    title = models.CharField(max_length=200)
    description = models.TextField()
    long_description = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title

class NewsletterSubscriber(models.Model):
    """Model for newsletter subscribers"""
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=200, blank=True)
    is_active = models.BooleanField(default=True)
    subscribed_date = models.DateTimeField(auto_now_add=True)
    unsubscribed_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.email

class PageSection(models.Model):
    """Model for dynamic page sections"""
    page = models.CharField(max_length=100, choices=[
        ('home', 'Home'),
        ('about', 'About'),
        ('services', 'Services'),
        ('resources', 'Resources'),
        ('contact', 'Contact'),
    ])
    section_name = models.CharField(max_length=200)
    title = models.CharField(max_length=500, default="Untitled Section")
    subtitle = models.CharField(max_length=500, blank=True)
    description = models.TextField(blank=True)
    content = models.JSONField(default=dict, blank=True)
    background_type = models.CharField(max_length=50, choices=[
        ('color', 'Color'),
        ('image', 'Image'),
        ('video', 'Video'),
        ('gradient', 'Gradient'),
    ], default='color')
    background_value = models.CharField(max_length=500, blank=True)
    text_color = models.CharField(max_length=20, default='gray-900')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['page', 'order']
        unique_together = ['page', 'section_name']

    def __str__(self):
        return f"{self.get_page_display()} - {self.section_name}"