import bcrypt as bcrypt
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView

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


class DetailLinkView(DetailView):
    model = Link
    pk_url_kwarg = 'link_id'
    template_name = 'detail.html'


def hash_link(full_link):
    short_link = bcrypt.hashpw(full_link.encode('utf-8'), bcrypt.gensalt())
    return short_link.decode("utf-8")[40:50].replace('/', '')


def create_short_link(request):
    full_link = request.POST['full_link']
    link = Link.objects.create(
        full_link=full_link,
        short_link=hash_link(full_link=full_link)
    )
    link.save()
    return HttpResponseRedirect(reverse('links:detail', args=(link.id,)))


def short_link_view(request, short_link):
    link = get_object_or_404(Link, tiny_link=short_link)
    full_link = link.full_link
    link.redirects += 1
    link.save()
    return HttpResponseRedirect(full_link)


def delete_link(request, link_id):
    link = get_object_or_404(Link, id=link_id)
    link.delete()
    return HttpResponseRedirect(reverse('links:index'))
