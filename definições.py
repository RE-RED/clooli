# Dicionário com as definições da máquina de estados do jogo.
estados = {
    0: {
        'frases': ['Digite "iniciar" para começar o jogo.'],
        'proximos_estados': {
            '[iI]niciar?': 1
        }
    },
    1: {'frases': ['Durante o jogo, digite 1 para seguir em frente, e 2 para voltar a frase anterior.'],
        'proximos_estados': {
            '1': 2,
            '2': 0
        }
    },
    2: {
        'frases': ['???: \n - ...droga...!'],
        'proximos_estados': {
            '1': 3,
            '2': 1
        }
    },
    3: {
        'frases': ['???: \n - Esqueci de desligar...'],
        'proximos_estados': {
            '1': 4,
            '2': 2
        }
    },
    4: {
        'frases': ['???: \n - Talvez eu deva dormir novamente... \n(ESCOLHA: "Levantar" ou "Dormir"' ],
        'proximos_estados': {
            'Levantar': 5,
            'Dormir': 6,
            '2': 3
        }
    },
    5: {
        'frases': ['???:\nVocê levanta e vai até a cozinha. \n - Bom dia mãe!'],
        'proximos_estados': {
            '1': 8, 
            '2': 4
        }
    },
    6: {
        'frases': ['???:\n...'],
        'proximos_estados': {
            '1': 7,
            '2': 4
        }
    },
    7: {
        'frases': ['???: \n -Que droooga, agora não consigo dormir mais.'],
        'proximos_estados': {
            '1': 5,
            '2': 6
        }
    },
    8: {
        'frases': ['Mãe:\n - Bom dia!~'],
        'proximos_estados': {
            '1': 9,
            '2': 5
        }
    },
    9: {
        'frases': ['???:\nEla parece animada\n - Aconteceu alguma coisa?'],
        'proximos_estados': {
            '1': 10,
            '2': 8
        }
    },
    10: {
        'frases': ['Mãe:\n - Eu passei naquela entrevista e começo hoje!'],
        'proximos_estados': {
            '1': 11,
            '2': 9
        }
    },
    11: {
        'frases': ['???:\n - Que bom! Vamos comemorar mais tarde?'],
        'proximos_estados': {
            '1': 12,
            '2': 10
        }
    },
    12: {
        'frases': ['Mãe:\n - Com certeza! Ah, mais uma coisa. Lucas, não chega muito tarde, sei que você se perde enquanto corre por ai.'],
        'proximos_estados': {
            '1': 13,
            '2': 11
        }
    },
    13: {
        'frases': ['Lucas:\n - OK! Não vou chegar tarde... Hoje.'],
        'proximos_estados': {
            '1': 14,
            '2': 12
        }
    },
    14: {
        'frases': ['Lucas:\nDe volta para o quarto. Você se arruma e vai correr'],
        'proximos_estados': {
            '1': 15,
            '2': 13
        }
    },
    15: {
        'frases': ['Lucas:\nO dia está realmente bonito hoje. Tenho uma sensação ótima.'],
        'proximos_estados': {
            '1': 16,
            '2': 14
        }
    },
    16: {
        'frases': ['Lucas:\nApós caminhar por um tempo você vê que já estou longe de casa, talvez seja hora de voltar. (ESCOLHER: "Voltar" ou "Continuar")'],
        'proximos_estados': {
            '[vV]oltar?': 17,
            '[cC]ontinuar': 1,
            '2': 15
        }
    },
    17: {
        'frases': ['Ou não. '],
        'proximos_estados': {
            '1': 18,
            '2': 16
        }
    },
    16: {
        'frases': ['Lucas:\nParado esperando o sinal abrir, posso ver uma estranha neblina se aproximar. Não é totalmente anormal, a região tende a ter esse fenômeno com frequência'],
        'proximos_estados': {
            '[vV]oltar': 17,
            '[cC]ontinuar': 15
        }
    },
}

# Dicionário com os estados correntes de cada jogador.
partidas = {}
