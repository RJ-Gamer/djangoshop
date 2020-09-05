from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Address
from .forms import AddressForm
import logging

logger = logging.getLogger(__name__)

# Create your views here.
@login_required(login_url=('user:login'))
def address_list(request):
    addresses = Address.objects.filter(user=request.user)
    context = {'addresses': addresses}
    return render(request, 'address/address_list.html', context)

@login_required(login_url=('user:login'))
def address_create(request):
    form = AddressForm()
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            logger.info('{} created a new address'.format(request.user))
            return redirect('address:address_list')
    context = {'form': form}
    return render(request, 'address/address_create.html', context)

@login_required(login_url=('user:login'))
def address_update(request, id):
    address = get_object_or_404(Address, id=id)
    form = AddressForm(instance=address)
    if request.method == 'POST':
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            logger.info('{} updated their address with id: {}'.format(request.user, address.id))
            return redirect('address:address_list')
    context = {'form': form}
    return render(request, 'address/address_update.html', context)

@login_required(login_url=('user:login'))
def address_delete(request, id):
    address = get_object_or_404(Address, id=id)
    if request.method == 'POST':
        address.delete()
        logger.info('{} has deleted his address with Address: {}'.format(request.user, address))
        return redirect('address:address_list')
    context = {'address': address}
    return render(request, 'address/address_delete.html', context)
