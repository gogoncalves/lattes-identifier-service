<h1>API de Validação de Número de Identificação Lattes</h1>

<p>Esta API tem como objetivo validar um número de identificação Lattes, podendo verificar se o mesmo existe em um banco de dados MySQL ou em um arquivo CSV.</p>

<h2>Requisitos</h2>

<p>Para utilizar esta API, é necessário ter o Python 3.6 ou superior instalado em sua máquina. Além disso, é preciso instalar os seguintes pacotes:</p>

<ul>
  <li>Flask</li>
  <li>pandas</li>
  <li>mysql-connector-python</li>
  <li>flasgger</li>
</ul>

<h2>Instalação</h2>

<p>Para instalar os pacotes necessários, basta utilizar o comando abaixo:</p>

<pre><code>pip install flask pandas mysql-connector-python flasgger</code></pre>

<h2>Como utilizar</h2>

<p>Para utilizar esta API, siga os passos abaixo:</p>

<ol>
  <li>Clone o repositório em sua máquina:</li>
  <pre><code>git clone https://github.com/GOGoncalves/api-lattes</code></pre>
  <li>Abra o arquivo db_config.txt localizado na pasta config e configure com as informações do seu banco de dados MySQL. Caso não possua um banco de dados, pode utilizar o arquivo lattes.csv como fonte de validação.</li>
  <li>Acesse a pasta do projeto e execute o arquivo app.py com o seguinte comando:</li>
  <pre><code>python app.py</code></pre>
  <li>A API estará disponível no endereço http://localhost:5000. Você pode acessar a documentação da API pelo Swagger UI no endereço http://localhost:5000/apidocs.</li>
</ol>

<h2>Endpoints</h2>

<h3>Validação de número de identificação Lattes</h3>

<p>Este endpoint realiza a validação de um número de identificação Lattes, verificando se o mesmo existe no banco de dados MySQL ou no arquivo CSV.</p>

<ul>
  <li>URL: /lattes/{lattes_number}</li>
  <li>Método: GET</li>
  <li>Parâmetros:</li>
  <ul>
    <li>lattes_number (obrigatório): Número de identificação Lattes.</li>
  </ul>
  <li>Respostas:</li>
  <ul>
    <li>200 OK: Retorna uma mensagem informando que o número de identificação Lattes é válido.</li>
    <li>400 Bad Request: Retorna uma mensagem informando que o número de identificação Lattes é inválido.</li>
  </ul>
</ul>

<h2>Documentação</h2>

<p>A documentação completa da API pode ser acessada através do Swagger UI, disponível no endereço http://localhost:5000/apidocs.</p>
