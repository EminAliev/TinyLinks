from django.views.generic import ListView

from links.models import Link


class LinkListView(ListView):
    template_name = 'index.html'
    context_object_name = 'links_list'

    def get_queryset(self):
        return Link.objects.filter().order_by('-redirects')
