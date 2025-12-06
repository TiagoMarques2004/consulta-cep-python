# Consulta de CEP em Python
Aplicação simples desenvolvida em Python para consultar informações de endereço a partir de um CEP, utilizando a API pública **BrasilAPI**.  
O projeto é ideal para quem está iniciando em Python, consumindo APIs e organizando um repositório profissional no GitHub.

# Funcionalidades

- Consulta de CEP via API BrasilAPI  
- Retorno com:
  - Logradouro
  - Bairro
  - Cidade
  - Estado (UF)    
- Tratamento de erros (CEP inválido, conexão, etc.)

# Estrutura do Projeto
consulta-cep-python/
│── src/
│ └── main.py # Arquivo principal do programa
│── README.md # Documentação do projeto
│── .gitignore # Arquivos/pastas ignoradas pelo Git


#  Tecnologias Utilizadas

- **Python 3.x**
- Biblioteca `requests`
- API ViaCEP (https://brasilapi.com.br/api/cep/v1/{cep})

# Instalação e Uso
1. Clone o repositório:
```bash
git clone https://github.com/TiagoMarques2004/consulta-cep-python.git
cd consulta-cep-python



