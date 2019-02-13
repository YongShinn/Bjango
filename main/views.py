from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def Main(request):
    return render(request, 'main/main.html')


@login_required
def retailer(request):
    return render(request, 'main/retailer.html')


def checkout(request):
    return render(request, 'main/checkout.html')


def payment(request):
    return render(request, 'main/payment.html')
