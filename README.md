# Tour House API

## Descrição
Este projeto foi desenvolvido para o desafio técnico da Tour House. Ele visa gerenciar relacionamentos entre três entidades principais: funcionários, departamentos e empresas. Confira o Diagrama Entidade-Relacionamento (DER) [aqui](der.png).
## Configuração do projeto

### Tecnologias Utilizadas
- Python 3.9
- Django 4.2.7 e Django REST Framework 3.14.0
- PostgreSQL 16.0
- Swagger para documentação da API
- Autenticação via JWT
- Docker (opcional para implantação)

### Passos para execução

1. Clone o repositório
> git clone ```https://github.com/itsmevicot/tour_house_challenge.git```

2. Crie um ambiente virtual
> python -m venv venv

3. Ative o ambiente virtual (Windows)
> venv\Scripts\activate

4. Instale as dependências
> pip install -r requirements.txt

5. Configure o banco de dados do projeto:  

* Nessa etapa, vá até a [raiz do projeto Django](tourhouse) e localize o arquivo [local_settings_sample.py](tourhouse/local_settings_sample.py). Utilize-o como base para configurar seu banco PostgreSQL.
* Crie um arquivo local_settings.py seguindo o exemplo. Você pode passar a SECRET_KEY do projeto tanto no arquivo local_settings.py quanto nas variáveis de ambiente.
* Similarmente, você pode configurar as variáveis de ambiente do projeto criando um arquivo .env seguindo o [arquivo de exemplo para variáveis de ambiente](.env_exemplo)
* **OBSERVAÇÃO**: A SECRET_KEY presente no exemplo é insegura e não deve ser utilizada em produção. Idealmente, você deve gerar uma nova SECRET_KEY e utilizar as variáveis de ambiente para mantê-la segura.
* Uma alternativa ao uso de um banco local é o uso de um container Docker, disponível nesse projeto. Para utilizá-lo, execute:
> docker-compose up -d
* Certifique-se de que o arquivo .env e o local_settings.py estejam configurados corretamente antes de iniciar o container, pois eles informarão ao docker-compose as variáveis a serem utilizadas.

6. Gerando uma SECRET_KEY (opcional):

- Abra o shell do Django com o comando:
> python manage.py shell

- Execute o comando:
> from django.core.management.utils import get_random_secret_key

- Chame a função:
> get_random_secret_key()

- Copie a saída do comando e cole no arquivo local_settings.py e/ou nas variáveis de ambiente.

7. Migrando o projeto:

Com o banco configurado, aplique as migrações do projeto:
> python manage.py migrate

Para iniciar o projeto, utilize o seguinte comando:
> python manage.py runserver

A documentação gerada via [Swagger](https://swagger.io/) está disponível em:
> http://localhost:8000

### Dados de teste
É possível carregar dados de teste para alimentar o banco de dados através de fixtures. Para isso, um comando que importa esses dados foi criado. Para executá-lo, utilize:
> python manage.py load_test_data

Nessa importação, também é criado um superusuário com as seguintes credenciais:
- email='admin@admin.com' 
- password='admin'

## Funcionamento
O tópico a seguir descreve o funcionamento da API e como utilizá-la. Aqui estão todos os endpoints disponíveis. Para mais detalhes, acesse a documentação disponível em http://localhost:8000.

### Register
- POST /api/v1/register/ - Registrar um novo usuário.

### Token
- POST /api/v1/token/ - Obter par de tokens JWT para autenticação.
- POST /api/v1/token/refresh/ - Renovar o token de acesso JWT.

### Employees
- GET /api/v1/employees/ - Listar todos os funcionários ativos.
- POST /api/v1/employees/ - Criar um novo funcionário.
- GET /api/v1/employees/{id}/ - Detalhes de um funcionário específico.
- PUT /api/v1/employees/{id}/ - Atualizar um funcionário.
- PATCH /api/v1/employees/{id}/ - Atualização parcial de um funcionário.
- DELETE /api/v1/employees/{id}/ - Deletar (inativar) um funcionário.
### Departments
- GET /api/v1/departments/ - Listar todos os departamentos ativos.
- POST /api/v1/departments/ - Criar um novo departamento.
- GET /api/v1/departments/{id}/ - Detalhes de um departamento específico.
- PUT /api/v1/departments/{id}/ - Atualizar um departamento.
- PATCH /api/v1/departments/{id}/ - Atualização parcial de um departamento.
- DELETE /api/v1/departments/{id}/ - Deletar (inativar) um departamento.
### Companies
- GET /api/v1/companies/ - Listar todas as empresas ativas.
- POST /api/v1/companies/ - Criar uma nova empresa.
- GET /api/v1/companies/{id}/ - Detalhes de uma empresa específica.
- PUT /api/v1/companies/{id}/ - Atualizar uma empresa.
- PATCH /api/v1/companies/{id}/ - Atualização parcial de uma empresa.
- DELETE /api/v1/companies/{id}/ - Deletar (inativar) uma empresa.

## Autenticação

- A autenticação ocorre em duas etapas. A primeira é a criação de uma conta via email e senha. Essa senha deve ter pelo menos 8 caracteres, sendo alfanumérica com pelo menos 1 caractere especial.
- A segunda etapa é utilizar o email criado para gerar um token JWT, que será utilizado para autenticar o usuário nas requisições.
- Para ter acesso a segunda etapa, é preciso que um administrador do sistema ative a sua conta. Atualmente, há 2 maneiras de fazer a ativação:
1. Via Django ADMIN:
- Crie uma conta de superusuário:
> python manage.py createsuperuser
- Acesse localhost:8000/admin e faça o login com a conta criada.
- Acesse a página de usuários e ative a conta do usuário criado.

2. Alternativamente:
- Utilize o comando abaixo passando o email da conta que deseja ativar:
> python manage.py activate_user [email]

3. Criando conta de superusuário (opcional):
- Para criar uma conta de superusuário, utilize o comando:
> python manage.py createsuperuser

- Após ter sua conta ativa, você precisa gerar um token de acesso (JWT) no endpoint 'api/v1/token/', passando o email e senha da conta criada.
- 2 tokens serão gerados: 'access' e 'refresh'. O token 'access' é o que será utilizado para autenticar o usuário nas requisições. Já o token 'refresh' deve ser usado para gerar um novo token de acesso caso o seu token atual expire. Você poderá usá-lo durante 1 hora.
- Para gerar um novo token de acesso, utilize o endpoint 'api/v1/token/refresh/', passando o token 'refresh' no corpo da requisição.
- Por fim, para utilizar o token na interface do Swagger, vá até o topo da página e localize o botão "Authorize".
- Digite "Bearer `token de acesso`" no campo de texto e clique em "Authorize". Pronto! Você está autenticado e pode utilizar a API.


## Testes

Foram realizados testes unitários para cada API. Foram feitos testes de: criação, listagem, atualização, atualização parcial, remoção e recuperação por id de cada entidade.

Para executar os testes, utilize o comando:
> python manage.py test

Se preferir executar os testes de forma individual:
> python manage.py test [nome do diretório]/[nome do app]

Exemplo:
> python manage.py test apis/employees


## API Collection

Dentro da pasta [api_collection](api_collection), há 3 arquivos criados originalmente com o Insomnia, que podem ser importados para testar a API. Estão disponíveis nos formatos:
- JSON
- YAML
- HAR (HTTP Archive)
