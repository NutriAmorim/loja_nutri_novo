import os
from collections import defaultdict

projeto_base = os.getcwd()
arquivo_por_nome = defaultdict(list)

for dirpath, dirnames, filenames in os.walk(projeto_base):
    if os.path.basename(dirpath) == 'static':
        for nome in filenames:
            caminho = os.path.join(dirpath, nome)
            arquivo_por_nome[nome].append(caminho)

# Mostrar duplicatas
print("\nArquivos duplicados encontrados:\n")
duplicados = False
for nome, caminhos in arquivo_por_nome.items():
    if len(caminhos) > 1:
        print(f"{nome}:")
        for caminho in caminhos:
            print(f"  - {caminho}")
        print()
        duplicados = True

if not duplicados:
    print("Nenhum arquivo duplicado encontrado!")
