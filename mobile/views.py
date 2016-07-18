from django.views.generic.list import ListView
from .models import Mobile


class IndexView(ListView):

    template_url = "/mobile/index.html"
    model = Mobile
