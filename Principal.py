from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QTextEdit, QPushButton
import pandas as pd
import subprocess
import matplotlib.pyplot as plt
from Estoque import MostrarEstoque
import Adc_Rmv


class Janela(QMainWindow):
    def __init__(self):
        super().__init__()

        # --------------------------------------------------------------------------------------------------------------

        #                                           ATRIBUTOS DA CLASSE

        # --------------------------------------------------------------------------------------------------------------

        self.setWindowTitle('ReprovadoStock')
        self.setGeometry(100, 100, 403, 670)
        self.setMinimumSize(403, 670)
        self.setMaximumSize(403, 670)

        icone = QIcon('Imagens/icone.png')

        self.setWindowIcon(icone)

        self.create_menu_bar()

        self.terminal = QTextEdit()
        self.terminal.setReadOnly(True)
        self.terminal.setGeometry(3, 375, 396, 250)
        self.terminal.setStyleSheet('font-size: 14px;'
                                    'background-color: black;'
                                    'color: white;')
        self.terminal.setParent(self)

        stock = QPushButton('Estoque', self)
        stock.move(3, 50)
        stock.setFixedSize(196, 150)
        stock.clicked.connect(self.mostra_estoque)
        stock.setStyleSheet('font-size: 20px;')

        graf = QPushButton('Gráfico', self)
        graf.move(203, 50)
        graf.setFixedSize(196, 150)
        graf.clicked.connect(self.Gerar_Grafico)
        graf.setStyleSheet('font-size: 20px;')

        Adc = QPushButton('Adicionar Itens', self)
        Adc.move(3, 204)
        Adc.setFixedSize(196, 150)
        Adc.clicked.connect(self.Adc_Item)
        Adc.setStyleSheet('font-size: 20px;')

        Rmv = QPushButton('Remover Itens', self)
        Rmv.move(203, 204)
        Rmv.setFixedSize(196, 150)
        Rmv.clicked.connect(self.Rmv_Item)
        Rmv.setStyleSheet('font-size: 20px;')

        self.show()

    # ------------------------------------------------------------------------------------------------------------------

    #                                             ▶ MÉTODOS DA CLASSE ◀

    # ------------------------------------------------------------------------------------------------------------------

    #                                              → ADICIONAR ITENS ←

    # ------------------------------------------------------------------------------------------------------------------

    def Adc_Item(self):
        self.adicionar = Adc_Rmv.Adc()
        self.adicionar.show()

    # ------------------------------------------------------------------------------------------------------------------

    #                                              → REMOVER ITENS ←

    # ------------------------------------------------------------------------------------------------------------------

    def Rmv_Item(self):
        self.remover = Adc_Rmv.Rmv()
        self.remover.show()

    # ------------------------------------------------------------------------------------------------------------------

    #                                                    → MENU ←

    # ------------------------------------------------------------------------------------------------------------------
    def create_menu_bar(self):
        barra_menu = self.menuBar()
        barra_menu.setStyleSheet("background-color: #202123;"
                                 "color: white;")

        # Criar menu "Arquivo"
        menu_arquivo = barra_menu.addMenu('Arquivo')

        Gera_Exce = QAction('Gerar planilha', self)
        Gera_Exce.triggered.connect(self.Gerar_Planilha)
        menu_arquivo.addAction(Gera_Exce)

        # Criar menu "Configurações"
        menu_config = barra_menu.addMenu('Configurações')

        AtivaBot = QAction('Ativar Bot', self)
        AtivaBot.triggered.connect(self.AtivarBot)
        menu_config.addAction(AtivaBot)

        DesativaBot = QAction('Desativar Bot', self)
        DesativaBot.triggered.connect(self.DesativarBot)
        menu_config.addAction(DesativaBot)

        # Criar menu "Ajuda"
        menu_ajuda = barra_menu.addMenu('Ajuda')

        # Criar ação "Sobre"
        acao_sobre = QAction('Sobre', self)
        acao_sobre.setStatusTip('Sobre o aplicativo')
        acao_sobre.triggered.connect(self.abrir_sobre)
        menu_ajuda.addAction(acao_sobre)

    # ------------------------------------------------------------------------------------------------------------------

    #                                                → PLANILHA ←

    # ------------------------------------------------------------------------------------------------------------------

    def Gerar_Planilha(self):
        # Use: pip install openpyxl
        df = pd.read_csv('produtos/estoque.csv')
        df.to_excel('estoque.xlsx', index=False)
        self.terminal.append('Planilha baixada')

    # ------------------------------------------------------------------------------------------------------------------

    #                                               → GERAR GRÁFICO ←

    # ------------------------------------------------------------------------------------------------------------------

    def Gerar_Grafico(self):
        arquivo = 'produtos/estoque.csv'
        data = pd.read_csv(arquivo)
        produto = data['Produto']
        quantidade = data['Quantidade']

        plt.bar(produto, quantidade)
        plt.title('Estoque')
        plt.xlabel('Produto')
        plt.ylabel('Quantidade')
        plt.xticks(rotation=90)
        plt.subplots_adjust(top=0.955, bottom=0.335, left=0.045, right=0.975, hspace=0.2, wspace=0.2)
        plt.show()
        self.terminal.append('Grafico gerado')

    # ------------------------------------------------------------------------------------------------------------------

    #                                              → MOSTRAR ESTOQUE ←

    # ------------------------------------------------------------------------------------------------------------------

    def mostra_estoque(self):
        self.JanelaEstoque = MostrarEstoque()
        self.JanelaEstoque.show()
        self.terminal.append('Estoque aberto.')

    def AtivarBot(self):
        import webbrowser
        webbrowser.open('https://discord.com/channels/1108748610318893137/1110692980093878314')
        caminho_arquivo = 'Bot.py'
        subprocess.Popen(['start', 'cmd', '/k', 'python', caminho_arquivo], shell=True)
        self.terminal.append('Bot ativado')

    def DesativarBot(self):
        import psutil
        filename = "Bot.py"
        for process in psutil.process_iter(['pid', 'name']):
            if process.info['name'] == 'python.exe' and process.cmdline()[-1] == filename:
                pid = process.info['pid']
                process.terminate()
                break
        processos = psutil.process_iter()
        terminais = [p for p in processos if p.name().lower() == 'cmd.exe' or p.name().lower() == 'powershell.exe']
        for terminal in terminais:
            terminal.terminate()
        self.terminal.append('Bot desativado')

    # ------------------------------------------------------------------------------------------------------------------

    def abrir_sobre(self):
        self.terminal.append('''
        
Data de Entrega: 01/06/2023
Apresentação: 08/06/2023

Uma ideia de trabalho complexo que envolva orientação a objetos e Python é o desenvolvimento de um sistema de 
gerenciamento de estoque para uma empresa de comércio eletrônico. O objetivo é criar um sistema que permita aos usuários
gerenciar o estoque de produtos, as vendas e as compras de forma eficiente.

Para isso, você pode explorar vários conceitos de orientação a objetos, como encapsulamento, herança, polimorfismo e 
abstração. Além disso, o trabalho pode envolver o uso de estruturas de dados complexas, como árvores de busca, tabelas 
hash e listas ligadas.

O sistema deve permitir que os usuários façam o cadastro de produtos, realizem compras e vendas, consultem o estoque, 
gerem relatórios e façam outras operações relevantes para o negócio. Além disso, é importante que o sistema seja 
otimizado para garantir uma boa performance, mesmo com um grande volume de dados.

Para tornar o trabalho mais atual e relevante para o mercado de trabalho, você pode incluir o uso de ferramentas como 
Django ou Flask para criar uma API REST para o sistema, permitindo que outras aplicações possam consumir seus serviços.

''')

    # ------------------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    app = QApplication([])
    janela = Janela()
    app.exec_()
