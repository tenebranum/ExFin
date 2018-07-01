from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.utils.translation import ugettext_lazy as _

from content.models import MenuAboutItem, StaticPage, AboutUsStatic
from communication.models import Response


def about(request):
    menu_about = MenuAboutItem.objects.all()
    static_pages = StaticPage.objects.all()
    about = AboutUsStatic.get_solo()
    return render(request, 'about.html', {'menu_about':menu_about,
    									  'static_pages':static_pages,
    									  'about':about})

