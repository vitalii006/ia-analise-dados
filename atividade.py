print("gerenciador de notas")

lista_de_notas = []
nome = input("digite seu nome:")
n1 = int(input("digite sua nota 1:"))
n2 = int(input("digite sua nota 2:"))
n3 = int(input("digite sua nota 3:"))
n4 = int(input("digite sua nota 4:"))

notas = [n1,n2,n3,n4]
print ("notas do aluno",notas)


print((nome),"sua maior nota:",max(notas))
print((nome),"sua menor nota:",min(notas))
print((nome),"soma de todas as notas:",sum(notas))
media = (sum(notas)/len(notas))
print((nome),"sua media de notas:",media)

if sum(notas)/len(notas) >= 5:
    print((nome), "aprovado")
    
else:
    print((nome), "reprovado")
    
                                       



      





