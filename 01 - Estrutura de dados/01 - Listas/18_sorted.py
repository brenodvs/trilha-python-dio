linguagens = ["python", "js", "c", "java", "csharp"]

print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]

nome=[]
cont=0
while cont<3:
    name=str(input('Digite um nome: '))
    nome.append(name)
    cont+=1
for n in nome:
     print(n)
nome.pop(2)
print(nome)
nome.append('carlos')
print(nome)
#print(nome.append['joao'])
#print(nome.count)


 