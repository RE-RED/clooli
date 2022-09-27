from os import getenv
from dotenv import load_dotenv
import discord
from discord.ext import commands
from random import choice
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(intents=intents, command_prefix='')

# Dicionário com as definições da máquina de estados do jogo.
estados = {
    0: {
        'frases': ['Digite "iniciar" para começar o jogo.'],
        'proximos_estados': {
            'iniciar': 1
        }
    },
    1: {'frases': ['Durante o jogo, digite 1 para seguir em frente, e 2 para voltar a frase anterior.'],
        'proximos_estados': {
            '1': 2,
            '2': 0
        }
    },
    2: {
        'frases': ['??? \n - ...droga...!'],
        'proximos_estados': {
            '1': 3,
            '2': 1
        }
    },
    3: {
        'frases': ['??? \n - Esqueci de desligar...'],
        'proximos_estados': {
            '1': 4,
            '2': 2
        }
    },
    4: {
        'frases': ['??? \n - Talvez eu deva dormir novamente... \n(ESCOLHA: "Levantar" ou "Dormir"' ],
        'proximos_estados': {
            'Levantar': 5,
            'Dormir': 6,
            '2': 3
        }
    },
    5: {
        'frases': ['???\nVocê levanta e vai até a cozinha. \n??? \n - Bom dia mãe!'],
        'proximos_estados': {
            '1': 8, 
            '2': 4
        }
    },
    6: {
        'frases': ['???\n...'],
        'proximos_estados': {
            '1': 7,
            '2': 4
        }
    },
    7: {
        'frases': ['??? \n -Que droooga, agora não consigo dormir mais.'],
        'proximos_estados': {
            '1': 5,
            '2': 6
        }
    },
    8: {
        'frases': ['Mãe\n - Bom dia!~'],
        'proximos_estados': {
            '1': 9,
            '2': 5
        }
    },
    9: {
        'frases': ['???\nEla parece animada\n - Aconteceu alguma coisa?'],
        'proximos_estados': {
            '1': 10,
            '2': 8
        }
    },
    10: {
        'frases': ['Mãe\n - Eu passei naquela entrevista e começo hoje'],
        'proximos_estados': {
            '1': 11,
            '2': 9
        }
    },
    11: {
        'frases': ['???\n - Que bom! Vamos comemorar mais tarde?'],
        'proximos_estados': {
            '1': 12,
            '2': 10
        }
    },
    12: {
        'frases': ['Mãe\n - Com certeza! Ah, mais uma coisa. Lucas, não chega muito tarde, sei que você se perde enquanto corre por ai'],
        'proximos_estados': {
            '1': 13,
            '2': 11
        }
    },
    13: {
        'frases': ['Lucas\n - OK! Não vou chegar tarde... Hoje'],
        'proximos_estados': {
            '1': 14,
            '2': 12
        }
    },
    14: {
        'frases': ['Lucas\nDe volta para o quarto. Você se arruma e vai correr'],
        'proximos_estados': {
            '1': 15,
            '2': 13
        }
    },
}

# Dicionário com os estados correntes de cada jogador.
partidas = {}


@bot.event
async def on_ready():
    print('Bot is ready.')


@bot.event
async def on_message(msg):
    # Armazenar o autor da mensagem
    autor = msg.author.id

    # Verificar se a mensagem não tem o próprio bot como autor.
    if autor == bot.application_id:
        return
    #
    # Verificar se o jogador ainda não começou a partida,
    # o que significa que precisa colocá-lo no estado zero (0).
    if autor not in partidas:
        partidas[autor] = 0
    #
    # Em ordem de operação:, 'Parabéns!'
    # 0) Obter o estado atual do jogador:
    #    partidas[autor]
    # 1) Obter a definição completa desse estado:
    #    estados[partidas[autor]]
    estado_do_jogador = estados[partidas[autor]]
    #
    # 3) Filtrar desse estado apenas a lista de próximos estados:
    #    estados_do_jogador['proximos_estados']
    # 4) Filtrar dessa lista as chaves (frases) quem levam a próximos estados:
    #    estado_de_jogador['proximos_estados'].keys()
    # 5) Verificar se a frase do usuário está na lista de chaves (frases) do estado:
    if msg.content in estado_do_jogador['proximos_estados'].keys():
        #
        # Atualizar o estado do jogador,
        # e para isso é usado o conteúdo da mensagem como chave do dicionário:
        partidas[autor] = estado_do_jogador['proximos_estados'][msg.content]
        #
        # A definição completa do estado do jogador,
        # por consequência, também é atualizada
        estado_do_jogador = estados[partidas[autor]]
        #
        # Enviar para o jogador a mensagem do estado (já atualizado)
        #
        # Em ordem de operação:
        # 0) Filtrar do estado do jogador apenas a lista de frases:
        #    estado_do_jogador['frases']
        # 1) Sortear uma frase dessa lista:
        #   choice(estado_do_jogador['frases'])
        await msg.channel.send(choice(estado_do_jogador['frases']))
    #
    # Caso contrário, avisar que a mensagem não avança no jogo.
    # Se o jogador ainda estiver no estado, ajudar com uma dica:
    elif partidas[autor] == 0:
        await msg.channel.send(choice(estado_do_jogador['frases']))
    else:
        #
        #  Nos estados seguintes, a resposta padrão de HAL:
        await msg.channel.send('I\'m sorry Dave, I\'m afraid I can\'t do that.')


bot.run(getenv('DISCORD_TOKEN'))