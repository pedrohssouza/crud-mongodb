from mongoengine import Document, StringField, ListField

class Contato(Document):
    nome = StringField(required=True)
    telefones = ListField(StringField(), default=list)


from mongoengine import connect

# Conectar ao banco de dados 'contatos'
connect('contatos', host='localhost', port=27017)

def criar_contato(nome, telefones):
    contato = Contato(nome=nome, telefones=telefones)
    contato.save()
    return contato

def obter_contatos():
    return Contato.objects

def atualizar_contato(id, nome, telefones):
    contato = Contato.objects(id=id).first()
    if contato:
        contato.nome = nome
        contato.telefones = telefones
        contato.save()
        return contato
    return None

def excluir_contato(id):
    contato = Contato.objects(id=id).first()
    if contato:
        contato.delete()
        return True
    return False

def menu():
    print("1. Criar Contato")
    print("2. Listar Contatos")
    print("3. Atualizar Contato")
    print("4. Excluir Contato")
    print("5. Sair")

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do contato: ")
        telefones = input("Digite os telefones separados por vírgula: ").split(',')
        criar_contato(nome, telefones)
        print("Contato criado com sucesso.")
    elif opcao == "2":
        contatos = obter_contatos()
        for contato in contatos:
            print(f"Nome: {contato.nome}, Telefones: {', '.join(contato.telefones)}")
    elif opcao == "3":
        id = input("Digite o ID do contato que deseja atualizar: ")
        nome = input("Digite o novo nome do contato: ")
        telefones = input("Digite os novos telefones separados por vírgula: ").split(',')
        if atualizar_contato(id, nome, telefones):
            print("Contato atualizado com sucesso.")
        else:
            print("Contato não encontrado.")
    elif opcao == "4":
        id = input("Digite o ID do contato que deseja excluir: ")
        if excluir_contato(id):
            print("Contato excluído com sucesso.")
        else:
            print("Contato não encontrado.")
    elif opcao == "5":
        break
    else:
        print("Opção inválida. Tente novamente.")

