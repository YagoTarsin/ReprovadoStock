import pandas as pd

def adicionar(nome_produto, quantidade_adicional, preco=None, tipo_produto=None):
    # Verifica se o tipo de produto é válido
    tipos_validos = ['Desktop', 'Notebook', 'Video game', 'Smartphone']
    if tipo_produto not in tipos_validos:
        print('Tipo de produto inválido!')
        return

    # Carrega o arquivo CSV do estoque completo
    df_estoque = pd.read_csv('produtos/estoque.csv')

    # Verifica se o produto já existe no estoque completo
    filtro_estoque = df_estoque['Produto'] == nome_produto
    if filtro_estoque.any():
        # Atualiza a quantidade do produto no estoque completo
        df_estoque.loc[filtro_estoque, 'Quantidade'] += quantidade_adicional

        # Verifica se um novo preço foi fornecido
        if preco is not None:
            # Converte o preço para float e atualiza no estoque completo
            preco = float(preco)
            df_estoque.loc[filtro_estoque, 'Preço'] = preco
    else:
        # Cria um novo registro para o produto no estoque completo
        novo_registro = {'Produto': nome_produto, 'Quantidade': quantidade_adicional, 'Preço': preco}
        df_estoque = df_estoque.append(novo_registro, ignore_index=True)

    # Salva o estoque completo de volta no arquivo CSV
    df_estoque.to_csv('produtos/estoque.csv', index=False)

    # Verifica se o tipo de produto foi fornecido
    if tipo_produto is not None:
        # Carrega o arquivo CSV do tipo de produto
        df_tipo_produto = pd.read_csv(f'produtos/{tipo_produto}.csv')

        # Verifica se o produto já existe no tipo de produto
        filtro_tipo_produto = df_tipo_produto['Produto'] == nome_produto
        if filtro_tipo_produto.any():
            # Verifica se um novo preço foi fornecido
            if preco is not None:
                # Converte o preço para float e atualiza no tipo de produto
                preco = float(preco)
                df_tipo_produto.loc[filtro_tipo_produto, 'Preço'] = preco
        else:
            # Cria um novo registro para o produto no tipo de produto
            novo_registro = {'Produto': nome_produto, 'Preço': preco}
            df_tipo_produto = df_tipo_produto.append(novo_registro, ignore_index=True)

        # Salva o tipo de produto de volta no arquivo CSV
        df_tipo_produto.to_csv(f'produtos/{tipo_produto}.csv', index=False)

# Exemplo de uso da função adicionar
adicionar('Desktop Computer HP Pavilion Gaming', 5, '1399.99', 'Desktop')
