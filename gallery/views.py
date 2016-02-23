from django.views import generic
from django.utils import timezone

# Create your views here.
from .models import Image, Exhibit


class IndexView(generic.ListView):
    template_name = 'gallery/index.html'
    context_object_name = 'latest_added_image'

    def get_queryset(self):
        return Exhibit.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:9]


class DetailView(generic.DetailView):
    model = Image
    template_name = 'gallery/preview.html'