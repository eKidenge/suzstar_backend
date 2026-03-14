# counseling/views.py

from rest_framework import viewsets, status
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser
from django.core.mail import send_mail
from django.conf import settings
from .models import (
    Service, Value, HeroSection, HeroSlider, Feature, 
    Testimonial, Appointment, ContactMessage, SiteSettings, 
    TherapeuticApproach, SupportOption, WellnessTip, 
    EducationalResource, EmergencyContact, MissionVision, 
    WhoWeServe, Stat, TeamMember, FAQ, BlogPost, Event,
    Partner, CallToAction, NewsletterSubscriber, PageSection
)
from .serializers import (
    ServiceSerializer, ValueSerializer, HeroSectionSerializer, HeroSliderSerializer,
    FeatureSerializer, TestimonialSerializer, AppointmentSerializer,
    ContactMessageSerializer, SiteSettingsSerializer, 
    TherapeuticApproachSerializer, SupportOptionSerializer, 
    WellnessTipSerializer, EducationalResourceSerializer, 
    EmergencyContactSerializer, MissionVisionSerializer, 
    WhoWeServeSerializer, StatSerializer, TeamMemberSerializer,
    FAQSerializer, BlogPostSerializer, EventSerializer,
    PartnerSerializer, CallToActionSerializer, 
    NewsletterSubscriberSerializer, PageSectionSerializer
)

# Homepage endpoints
@api_view(['GET'])
def homepage_data(request):
    """Get all data needed for the homepage"""
    hero = HeroSection.objects.filter(is_active=True).first()
    hero_slides = HeroSlider.objects.filter(is_active=True)
    settings = SiteSettings.objects.first()
    featured_services = Service.objects.filter(is_active=True, is_featured=True)
    featured_testimonials = Testimonial.objects.filter(is_active=True, is_featured=True)
    stats = Stat.objects.filter(is_active=True)
    team_members = TeamMember.objects.filter(is_active=True, is_featured=True)
    faqs = FAQ.objects.filter(is_active=True)[:6]
    partners = Partner.objects.filter(is_active=True)
    
    data = {
        'hero': HeroSectionSerializer(hero).data if hero else None,
        'hero_slides': HeroSliderSerializer(hero_slides, many=True).data,
        'services': ServiceSerializer(Service.objects.filter(is_active=True), many=True).data,
        'featured_services': ServiceSerializer(featured_services, many=True).data,
        'values': ValueSerializer(Value.objects.filter(is_active=True), many=True).data,
        'features': FeatureSerializer(Feature.objects.filter(is_active=True), many=True).data,
        'testimonials': TestimonialSerializer(Testimonial.objects.filter(is_active=True), many=True).data,
        'featured_testimonials': TestimonialSerializer(featured_testimonials, many=True).data,
        'stats': StatSerializer(stats, many=True).data,
        'team_members': TeamMemberSerializer(team_members, many=True).data,
        'faqs': FAQSerializer(faqs, many=True).data,
        'partners': PartnerSerializer(partners, many=True).data,
        'settings': SiteSettingsSerializer(settings).data if settings else None,
    }
    return Response(data)

# Resources page endpoints
@api_view(['GET'])
def resources_data(request):
    """Get all data needed for the resources page"""
    data = {
        'supportOptions': SupportOptionSerializer(SupportOption.objects.filter(is_active=True), many=True).data,
        'wellnessTips': WellnessTipSerializer(WellnessTip.objects.filter(is_active=True), many=True).data,
        'educationalResources': EducationalResourceSerializer(EducationalResource.objects.filter(is_active=True), many=True).data,
        'emergencyContacts': EmergencyContactSerializer(EmergencyContact.objects.filter(is_active=True), many=True).data,
        'blogPosts': BlogPostSerializer(BlogPost.objects.filter(is_active=True)[:6], many=True).data,
        'events': EventSerializer(Event.objects.filter(is_active=True, start_date__gte=timezone.now())[:6], many=True).data,
        'faqs': FAQSerializer(FAQ.objects.filter(is_active=True), many=True).data,
    }
    return Response(data)

