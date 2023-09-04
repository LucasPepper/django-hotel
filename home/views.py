from django.shortcuts import render

from .forms import ContatoForm

from django.contrib import messages

# Create your views here.

def index(request):

    return render(request, 'index.html')

def quartos(request):

    num_quartos_casal_suite = 6
    num_quartos_casal = 5
    num_quartos_triplo = 4

    # Quartos Disponíveis

    context = {
        'num_quartos_casal': num_quartos_casal,
        'num_quartos_casal_suite': num_quartos_casal_suite,
        'num_quartos_triplo': num_quartos_triplo,
    }

    return render(request, 'quartos.html', context = context)

def reserva(request):
    return render(request, 'reserva.html')

def contato(request, *args, **kwargs):

    form = ContatoForm()
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():

            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']
            
            print('Mensagem Enviada')
            messages.success(request, 'E-mail enviado com sucesso')
            print(f'Nome: {nome}')
            print(f'E-mail: {email}')
            print(f'Assunto: {assunto}')
            print(f'Mensagem: {mensagem}')
            
        else:
            messages.error(request,'Erro ao enviar e-mail')

    return render(request, 'contact.html', {'form': form})