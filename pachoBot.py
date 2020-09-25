import discord
import os
import random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

bot = commands.Bot("Pacho", command_prefix="&",
                   description= "Virtualización de la"
                                " voluntad de Pacho.")
bot.remove_command("help")


@bot.event
async def on_ready():
    print(f"Todopoderosa {bot.user.name} ha llegado")


@bot.command(name="help")
async def help(ctx):
    embed = discord.Embed(title="Pacho Bot",
                          description="Comandos incluidos:",
                          color=0xff0000)
    embed.add_field(name="&hola X",
                    value="Devuelve un saludo de X.")
    embed.add_field(name="&info",
                    value="Muestra información del Bot.")
    embed.add_field(name="&pachi_dados",
                    value="Lanza un dado de 100 caras.")
    embed.add_field(name="&status X",
                    value="Muestra el estado de X.")
    await ctx.send(embed=embed)


@bot.command(name="info")
async def info(ctx):
    embed = discord.Embed(title="Pacho Bot",
                          description="Virtualización de"
                                      " la imagen de Pacho.",
                          color=0xff0000)
    embed.add_field(name="Autora", value="Pacho")
    embed.add_field(name="Colaboradores", value="Dodi, Pachi.")
    await ctx.send(embed=embed);


@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Estimado/a {member.name}, Pacho envía sus saludos.'
    )


@bot.event
async def joined(ctx, member: discord.Member):
    await ctx.send('{0.name} se ha unido a {0.joined_at}'.format(member))


@bot.command(name="hola", help="Devuelve un saludo")
async def on_salute(ctx, arg1: str):
    pacho_quotes = [
        (
            "..."
        ),
        (
            "En este momento, Pacho se encuentra ocupada. Deje su"
            " mensaje con Ariel."
        ),
        (
                "/" + "\\"
        )
    ]
    pachi_quotes = [
        (
                "/" + "\\"
        ),
        (
            "Pachi no quiere tus saludos, ¡exige reverencias!"
        ),
        (
            "Pachi-saludos, bello humano."
        ),
        (
            "Intruso de nombre Pachi detectado. Comenzando eliminación en"
            " la base de datos."
        )
    ]
    if arg1 == "Pacho":
        response = random.choice(pacho_quotes)
        await ctx.send(response)
    elif arg1 == "Pachi":
        response = random.choice(pachi_quotes)
        await ctx.send(response)
    else:
        await ctx.send("Ser no registrado en la base de"
                       " datos de Pacho.")


@bot.command(name="pachi_dados", help="Lanza un dado de 100 caras")
async def on_dice_roll(ctx):
    num = random.choice(range(1, 100))
    await ctx.send("¡Obtuviste " + str(num) + " Pachis!")


@bot.command(name="status", help="Muestra el estado actual de la persona")
async def on_status(ctx, arg: str):
    if arg == "Pacho":
        await ctx.send("Extremadamente ocupada en su investigación.")
    elif arg == "Pachi":
        await ctx.send("De cita con Nightwing.")
    elif arg == "Foton":
        await ctx.send("Vaciando su lista de mercenario.")
    elif arg == "Fran":
        await ctx.send("Progresando en su arte.")
    elif arg == "Ephy":
        await ctx.send("Estudiando Java.")
    elif arg == "Ariel":
        await ctx.send("Investigando junto a Pacho.")
    elif arg == "Elias":
        await ctx.send("Creando música virtuosa.")
    elif arg == "Dibujin":
        await ctx.send("Acumulando poder artístico visual.")
    elif arg == "Dodi":
        await ctx.send("Haciendo de Dodoria un lugar mejor.")
    else:
        await ctx.send("Usuario no registrado en la base"
                       " de datos de Pacho.")


bot.run(TOKEN)
