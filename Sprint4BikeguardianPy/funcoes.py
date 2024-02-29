from classes import Bike, Cliente
from database import session
from sqlalchemy.orm import joinedload
from funcoes_arquivos import salvar_cliente_json, salvar_bike_txt

def estado_civil():

    print("Escolha o seu estado civil:")
    print("1. solteiro")
    print("2. casado")
    print("3. divorciado")
    print("4. viúvo")

    while True:
        try:
            escolhaCv = int(input("Digite o número correspondente à sua escolha: "))
            if escolhaCv in [1, 2, 3, 4]:
                break  
            else:
             print("Por favor, escolha uma opção válida (1, 2, 3 ou 4).")
        except ValueError:
            print("Por favor, digite um número válido (1, 2, 3 ou 4).")

    if escolhaCv == 1:
        return "Solteiro"
    elif escolhaCv == 2:
        return "Casado"
    elif escolhaCv == 3:
        return "Divorciado"
    else:
        return "Viúvo"

def grau_ecolaridade():

    print("Informe o sua escolaridade:")
    print("1. Fundamental")
    print("2. Médio")
    print("3. Superior incompleto")
    print("4. Superior completo")

    while True:
        try:
            escolhaEs = int(input("Digite o número correspondente à sua escolha: "))
            if escolhaEs in [1, 2, 3, 4]:
                break  
            else:
             print("Por favor, escolha uma opção válida (1, 2, 3 ou 4).")
        except ValueError:
            print("Por favor, digite um número válido (1, 2, 3 ou 4).")

    if escolhaEs == 1:
        return "Fundamental"
    elif escolhaEs == 2:
        return "Médio"
    elif escolhaEs == 3:
        return "Superior incompleto"
    else:
        return "Superior completo"

def rev_bike():

    print("você fez alguma revisão na sua bike no ultimo ano?:")
    print("1. sim")
    print("2. não")
    while True:
        try:
            escolhaRev = int(input("Digite o número correspondente à sua escolha: "))
            if escolhaRev in [1, 2]:
                break  
            else:
             print("Por favor, escolha uma opção válida (1 ou 2).")
        except ValueError:
            print("Por favor, digite um número válido (1 ou 2).")

    if escolhaRev == 1:
        return "sim"
    else:
        return "não"
    
def inf_acessorios():

    print("você possui algum acessorio em sua bike?:")
    print("1. GPS")
    print("2. Velocímetro")
    print("3. Ciclocomputador")
    print('4. Nenhum')
    while True:
        try:
            escolhaAces = int(input("Digite o número correspondente à sua escolha: "))
            if escolhaAces in [1, 2, 3, 4]:
                break  
            else:
             print("Por favor, escolha uma opção válida (1, 2, 3 ou 4).")
        except ValueError:
            print("Por favor, digite um número válido (1, 2, 3 ou 4).")

    if escolhaAces == 1:
        return "GPS"
    elif escolhaAces == 2:
        return 'Velocímetro'
    elif escolhaAces == 3:
        return 'Ciclocomputador'
    else:
        return 'Nenhum'   

def escolha_plano():

    print("Escolha seu plano:")
    print("1. Pedal essencial")
    print("2. Pedal leve")
    print("3. Pedal elite")
    while True:
        try:
            escolhaPlan = int(input("Digite o número correspondente à sua escolha: "))
            if escolhaPlan in [1, 2, 3]:
                break  
            else:
             print("Por favor, escolha uma opção válida (1, 2, ou 3).")
        except ValueError:
            print("Por favor, digite um número válido (1, 2, ou 3).")

    if escolhaPlan == 1:
        return "Pedal essencial"
    elif escolhaPlan == 2:
        return 'Pedal leve'
    else:
        return 'Pedal elite'
    

def visualizar_cadastros():
    clientes = session.query(Cliente).options(joinedload(Cliente.bikes)).all()
    
    for cliente in clientes:
        cliente.exibir_detalhes()  

    
def escolha_genero():

    print("Escolha o seu gênero:")
    print("1. Mulher")
    print("2. Homem")
    print("3. Outros")

    while True:
        try:
            escolhaGen = int(input("Digite o número correspondente à sua escolha: "))
            if escolhaGen in [1, 2, 3]:
                break  
            else:
             print("Por favor, escolha uma opção válida (1, 2 ou 3).")
        except ValueError:
            print("Por favor, digite um número válido (1, 2 ou 3).")

    if escolhaGen == 1:
        return "Mulher"
    elif escolhaGen == 2:
        return "Homem"
    else:
        return "Outros"

