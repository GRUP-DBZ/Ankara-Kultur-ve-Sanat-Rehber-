from django.shortcuts import render
from .models import Event

from django.shortcuts import render
from .models import Event

def home(request):
    q = request.GET.get("q", "")
    city = request.GET.get("city", "")
    date = request.GET.get("date", "")

    events = Event.objects.all()

    if q:
        events = events.filter(title__icontains=q)
    if city:
        events = events.filter(city__icontains=city)
    if date:
        events = events.filter(date__date=date)

    categories = [
        "Tiyatro", "Sinema", "Müzik", "Stand Up",
        "Konser", "Sergi", "Atölye", "Festival",
    ]

    context = {
        "featured_events": events[:6],
        "categories": categories,
    }
    return render(request, "events/home.html", context)
