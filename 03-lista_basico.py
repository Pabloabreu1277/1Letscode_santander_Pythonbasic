"""3.Vamos fazer um programa para verificar quem é o assassino de um crime.
 Para descobrir o assassino, a polícia faz um pequeno questionário com 5 perguntas
 onde a resposta só pode ser sim ou não:
 a.Mora perto da vítima?
 b.Já trabalhou com a vítima?
 c.Telefonou para a vítima?
 d.Esteve no local do crime?
 e.Devia para a vítima?
 Cada resposta sim dá um ponto para o suspeito.
 A polícia considera que os suspeitos com 5 pontos são os assassinos,
  com 4 a 3 pontos são cúmplices e 2 pontos são apenas suspeitos,
 necessitando outras investigações. Valores iguais ou abaixo de 1 são liberados."""


print("Responda somente com numeros = 1-Sim ou 0-Não")
a1 = int(input("a.Mora perto da vítima?"))
a2 = int(input("b.Já trabalhou com a vítima?"))
a3 = int(input("c.Telefonou para a vítima?"))
a4 = int(input("d.Esteve no local do crime?"))
a5 = int(input("e.Devia para a vítima?"))

listar = [a1,a2,a3,a4,a5]

listSum = sum(listar)
print(listSum)

if listSum == 5:
    print("Entrevistado é o assassino!")
elif listSum >= 3 and listSum <= 4:
    print("Entrevistado é Cumplices do assassinato!")
elif listSum == 2:
    print("Entrevistado é suspeito!")
elif listSum <= 1:
    print("Entrevistado é liberado")



            
    
     