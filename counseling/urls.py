# counseling/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework.authtoken.views import obtain_auth_token

# Create the router
router = DefaultRouter()

# Register all ViewSets
router.register(r'services', views.ServiceViewSet)
router.register(r'hero-slides', views.HeroSliderViewSet)
router.register(r'features', views.FeatureViewSet)
router.register(r'testimonials', views.TestimonialViewSet)
router.register(r'stats', views.StatViewSet)
router.register(r'team-members', views.TeamMemberViewSet)
router.register(r'faqs', views.FAQViewSet)
router.register(r'blog-posts', views.BlogPostViewSet)
router.register(r'events', views.EventViewSet)
router.register(r'partners', views.PartnerViewSet)
router.register(r'ctas', views.CallToActionViewSet)
router.register(r'approaches', views.TherapeuticApproachViewSet)
router.register(r'support-options', views.SupportOptionViewSet)
router.register(r'wellness-tips', views.WellnessTipViewSet)
router.register(r'educational-resources', views.EducationalResourceViewSet)
router.register(r'emergency-contacts', views.EmergencyContactViewSet)
router.register(r'values', views.ValueViewSet)
router.register(r'mission-vision', views.MissionVisionViewSet)
router.register(r'who-we-serve', views.WhoWeServeViewSet)
router.register(r'appointments', views.AppointmentViewSet)
router.register(r'contact-messages', views.ContactMessageViewSet)
router.register(r'newsletter-subscribers', views.NewsletterSubscriberViewSet)
router.register(r'page-sections', views.PageSectionViewSet)
router.register(r'site-settings', views.SiteSettingsViewSet)

urlpatterns = [
    # API endpoints
    path('', include(router.urls)),
    
    # Page-specific endpoints (get all data for a page in one request)
    path('homepage/', views.homepage_data, name='homepage-data'),
    path('resources/', views.resources_data, name='resources-data'),
    path('about/', views.about_data, name='about-data'),
    path('services/', views.services_data, name='services-data'),
    path('contact/', views.contact_data, name='contact-data'),
    #path('api/auth/login/', obtain_auth_token, name='api_token_auth'),
    path('auth/login/', obtain_auth_token, name='api_token_auth'),
]

# API Endpoints Summary:
# 
# Page-specific endpoints (GET only):
# /api/homepage/ - All homepage content
# /api/resources/ - All resources page content
# /api/about/ - All about page content
# /api/services/ - All services page content
# /api/contact/ - All contact page content
#
# CRUD endpoints (GET, POST, PUT, DELETE):
# /api/services/ - Service management
# /api/hero-slides/ - Hero slider management
# /api/features/ - Feature management
# /api/testimonials/ - Testimonial management
# /api/stats/ - Statistics management
# /api/team-members/ - Team member management
# /api/faqs/ - FAQ management
# /api/blog-posts/ - Blog post management
# /api/events/ - Event management
# /api/partners/ - Partner management
# /api/ctas/ - Call to action management
# /api/approaches/ - Therapeutic approach management
# /api/support-options/ - Support option management
# /api/wellness-tips/ - Wellness tip management
# /api/educational-resources/ - Educational resource management
# /api/emergency-contacts/ - Emergency contact management
# /api/values/ - Value management
# /api/mission-vision/ - Mission & vision management
# /api/who-we-serve/ - Who we serve management
# /api/appointments/ - Appointment booking (POST public, rest admin)
# /api/contact-messages/ - Contact messages (POST public, rest admin)
# /api/newsletter-subscribers/ - Newsletter subscription (POST public, rest admin)
# /api/page-sections/ - Dynamic page sections