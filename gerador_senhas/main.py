import file_functions as gs

def main():
    servico = input("Digite um nome para identificar local da senha: ")
    usuario = input("Digite o nome de usuário: ")
    tamanho = int(input("Digite a quantidade de caracteres que deseja ter na senha: "))
    nova_senha = gs.gerador_senhas()
    gs.salva_em_arquivo(servico, usuario, nova_senha)

if __name__ == '__main__':
    print()
    print("-------------------------")
    print("GERADOR DE SENHAS")
    print("-------------------------")
    print()

    main()