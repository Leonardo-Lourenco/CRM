from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import AddLeadForm
from .models import Lead


#LISTAR OS LEADS
@login_required
def leads_list(request):
    leads = Lead.objects.filter(created_by=request.user)

    return render(request, 'lead/leads_list.html', {
        'leads': leads
    })


#DETAIL LEADS
@login_required
def leads_detail(request, pk):
    
    lead = Lead.objects.filter(created_by=request.user).get(pk=pk)

    return render(request, 'lead/leads_detail.html', {

        'lead': lead

    })





# ADD LEAD
@login_required
def add_lead(request):

    if request.method == 'POST':
        form = AddLeadForm(request.POST)

        if form.is_valid():
            lead = form.save(commit=False)
            lead.created_by = request.user
            lead.save()

            return redirect('dashboard')

    else:
        form = AddLeadForm()

    return render(request, 'lead/add_lead.html', {

        'form': form

    })