import csv
from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QAbstractItemView
from PyQt5.QtGui import QIcon


# ----------------------------------------------------------------------------------------------------------------------


class MostrarEstoque(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Estoque')
        self.setGeometry(1200, 100, 500, 750)
        self.setMinimumSize(440, 750)

        icone = QIcon('Imagens/icone.png')
        self.setWindowIcon(icone)

        # Cria uma tabela com 3 colunas
        self.table = QTableWidget()
        self.table.setColumnCount(3)

        # Adiciona cabeçalhos para as colunas
        self.table.setHorizontalHeaderLabels(['Produto', 'Quantidade', 'Preço/R$'])

        # Lê os dados do arquivo CSV
        with open('produtos/estoque.csv', newline='', encoding='UTF-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for linha in reader:
                self.table.insertRow(self.table.rowCount())
                for i, field in enumerate(linha):
                    if linha == ['Produto', 'Quantidade', 'Preço']:
                        pass
                    else:
                        item = QTableWidgetItem(field)
                        self.table.setItem(self.table.rowCount() - 1, i, item)
        self.setCentralWidget(self.table)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)

