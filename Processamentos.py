import csv


class estoque:
    def __init__(self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def adicionar_produto(self):
        with open('produtos/estoque.csv', 'r', newline='', encoding='UTF-8') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
        self.nome = self.nome.lower().strip()
        for row in rows:
            if row[0].lower().strip() == self.nome:
                estoque_atual = int(row[1])
                row[1] = str(estoque_atual + int(self.quantidade))
                row[2] = self.preco
                with open('produtos/estoque.csv', 'w', newline='', encoding='UTF-8') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerows(rows)
                print(f'{self.quantidade} unidades de {self.nome} foram adicionadas ao estoque.')
                return

        # Se o produto não existe no CSV, adiciona um novo registro
        with open('produtos/estoque.csv', 'a', newline='', encoding='UTF-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([self.nome, self.quantidade, self.preco])

    def retirar_produto(self, nome, quantidade):
        with open('produtos/estoque.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)

        nome = nome.lower().strip()  # ajusta o nome para comparar com o CSV

        for row in rows:
            row_nome = row[0].lower().strip()  # ajusta o nome do CSV para comparar com o parâmetro
            if row_nome == nome:
                estoque_atual = int(row[1])
                if estoque_atual >= quantidade:
                    row[1] = str(estoque_atual - quantidade)
                    with open('produtos/estoque.csv', 'w', newline='', encoding='UTF-8') as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerows(rows)
                    print(f'{quantidade} unidades de {nome} foram retiradas do estoque.')
                    return
                else:
                    print(
                        f'Não é possível retirar {quantidade} unidades de {nome}. Apenas {estoque_atual} unidades estão disponíveis no estoque.')
                    return

        print(f'{nome} não encontrado no estoque.')

