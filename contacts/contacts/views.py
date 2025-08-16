from django.shortcuts import render,redirect
from .models import Contact
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from django.db.models import Q
# Create your views here.

# def Home(request):
#     if request.user.is_authenticated:
#         contacts = request.user.contacts.all()
#         context = {"contacts":contacts}
#         return render(request,"contacts/home.html",context)
#     return redirect("login")

class Home(ListView):
    model = Contact
    template_name = "contacts/home.html"
    context_object_name = "contacts"
    ordering = ["-created_at"]
    def get_queryset(self):
        queryset = super().get_queryset().filter(user = self.request.user)
        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(Q(username__icontains=query)|
                                       Q(email__icontains = query) |
                                       Q(phone__icontains=query)   )
        return queryset

class AddContact(CreateView):
    model = Contact
    fields = ["username", 'email', 'phone']
    template_name = "contacts/add_contact.html"
    success_url = reverse_lazy("home") # redirect to home
    
    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super().form_valid(form)
    
    # Assign current user before validation
    def get_form(self, form_class=None):
       form = super().get_form(form_class)
       form.instance.user = self.request.user
       return form
    
class EditContact(UpdateView):
    model = Contact
    fields= ["username","email","phone"]
    template_name = "contacts/edit_contact.html"
    success_url = reverse_lazy("home") 
    
class DeleteContact(DeleteView):
    model = Contact
    success_url = reverse_lazy("home")