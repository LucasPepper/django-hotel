from django.shortcuts import render

# Create your views here.

def index(request):
    """View function for home page of site."""

    num_quartos_casal_suite = 6
    num_quartos_casal = 5
    num_quartos_triplo = 4

    # Quartos Disponíveis

    context = {
        'num_quartos_casal': num_quartos_casal,
        'num_quartos_casal_suite': num_quartos_casal_suite,
        'num_quartos_triplo': num_quartos_triplo,
    }

    return render(request, 'index.html', context=context)

def quartos(request):
    return render(request, 'quartos.html')

def reserva(request):
    return render(request, 'reserva.html')