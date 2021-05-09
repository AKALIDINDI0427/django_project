"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import about_page, portfolio_page, ContactPage, thankyou_page


# home_page, new_home_page, HForm, Calendar, Sale, ContactUs, Testimonials, QForm, about_page

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', home_page)  # home page
    # path('', new_home_page)
    # path('', home_form)
    # path('', HForm.as_view()),
    path('', portfolio_page),
    path('AboutMe/', about_page),
    # path('Contact/', Contact.as_view()),
    # path('Contact/', contactform),
    # path('Contact/', HForm.as_view()),
    # path('Sale/', Sale),
    # path('ContactUs/', ContactUs),
    # path('Testimonials', Testimonials),
    path('Contact/', ContactPage.as_view(), name='contact'),
    path('Contact/ThankYou/', thankyou_page)
]
