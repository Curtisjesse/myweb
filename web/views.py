from django.shortcuts import render
from .models import Furniture, Blog , Services, Teams, Testimonials

# Create your views here.
def index(request):
    testimonials = Testimonials.objects.all()
    blogs = Blog.objects.all().order_by('?')[:3]
    services = Services.objects.all().order_by('?')[:4]
    furnitures = Furniture.objects.all().order_by('?')[:3]
    
    return render(request, "index.html", {'furnitures' : furnitures , 'services' : services, 'blogs': blogs , 'testimonials': testimonials })

def about(request):
    testimonials = Testimonials.objects.all()
    services = Services.objects.all().order_by('?')[:4]
    teams = Teams.objects.all().order_by('?')[:4]
    return render(request, "about.html",{'teams': teams, 'services':services, 'testimonials': testimonials})


def blog(request):
    testimonials = Testimonials.objects.all()
    blogs = Blog.objects.all().order_by('?')
    return render(request, "blog.html", {'blogs' : blogs , 'testimonials': testimonials})


def cart(request):
    return render(request, "cart.html")


def checkout(request):
    return render(request, "checkout.html")

def contact(request):
    return render(request, "contact.html")

def services(request):
    testimonials = Testimonials.objects.all()
    services = Services.objects.all()
    furnitures = Furniture.objects.all()[:3]
    
    return render(request, "services.html", {'furnitures' : furnitures,'services' : services, 'testimonials': testimonials } )

def shop(request):
    
     furnitures = Furniture.objects.all().order_by('?')[:12]
     return render(request, "shop.html", {'furnitures' : furnitures })

def thankyou(request):
    return render(request, "thankyou.html")


