
import json

def salvar_cliente_json(cliente):
    dados_cliente = {
        "id": cliente.id,
        "nome": cliente.nome,
        "cpf": cliente.cpf,
        "idade": cliente.idade,
        "endereco": cliente.endereco,
        "email": cliente.email,
    }

    with open(f"cliente_{cliente.id}.json", "w") as json_file:
        json.dump(dados_cliente, json_file, indent=4)

def salvar_bike_txt(bike):
    dados_bike = (
        f"Bike ID: {bike.bike_id}\n"
        f"Modelo: {bike.modelo}\n"
        f"Cor: {bike.cor}\n"
        f"Número de Série: {bike.numero_serie}\n"
        f"Preço: {bike.preco}\n"
    )

    with open(f"bike_{bike.bike_id}.txt", "w") as txt_file:
        txt_file.write(dados_bike)