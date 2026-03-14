# counseling/admin.py

from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Service, Value, HeroSection, HeroSlider, Feature, 
    Testimonial, Appointment, ContactMessage, SiteSettings, 
    TherapeuticApproach, SupportOption, WellnessTip, 
    EducationalResource, EmergencyContact, MissionVision, 
    WhoWeServe, Stat, TeamMember, FAQ, BlogPost, Event,
    Partner, CallToAction, NewsletterSubscriber, PageSection
)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon', 'is_featured', 'order', 'is_active']
    list_editable = ['is_featured', 'order', 'is_active']
    search_fields = ['title', 'description', 'short_description']
    list_filter = ['is_active', 'is_featured', 'icon']
    fieldsets = (
        ('Basic Information', {
            'fields': ('icon', 'title', 'short_description', 'description')
        }),
        ('Media', {
            'fields': ('image_url', 'video_url')
        }),
        ('Pricing', {
            'fields': ('price', 'duration')
        }),
        ('Settings', {
            'fields': ('is_featured', 'order', 'is_active')
        }),
    )

@admin.register(Value)
class ValueAdmin(admin.ModelAdmin):
    list_display = ['text', 'title', 'icon', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    search_fields = ['text', 'title', 'description']

@admin.register(HeroSlider)
class HeroSliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'badge_text', 'animation_type', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    list_filter = ['animation_type', 'is_active']
    search_fields = ['title', 'subtitle', 'description']
    fieldsets = (
        ('Content', {
            'fields': ('title', 'title_highlight', 'subtitle', 'description', 'badge_text')
        }),
        ('Buttons', {
            'fields': ('primary_button_text', 'primary_button_link', 'secondary_button_text', 'secondary_button_link')
        }),
        ('Background', {
            'fields': ('background_image_url', 'background_video_url', 'overlay_color', 'overlay_opacity')
        }),
        ('Styling', {
            'fields': ('text_color', 'animation_type', 'slide_duration')
        }),
        ('Settings', {
            'fields': ('order', 'is_active')
        }),
    )

@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ['badge_text', 'title_preview', 'is_active']
    
    def title_preview(self, obj):
        return obj.title[:50] + '...' if len(obj.title) > 50 else obj.title
    title_preview.short_description = 'Title'

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon', 'icon_color', 'order', 'is_active']
    list_editable = ['icon_color', 'order', 'is_active']
    list_filter = ['icon_color', 'is_active']

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['author_name', 'rating', 'is_featured', 'order', 'is_active']
    list_editable = ['rating', 'is_featured', 'order', 'is_active']
    list_filter = ['rating', 'is_featured', 'is_active']
    search_fields = ['author_name', 'author_title', 'quote']
    fieldsets = (
        ('Content', {
            'fields': ('quote', 'author_name', 'author_title', 'author_image_url')
        }),
        ('Rating', {
            'fields': ('rating',)
        }),
        ('Settings', {
            'fields': ('is_featured', 'order', 'is_active')
        }),
    )

@admin.register(Stat)
class StatAdmin(admin.ModelAdmin):
    list_display = ['title', 'value_with_suffix', 'icon', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    search_fields = ['title', 'description']
    
    def value_with_suffix(self, obj):
        return f"{obj.prefix}{obj.value}{obj.suffix}"
    value_with_suffix.short_description = 'Value'

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'years_experience', 'is_featured', 'order', 'is_active']
    list_editable = ['is_featured', 'order', 'is_active']
    list_filter = ['is_featured', 'is_active']
    search_fields = ['name', 'title', 'bio']
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'title', 'bio', 'image_url', 'email', 'phone')
        }),
        ('Professional', {
            'fields': ('specialties', 'education', 'languages', 'years_experience')
        }),
        ('Settings', {
            'fields': ('is_featured', 'order', 'is_active')
        }),
    )

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'category', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    list_filter = ['category', 'is_active']
    search_fields = ['question', 'answer']

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'is_featured', 'views_count', 'published_date']
    list_editable = ['is_featured']
    list_filter = ['category', 'is_featured', 'is_active']
    search_fields = ['title', 'excerpt', 'content', 'author']
    readonly_fields = ['views_count', 'published_date', 'updated_date']
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'excerpt', 'content', 'author', 'author_image_url')
        }),
        ('Media', {
            'fields': ('featured_image_url',)
        }),
        ('Categorization', {
            'fields': ('category', 'tags')
        }),
        ('Settings', {
            'fields': ('read_time', 'is_featured', 'is_active')
        }),
        ('Statistics', {
            'fields': ('views_count', 'published_date', 'updated_date'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'event_type', 'start_date', 'end_date', 'is_featured', 'is_active']
    list_editable = ['is_featured', 'is_active']
    list_filter = ['event_type', 'is_online', 'is_featured', 'is_active']
    search_fields = ['title', 'description']
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'event_type')
        }),
        ('Date & Location', {
            'fields': ('start_date', 'end_date', 'location', 'is_online', 'meeting_link')
        }),
        ('Capacity & Pricing', {
            'fields': ('capacity', 'registered_count', 'price', 'is_free')
        }),
        ('Media', {
            'fields': ('featured_image_url',)
        }),
        ('Settings', {
            'fields': ('is_featured', 'is_active')
        }),
    )

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'logo_preview', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    search_fields = ['name', 'description']
    
    def logo_preview(self, obj):
        if obj.logo_url:
            return format_html('<img src="{}" style="max-height: 40px; max-width: 100px;" />', obj.logo_url)
        return "No logo"
    logo_preview.short_description = 'Logo'

