import asyncio
import csv
import discord
from discord.ext import commands
from Processamentos import remover

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print('Bot logado em: {0}!'.format(bot.user))


@bot.command()
async def ajuda(ctx):
    await ctx.send('Use: "!produtos" para verificar os produtos no estoque')


@bot.command()
async def produtos(ctx):
    message = await ctx.send("**Selecione o tipo de produto que está interessado.**\n\n"
                             "💻 - Laptops       📱 - Smartphones\n\n"
                             "🖥️ - Desktops      🎮 - Video Games\n\n\n"
                             "-----------------------------------"
                             )

    await message.add_reaction("💻")  # Laptop
    await message.add_reaction("📱")  # Smartphone
    await message.add_reaction("🖥️")  # Desktop Computer
    await message.add_reaction("🎮")  # Game Console

    produtos_eletronicos = [
        "💻 Laptop",
        "📱 Smartphone",
        "🖥️ Desktop",
        "🎮 Video game",
    ]

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in [produto.split()[0] for produto in produtos_eletronicos]

    async def mostrar_produtos(ctx, arquivo):
        await ctx.send(f'-----------------------------------'
                       f'\n\n**Aqui estão alguns produtos presentes em nosso estoque:**\n\n'
                       f'↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓')

        with open(f'produtos/{arquivo}.csv', 'r', newline='', encoding='utf-8') as arquivo_csv:
            leitor_csv = csv.DictReader(arquivo_csv)
            produtos = []
            nome = []
            cont = 1
            for linha in leitor_csv:
                produto = linha['Produto']
                preco = linha['Preço']
                linha_texto = f"{produto} - R$ {preco}"
                produtos.append(linha_texto)
                nome.append(produto)
                await ctx.send(f'{cont} - {linha_texto}')
                cont += 1

        def check_mensagem(mensagem):
            return mensagem.author == ctx.author and mensagem.channel == ctx.channel

        try:
            mensagem_escolha = await bot.wait_for('message', check=check_mensagem, timeout=60)
            escolha = int(mensagem_escolha.content)
            if 1 <= escolha <= len(produtos):
                produto_escolhido = produtos[escolha - 1]
                produto_nome = nome[escolha - 1]

                await ctx.send(f"Você escolheu: {produto_escolhido}\n"
                               f"-----------------------------------\n"
                               f"Esse bot é um trabalho para faculdade e não existe venda real\n"
                               f"Logo o bot irá confirmar a venda e retirar 1 unidade do produto do estoque.\n"
                               f"-----------------------------------\n"
                               f"Compra realizada com sucesso!!")
                remover(produto_nome, 1)

            else:
                await ctx.send("Opção inválida.")
        except asyncio.TimeoutError:
            await ctx.send("Tempo limite excedido. Nenhuma resposta foi recebida.")
        except ValueError:
            await ctx.send("Escolha inválida. Digite o número correspondente ao produto.")

    try:
        reaction, user = await bot.wait_for("reaction_add", check=check)
        if str(reaction.emoji) == "💻":
            await mostrar_produtos(ctx, 'Notebook')
        elif str(reaction.emoji) == "📱":
            await mostrar_produtos(ctx, 'Smartphone')
        elif str(reaction.emoji) == "🖥️":
            await mostrar_produtos(ctx, 'Desktop')
        elif str(reaction.emoji) == "🎮":
            await mostrar_produtos(ctx, 'Video Game')
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


bot.run('MTEwODc1NTUzNzc2NTYwMTQxMg.GY28_I.JLAavgd5JRtGeGkIYAywX74xzhtUCUoqukhhIs')