# About page endpoints
@api_view(['GET'])
def about_data(request):
    """Get all data needed for the about page"""
    mission_vision = MissionVision.objects.filter(is_active=True).first()
    who_we_serve = WhoWeServe.objects.filter(is_active=True).first()
    
    data = {
        'mission_vision': MissionVisionSerializer(mission_vision).data if mission_vision else None,
        'values': ValueSerializer(Value.objects.filter(is_active=True), many=True).data,
        'who_we_serve': WhoWeServeSerializer(who_we_serve).data if who_we_serve else None,
        'stats': StatSerializer(Stat.objects.filter(is_active=True), many=True).data,
        'team_members': TeamMemberSerializer(TeamMember.objects.filter(is_active=True), many=True).data,
        'testimonials': TestimonialSerializer(Testimonial.objects.filter(is_active=True), many=True).data,
    }
    return Response(data)

# Services page endpoints
@api_view(['GET'])
def services_data(request):
    """Get all data needed for the services page"""
    data = {
        'services': ServiceSerializer(Service.objects.filter(is_active=True), many=True).data,
        'therapeutic_approaches': TherapeuticApproachSerializer(TherapeuticApproach.objects.filter(is_active=True), many=True).data,
        'faqs': FAQSerializer(FAQ.objects.filter(is_active=True, category='services')[:6], many=True).data,
        'testimonials': TestimonialSerializer(Testimonial.objects.filter(is_active=True)[:6], many=True).data,
    }
    return Response(data)

# Contact page endpoints
@api_view(['GET'])
def contact_data(request):
    """Get all data needed for the contact page"""
    settings = SiteSettings.objects.first()
    faqs = FAQ.objects.filter(is_active=True, category='contact')[:6]
    
    data = {
        'settings': SiteSettingsSerializer(settings).data if settings else None,
        'faqs': FAQSerializer(faqs, many=True).data,
        'support_options': SupportOptionSerializer(SupportOption.objects.filter(is_active=True), many=True).data,
    }
    return Response(data)

# ViewSets for CRUD operations
class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    
    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            return [AllowAny()]
        return [IsAdminUser()]

class HeroSliderViewSet(viewsets.ModelViewSet):
    queryset = HeroSlider.objects.all()
    serializer_class = HeroSliderSerializer
    
    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            return [AllowAny()]
        return [IsAdminUser()]

