from django.shortcuts import render, redirect, get_object_or_404
from .models import Medication
from .forms import MedsForm
from django.urls import reverse_lazy
from django.views import View

# Create your views here.

def main(request):
    return render(request, 'main.html')


class MedsList(View):
    def get(self, request):
        meds = Medication.objects.all()
        return render(request, 'meds/meds_list.html', {'meds': meds})


class MedDetail(View):
    def get(self, request, pk):
        med = Medication.objects.get(id=pk)
        return render(request, 'meds/med_detail.html', {'med': med})


class MedCreate(View):
    def get(self, request):
        form = MedsForm()
        return render(request, 'meds/med_create.html', {'form': form})

    def post(self, request):
        form = MedsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('meds-list')
        return render(request, 'meds/med_create.html', {'form': form})


class MedUpdate(View):
    def get(self, request, pk):
        med = Medication.objects.get(id=pk)
        form = MedsForm(instance=med)
        return render(request, 'meds/med_update.html', {'form': form, 'med': med})

    def post(self, request, pk):
        med = Medication.objects.get(id=pk)
        form = MedsForm(request.POST, request.FILES, instance=med)
        if form.is_valid():
            form.save()
            return redirect('med-detail', pk=pk)
        return render(request, 'meds/med_update.html', {'form': form, 'med': med})


class MedDelete(View):
    def get(self, request, pk):
        med = get_object_or_404(Medication, id=pk)
        return render(request, 'meds/med_delete.html', {'med': med})

    def post(self, request, pk):
        med = get_object_or_404(Medication, id=pk)
        med.delete()
        return redirect('meds-list')
