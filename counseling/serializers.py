# counseling/serializers.py

from rest_framework import serializers
from .models import (
    Service, Value, HeroSection, HeroSlider, Feature, 
    Testimonial, Appointment, ContactMessage, SiteSettings, 
    TherapeuticApproach, SupportOption, WellnessTip, 
    EducationalResource, EmergencyContact, MissionVision, 
    WhoWeServe, Stat, TeamMember, FAQ, BlogPost, Event,
    Partner, CallToAction, NewsletterSubscriber, PageSection
)

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'icon', 'title', 'short_description', 'description', 
                 'image_url', 'video_url', 'price', 'duration', 'is_featured', 
                 'order', 'is_active']

class ValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Value
        fields = ['id', 'icon', 'title', 'description', 'text', 'order', 'is_active']

class HeroSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSlider
        fields = ['id', 'title', 'title_highlight', 'subtitle', 'description', 
                 'badge_text', 'primary_button_text', 'primary_button_link',
                 'secondary_button_text', 'secondary_button_link', 
                 'background_image_url', 'background_video_url', 
                 'overlay_opacity', 'overlay_color', 'text_color',
                 'animation_type', 'slide_duration', 'order', 'is_active']

class HeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSection
        fields = ['badge_text', 'title', 'title_highlight', 'description', 
                 'button_text', 'button_link', 'phone_number', 
                 'background_image_url', 'background_video_url', 'is_active']

class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ['id', 'icon', 'title', 'description', 'icon_color', 'order', 'is_active']

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ['id', 'quote', 'author_name', 'author_title', 'author_image_url',
                 'rating', 'is_featured', 'order', 'is_active']

class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stat
        fields = ['id', 'icon', 'title', 'value', 'suffix', 'prefix', 
                 'description', 'animation_duration', 'order', 'is_active']

class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = ['id', 'name', 'title', 'bio', 'image_url', 'email', 'phone',
                 'specialties', 'education', 'languages', 'years_experience',
                 'is_featured', 'order', 'is_active']

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer', 'category', 'order', 'is_active']

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'slug', 'excerpt', 'content', 'author',
                 'author_image_url', 'featured_image_url', 'category', 'tags',
                 'read_time', 'is_featured', 'views_count', 'published_date',
                 'updated_date', 'is_active']

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'event_type', 'start_date',
                 'end_date', 'location', 'is_online', 'meeting_link',
                 'capacity', 'registered_count', 'price', 'is_free',
                 'featured_image_url', 'is_featured', 'is_active']

class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ['id', 'name', 'description', 'logo_url', 'website_url',
                 'order', 'is_active']

class CallToActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallToAction
        fields = ['id', 'title', 'subtitle', 'description', 
                 'primary_button_text', 'primary_button_link',
                 'secondary_button_text', 'secondary_button_link',
                 'background_color', 'text_color', 'background_image_url',
                 'section_type', 'order', 'is_active']

class SupportOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportOption
        fields = ['id', 'icon', 'title', 'description', 'features', 'color', 
                 'order', 'is_active']

class WellnessTipSerializer(serializers.ModelSerializer):
    class Meta:
        model = WellnessTip
        fields = ['id', 'icon', 'title', 'description', 'order', 'is_active']

class EducationalResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalResource
        fields = ['id', 'icon', 'title', 'description', 'button_text', 
                 'button_action', 'color', 'is_coming_soon', 'order', 'is_active']

class EmergencyContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergencyContact
        fields = ['id', 'title', 'contact', 'description', 'action', 'order', 'is_active']

class MissionVisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MissionVision
        fields = ['mission_badge', 'mission_title', 'mission_description', 
                 'vision_badge', 'vision_title', 'vision_description', 'is_active']

class WhoWeServeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhoWeServe
        fields = ['title', 'description', 'items', 'is_active']

class AppointmentSerializer(serializers.ModelSerializer):
    service_name = serializers.CharField(source='service.title', read_only=True)
    counselor_name = serializers.CharField(source='counselor.name', read_only=True)
    
    class Meta:
        model = Appointment
        fields = ['id', 'name', 'email', 'phone', 'preferred_date', 
                 'preferred_time', 'preferred_contact_method', 'service', 
                 'service_name', 'counselor', 'counselor_name', 'message', 
                 'status', 'is_urgent', 'created_at', 'updated_at']
        read_only_fields = ['status', 'created_at', 'updated_at']

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['id', 'name', 'email', 'phone', 'subject', 'message', 
                 'is_read', 'is_replied', 'created_at']
        read_only_fields = ['is_read', 'is_replied', 'created_at']

class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = ['site_name', 'site_description', 'contact_email', 'contact_phone',
                 'whatsapp_number', 'address', 'google_maps_url',
                 'facebook_url', 'twitter_url', 'instagram_url', 'linkedin_url',
                 'youtube_url', 'tiktok_url', 'working_hours', 'footer_text',
                 'logo_url', 'favicon_url', 'primary_color', 'secondary_color',
                 'accent_color', 'google_analytics_id']

class TherapeuticApproachSerializer(serializers.ModelSerializer):
    class Meta:
        model = TherapeuticApproach
        fields = ['id', 'icon', 'title', 'description', 'long_description',
                 'image_url', 'is_featured', 'order', 'is_active']

class NewsletterSubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterSubscriber
        fields = ['id', 'email', 'name', 'is_active', 'subscribed_date']
        read_only_fields = ['subscribed_date']

class PageSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageSection
        fields = ['id', 'page', 'section_name', 'title', 'subtitle', 
                 'description', 'content', 'background_type', 'background_value',
                 'text_color', 'order', 'is_active']