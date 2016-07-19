from django.views.generic.list import ListView
from .models import Mobile


class IndexView(ListView):
    model = Mobile
