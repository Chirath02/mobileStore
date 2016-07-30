from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Mobile


class IndexView(ListView):
    model = Mobile


class MobileDetail(DetailView):
    model = Mobile
    template_name = 'mobile/mobile_details.html'

class AddMobileView(CreateView):
    model = Mobile
    fields = ['model_name', 'battery_capacity', 'quantity', 'back_cam', 'ram', 'price', 'img']