'''
[17:52, 15/11/2023] Vinicius Becker: from tkinter import filedialog, Label, Tk
from PIL import Image, ImageTk
from database import session
from sqlalchemy.orm import joinedload

def criar_label_imagem(janela):
    label_imagem = Label(janela)
    label_imagem.pack()
    return label_imagem

def selecionar_imagem(label_imagem):
    caminho_imagem = filedialog.askopenfilename()
    if caminho_imagem:
        imagem = Image.open(caminho_imagem)
        imagem.thumbnail((300, 300))
        foto = ImageTk.PhotoImage(imagem)
        label_imagem.config(image=foto)
        label_imagem.image = foto
        return caminho_imagem
    else:
        return None
[17:52, 15/11/2023] Vinicius Becker: def cadastrar_bike_com_imagens(label_imagem, selecionar_imagem):
    janela_imagens = Tk()  # Crie uma nova janela para imagens
    label_imagem_janela = imagem.criar_label_imagem(janela_imagens)  # Crie um novo rótulo de imagem

    try:
        imagens = carregar_imagens(label_imagem_janela, selecionar_imagem)  # Carregue as imagens

        cpf_cliente = int(input("Digite o CPF do cliente: "))
        cliente = session.query(Cliente).filter_by(cpf=cpf_cliente).first()

        if cliente:
            bike_id = int(input("Digite o ID da bike: "))
            modelo = input("Digite o modelo da bike: ")
            marca = input('Digite a marca da bicicleta: ')
            cor = input('Digite a cor da bicicleta: ')
            data_compra = input('Digite a data de compra da bicicleta (formato YYYY-MM-DD): ')
            local_compra = input('Digite o local da compra da bicicleta: ')
            numero_serie = int(input("Digite o número de série: "))
            preco = float(input("Digite o preço da bike: "))
            revisao = rev_bike()
            acessorios = inf_acessorios()
            plano = escolha_plano()

            bike = Bike(bike_id=bike_id, modelo=modelo, marca=marca, numero_serie=numero_serie, preco=preco, revisao=revisao,
                        acessorios=acessorios, plano=plano, cor=cor, data_compra=data_compra, local_compra=local_compra)
            cliente.bikes.append(bike)
            session.add(bike)
            session.commit()
            salvar_bike_txt(bike)
            print("Bike cadastrada com sucesso!")

        else:
            opcao = input("Cliente não encontrado. Deseja cadastrar um novo cliente? Digite 5 para sim e 6 para não: ")
            if opcao == '5':
                cadastrar_cliente()

    except ValueError as ve:
        print(f"Erro de valor: {ve}")
        session.rollback()

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        session.rollback()

    finally:
        janela_imagens.destroy() 

def carregar_imagens(label_imagem, selecionar_imagem):
    imagens = []

    print("Por favor, selecione a imagem da frente da bicicleta.")
    imagem_frente = selecionar_imagem(label_imagem)
    imagens.append(imagem_frente) if imagem_frente else imagens.append('')

    print("Agora, selecione a imagem do lado direito da bicicleta.")
    imagem_direito = selecionar_imagem(label_imagem)
    imagens.append(imagem_direito) if imagem_direito else imagens.append('')

    print("Agora, selecione a imagem do lado esquerdo da bicicleta.")
    imagem_esquerdo = selecionar_imagem(label_imagem)
    imagens.append(imagem_esquerdo) if imagem_esquerdo else imagens.append('')

    print("Por fim, selecione a imagem de trás da bicicleta.")
    imagem_tras = selecionar_imagem(label_imagem)
    imagens.append(imagem_tras) if imagem_tras else imagens.append('')

    return imagens

# Criar a janela para a função carregar_imagens
janela_imagens = Tk()
label_imagem = Label(janela_imagens)
label_imagem.pack()

# Chamar a função cadastrar_bike_com_imagens
cadastrar_bike_com_imagens(label_imagem, imagem.selecionar_imagem)

# Iniciar o loop da interface gráfica
janela_imagens.mainloop()

if _name_ == "_main_":
    # Criar a janela para a função carregar_imagens
    janela_imagens = Tk()
    label_imagem = imagem.criar_label_imagem(janela_imagens)

    # Chamar a função cadastrar_bike_com_imagens
    cadastrar_bike_com_imagens(label_imagem, imagem.selecionar_imagem)

    # Iniciar o loop da interface gráfica
    janela_imagens.mainloop()
        '''




