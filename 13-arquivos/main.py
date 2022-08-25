try:
    arquivo = open("dados.txt", "w")
    continuar = True
    while continuar:
        time = input("Digite o nome do time: (vazio para sair)")
        # toda str vazia é False
        # entra no if se a str for vazia
        if not time:
            continuar = False
            continue
        arquivo.write(time + "\n")
    arquivo.close()
except FileNotFoundError:
    print("Arquivo não encontrado")