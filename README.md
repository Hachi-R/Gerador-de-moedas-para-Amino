
<br>
<h1 align="center"> <br>
  <a href="https://github.com/Hachi-R/Gerador-de-moedas-para-Amino"> <img src="https://i.ibb.co/2vs0mW0/Sem-t-tulo82.jpg" alt="Coin img" width="300"></a><br>
    
Machine Coin<br><br>
![GitHub repo size](https://img.shields.io/github/repo-size/Hachi-R/Gerador-de-moedas-para-Amino?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/Hachi-R/Gerador-de-moedas-para-Amino?style=for-the-badge)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Doker?color=green&logo=python&logoColor=white&style=for-the-badge)
[![GitHub license](https://img.shields.io/github/license/Hachi-R/Gerador-de-moedas-para-Amino?color=red&style=for-the-badge)](https://github.com/Hachi-R/Gerador-de-moedas-para-Amino/blob/main/LICENSE)

</h1>
        
## 🚩 O que é isso?
O Machine Coin é um *exploit*, que através da **API [Amino.py](https://github.com/Slimakoi/Amino.py)**, utiliza um ou mais "_bots do Amino_" para farmar uma determinada quantidade de **Amino Coins**. Esse processo é feito através de um scrip em Python, que se aproveitando de inúmeras vulnerabilidades existentes no aplicativo, as usa para coordenar um grupo de bots à **visualização de anúncios na plataforma**, enquanto se passam por **usuários comuns** do aplicativo.    
    
<br>
    
## 🕵️‍♂️ Atenção?
### Eu só fui escrevendo e escrevendo isso aqui e dps desanimei por uns motivos aí, por isso ainda não tá bem organizado e tá cheio de erros de português. De qualquer forma, é só ler direitinho e não ser uma mula que dá tudo certo. Eu fiquei com preguiça de fazer o tópico de usabilidade dentro do script, mas é só seguir os passos e se for fazer no celular usa o pydroid que é mais fácil.</a>
 
<br>
    
## 💻 Pré-requisitos
##### <b>Atenção:</b> Os links para download de todos os recursos necessários estarão listados <a href="#d">aqui.</a>
Tenha certeza de escolher **apenas um aplicativo** para realizar o processo, pois **não é necessário** o uso de dois ou mais deles. Também tenha certeza de atender a **todos os pré-requisitos** da sua plataforma escolhida antes de iniciar a instalação, assim evitando possíveis frustrações.

<br>
    
- ## [Termux (Android)](https://f-droid.org/packages/com.termux/)
  | Ter uma versão recente do Termux instalada no seu dispositivo.            |
  |------------------------------------------------------------------------------|
  | Não estar usando a versão da Play Store, e sim a do FDroid, disponível aqui. |
  | Ter um smartphone com Android 7.0 ou superior.                               |
  
  <br>
    
- ## [Pydroid 3 (Android)](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3&hl=pt_BR&gl=BR)
  | Ter uma versão recente do Pydroid instalada no seu dispositivo.                   |
  |--------------------------------------------------------------------------------------|
  | Ter uma versão recente do [Pydroid repository plugin](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3.quickinstallrepo&hl=pt_BR&gl=BR) instalada no seu dispositivo.     |
  |Ter um smartphone com Android 6.0 ou superior.                                        |
 
  <br>
    
- ## [VS Code (Windows, Mac OS e Linux)](https://code.visualstudio.com/)
  | Ter uma versão recente do VS Code instalado no seu computador.                               |
  |-------------------------------------------------------------------------------------------------|
  | Ter alguma versão do [Python 3](https://python.org/) instalada no seu computador. Recomendado Python 3.8 ou 3.9 |
  | Ter uma versão recente do [Git](https://git-scm.com/) instalado no seu PC.             <div id="d"></div>             |
  | Possuir um PC com Windows 7+, Mac OS 10.10+ ou alguma versão compatível de Linux.                    |

<br>  
    
## 📂 Downloads 
- ## Android.
1. [Termux]()
2. [Pydroid 3](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3&hl=pt_BR&gl=BR)
3. [Pydroid repository plugin](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3.quickinstallrepo&hl=pt_BR&gl=BR)
    
    <br>

- ## Windows, Mac OS e Linux.
1. [VS Code](https://code.visualstudio.com/Download)
2. [Python](https://www.python.org/downloads/)
3. [Git](https://git-scm.com/downloads)
    
    <br>

- ## Gerador.
1. [Machine Coin](https://github.com/Hachi-R/Gerador-de-moedas-para-Amino/archive/refs/tags/1.5.zip)
    
<br>    
    
## 💿 Instalação

## Termux:
- Crie uma pasta na raiz do seu dispositivo, entitulada **"termux"**, em seguida, abra o aplicativo e execute os seguintes comandos no terminal:

 - ` termux-setup-storage `

 - Após isso, conceda a permissão de acesso ao armazenamento e siga para os seguintes comandos, **executando um por vez**:

 - ` cd storage/shared/termux `

 - ` apt upgrade && apt update -y `

 - ` pkg install python -y `

 - ` pkg install git -y `

 - ` pip install colorama `
 
 - ` pip install hashlib `

 - ` pip install amino.py==1.2.17 `

 - ` git clone https://github.com/Hachi-R/Gerador-de-moedas-para-Amino `

- ### Tudo pronto, agora siga para <a href="#i"> funcionamento. </a><br>

## Pydroid:
- Extraia na raiz do seu dispositivo o arquivo `Machine_Coin.zip`, que você baixou [aqui](#d).

- Abra o aplicativo e clique nas três barras, do canto superior direito e, após isso, selecione a opção `"Pip"`.

- Agora clique em `"Library name"`, e cole os comandos a seguir, lembrando-se de colar apenas um comando por vez e pressionar `"INSTALL"` a cada comando.

- ` colorama `

- ` hashlib `

- ` amino.py==1.2.17 ` 

- ### Tudo pronto, agora siga para <a href="#i"> funcionamento. </a><br>

## VS Code:
- Comece instalado a extenção do Python no marketplace do VS Code, usando (`Ctrl + Shift + X`), e depois pesquisando por: `Python`.

- Após isso, crie uma pasta e a abra utilizando (`Ctrl + K` e `Ctrl + O`)

- Agora abra um terminal, pressionando (`Ctrl + Shift + '`), depois espere o terminal carregar e digite os seguintes comandos:

- `pip install colorama`
- `pip install amino.py==1.2.17`
- `pip install hashlib`

- Agora clone este repositorio, usando as teclas (`Ctrl + Shift + G`), e selecionando a opção `Clone Repository`.

- Após clicar em `Clone Repository`, cole essa url: `https://github.com/Hachi-R/Gerador-de-moedas-para-Amino` na caixa que aparecerá na parte superior da sua tela, em seguida, presione a tecla enter e aguarde.

- ### Tudo pronto, agora siga para <a href="#i"> funcionamento. </a><br>

 <div id="i"></div><br>

## 📖 Funcionamento 
>### Como isso funciona?
>Em poucas palavras, esse script utiliza uma ou mais contas do amino, para se passar por um usuario comum e vizualiar os anuncios da plataforma, assim gerando diariamente uma certa quantidade de amino coins.


>### Quanto isso rende em moedas?
>A quantidade de moedas geradas pelo script depende de quantas contas você estiver utilizando para farmar, pois cada conta gera entre 97 e 100 moedas diarias, mais ou menos.
>
>### Exemplos:
>1 conta = 97 ~ 100 AC's por dia. <br>
>
>5 contas = 485 ~ 500 AC's por dia. <br>
>
>10 contas = 970 ~ 1.000 AC's por dia. <br>
>
>30 contas = 2.910 ~ 3.000 AC's por dia. <br>
>
>50 contas = 4.850 ~ 5000 AC's por dia. <br>
>
>100 contas = 9.700 ~ 10.000 AC's por dia.

>### Quando eu as recebo?
>As moedas são entregues pelo amino todos os dias entre às 21:00 e 22:00 horas do GTM-03:00, em suas respectivas contas. Após isso, você deve executar o script no modo de recebimento para mandar todas as moedas para a sua conta principal.

>### Exemplificação do processo de farm:
>1. O script é executado:
><img src="https://raw.githubusercontent.com/Hachi-R/assets/main/IMG_20210728_170535.png">

<br>

>2. As moedas chegam no modulo de anuncios do amino:
><img src="https://raw.githubusercontent.com/Hachi-R/assets/main/IMG_20210728_170746.png">

<br>

>3. As moedas são entregues às 22:00 e você continua gerando até ficar rico 😎:
><img src="https://raw.githubusercontent.com/Hachi-R/assets/main/IMG_20210728_170437.png">

<div id="u">
<br>
    
## 📚 Usabilidade
## E-mails e contas:
- ### Antes de rodar o script pela primeira vez, é necessario criar um arquivo .txt entitulado de `emails`, com os emails das contas que você usará para farmar. Eles deverão ser colocdos em fileira, e não em linha unica. Além disso, também não poderão haver spaços no arquivo.

<br>

- ## **AVISOS IMPORTANTES**
  1. Todas as contas precisam possuir a mesma senha.

  2. Todas as contas precisam estar na mesma comunidade

  3. Todas as contas precisam estar verificadas.

  4. O envio de moedas deve sempre ser feito para um blog, nunca para uma wiki, quiz, enquete etc.

  5. O envio de moedas deve sempre ser feito para uma conta de nivel 5 ou posterior. 

<br>

## Como iniciar o Script
- ### Termux
  1. Primeiro, se for a primeira vez executando o script, coloque o arquivo `emails.txt` na pasta do termux. Se já tiver feito isso, pule para aproxima etapa.

  2. Abra o aplicativo execute os seguintes comandos.

  3. `cd storage/shared/termux`
  4. `cd Gerador-de-moedas-para-Amino`
  5. `python Machine Coin.py`

     >#### Siga lendo para as instruções de como usar.

<br>

- ### Pydroid 
  1. Coloque o arquivo `emails.txt` dentro da pasta do Machine Coin, que você extraiu. 
  
  2. Em seguida, clique na pasta no canto superior direito e selecione a opção `"Open"`. Em seguida, vá para a pasta do Machine Coin e selecione o arquivo `"Machine Coin.py"`.
     >#### Siga lendo para instruções de como usar.

<br>

- ### VS Code
  1. Abra o VS Code, e abra a pasta que você criou, usando (`Ctrl + K`) e (`Ctrl + O`).

  2. Crie um novo arquivo nessa pasta usando (`Ctrl + N`) e o nomeie de `emails.txt.`

  3. Abra o arquivo `"Machine Coin.py"` e o execute clicando na seta verde do canto superior direito.
     >#### Siga lendo para instruções de como usar.

  <br> 
  
## 🧡 Créditos

<br><br>

<div align="center" class="S2">
<h2>Meus agradecimentos ao Slimakoi, pela <B>API <a href="https://github.com/Slimakoi/Amino.py">Amino.py</B></a>
 e ao Lil Zevi, pela <B>coingeneratorfunctions.py</B> e a base desse sscript!
</h2>
<br>
 </div>

<div class="tb" align="center">
<table>
<tr>
<td align="center">
<a href="https://github.com/Slimakoi">
<img src="https://avatars.githubusercontent.com/u/24621566?v=4" width="150px;" alt="slimakoi"/><br>
<sub>
<b>SlimaKoi</b>
</sub>
</a>
</td>
<td align="center">
<a href="https://github.com/LilZevi">
<img src="https://avatars.githubusercontent.com/u/77536370?v=4" width="150px;" alt="lil zevi"/><br>
<sub>
<b>Lil Zevi</b>
</sub>
</a>
</td>
</tr>
</table>
</div>
  
  <br>
  
## 📝 Licença e Copyrigth
### Esse repositorio e suas dependencias, incluindo os seus arquivos, estão sob a licença AGPL-3.0

### Clique em [licença](https://github.com/Hachi-R/Gerador-de-moedas-para-Amino) para ler a respeito e, entender o que você pode ou não fazer com os arquivos desse repositorio.
<hr>
<br>

#### Fique web rico e seja feliz! 😉      
