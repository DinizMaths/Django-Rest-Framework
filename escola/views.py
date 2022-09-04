# from django.http import JsonResponse

# # Create your views here.
# def alunos(request):
#   if request.method == 'GET':
#     aluno = {
#       "id"  : 1,
#       "nome": "Matheus",
#     }

#     return JsonResponse(aluno)

from rest_framework    import viewsets
from escola.models     import Aluno, Curso
from escola.serializer import AlunoSerializer, CursoSerializer

class AlunosViewSet(viewsets.ModelViewSet):
  """
    Exibe todos os alunos e alunas
  """

  queryset = Aluno.objects.all()
  serializer_class = AlunoSerializer

class CursosViewSet(viewsets.ModelViewSet):
  """
    Exibe todos os Cursos
  """

  queryset = Curso.objects.all()
  serializer_class = CursoSerializer