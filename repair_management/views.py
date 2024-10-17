from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Property, Appliance, Repairs, Investments
from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView

# the functions for the endpoints
# handle the logic of the app. they determine what data to display, process user inpt

#===========Property=========#


class PropertyList(LoginRequiredMixin, ListView):
    model = Property
    template_name = 'properties_list.html'
    context_object_name = 'properties'

    def get_queryset(self):
        return Property.objects.filter(user=self.request.user)
    
class PropertyDetailView(LoginRequiredMixin, DetailView):
    model = Property
    template_name = 'property_detail.html'
    context_object_name = 'property'

class PropertyCreateView(LoginRequiredMixin, CreateView):
    model = Property
    template_name = 'property_form.html'
    context_object_name = 'property'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
class PropertyDeleteView(LoginRequiredMixin, DeleteView):
    model = Property
    template_name = 'property_delete.html'
    success_url = reverse_lazy('property-list')
    
#=============Repairs========#
class RepairList(LoginRequiredMixin, ListView):
    model = Repairs
    template_name = 'repairs_list.html'
    context_object_name = 'repairs'


