from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Skill,Achievement,Project,Contact
from .forms import ContactForm
from django.contrib import messages

# Create your views here.
def home(request):
    skills=Skill.objects.all()
    achivements=Achievement.objects.all().order_by('-sno')
    projects=Project.objects.all()
    return render(request,'home.html',{'skills':skills,'achivements':achivements,'projects':projects})




def contactMe(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            comment = form.cleaned_data['comment']
            contact = Contact(name=name, email=email,
                              phone=phone,comment=comment)
            contact.save()
            messages.success(
                request, "Thank you for reaching out to me")
            return redirect('/')
        else:
            return render(request, 'contact.html', {'form': form})

    else:
        form = ContactForm()
        return render(request, 'contact.html', {'form': form})