from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag')
    if not bag:
        messages.error(request, "There's nothing in your bag!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Jv5j8DCCRtNzyqm2EPWyMDp92MInKO01GEQ95avUQVOd9NEFeCrSricKfuDRtYp6pkN3Bnq1nV0BB8TOMCBBLYb00RJk49n28',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
