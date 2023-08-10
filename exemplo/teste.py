from aluno import Aluno

a1 = Aluno("pedro", "informatica")
a2 = Aluno("Fulano", "informatica")

print(a1.nome, "está sem dormir há", a1.get_tempoSemDormir(), "horas")

a1.estudar(10)
a2.estudar(12)
print(a1.nome, "está sem dormir há", a1.get_tempoSemDormir(), "horas")
print(a2.nome, "está sem dormir há", a2.get_tempoSemDormir(), "horas")
a1.dormir(4)
print(a1.nome, "está sem dormir há", a1.get_tempoSemDormir(), "horas")