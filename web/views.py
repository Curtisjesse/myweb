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
    context= {
        'teams': teams, 
        'services':services,
        'nav':'about',
        'testimonials': testimonials }
    return render(request, "about.html",context)


def blog(request):
    testimonials = Testimonials.objects.all()
    blogs = Blog.objects.all().order_by('?')
    context =  {
        'blogs' : blogs ,
        'nav':'blog', 
        'testimonials': testimonials}
    return render(request, "blog.html",context)

def item(request, id):
    product = Furniture.objects.get(id=id)
    return render(request, 'card.html', {'product':product})
    
def cart(request):
    return render(request, "cart.html")


def checkout(request):
    return render(request, "checkout.html")



def register(request):
    return render(request, "register.html",{'nav':'register'})

def contact(request):
    # contact_info = Contact_info.object.all()
    context = {'nav':'contact' }
    return render(request, "contact.html", context)
    

def services(request):
    testimonials = Testimonials.objects.all()
    services = Services.objects.all()
    furnitures = Furniture.objects.all()[:3]
    context = {'furnitures' : furnitures,
               'nav':'services', 
               'services' : services, 
               'testimonials': testimonials }
    return render(request, "services.html", context )

def shop(request):
    
     furnitures = Furniture.objects.all().order_by('?')[:12]
     context = {'furnitures' : furnitures,
                'nav':'shop' }
     return render(request, "shop.html", context)

def thankyou(request):
    return render(request, "thankyou.html")

def terms(request):
    return render(request, "terms.html")