def cadastrar_bike():
    print("- - - Cadastro de Nova Bike - - -")
    
    try:
        cpf_cliente = int(input("Digite o CPF do cliente: "))
        cliente = session.query(Cliente).filter_by(cpf=cpf_cliente).first()
    except ValueError as ve:
        print("Por favor, certifique-se de inserir valores válidos.")
        session.rollback()
        return 

    if cliente:
            bike_id = int(input("Digite o id da bike"))
            modelo = input("Digite o modelo da bike: ")
            marca = input('Digite a marca da bicicleta: ')
            cor = input('Digite a cor da bicicleta: ')
            data_compra = input('Digite a data de compra da bicicleta (formato YYYY-MM-DD): ')
            local_compra = input('Digite o local da compra da bicicleta: ')
            numero_serie = int(input("Digite o número de série: "))
            preco = float(input("Digite o preço da bike: ")) 
            revisao = rev_bike()
            acessorios = inf_acessorios()
            plano = escolha_plano()

            print("== Adicionar Fotos ==")
            foto1 = input("Digite o nome do arquivo da foto da Frente: ")
            foto2 = input("Digite o nome do arquivo da foto de Trás: ")
            foto3 = input("Digite o nome do arquivo da foto do Lado Esquerdo: ")
            foto4 = input("Digite o nome do arquivo da foto do Lado Direito: ")

            bike = Bike(bike_id=bike_id, modelo=modelo, marca=marca, numero_serie=numero_serie, preco=preco, revisao=revisao,
                        acessorios=acessorios, plano=plano, foto1=foto1, foto2=foto2, foto3=foto3, foto4=foto4,
                        cor=cor, data_compra=data_compra, local_compra=local_compra)
            cliente.bikes.append(bike)
            session.add(bike)
            session.commit()
            salvar_bike_txt(bike)
            print("Bike cadastrada com sucesso!")

    else:
            opcao = input("Cliente não encontrado. Deseja cadastrar um novo cliente? Digite 5 para sim e 6 para não: ")
            if opcao == '5':
                cadastrar_cliente()
    

def cadastrar_cliente():
    print("- - - Cadastro de Cliente - - -")
    try:
        id_cliente = int(input("Digite o ID do cliente: "))
        nome = str(input("Digite o seu nome completo: "))
        rg = int(input("Digite o numero do seu rg: "))
        genero = escolha_genero()
        estd_civil = estado_civil()
        escolaridade = grau_ecolaridade()
        dt_emiss_rg = input('Digite a data de emissão do seu RG: ')
        uf = input("Digite o UF de seu documento: ")
        email = input('Digite o seu email: ')
        data_nasc = input("Digite sua data de nascimento (formato YYYY-MM-DD): ")
        nacionalidade = str(input("Digite a sua nacionalidade: "))
        telefone = int(input("Digite o seu telefone: "))
        cpf = int(input("Digite o seu CPF: "))
        existing_client = session.query(Cliente).filter_by(cpf=cpf).first()
        if existing_client:
            print("CPF já existe. Escolha outro CPF.")
            return
        idade = int(input("Digite a sua idade: "))
        endereco = input("Digite o seu endereço: ")
        cep = int(input("Digite o seu CEP: "))

        cliente = Cliente(id=id_cliente, nome=nome, cpf=cpf, idade=idade, endereco=endereco, rg=rg, dt_emiss_rg=dt_emiss_rg, email=email,
                          data_nasc=data_nasc, nacionalidade=nacionalidade, telefone=telefone, cep=cep, uf=uf,
                          genero=genero, estd_civil=estd_civil, escolaridade=escolaridade)
        session.add(cliente)
        session.commit()

        cliente = session.query(Cliente).filter_by(cpf=cpf).first()
        salvar_cliente_json(cliente)

        print("Cliente cadastrado com sucesso!")

    except ValueError as ve:
        print("Por favor, certifique-se de inserir valores válidos.")
        session.rollback()

    except TypeError as te:
        print("Certifique-se de fornecer o tipo de dado correto.")
        session.rollback()

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        session.rollback()