class FeatureViewSet(viewsets.ModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
    
    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            return [AllowAny()]
        return [IsAdminUser()]

class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    
    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            return [AllowAny()]
        return [IsAdminUser()]

class StatViewSet(viewsets.ModelViewSet):
    queryset = Stat.objects.all()
    serializer_class = StatSerializer
    
    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            return [AllowAny()]
        return [IsAdminUser()]

class TeamMemberViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
    
    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            return [AllowAny()]
        return [IsAdminUser()]

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    
    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            return [AllowAny()]
        return [IsAdminUser()]

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    
    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            return [AllowAny()]
        return [IsAdminUser()]

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            return [AllowAny()]
        return [IsAdminUser()]

class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    
    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            return [AllowAny()]
        return [IsAdminUser()]

class CallToActionViewSet(viewsets.ModelViewSet):
    queryset = CallToAction.objects.all()
    serializer_class = CallToActionSerializer
    
    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            return [AllowAny()]
        return [IsAdminUser()]

class TherapeuticApproachViewSet(viewsets.ModelViewSet):
    queryset = TherapeuticApproach.objects.all()
    serializer_class = TherapeuticApproachSerializer
    
    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            return [AllowAny()]
        return [IsAdminUser()]

class SupportOptionViewSet(viewsets.ModelViewSet):
    queryset = SupportOption.objects.all()
    serializer_class = SupportOptionSerializer
    
    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            return [AllowAny()]
        return [IsAdminUser()]

class WellnessTipViewSet(viewsets.ModelViewSet):
    queryset = WellnessTip.objects.all()
    serializer_class = WellnessTipSerializer
    
    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            return [AllowAny()]
        return [IsAdminUser()]

class EducationalResourceViewSet(viewsets.ModelViewSet):
    queryset = EducationalResource.objects.all()
    serializer_class = EducationalResourceSerializer
    
    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            return [AllowAny()]
        return [IsAdminUser()]

class EmergencyContactViewSet(viewsets.ModelViewSet):
    queryset = EmergencyContact.objects.all()
    serializer_class = EmergencyContactSerializer
    
    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            return [AllowAny()]
        return [IsAdminUser()]

class ValueViewSet(viewsets.ModelViewSet):
    queryset = Value.objects.all()
    serializer_class = ValueSerializer
    
    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            return [AllowAny()]
        return [IsAdminUser()]

class MissionVisionViewSet(viewsets.ModelViewSet):
    queryset = MissionVision.objects.all()
    serializer_class = MissionVisionSerializer
    
    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            return [AllowAny()]
        return [IsAdminUser()]

class WhoWeServeViewSet(viewsets.ModelViewSet):
    queryset = WhoWeServe.objects.all()
    serializer_class = WhoWeServeSerializer
    
    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            return [AllowAny()]
        return [IsAdminUser()]

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    
    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [IsAdminUser()]
    
    def perform_create(self, serializer):
        appointment = serializer.save()
        self.send_appointment_email(appointment)
    
    def send_appointment_email(self, appointment):
        subject = f"New Appointment Request - {appointment.name}"
        message = f"""
        New appointment request:
        
        Name: {appointment.name}
        Email: {appointment.email}
        Phone: {appointment.phone}
        Date: {appointment.preferred_date}
        Time: {appointment.preferred_time}
        Service: {appointment.service.title if appointment.service else 'Not specified'}
        Counselor: {appointment.counselor.name if appointment.counselor else 'Not specified'}
        Contact Method: {appointment.preferred_contact_method}
        Urgent: {'Yes' if appointment.is_urgent else 'No'}
        Message: {appointment.message}
        """
        
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.CONTACT_EMAIL],
            fail_silently=True,
        )

class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    
    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [IsAdminUser()]
    
    def perform_create(self, serializer):
        contact = serializer.save()
        self.send_contact_email(contact)
    
    def send_contact_email(self, contact):
        subject = f"New Contact Message - {contact.subject}"
        message = f"""
        New contact message:
        
        Name: {contact.name}
        Email: {contact.email}
        Phone: {contact.phone}
        Subject: {contact.subject}
        Message: {contact.message}
        """
        
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.CONTACT_EMAIL],
            fail_silently=True,
        )

class NewsletterSubscriberViewSet(viewsets.ModelViewSet):
    queryset = NewsletterSubscriber.objects.all()
    serializer_class = NewsletterSubscriberSerializer
    
    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [IsAdminUser()]
    
    def perform_create(self, serializer):
        subscriber = serializer.save()
        # Send welcome email
        subject = "Welcome to Suzstar Counseling Newsletter"
        message = f"""
        Dear {subscriber.name or 'Subscriber'},
        
        Thank you for subscribing to our newsletter! You'll receive updates about our services, 
        mental health tips, and upcoming events.
        
        Best regards,
        Suzstar Counseling Team
        """
        
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [subscriber.email],
            fail_silently=True,
        )

class PageSectionViewSet(viewsets.ModelViewSet):
    queryset = PageSection.objects.all()
    serializer_class = PageSectionSerializer
    
    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            return [AllowAny()]
        return [IsAdminUser()]
    
class SiteSettingsViewSet(viewsets.ModelViewSet):
    queryset = SiteSettings.objects.all()
    serializer_class = SiteSettingsSerializer
    
    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            return [AllowAny()]
        return [IsAdminUser()]