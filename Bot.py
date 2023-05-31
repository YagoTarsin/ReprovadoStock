import asyncio
import csv
import discord
from discord.ext import commands
import Principal

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print('Logged on as {0}!'.format(bot.user))


@bot.command()
async def produtos(ctx):
    message = await ctx.send("**Reaja ao tipo de produto que está interessado.**\n\n"
                             "💻 - Laptops       📱 - Smartphone\n\n"
                             "🖥️ - Desktop      🎮 - Video Games\n\n\n"
                             "-----------------------------------"
                             )

    await message.add_reaction("💻")  # Laptop
    await message.add_reaction("📱")  # Smartphone
    await message.add_reaction("🖥️")  # Desktop
    await message.add_reaction("🎮")  # Game

    produtos_eletronicos = [
        "📱 Smartphone",
        "💻 Laptop",
        "🖥️ Desktop",
        "🎮 Video game",
    ]

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in [produto.split()[0] for produto in produtos_eletronicos]

    try:
        reaction, user = await bot.wait_for("reaction_add", check=check)

        if str(reaction.emoji) == "💻":
            await ctx.send('-----------------------------------'
                           '\n\n**Aqui estão alguns Laptops presente em nosso estoque:**\n\n'
                           '↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓')
            with open(f'produtos/Notebook.csv', 'r', newline='', encoding='utf-8') as arquivo_csv:
                leitor_csv = csv.DictReader(arquivo_csv)
                for linha in leitor_csv:
                    produto = linha['Produto']
                    preco = linha['Preço']
                    linha_texto = f"{produto} - R$ {preco}"
                    await ctx.send(linha_texto)

        elif str(reaction.emoji) == "📱":
            await ctx.send('-----------------------------------'
                           '\n\n**Aqui estão alguns Smartphones presente em nosso estoque:**\n\n'
                           '↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓')
            with open(f'produtos/celulares.csv', 'r', newline='', encoding='utf-8') as arquivo_csv:
                leitor_csv = csv.DictReader(arquivo_csv)
                for linha in leitor_csv:
                    produto = linha['Produto']
                    preco = linha['Preço']
                    linha_texto = f"{produto} - R$ {preco}"
                    await ctx.send(linha_texto)

        elif str(reaction.emoji) == "🖥️":
            await ctx.send('-----------------------------------'
                           '\n\n**Aqui estão alguns Desktops presente em nosso estoque:**\n\n'
                           '↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓')
            with open(f'produtos/Desktop.csv', 'r', newline='', encoding='utf-8') as arquivo_csv:
                leitor_csv = csv.DictReader(arquivo_csv)
                for linha in leitor_csv:
                    produto = linha['Produto']
                    preco = linha['Preço']
                    linha_texto = f"{produto} - R$ {preco}"
                    await ctx.send(linha_texto)

        elif str(reaction.emoji) == "🎮":
            await ctx.send('-----------------------------------'
                           '\n\n**Aqui estão alguns Video Games presente em nosso estoque:**\n\n'
                           '↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓')
            with open(f'produtos/video_games.csv', 'r', newline='', encoding='utf-8') as arquivo_csv:
                leitor_csv = csv.DictReader(arquivo_csv)
                for linha in leitor_csv:
                    produto = linha['Produto']
                    preco = linha['Preço']
                    linha_texto = f"{produto} - R$ {preco}"
                    await ctx.send(linha_texto)

    except asyncio.TimeoutError:
        await ctx.send("Tempo limite excedido. Nenhuma reação foi recebida.")


bot.run('MTEwODc1NTUzNzc2NTYwMTQxMg.GY28_I.JLAavgd5JRtGeGkIYAywX74xzhtUCUoqukhhIs')
