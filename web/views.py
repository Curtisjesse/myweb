from django.shortcuts import render
from .models import Furniture, Blog , Services, Teams, Testimonials, Contact_info

# Create your views here.
def index(request):
    testimonials = Testimonials.objects.all()
    blogs = Blog.objects.all().order_by('?')[:3]
    services = Services.objects.all().order_by('?')[:4]
    furnitures = Furniture.objects.all().order_by('?')[:3]
    context = {
        'furnitures' : furnitures , 
        "nav" : 'home',
        'services' : services, 
        'blogs': blogs , 
        'testimonials': testimonials }
    return render(request, "index.html", context)

def about(request):
    testimonials = Testimonials.objects.all()
    services = Services.objects.all().order_by('?')[:4]
    teams = Teams.objects.all().order_by('?')[:4]
    return render(request, "about.html",{'teams': teams, 'services':services,'nav':'about', 'testimonials': testimonials})


def blog(request):
    testimonials = Testimonials.objects.all()
    blogs = Blog.objects.all().order_by('?')
    return render(request, "blog.html", {'blogs' : blogs , 'testimonials': testimonials})

def item(request, id):
    product = Furniture.objects.get(id=id)
    return render(request, 'card.html', {'product':product})
    
def cart(request):
    return render(request, "cart.html")


def checkout(request):
    return render(request, "checkout.html")

def login(request):
    return render(request, "login.html")

def contact(request):
    # contact_info = Contact_info.object.all()
    return render(request, "contact.html")
    

def services(request):
    testimonials = Testimonials.objects.all()
    services = Services.objects.all()
    furnitures = Furniture.objects.all()[:3]
    
    return render(request, "services.html", {'furnitures' : furnitures,'services' : services, 'testimonials': testimonials } )

def shop(request):
    
     furnitures = Furniture.objects.all().order_by('?')[:12]
     return render(request, "shop.html", {'furnitures' : furnitures,'nav':'shop' })

def thankyou(request):
    return render(request, "thankyou.html")

def terms(request):
    return render(request, "terms.html")


