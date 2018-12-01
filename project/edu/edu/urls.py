from django.conf.urls import url

from django_mongoengine import mongo_admin


urlpatterns = [
    url(r'^admin/', mongo_admin.site.urls),
]
