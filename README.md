
<br>
<h1 align="center"> <br>
  <a href="https://github.com/Hachi-R/Gerador-de-moedas-para-Amino"> <img src="https://i.ibb.co/2vs0mW0/Sem-t-tulo82.jpg" alt="Coin img" width="300"></a><br>
    
Machine Coin<br><br>
![GitHub repo size](https://img.shields.io/github/repo-size/iuricode/README-template?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/Hachi-R/Gerador-de-moedas-para-Amino?style=for-the-badge)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Doker?color=green&logo=python&logoColor=white&style=for-the-badge)
[![GitHub license](https://img.shields.io/github/license/Hachi-R/Gerador-de-moedas-para-Amino?color=red&style=for-the-badge)](https://github.com/Hachi-R/Gerador-de-moedas-para-Amino/blob/main/LICENSE)

</h1>
        
## 🚩 O que é isso?
O Machine Coin é um **exploit**, que através da **API [Amino.py](https://github.com/Slimakoi/Amino.py)**, utiliza um ou mais "_bots do Amino_" para farmar uma determinada quantidade de **Amino Coins**. Esse processo é feito através de um scrip em Python, que aproveitando-se de inúmeras vulnerabilidades existentes no aplicativo, as usa para coordenar um grupo de bots à **visualização de anúncios dentro da plataforma**, enquanto se passam por **usuários comuns** do aplicativo.    
    
<br>
    
## 🕵️‍♂️ Como isso funciona?
### Para detalhes de funcionamento e usabilidade, vá para: <a href="#i">Usabilidade.</a>
 
<br>
    
## 💻 Pré-requisitos
##### <b>Atenção:</b> Os links para download de todos os recursos necessarios estarão listados <a href="#d">aqui.</a>
Tenha certeza de escolher **apenas um aplicativo** para realizar o processo, pois **não é necessario** o uso de dois ou mais deles. também tenha certeza de atender **todos os pré-requisitos** da sua plataforma escolhida antes de iniciar a instalação, assim evitando possiveis frustrações

<br>
    
- ## [Termux (Android)](https://f-droid.org/packages/com.termux/)
  | Ter uma versão recente do Termux instalada no seu dispositivo.            |
  |------------------------------------------------------------------------------|
  | Não estar usando a versão da Play Store, e sim a do FDroid, disponivel aqui. |
  |Ter um smartphone com Android 7.0 ou superior                                 |
  
  <br>
    
- ## [Pydroid 3 (Android)](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3&hl=pt_BR&gl=BR)
  | Ter uma versão recente do Pydroid instalada no seu dispositivo.                   |
  |--------------------------------------------------------------------------------------|
  | Ter uma versão recente do [Pydroid repository plugin](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3.quickinstallrepo&hl=pt_BR&gl=BR) instalada no seu dispositivo.     |
  |Ter um smartphone com Android 6.0 ou superior                                         |
 
  <br>
    
- ## [VS Code (Windows, Mac OS e Linux)](https://code.visualstudio.com/)
  | Ter uma versão recente do VS code instalado no seu computador                                |
  |-------------------------------------------------------------------------------------------------|
  | Ter alguma versão do [Python 3](https://python.org/) instalada no seu computador. recomenda-se utilizar o python 3.8 ou 3.9 |
  | Ter uma versão recente do [Git](https://git-scm.com/) instalado no seu PC             <div id="d"></div>             |
  | Possuir um PC com Windows 7+, Mac OS 10.10+ ou uma versão compatível do Linux                     |

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
1. [Machine Coin]()
    
<br>    
    
## 💿 Instalação

## Termux:
- Crie uma pasta na raiz do seu dispositivo, entitulada **"termux"**, em seguida, abra o aplicativo e execute os seguintes comandos no terminal:

 - ` termux-setup-storage `

 - Em seguida, conceda a permissão de acesso ao armazenamento e siga para os seguintes comandos, **executando um por vez**:

 - ` HOME=/storage/shared/termux `

 - ` apt upgrade && apt update -y `

 - ` pkg install python -y `

 - ` pkg install git -y `

 - ` pip install colorama `
 
 - ` pip install hashlib `

 - ` pip install amino.py==1.2.17 `

 - ` git clone https://github.com/Hachi-R/Gerador-de-moedas-para-Amino `

- ### Tudo pronto, agora siga para <a href="#u"> Usabilidade </a><br>

## Pydroid:
- Extraia o arquivo `Machine_Coin.zip` que você baixou aqui, na raiz do seu dispositivo.

- Clique na pasta no canto superior direito e selecione a opção `"Open"`. Em seguida, vá para a pasta do Machine Coin e selecione o arquivo `"Machine Coin.py"`.

- Agora, repita o mesmo processo com os arquivos `"emails.txt"` — falaremos dele em breve, então ignore-o por hora — e `"coingeneratorfunctions.py"`

- Volte para a tela inicial do aplicativo e clique nas três barras do canto superior direito, após isso, selecione a opção `"Pip"`.

- Agora clique em `"Library name"` e cole os comandos a seguir, lembrando de colar apenas um comando por vez e pressionar `"INSTALL"` a cada comando.

- ` colorama `

- ` hashlib `

- ` amino.py==1.2.17 ` 

- ### Tudo pronto, agora siga para <a href="#u"> Usabilidade </a><br>

## VS Code:
- Comece instalado a extenção do Python no marketplace do VS Code com (`Ctrl + Shift + X`) e pesquisando por: `Python`.

- Crie uma pasta e a abra utilizando (`Ctrl + K` e `Ctrl + O`)

- Agora abra um terminal com (`Ctrl + Shift + '`), espere carregar e digite os seguintes comandos:

- `pip install colorama`
- `pip install amino.py==1.2.17`
- `pip install hashlib` (se necesario)

- Agora clone este repositorio usando (`Ctrl + Shift + G`) e apertando em `Clone Repository`.

- Após clicar em `Clone Repository`, cole essa url: `https://github.com/Hachi-R/Gerador-de-moedas-para-Amino` na caixa que aparecerá na parte superior da sua tela, em seguida, presione e a tecla enter e aguarde.

- ### Tudo pronto, agora siga para <a href="#u"> Usabilidade </a><br>

 <div id="u"></div><br>

## 📖 Funcionamento 




<br>
    
## 📚 Usabilidade
 
  <hr> 
  
## 🧡 Créditos
  
  <hr>
  
## 📝 Licença e Copyrigth
    

     
    
     

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#
