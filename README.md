# ReprovadoStock

![logo_horizontal_univasso](https://github.com/YagoTarsin/ReprovadoStock/assets/102929131/21da1cfd-9758-4120-865c-649148df673c)

Curso: Engenharia de software <br>
Matéria: Programação orientada a objeto<br>
Professor: Fabricio <br>
Aluno: Yago Guimarães Tavares <br>
Matricula: 202211459 <br>
Período: 3º Período <br>

## Dependências de bibliotecas para utilização

- PyQt5 (Interface)
- Pandas (Manipulação dos dados)
- subprocess (executar bot em subprocesso)
- Matplotlib (Gerador do gráfico)
- discord (Bot do discord)
- csv (Trabalhar com arquivo .csv)
- asyncio (Tabalhar com funções asyncio)
- psutil (Fechar corretamente o subprocesso do bot)
- webbrowser (Abrir link do discord)
- openpyxl (Baixar planilha excell)

## Introdução

ReprovadoStock é um sistema para um trabalho da faculdade. Sua ideia é ser estoque inteligente com vendas automáticas dentro do discord através de um bot. O app é totalmente uma simulação, as vendas não acontecem de verdade apenas notifica que a venda foi concluída e retira 1 produto do estoque.

## Uso

O programa deve ser executado no arquivo "Principal.py" no qual abre sua interface principal. Nela temos alguns botões que dão suas funcionalidades.

## Interface principal

A Interface principal é simples e intuitiva, irei mostrar a funcionalidade de cada parte do programa.

![image](https://github.com/YagoTarsin/ReprovadoStock/assets/102929131/0fddc697-f230-4a03-9f44-9b69f8e334c3)

## Estoque

No botão "Estoque" é executada a função para ler todo o arquivo csv do estoque e nos gerar uma tela tabelada com: Produto, Quantidade e Preço.

![image](https://github.com/YagoTarsin/ReprovadoStock/assets/102929131/7c30b325-d7f4-4dec-903c-ff53cb09986a)

## Gráfico

No botão "Gráfico" é executada a função para ler todo o arquivo csv do estoque e plotar um gráfico intuitivo tratando nome e quantidade de cada produto.

![image](https://github.com/YagoTarsin/ReprovadoStock/assets/102929131/c1ff57b3-dcf6-4247-9d8c-2a6cc74d05de)

## Adicionar Itens

No botão "Adicionar Itens" é onde podemos adicionar um item novo ao estoque dando também sua quantidade, tipo e preço para adicionar ao estoque. Também pode adicionar mais quantidade a itens já existentes assim como alterar seu respectivo preço.

![image](https://github.com/YagoTarsin/ReprovadoStock/assets/102929131/d911e177-9b71-4ed2-9675-b69ef0062da2)

## Remover Itens

No botão "Remover itens" é onde removemos itens do estoque especificando o nome do produto e a quantidade a ser retirada.

![image](https://github.com/YagoTarsin/ReprovadoStock/assets/102929131/d0631a3d-11d3-4b9d-aac7-b3dfcef52c93)

## Arquivo

Em "Arquivo" no menu acima teremos a opção "Gerar planilha" aonde executa uma função para gerar uma planilha excell do arquivo csv do estoque.

![image](https://github.com/YagoTarsin/ReprovadoStock/assets/102929131/23618b96-37ea-45e3-b610-9fca3a2d54cb)

## Configurações

Em "Configurações" no menu acima teremos duas opções:
- Ativar bot
- Desativar bot

Como os proprios nomes ja diz, é aonde mudamos o estado do bot para ativado ou desativado. Inicialmente o bot vem desativado por padrão e só é ativado quando clicamos no botão de ativar. o Bot será aberto em outro terminal como subprocesso e já abrindo o link para o canal no discord:

![image](https://github.com/YagoTarsin/ReprovadoStock/assets/102929131/48a1f0b1-c081-488f-bee3-91242aeca7c7)

O bot é aberto no terminal dessa forma:

![image](https://github.com/YagoTarsin/ReprovadoStock/assets/102929131/eff2086d-a6eb-4c0f-8d50-347fec386970)

Quando o bot é desativado a janela do terminal é fechada e bot para de funcionar.

## Sobre

Em "Sobre" no menu acima, é onde irá mostrar o que foi pedido pelo professor fabricio:

![image](https://github.com/YagoTarsin/ReprovadoStock/assets/102929131/39596197-56bd-4349-af54-569691e3fc4c)

## Uso do bot

O bot pode ser encontrado no canal do discord: https://discord.com/channels/1108748610318893137/1113845312000376994

Pode ser usado tanto diretamente no canal como no privado do bot para maior privacidade.

O bot executa apenas 2 comandos: !ajuda e !produtos

Executando o comando !produtos o bot irá dar 4 opções de tipos de produtos:

![image](https://github.com/YagoTarsin/ReprovadoStock/assets/102929131/96084b18-ba21-4f9a-aec6-b261bc5de099)

Para selecionar o tipo de produto é necessário apenas reagir ao emoji que corresponde ao tipo de produto interessado e ele irá listar todos os produtos disponíveis daquele tipo assim como seus respectivos preços:

![image](https://github.com/YagoTarsin/ReprovadoStock/assets/102929131/932bddd6-511c-4215-a174-90fb0956633c)

Para selecionar o produto interessado, digite o número correspondente ao produto e ele irá fazer a simulção de venda assim como retirar do estoque 1 unidade do produto escolhido.

![image](https://github.com/YagoTarsin/ReprovadoStock/assets/102929131/60cabf57-131b-400a-a708-52f8f744d95c)

Obs: Existe um delay de 5 segundos para selecionar o produto interessado, uma falha que não deu tempo de contornar até o fim do prazo do trabalho.



