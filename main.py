import discord
import asyncio
import os

client = discord.Client()

is_prod = os.environ.get('IS_HEROKU', None)
if is_prod:
    token = os.environ.get('TOKEN')
else:
    import secreto
    token = secreto.token

version = "Beta 1.0.0"

@client.event
async def on_ready():
    print("=================================")
    print("Bot iniciado com sucesso!")
    print (client.user.name)
    print (client.user.id)
    print(f"Bot Versão: {version}")
    print("=================================")

@client.event
async def on_message(message):
# BOT AVISA O QUE FOI DITO.
    if message.content.lower().startswith("!say"):
        if not message.author.server_permissions.administrator:
            return await client.send_message(message.channel, ':x: Você não possui permissão para executar este comando!')
        msg = message.content[5:2000]
        await client.send_message(message.channel, msg)
        await client.delete_message(message)

client.run(token)