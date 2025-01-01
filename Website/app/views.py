from django.shortcuts import render,get_object_or_404,redirect
from .models import Blog,Events,Home,About,ContactForm,Wedding,Birthday,Haldi,Party,Subscription,Gallery
from .forms import blogForm,eventForm,homeForm,aboutForm,weddingForm,birthdayForm,haldiForm,partyForm
# Create your views here.

from django.contrib import messages

def HomeView(request):
    home = Home.objects.all()
    obj = Blog.objects.all()
    
    if request.method == 'POST':
        email = request.POST.get('email')
        
        if Subscription.objects.filter(email=email).exists():
            # Email already exists
            messages.error(request, "This email is already subscribed!")
        else:
            # Add the subscription
            subs = Subscription(email=email)
            subs.save()
            messages.success(request, "Subscription successful!")
    
    return render(request, 'home.html', {'obj': obj, 'home': home})


def AboutView(request):
    about = About.objects.all()
    return render(request,'About.html',{'about':about})


def GalleryView(request):
    obj = Gallery.objects.all()
    return render(request,'Gallery.html',{'obj':obj})


def WeddingView(request):
    obj = Wedding.objects.all()
    return render(request,'gallery/wedding.html',{'obj':obj})

def WeddingViewEdit(request):
 
    if request.method == 'POST':
        form = weddingForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('wedding')
    else:
        form = weddingForm()
    return render(request,'forms/wedding.html',{'form':form}) 

def WeddingDelete(request,id):
    obj = get_object_or_404(Wedding,id=id)
    obj.delete()
    return redirect('wedding')



def BirthdayView(request):
    obj = Birthday.objects.all()
    return render(request,'gallery/birthday.html',{'obj':obj})

def BirthdayViewEdit(request):
    if request.method == 'POST':
        form = birthdayForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('birthday')
    else:
        form = birthdayForm()
    return render(request,'forms/birthday.html',{'form':form}) 

def BirthdayDelete(request,id):
    obj = get_object_or_404(Birthday,id=id)
    obj.delete()
    return redirect('birthday')





def HaldiView(request):
    obj = Haldi.objects.all()
    return render(request,'gallery/haldi.html',{'obj':obj})

def HaldiViewEdit(request):
    if request.method == 'POST':
        form = haldiForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('haldi')
    else:
        form = haldiForm()
    return render(request,'forms/haldi.html',{'form':form}) 

def HaldiDelete(request,id):
    obj = get_object_or_404(Haldi,id=id)
    obj.delete()
    return redirect('haldi')





def PartyView(request):
    obj = Party.objects.all()
    return render(request,'gallery/party.html',{'obj':obj})

def PartyViewEdit(request):
    if request.method == 'POST':
        form = partyForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('party')
    else:
        form = partyForm()
    return render(request,'forms/party.html',{'form':form}) 

def PartyDelete(request,id):
    obj = get_object_or_404(Party,id=id)
    obj.delete()
    return redirect('party')



def Contact(request):
    if request.method == "POST":
        # Retrieve form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        phone = request.POST.get('phone')
        message = request.POST.get('msg')

        # Validate form fields
        if not name or not email or not subject or not message:
            messages.error(request, "Please fill in all required fields.")
        elif not phone or len(phone) != 10 or not phone.isdigit():
            messages.error(request, "Please enter a valid 10-digit phone number.")
        else:
            try:
                # Save the data to the database
                contact_entry = ContactForm(
                    name=name,
                    email=email,
                    subject=subject,
                    phone=phone if phone else None,  # Handle optional phone field
                    message=message
                )
                contact_entry.save()
                messages.success(request, "Your message has been sent successfully!")
                return redirect('contact')  # Replace with your success page or view name
            except Exception as e:
                messages.error(request, "An error occurred while submitting the form. Please try again.")
    
    return render(request, 'Contact.html')
    
    

def BlogView(request):
    obj = Blog.objects.all()
    return render(request,'Blog.html',{'obj':obj})

def EventView(request):
    obj = Events.objects.all()
    return  render(request,'Events.html',{'obj':obj})
 
 
def HomeViewEdit(request,id):
    home = get_object_or_404(Home,id=id)
    if request.method == 'POST':
        form = homeForm(request.POST,request.FILES,instance=home)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = homeForm(instance=home)
    return render(request,'forms/home_form.html',{'form':form}) 
       
def AboutViewEdit(request,id):
    about = get_object_or_404(About,id=id)
    if request.method == 'POST':
        form = aboutForm(request.POST,request.FILES,instance=about)
        if form.is_valid():
            form.save()
            return redirect('about')
    else:
        form = aboutForm(instance=about)
    return render(request,'forms/about_form.html',{'form':form})        
    
    

    
def BlogViewCreate(request):
    if request.method == 'POST':
        form  = blogForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog')
    else:
        form = blogForm()
    return render(request,'forms/blog_form.html',{'form':form}) 
  
  
  
def EventViewCreate(request):
    if request.method == 'POST':
        form  = eventForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('event')
    else:
        form = eventForm()
    return render(request,'forms/event_form.html',{'form':form})   



def BlogDelete(request,id):
    blog = get_object_or_404(Blog,id=id)
    blog.delete()
    return redirect('blog')
 
def EventDelete(request,id):
    blog = get_object_or_404(Events,id=id)
    blog.delete()
    return redirect('event') 
                
                
                
def AdminView(request):
    contact = ContactForm.objects.all()
    subs = Subscription.objects.all()
    return render(request,'admin.html',{'con':contact,'subs':subs})                



def contactDelete(request,id):
    obj = get_object_or_404(ContactForm,id=id)
    obj.delete()
    return redirect('adminProfile')

def SubsDelete(request,id):
    obj = get_object_or_404(Subscription,id=id)
    obj.delete()
    return redirect('adminProfile')