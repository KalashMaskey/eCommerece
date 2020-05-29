from django.http import HttpResponse
from django.shortcuts import  render,redirect
from .forms import ContactForm
from django.contrib.auth import authenticate, login, get_user_model

def home_page(request):
    # print(request.session.get('cart_id'))
    # request.session['cart_id']
    context = {
        "home": "Kindly Login",
        }
    if request.user.is_authenticated:
        context['premium_content'] = 'Richy'
        # context={'premium_content': 'Rich peoples'}
    return render(request, "home_page.html",context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contact",
        "content":"Contact Us",
        "form" : contact_form,
        "brand_view" : "New Brand from views.py"
    }

    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    if request.method == 'POST':
        print(request.POST.get('name'))
        print(request.POST.get('email'))

    return render(request, "contact/view.html", context)
