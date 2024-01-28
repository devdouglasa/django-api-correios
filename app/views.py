from django.shortcuts import render
from app.api import Api

def home(request):
    return render(request, template_name='index.html')

def endereco(request):

    cep = request.POST.get('cep')
    api = Api()
    api._cep = cep
    dados = api.receber_dados()
    if dados == "Not a found!":
        return render(request, template_name='erro.html')
    else:
        return render(request, template_name='endereco.html', context={"endereco":dados})

    