from django.shortcuts import HttpResponse,render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Person
from .forms import PersonForm
# Create your views here.


@login_required
def ola(request):
    return render(request, 'html.html')


def lerDoBanco(nome):
    lista_nomes = [
        {'nome': 'Ana', 'idade': 20},
        {'nome': 'Pedro', 'idade': 25},
        {'nome': 'Joao', 'idade': 27},
    ]

    for pessoa in lista_nomes:
        if pessoa['nome'] == nome:
            return pessoa
    else:
            return {'nome': 'Não encontrado', 'idade': 0}

@login_required
def fname(request, nome):
    result = lerDoBanco(nome)
    if result['idade'] > 0:
        return HttpResponse('A pessoa foi encontrada, ela tem ' + str(result['idade'])+'anos')
    else:
        return HttpResponse('Pessoa não encontrada')

@login_required
def persons_list(request):
    person = Person.objects.all()
    return render(request,'person.html', {'person': person})


@login_required
def persons_new(request):
    form = PersonForm(request.POST or None)

    if form.is_valid():
            form.save()
            return redirect('persons_list')
    return render(request, 'person_form.html', {'form': form})


@login_required
def persons_update(request,id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None,instance=person)

    if form.is_valid():
            form.save()
            return redirect('persons_list')
    return render(request, 'person_form.html', {'form':form})


@login_required
def persons_delete(request, id):
    person = get_object_or_404(Person, pk=id)

    if request.method == 'POST':
        person.delete()
        return redirect('persons_list')
    return render(request, 'person_delete_confirm.html', {'person':person})
