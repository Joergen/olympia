from django.conf import settings
from django.conf.urls import patterns, url
from django.http import HttpResponsePermanentRedirect as perma_redirect
from django.views.generic.base import TemplateView

from amo.urlresolvers import reverse

from . import views


urlpatterns = patterns(
    '',
    url('^about$',
        TemplateView.as_view(template_name='pages/about.lhtml'),
        name='pages.about'),
    url('^credits$', views.credits, name='pages.credits'),
    url('^faq$',
        TemplateView.as_view(template_name='pages/faq.html'),
        name='pages.faq'),
    url('^google1f3e37b7351799a5.html$',
        TemplateView.as_view(
            template_name='pages/google_webmaster_verification.html')),

    url('^compatibility_firstrun$',
        TemplateView.as_view(template_name='pages/acr_firstrun.html'),
        name='pages.acr_firstrun'),
    url('^developer_faq$',
        TemplateView.as_view(template_name='pages/dev_faq.html'),
        name='pages.dev_faq'),
    url('^review_guide$',
        TemplateView.as_view(template_name='pages/review_guide.html'),
        name='pages.review_guide'),

    url('^pages/compatibility_firstrun$',
        lambda r: perma_redirect(reverse('pages.acr_firstrun'))),
    url('^pages/developer_faq$',
        lambda r: perma_redirect(reverse('pages.dev_faq'))),
    url('^pages/review_guide$',
        lambda r: perma_redirect(reverse('pages.review_guide'))),
    url('^pages/developer_agreement$',
        lambda r: perma_redirect(reverse('devhub.docs',
                                         args=['policies/agreement']))),
    url('^pages/validation$',
        lambda r: perma_redirect(settings.VALIDATION_FAQ_URL)),

    url('^sunbird$',
        TemplateView.as_view(template_name='pages/sunbird.html'),
        name='pages.sunbird'),
    url('^sunbird/', lambda r: perma_redirect(reverse('pages.sunbird'))),
)
