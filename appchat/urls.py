from django.conf.urls import url, include
import views

urlpatterns = [
    url(r'^$', views.hello),
    url(r'^common/$', views.CommonUrl.as_view()), # mapping for a class is different than function
    url(r'^chatboturl/?$', views.ChatBot.as_view()),
]

#app_token = EAAaKTD1rQl4BAAIA29amzI9YCy74ZCOxArwp1wbiAUsGZC6WAqRZAfFZBMbCd6hxW7eBtDrViB0klU4vmy0Ukx2RgfQToZByLy6BkYCKjzdXWIcQP449aZA7muZASID1BNaUWO7zPndtoel3OEcHQzCi0j9YWjakNVpSKaPkh1kDwZDZD
#used when our bot will send a message back to user