from django.conf.urls import url

from .views import ( add_to_bag )

app_name = 'shopping_cart'

urlpatterns = [
    url(r'^add-to-bag/(?P<item_id>[-\w]+)/$', add_to_bag, name="add_to_bag"),
]