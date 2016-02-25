from django.views import generic
from django.utils import timezone
import datetime

# Create your views here.
from .models import Exhibit, Author


class IndexView(generic.ListView):
    template_name = 'exhibit/index.html'
    context_object_name = 'latest_added_exhibit'

    def get_queryset(self):
        return Exhibit.objects.filter(pub_date__lte=datetime.date.today())


class DetailView(generic.DetailView):
    model = Exhibit
    template_name = 'exhibit/preview.html'

    def get_queryset(self):
        return Exhibit.objects.filter(pub_date__lte=timezone.now())