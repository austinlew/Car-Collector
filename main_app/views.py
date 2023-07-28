from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Car, Upgrade
from .forms import ShowForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cars_index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', {
        'cars': cars
    })

def cars_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    id_list = car.upgrades.all().values_list('id')
    upgrades_car_doesnt_have = Upgrade.objects.exclude(id__in=id_list)
    show_form = ShowForm()
    return render(request, 'cars/detail.html', {
        'car': car, 'show_form': show_form,
        'upgrades': upgrades_car_doesnt_have
    })

class CarCreate(CreateView):
    model = Car
    fields = '__all__'
    success_url = '/cars'

class CarUpdate(UpdateView):
    model = Car
    fields = ['model', 'year', 'color', 'description']

class CarDelete(DeleteView):
    model = Car
    success_url = '/cars'

def add_show(request, car_id):
    form = ShowForm(request.POST)
    if form.is_valid():
        new_show = form.save(commit=False)
        new_show.car_id = car_id
        new_show.save()
    return redirect('detail', car_id=car_id)

class UpgradeList(ListView):
    model = Upgrade

class UpgradeDetail(DetailView):
    model = Upgrade

class UpgradeCreate(CreateView):
    model = Upgrade
    fields = '__all__'
    success_url = '/upgrades'

class UpgradeUpdate(UpdateView):
  model = Upgrade
  fields = ['item', 'brand']

class UpgradeDelete(DeleteView):
  model = Upgrade
  success_url = '/upgrades'

def assoc_upgrade(request, car_id, upgrade_id):
    Car.objects.get(id=car_id).upgrades.add(upgrade_id)
    return redirect('detail', car_id=car_id)

def unassoc_upgrade(request, car_id, upgrade_id):
    Car.objects.get(id=car_id).upgrades.remove(upgrade_id)
    return redirect('detail', car_id=car_id)