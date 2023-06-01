from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QLabel, QPushButton, QComboBox
import csv
import Processamentos


class Adc(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Adicionar Item')
        self.setGeometry(100, 100, 403, 270)
        self.setMinimumSize(403, 270)
        self.setMaximumSize(403, 270)

        icone = QIcon('Imagens/icone.png')
        self.setWindowIcon(icone)

        self.tipo_label = QLabel('Tipo:', self)
        self.tipo_label.move(30, 30)
        self.tipo_label.setStyleSheet('font-size: 20px')

        self.combobox = QComboBox(self)
        self.combobox.move(100, 30)
        self.combobox.setFixedWidth(280)

        self.carregar_nomes()

        self.nome_label = QLabel('Nome:', self)
        self.nome_label.move(30, 80)
        self.nome_label.setStyleSheet('font-size: 20px')

        self.nome_edit = QLineEdit(self)
        self.nome_edit.move(100, 80)
        self.nome_edit.setFixedSize(230, 30)
        self.nome_edit.setFixedWidth(280)

        self.quantidade = QLabel('Quantidade:', self)
        self.quantidade.move(30, 130)
        self.quantidade.setFixedWidth(150)
        self.quantidade.setStyleSheet('font-size: 20px')

        self.quantidade_edit = QLineEdit(self)
        self.quantidade_edit.move(150, 130)
        self.quantidade_edit.setFixedSize(230, 30)
        self.quantidade_edit.setStyleSheet('font-size: 17px')

        self.preco = QLabel('Preço:', self)
        self.preco.move(30, 180)
        self.preco.setFixedWidth(150)
        self.preco.setStyleSheet('font-size: 20px')

        self.preco_edit = QLineEdit(self)
        self.preco_edit.move(100, 180)
        self.preco_edit.setFixedSize(280, 30)
        self.preco_edit.setStyleSheet('font-size: 17px')

        def Salvar():
            try:
                Processamentos.adicionar(
                    self.nome_edit.text(),
                    int(self.quantidade_edit.text()),
                    self.preco_edit.text(),
                    self.combobox.currentText()
                )

            except:
                print('ERROR')

        ok_button = QPushButton('OK', self)
        ok_button.move(30, 220)
        ok_button.setFixedSize(350, 30)
        ok_button.clicked.connect(Salvar)

        self.show()

    def carregar_nomes(self):
        tipos = ['Desktop', 'Notebook', 'Smartphone', 'Video game']
        for tipo in range(len(tipos)):
            self.combobox.addItem(tipos[tipo])


class Rmv(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Remover Item')
        self.setGeometry(600, 100, 403, 200)
        self.setMinimumSize(403, 200)
        self.setMaximumSize(403, 200)

        icone = QIcon('Imagens/icone.png')
        self.setWindowIcon(icone)

        self.nome_label = QLabel('Nome:', self)
        self.nome_label.move(30, 30)
        self.nome_label.setStyleSheet('font-size: 20px')

        self.combobox = QComboBox(self)
        self.combobox.move(100, 30)
        self.combobox.setFixedWidth(280)

        self.carregar_nomes()

        self.quantidade = QLabel('Quantidade:', self)
        self.quantidade.move(30, 80)
        self.quantidade.setFixedWidth(150)
        self.quantidade.setStyleSheet('font-size: 20px')

        self.quantidade_edit = QLineEdit(self)
        self.quantidade_edit.move(150, 80)
        self.quantidade_edit.setFixedSize(230, 30)
        self.quantidade_edit.setStyleSheet('font-size: 17px')

        def Salvar():
            try:
                Processamentos.remover(
                    self.combobox.currentText(),
                    int(self.quantidade_edit.text()),
                )
            except:
                print('ERROR')

        ok_button = QPushButton('OK', self)
        ok_button.move(30, 130)
        ok_button.setFixedSize(350, 30)
        ok_button.clicked.connect(Salvar)

        self.show()

    def carregar_nomes(self):
        with open('produtos/estoque.csv', 'r', encoding='utf-8') as arquivo_csv:
            leitor_csv = csv.reader(arquivo_csv)
            cabecalho = next(leitor_csv)  # Ignorar a linha do cabeçalho
            for linha in leitor_csv:
                nome = linha[0]  # Nome está na primeira coluna do CSV
                self.combobox.addItem(nome)
