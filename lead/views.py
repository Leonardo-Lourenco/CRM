from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import AddLeadForm

# Create your views here.
@login_required
def add_lead(request):

    if request.method == 'POST':
        form = AddLeadForm(request.POST)

        if form.is_valid():
            lead = form.save(commit=False)
            lead.created_by = request.user
            lead.save()

    form = AddLeadForm()

    return render(request, 'lead/add_lead.html', {

        'form': form

    })