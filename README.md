![lattes-identifier-service](https://user-images.githubusercontent.com/100040132/233802158-d7285bb6-9ee8-42d9-9e0c-969f7b49a6c6.png)
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fgogoncalves%2Flattes-identifier-api.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2Fgogoncalves%2Flattes-identifier-api?ref=badge_shield)
<h1>API RESTful Lattes CNPq</h1>
<p>Esta API tem como objetivo validar o número identificador Lattes, podendo verificar se o mesmo existe em um banco de dados MySQL ou em um arquivo CSV;</p>
<p>O <a href="https://www.gov.br/cnpq/pt-br">CNPq</a> disponibiliza, periodicamente, todos os ID dos Currículos Lattes cadastrados;</p>
<p>Foi utilizado como base os <a href="http://memoria.cnpq.br/documents/313759/83395da6-f582-46bc-a308-060a6ec1ceaa">dados</a> fornecidos pela <a href="http://memoria.cnpq.br/web/portal-lattes/extracoes-de-dados">Plataforma Lattes</a>, que é uma base de dados pública do <a href="https://www.gov.br/cnpq/pt-br">CNPq</a>, para realizar a validação do Número identificador.</p>



<h2>Requisitos</h2>

<p>Para utilizar esta API, é necessário ter o Python 3.6 ou superior instalado em sua máquina. Além disso, é preciso instalar os seguintes pacotes:</p>

<ul>
  <li>Flask</li>
  <li>pandas</li>
  <li>tdqm</li>
  <li>mysql-connector-python</li>
  <li>urllib3</li>
  <li>flasgger</li>
</ul>

<h2>Instalação</h2>

<p>Para instalar os pacotes necessários, basta utilizar o comando abaixo:</p>
<h4>Linux:</h4>
<pre><code>pip install -r requirements.txt</code></pre>
<h4>Windows:</h4>
<pre><code>py -m pip install -r requirements.txt</code></pre>

<h2>Como utilizar</h2>

<p>Para utilizar esta API, siga os passos abaixo: </p>

<ol>
  <li>Clone o repositório em sua máquina:</li>
  <pre><code>git clone https://github.com/GOGoncalves/lattes-identifier-service</code></pre>
  <li>Abra o arquivo db_config.txt localizado na pasta config e configure com as informações do seu banco de dados MySQL. Caso não possua um banco de dados, pode utilizar o arquivo lattes_transformed.csv como fonte de validação ou altere o toggle para True e baixe da Web um arquivo CSV atualizado, não esqueça de manter a URL para download atualizada.</li>
  <li>Acesse a pasta do projeto e execute o arquivo main.py com o seguinte comando:</li>
  <h4>Linux:</h4>
  <pre><code>python3 main.py</code></pre>
  <h4>Windows:</h4>
  <pre><code>py main.py</code></pre>
  <li>Caso queira realizar testes unitarios, acesse a pasta raiz do projeto e execute o seguinte comando:</li>
  <h4>Linux:</h4>
  <pre><code>python3 -m unittest discover tests</code></pre>
  <h4>Windows:</h4>
  <pre><code>py -m unittest discover .\tests</code></pre>
  <li>A API estará disponível no endereço http://localhost:5000. Você pode acessar a documentação da API pelo Swagger UI no endereço http://localhost:5000/apidocs.</li>
</ol>

<h2>Estrutura do Projeto</h2>

<ul>
  <li>lattes-identifier-api
    <ul>
      <li>main.py</li>
      <li>requirements.txt</li>
      <li>README.md</li>
      <li>swagger.yml</li>
      <li>tests
        <ul>
          <li>TestLattesController.py</li>
          <li>TestLattesService.py</li>
        </ul>
      </li>
      <li>config
        <ul>
          <li>config_service.py</li>
          <li>db_config.txt</li>
        </ul>
      </li>
      <li>controller
        <ul>
          <li>lattes_controller.py</li>
        </ul>
      </li>
      <li>service
        <ul>
          <li>lattes_service.py</li>
        </ul>
      </li>
      <li>static
        <ul>
          <li>lattes_transformed.csv</li>
        </ul>
      </li>
    </ul>
  </li>
</ul>

<h2>Endpoint</h2>

<h3>Validação de número de identificação Lattes</h3>

<p>Este endpoint realiza a validação de um número de identificação Lattes, verificando se o mesmo existe no banco de dados MySQL ou no arquivo CSV.</p>

<ul>
  <li>URI: /lattes/{lattes_number}</li>
  <li>Método: GET</li>
  <li>Parâmetro:</li>
  <ul>
    <li>lattes_number (obrigatório): Número de identificação Lattes.</li>
  </ul>
  <li>Respostas:</li>
  <ul>
    <li>200 OK: Retorna uma mensagem informando que o número de identificação Lattes é válido.</li>
    <li>404 Not Found: Retorna uma mensagem informando que o número de identificação Lattes não foi encontrado.</li>
  </ul>
</ul>

<h2>Documentação</h2>

<p>A documentação completa da API pode ser acessada através do Flasgger, baseado em Swagger, disponível no endereço http://localhost:5000/apidocs.</p>

<h2>Licença</h2>

<p>Este projeto está licenciado sob a Licença Apache 2.0 - consulte o arquivo <a href="https://github.com/GOGoncalves/lattes-identifier-service/blob/main/LICENSE.md">LICENSE</a> para obter mais detalhes.</p>

<a href="https://app.fossa.com/projects/git%2Bgithub.com%2Fgogoncalves%2Flattes-identifier-api?ref=badge_large" alt="FOSSA Status"><img src="https://app.fossa.com/api/projects/git%2Bgithub.com%2Fgogoncalves%2Flattes-identifier-api.svg?type=large"/></a>
