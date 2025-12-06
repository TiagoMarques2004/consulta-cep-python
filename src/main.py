import requests

URL_PADRAO = "https://brasilapi.com.br/api"


def consultar_cep():
    try:
        """Chamada a API e consulta de cep"""
    
        # Configurando input para o usuario
        cep = input("Digite seu cep para consultar: ")

        # Configurando URL + endpoint
        url = URL_PADRAO + "/cep/v1/{}".format(cep)

        # Configurando body
        headers = {'Content-Type': 'application/json'}

        # Configurando request
        response = requests.get(url, headers=headers, timeout=10)
        
        # Tratamento do status code
        if response.status_code == 200:

            # Transformando os dados em lista python
            dados = response.json()

            # Alterando os nomes
            dados_formatados = {
                "Estado": dados.get("state"),
                "Cidade": dados.get("city"),
                "Bairro": dados.get("neighborhood"),
                "Rua": dados.get("street"),
                "Serviço": dados.get("service")
            }

            # Mostrando resultado
            print(dados_formatados)

            # Retornando os dados
            return dados_formatados
        
    # Tratamento de erros    
    except Exception as e:
        raise ValueError(f"Erro ao consultar o cep: {e}")
    return None
    
# Chamando função    
consultar_cep()



    







