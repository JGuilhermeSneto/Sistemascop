from django.shortcuts import render, redirect
from .models import Area, Instrutor, Publico,Cursos
from .forms import AreaForms, InstrutorForms, PublicoForms,CursosForms


def areas(request):
    areas = Area.objects.all()
    Context = {
        'areas' : areas
    }
    return render(request, 'areas.html', Context)



def Cadastrar_area(request):
    form = AreaForms(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('areas')

    Context = {
        'form':form
    }

    return render(request, 'Cadastro_areas.html', Context)



def AreaRemover(request,id):
    area = Area.objects.get(pk=id)
    area.delete()
    return redirect('Áreas')



def AreaEditar(request, id):
    area = Area.objects.get(pk = id)
    form = AreaForms(request.POST or None,instance=area)

    if form.is_valid():
        form.save()
        return redirect('areas')



    Context = {
        'form': form
    }

    return render(request,'Cadastro_areas.html' ,Context)


# ==================== LISTAR ====================
def instrutores(request):
    instrutores = Instrutor.objects.all()
    context = {
        'instrutores': instrutores
    }
    return render(request, 'areas.html', context)


# ==================== CADASTRAR ====================
def CadastrarInstrutor(request):
    form = InstrutorForms(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('instrutores')

    context = {
        'form': form
    }
    return render(request, 'Cadastrar_instrutor.html', context)

# ==================== REMOVER ====================
def InstrutorRemover(request, id):
    instrutor = Instrutor.objects.get(pk=id)
    instrutor.delete()
    return redirect('instrutores')

# ==================== EDITAR ====================
def InstrutorEditar(request, id):
    instrutor = Instrutor.objects.get(pk=id)
    form = InstrutorForms(request.POST or None, instance=instrutor)

    if form.is_valid():
        form.save()
        return redirect('instrutores')

    context = {
        'form': form
    }
    return render(request, 'Cadastrar_instrutor.html', context)


def publicos(request):
    publicos = Publico.objects.all()
    context = {
        'publicos': publicos
    }
    return render(request, 'areas.html', context)

# ==================== CADASTRAR ====================
def CadastrarPublico(request):
    form = PublicoForms(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('publicos')

    context = {
        'form': form
    }
    return render(request, 'Cadastra_publico.html', context)

# ==================== REMOVER ====================
def PublicoRemover(request, id):
    publico = Publico.objects.get(pk=id)
    publico.delete()
    return redirect('publicos')

# ==================== EDITAR ====================
def PublicoEditar(request, id):
    publico = Publico.objects.get(pk=id)
    form = PublicoForms(request.POST or None, instance=publico)

    if form.is_valid():
        form.save()
        return redirect('publicos')

    context = {
        'form': form
    }
    return render(request, 'Cadastra_publico.html', context)



#==========================Curso======================

# ===================== LISTAR CURSOS =====================
def CursosListar(request):
    cursos = Cursos.objects.all()  # ✅ usar o modelo correto
    Context = {
        'Cursos': cursos
    }
    return render(request, 'Cursos.html', Context)

# ===================== CADASTRAR CURSO =====================
def CadastrarCurso(request):
    Form = CursosForms(request.POST or None)

    if Form.is_valid():  # ✅ salvar se válido
        Form.save()
        return redirect('CursosListar')  # redireciona para a listagem

    Context = {
        'form': Form
    }

    return render(request, 'CadastrarCurso.html', Context)


def CursoEditar(request, id):
    cursos = Cursos.objects.get(pk=id)
    form = CursosForms(request.POST or None, instance=id)

    if form.is_valid():
        form.save()
        return redirect('publicos')

    context = {
        'cursos': cursos
    }
    return render(request, 'Cadastra_publico.html', context)



def RemoverCurso(request,id):
    curso = Cursos.objects.get(pk=id)
    curso.delete()

    return redirect('CursosListar')
