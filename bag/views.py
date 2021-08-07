from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404

from users.models import Profile
from products.models import Product
from bag.models import BagItem, Bag

# Create your views here.
@login_required()
def add_to_bag(request, **kwargs):
    user_profile = get_object_or_404(Profile, user=request.user)
    product = Product.objects.filter(id=kwargs.get('item_id', "")).first()

    if product in request.user.profile.products.all():
        messages.info(request, 'You already have this product')
        return redirect(reverse('products:product-list'))

    bag_item = BagItem.objects.get_or_create(product=product)
    user_bag = Bag.objects.get_or_create(owner=user_profile, is_added=False)
    user_bag.items.add(bag_item)

    messages.info(request, "Item added to bag!!")
    return redirect(reverse('products:product-list'))
    