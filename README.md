## DEVARIA API

É uma api feita para teste dada pela empresa Verzel, com objectivos de teste os meus conhecimentos ou experiência como desenvolvedor, nas seguintes linguagem: `Python(Django) e React js`.

A aplicação tem como objectivos cadastrar módulos os cursos e aulas.

Endpoints da aplicação:

<table>
<tr>
    <th>name</th>
    <th>method</th>
    <th>endpoint</th>
</tr>
<tr>

<td>Todos os modulos</td>
<td>

`GET`

</td>

<td>

`/api/module/`

</td>

</tr>

<td>detalhe do modulo</td>
<td>

`GET`

</td>

<td>

`/api/module/<str:id>`

</td>

</tr>

<td>Criar um modulo</td>
<td>

`POST`

</td>

<td>

`/api/module_create/`

</td>

</tr>

<td>Actualizar modulo</td>
<td>

`POST`

</td>

<td>

`/api/module_update/<str:id>`

</td>

</tr>

<td>Delete modulo</td>
<td>

`DELETE`

</td>

<td>

`/api/module_delete/<str:id>`

</td>

</tr>

</table>


### BASE DE DADOS DA APLICAÇÃO

Para rodar o app não é neccessario alterar as configuração de base de dados, neste caso podemos utilizar a configuração padrão que neste caso estaremos a usar o `SQLITE3`.

```py

DATABASES  = {
    'default': { 
    'ENGINE': 'django.db.backends.sqlite3', 
    'NAME': BASE_DIR / 'db.sqlite3', 
} 

```


### MÉTODOS

<hr />


Requisito da API:

<table>
<tr>
    <th>name</th>
    <th>description</th>
</tr>
<tr>
<td>GET</td>
<td>Retorna informações de um ou mais registros.</td>
</tr>

<tr>
<td>POST</td>
<td>Utilizado para criar um novo registro ou actualizar.</td>
</tr>

<tr>
<td>POST</td>
<td>Remova um registro do sistema..</td>
</tr

</table>

### ENDPOINT PARA ACESSAR A DOCUMENTAÇÃO SWAGGER DA API
<hr />

```py
    /api/docs
```

### FUNCIONALIDADES DA APLICAÇÃO
<hr />
Os recursos necessários da aplicação são:

- [x] Criação, remoção e atualização de usuário
- [x] Criação, remoção, atualização e deleção de módulo
- [x] Criação, remoção, atualização e deleção de aula
- [x] Authenticação de usuário
- [x] Validação dos campos antes da inserção
- [ ] Listagem das aulas em ordem alfabética