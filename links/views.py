from django.views.generic import ListView, CreateView

from links.models import Link


class LinkListView(ListView):
    template_name = 'index.html'
    context_object_name = 'links_list'

    def get_queryset(self):
        return Link.objects.filter().order_by('-redirects')


class CreateLinkView(CreateView):
    template_name = 'create.html'
    model = Link
    fields = ['full_link']
