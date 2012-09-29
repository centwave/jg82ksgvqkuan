#guestbook/views.py
from django.shortcuts import render_to_response
from gbook.models import Entry
from gbook.forms import EntryForm

def guestbook(request):
	form=EntryForm(request.POST)
	if form.is_valid():
		form.save()
	entries=Entry.objects.all().order_by("-date")
	templates={'form': form, 'entries': entries}
	return render_to_response("gbook.html", templates)