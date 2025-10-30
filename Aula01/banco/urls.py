from django.urls import path
from .views import (
    areas, AreaRemover, AreaEditar, Cadastrar_area,
    instrutores, InstrutorRemover, InstrutorEditar, CadastrarInstrutor,publicos, PublicoRemover, PublicoEditar, CadastrarPublico, CursosListar,CadastrarCurso,RemoverCurso,CursoEditar
)

urlpatterns = [
    # ==================== ÁREAS ====================
    path('areas/', areas, name='areas'),  
    path('AreaRemover/<int:id>/', AreaRemover, name='AreaRemover'),
    path('AreaEditar/<int:id>/', AreaEditar, name='AreaEditar'),
    path('Cadastrar_area/', Cadastrar_area, name='Cadastrar_area'),

    # ==================== INSTRUTORES ====================
    path('instrutores/', instrutores, name='instrutores'),  
    path('InstrutorRemover/<int:id>/', InstrutorRemover, name='InstrutorRemover'),
    path('InstrutorEditar/<int:id>/', InstrutorEditar, name='InstrutorEditar'),
    path('CadastrarInstrutor/', CadastrarInstrutor, name='CadastrarInstrutor'),

    # ==================== PÚBLICOS ====================
    path('publicos/', publicos, name='publicos'),  
    path('PublicoRemover/<int:id>/', PublicoRemover, name='PublicoRemover'),
    path('PublicoEditar/<int:id>/', PublicoEditar, name='PublicoEditar'),
    path('CadastrarPublico/', CadastrarPublico, name='CadastrarPublico'),

    #====================== Curso =======================
    path('Cursos/', CursosListar, name='CursosListar'),
    path('Cursos/Cadastrar/', CadastrarCurso, name='CadastrarCurso'),
    path('CursoEditar/<int:id>/',CursoEditar,name= 'EditarCurso'),
    path('RemoverCurso/<int:id>/', RemoverCurso, name='RemoverCurso')

]