@admin.register(CallToAction)
class CallToActionAdmin(admin.ModelAdmin):
    list_display = ['title', 'section_type', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    list_filter = ['section_type', 'is_active']
    search_fields = ['title', 'subtitle', 'description']

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'preferred_date', 'preferred_time', 'service', 'counselor', 'status', 'is_urgent']
    list_editable = ['status']
    list_filter = ['status', 'preferred_contact_method', 'is_urgent', 'service', 'counselor']
    search_fields = ['name', 'email', 'phone', 'message']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Client Information', {
            'fields': ('name', 'email', 'phone', 'preferred_contact_method')
        }),
        ('Appointment Details', {
            'fields': ('preferred_date', 'preferred_time', 'service', 'counselor', 'message', 'is_urgent')
        }),
        ('Status', {
            'fields': ('status',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'is_read', 'is_replied', 'created_at']
    list_editable = ['is_read', 'is_replied']
    list_filter = ['is_read', 'is_replied', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['created_at']
    
    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "Mark selected messages as read"
    
    def mark_as_replied(self, request, queryset):
        queryset.update(is_replied=True)
    mark_as_replied.short_description = "Mark selected messages as replied"
    
    actions = ['mark_as_read', 'mark_as_replied']

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Basic Information', {
            'fields': ('site_name', 'site_description', 'logo_url', 'favicon_url')
        }),
        ('Contact Information', {
            'fields': ('contact_email', 'contact_phone', 'whatsapp_number', 'address', 'google_maps_url')
        }),
        ('Social Media', {
            'fields': ('facebook_url', 'twitter_url', 'instagram_url', 'linkedin_url', 'youtube_url', 'tiktok_url')
        }),
        ('Business Hours', {
            'fields': ('working_hours', 'footer_text')
        }),
        ('Branding', {
            'fields': ('primary_color', 'secondary_color', 'accent_color')
        }),
        ('Analytics', {
            'fields': ('google_analytics_id',)
        }),
    )

@admin.register(TherapeuticApproach)
class TherapeuticApproachAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon', 'is_featured', 'order', 'is_active']
    list_editable = ['is_featured', 'order', 'is_active']
    list_filter = ['is_featured', 'is_active']
    search_fields = ['title', 'description', 'long_description']

@admin.register(SupportOption)
class SupportOptionAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon', 'color', 'order', 'is_active']
    list_editable = ['color', 'order', 'is_active']
    list_filter = ['color', 'is_active']
    search_fields = ['title', 'description']

@admin.register(WellnessTip)
class WellnessTipAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['title', 'description']

@admin.register(EducationalResource)
class EducationalResourceAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon', 'color', 'is_coming_soon', 'order', 'is_active']
    list_editable = ['is_coming_soon', 'color', 'order', 'is_active']
    list_filter = ['color', 'is_coming_soon', 'is_active']
    search_fields = ['title', 'description']

@admin.register(EmergencyContact)
class EmergencyContactAdmin(admin.ModelAdmin):
    list_display = ['title', 'contact', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['title', 'contact', 'description']

@admin.register(MissionVision)
class MissionVisionAdmin(admin.ModelAdmin):
    list_display = ['mission_title', 'vision_title', 'is_active']
    list_editable = ['is_active']
    fieldsets = (
        ('Mission', {
            'fields': ('mission_badge', 'mission_title', 'mission_description')
        }),
        ('Vision', {
            'fields': ('vision_badge', 'vision_title', 'vision_description')
        }),
        ('Settings', {
            'fields': ('is_active',)
        }),
    )

@admin.register(WhoWeServe)
class WhoWeServeAdmin(admin.ModelAdmin):
    list_display = ['title', 'items_count', 'is_active']
    list_editable = ['is_active']
    
    def items_count(self, obj):
        return len(obj.items) if obj.items else 0
    items_count.short_description = 'Number of Items'

@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'is_active', 'subscribed_date']
    list_editable = ['is_active']
    list_filter = ['is_active']
    search_fields = ['email', 'name']
    readonly_fields = ['subscribed_date', 'unsubscribed_date']

@admin.register(PageSection)
class PageSectionAdmin(admin.ModelAdmin):
    list_display = ['page', 'section_name', 'title', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    list_filter = ['page', 'background_type', 'is_active']
    search_fields = ['page', 'section_name', 'title', 'subtitle', 'description']
    fieldsets = (
        ('Page Information', {
            'fields': ('page', 'section_name')
        }),
        ('Content', {
            'fields': ('title', 'subtitle', 'description', 'content')
        }),
        ('Background', {
            'fields': ('background_type', 'background_value', 'text_color')
        }),
        ('Settings', {
            'fields': ('order', 'is_active')
        }),
    )