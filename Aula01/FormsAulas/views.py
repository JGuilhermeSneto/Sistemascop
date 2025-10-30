from django.shortcuts import render

def Cadastro(request):
    return render(request, 'Cadastro.html')

def dados(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        personagem = request.POST.get('personagem')
        filme = request.POST.get('filme')

        resposta_certa_personagem = "Rei"
        resposta_certa_filme = "Carros"


        resultado = []

        if personagem == resposta_certa_personagem:
            resultado.append(("Personagem: Correto!", "certo"))
        else:
            resultado.append((f"Personagem: Errado! A resposta certa é {resposta_certa_personagem}.", "errado"))

        if filme == resposta_certa_filme:
            resultado.append(("Filme: Correto!", "certo"))
        else:
            resultado.append((f"Filme: Errado! A resposta certa é {resposta_certa_filme}.", "errado"))

        contexto = {
            "nome": nome,
            "resultado": resultado
        }

        return render(request, 'dados.html', contexto)

    return render(request, 'Cadastro.html')
