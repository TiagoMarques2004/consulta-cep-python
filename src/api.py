# Importando biblioteca
import requests

# URL PADRAO API
BASE_URL = "https://brasilapi.com.br"

# Criando função
def buscar_cep():

    # Criando input para o usuario pesquisar
    cep = input("Digite o CEP que deseja pesquisar:")

    # Configurando URL PADRAO + endpoint
    url = BASE_URL + "/api/cep/v1/{}".format(cep)

    # Configurando body
    headers = {'Content-Type': 'application/json'}

    # Realizando request
    response = requests.get(url, headers=headers, timeout=10)

    # Verificando resposta da request
    if response.status_code == 200:

        # Transformando os dados em JSON para dicionario python
        dados = response.json()


        dados_formatados = {
            "estado": dados.get("state"),
            "cidade": dados.get("city"),
            "Bairro": dados.get("neighborhood"),
            "Rua": dados.get("street"),
            "Serviço": dados.get("service")
        }

        print("DADOS", dados_formatados)
    # Tratamento de erros e do código da requisição    
    else:
        print("Erro na consulta dos dados", response.status_code)
        return None

# Chamando a função
buscar_cep()
















