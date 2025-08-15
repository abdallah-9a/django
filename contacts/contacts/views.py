from django.shortcuts import render,redirect
from .models import Contact
from django.views.generic import CreateView, UpdateView, DeleteView
# Create your views here.

def Home(request):
    if request.user.is_authenticated:
        contacts = request.user.contacts.all()
        context = {"contacts":contacts}
        return render(request,"contacts/home.html",context)
    return redirect("login")


class AddContact(CreateView):
    model = Contact
    fields = ["username", 'email', 'phone']
    template_name = "contacts/add_contact.html"
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    