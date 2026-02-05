#Os itens da lista são acessados através de um número chamado índice

nomes = ["Joaquina" , 'Maria' , 'João']

#Adiciona nomes:

nomes.append("João")
nomes.append("Joana")

#append(item): adiciona um item no final da lista
#insert(indice,item): isere um item em ums posicao especifica

print(nomes[0])
print(nomes[1])
print(nomes[2])
print(nomes[3])
print(nomes[4])

#É possivel alteral, adicionar ou remover elementos após a criação
#Podem conter elementos de tipos difeentas, como números, strings, boleanos, até outras listas:

lista_mista = [1, 'Dois', 3.0, True]