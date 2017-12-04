from django.conf.urls import url
from django.views.generic.base import TemplateView

from g1_helper import views

app_name = 'g1_helper'
urlpatterns = [
    url(r'g1file/$', views.G1FileCreate.as_view(), name='g1file'),
    url(r'g1file/add/$', views.G1FileCreate.as_view(), name='g1file-add'),
    url(r'g1file/(?P<pk>[0-9]+)/update/$', views.G1FileUpdate.as_view(), name='g1file-update'),
    url(r'g1file/(?P<pk>[0-9]+)/delete/$', views.G1FileDelete.as_view(), name='g1file-delete'),
    url(r'postingtypes/',
        views.G1PostingTypesView.as_view(),
        name='posting_types'),
    url(r'tradeuploaderrormessages/',
        views.G1TradeUploadErrorMessagesView.as_view(),
        name='trade_upload_error_messages'),
    url(r'settlementuploaderrormessages/',
        views.G1SettlementUploadErrorMessagesView.as_view(),
        name='settlement_upload_error_messages'),
    url(r'whatissecuritieslending/',
        TemplateView.as_view(template_name='g1_helper\what_is_securities_lending.html'),
        name='what_is_securities_lending'),
    url(r'parse_gci/', views.parse_gci,
        name='parse_gci'),
    url(r'',
        TemplateView.as_view(template_name='g1_helper\home.html'),
        name='home'),
]