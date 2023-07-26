dados = {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}

print(dados["nome"])  # "Guilherme"
print(dados["idade"])  # 28
print(dados["telefone"])  # "3333-1234"

dados["nome"] = "Maria"
dados["idade"] = 18
dados["telefone"] = "9988-1781"

print(dados)  # {"nome": "Maria", "idade": 18, "telefone": "9988-1781"}

del dados["telefone"]
print(dados)
dados.update({"dados":{"nome": "carlos"}})
print(dados)
dados.pop("nome")
print(dados)
dados.setdefault("nome", "Pedrilicia")
print(dados)

dados.update({"pessoa":{"nome":"val","idade":30,"sexo":"masc"}})

for chave,valor in dados.items():
    print(chave,valor)
    
print(dados["pessoa"]["idade"])
del dados["pessoa"]["sexo"]
print(dados)

print("idade" in dados["pessoa"])