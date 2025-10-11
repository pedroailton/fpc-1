def editor():
    feitos = []
    desfeitos = []

    while True:
        comando = input("> ").strip()

        if comando.startswith("escrever "):
            texto = comando[len("escrever ")]
            feitos.append(texto)
            desfeitos.clear() # Limpa a pilha "desfeitos"
        elif comando == "mostrar":
            print("Texto atual:", " ".join(feitos))
        elif comando == "desfazer":
            if feitos: # a pilha de feitos tem alguma coisa?
                desfeitos.append(feitos.pop())
            else: 
                print("Nada a desfazer.")
        elif comando == "refazer":
            if desfeitos:
                feitos.append(desfeitos.pop())
            else:
                print("Nada a desfazer.")
        elif comando == "sair":
            print("Encerrando editor...")
            break

editor()