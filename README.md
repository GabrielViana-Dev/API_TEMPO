# API DE CLIMA
Este é um aplicativo web simples desenvolvido com Flask que permite aos usuários consultar informações meteorológicas usando a API OpenWeatherMap. Os usuários podem inserir o nome da cidade e receberão a temperatura atual e uma breve descrição do clima.

## Tecnologias Utilizadas
- Python
- Flask
- Web (Html, Css, Javascript)

## Rotas

O aplicativo é composto por 3 rotas:

- **Index:** `(/)`: Nesta rota o usuário deve inserir a cidade que deseja buscar as condições meteorológicas.

- **Resultados:** `(/Resultados/)`: Nesta rota o usuário recebe da aplicação o retorno para a cidade buscada.

- **Erro:** `(/erro/)`: Nesta rota o usuário recebe uma mensagem de erro caso a consulta não seja bem sucedida.

