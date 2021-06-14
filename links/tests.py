from django.shortcuts import get_object_or_404
from django.test import TestCase
from django.urls import reverse

from links.models import Link
from links.views import hash_link


def create_short_link(full_link):
    """Функция создания короткой ссылки для теста"""
    link = Link.objects.create(
        full_link=full_link,
        short_link=hash_link(full_link=full_link)
    )
    link.save()
    return link


class LinkModelTests(TestCase):

    def test_hash_link(self):
        """Хеширование ссылки, проверка на None"""
        tiny_link = hash_link("https://stackoverflow.com/company")
        self.assertIsNotNone(tiny_link)

    def test_increase_redirects(self):
        """Проверка на редиректы"""
        link = create_short_link(
            "https://stackoverflow.com/company")
        link.redirects += 1
        link.save()
        self.assertIs(link.redirects, 1)


class LinkViewTests(TestCase):

    def test_create_link(self):
        """Проверка, что объект Response и содержит short_link"""
        link = create_short_link(
            "https://stackoverflow.com")
        url = reverse('links:index')
        response = self.client.get(url)
        self.assertContains(response, link.short_link)

    def test_delete_link(self):
        """Проверка на удаление ссылки"""
        link = create_short_link(
            "https://stackoverflow.com")
        link.delete()
        url = reverse('links:index')
        response = self.client.get(url)
        self.assertNotContains(response, link.full_link)

    def test_nonexistent_link(self):
        """Проверка на несуществующую ссылку"""
        url = reverse('links:index')
        response = self.client.get(url)
        full_link = "https://kpfu.ru/"
        self.assertNotContains(response, full_link)

    def test_view_link(self):
        """Проверка на перенаправление на оригинальную ссылку, при нажатии короткой ссылки"""
        link = create_short_link(
            "https://kpfu.ru/")
        url = reverse('links:view', args=(link.short_link,))
        response = self.client.get(url)
        self.assertRedirects(response,
                             link.full_link,
                             status_code=302,
                             target_status_code=200,
                             msg_prefix='',
                             fetch_redirect_response=False)

    def test_test_increase_follow_quantity_after_open_link(self):
        """Проверка на редиректы после открытия ссылки"""
        link = create_short_link(
            "https://kpfu.com")
        url = reverse('links:view', args=(link.short_link,))
        self.client.get(url)
        updated_link = get_object_or_404(Link, short_link=link.short_link)
        self.assertIs(updated_link.redirects, link.redirects + 1)
