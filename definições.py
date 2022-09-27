# Dicionário com as definições da máquina de estados do jogo.
estados = {
    0: {
        'frases': ['Digite "iniciar" para começar o jogo.'],
        'proximos_estados': {
            '[iI]niciar?': 1
        },
        'tempo_limite': 0
    },
    1: {'frases': ['Durante o jogo, digite "Seguir" para continuar a história, e "Retornar" para voltar a frase anterior.'],
        'proximos_estados': {
            '[sS]eguir?': 2,
            '[rR]etornar?': 0
        },
        'tempo_limite': 10
    },
    2: {
        'frases': ['???: \n - ...droga...!'],
        'proximos_estados': {
            '[sS]eguir?': 3,
            '[rR]etornar?': 1
        },
        'tempo_limite': 10
    },
    3: {
        'frases': ['???: \n - Esqueci de desligar...'],
        'proximos_estados': {
            '[sS]eguir?': 4,
            '[rR]etornar?': 2
        },
        'tempo_limite': 10
    },
    4: {
        'frases': ['???: \n - Talvez eu deva dormir novamente... \n(ESCOLHA: "Levantar" ou "Dormir"' ],
        'proximos_estados': {
            '[lL]evantar?': 5,
            '[dD]ormir?': 6,
            '[rR]etornar?': 3
        },
        'tempo_limite': 10
    },
    5: {
        'frases': ['???:\nVocê levanta e vai até a cozinha. \n - Bom dia mãe!'],
        'proximos_estados': {
            '[sS]eguir?': 8, 
            '[rR]etornar?': 4
        },
        'tempo_limite': 10
    },
    6: {
        'frases': ['???:\n...'],
        'proximos_estados': {
            '[sS]eguir?': 7,
            '[rR]etornar?': 4
        },
        'tempo_limite': 10
    },
    7: {
        'frases': ['???: \n -Que droooga, agora não consigo dormir mais.'],
        'proximos_estados': {
            '[sS]eguir?': 5,
            '[rR]etornar?': 6
        },
        'tempo_limite': 10
    },
    8: {
        'frases': ['Mãe:\n - Bom dia!~'],
        'proximos_estados': {
            '[sS]eguir?': 9,
            '[rR]etornar?': 5
        },
        'tempo_limite': 10
    },
    9: {
        'frases': ['???:\nEla parece animada\n - Aconteceu alguma coisa?'],
        'proximos_estados': {
            '[sS]eguir?': 10,
            '[rR]etornar?': 8
        },
        'tempo_limite': 10
    },
    10: {
        'frases': ['Mãe:\n - Eu passei naquela entrevista, e começo hoje!'],
        'proximos_estados': {
            '[sS]eguir?': 1,
            '[rR]etornar?': 9
        },
        'tempo_limite': 10
    },
    11: {
        'frases': ['???:\n - Que bom! Vamos comemorar mais tarde?'],
        'proximos_estados': {
            '[sS]eguir?': 12,
            '[rR]etornar?': 10
        },
        'tempo_limite': 10
    },
    12: {
        'frases': ['Mãe:\n - Com certeza! Ah, mais uma coisa. Lucas, não chega muito tarde, sei que você se perde enquanto corre por ai.'],
        'proximos_estados': {
            '[sS]eguir?': 13,
            '[rR]etornar?': 11
        },
        'tempo_limite': 10
    },
    13: {
        'frases': ['Lucas:\n - OK! Não vou chegar tarde... Hoje.'],
        'proximos_estados': {
            '[sS]eguir?': 14,
            '[rR]etornar?': 12
        },
        'tempo_limite': 10
    },
    14: {
        'frases': ['Lucas:\nDe volta para o quarto. Você se arruma e vai correr'],
        'proximos_estados': {
            '[sS]eguir?': 15,
            '[rR]etornar?': 13
        },
        'tempo_limite': 10
    },
    15: {
        'frases': ['Lucas:\nO dia está realmente bonito hoje. Tenho uma sensação ótima.'],
        'proximos_estados': {
            '[sS]eguir?': 16,
            '[rR]etornar?': 14
        },
        'tempo_limite': 10
    },
    16: {
        'frases': ['Lucas:\nApós caminhar por um tempo você vê que já estou longe de casa, talvez seja hora de voltar. (ESCOLHER: "Voltar" ou "Continuar")'],
        'proximos_estados': {
            '[vV]oltar?': 17,
            '[cC]ontinuar?': 18,
            '[rR]etornar?': 15
        },
        'tempo_limite': 10
    },
    17: {
        'frases': ['Lucas:\nOu não. Conheço uma padaria muito boa por aqui, vou comer algo e depois volto.'],
        'proximos_estados': {
            '[sS]eguir?': 18,
            '[rR]etornar?': 16
        },
        'tempo_limite': 10
    },
    18: {
        'frases': ['Lucas:\n Voltando você espera no sinal, e percebe que uma neblina se aproxima. Não era um evento estranho. Esse fenômeno tende a acontecer bastante na região'],
        'proximos_estados': {
            '[sS]eguir?': 19,
            '[rR]etornar?': 16
        },
        'tempo_limite': 10
    },
    19: {
        'frases': ['Mas estranhamente a neblina se aproxima cada vez mais. Uma moça que estava perto acaba tendo contato'],
        'proximos_estados': {
            '[sS]eguir?': 20,
            '[rR]etornar?': 18
        },
        'tempo_limite': 10
    },
    20: {
        'frases': ['Ela começa a gritar. Aterrorizada pede por ajuda enquanto seus olhos ficam cada vez mais vermelhos'],
        'proximos_estados': {
            '[sS]eguir?': 21,
            '[rR]etornar?': 16
        },
        'tempo_limite': 10
    },
    21: {
        'frases': ['Todos ao redor entram em pânico e tentam fugir da neblina. Enquanto isso aquela mulher para de gritar, mas começa a falar sozinha. Parece estar ficando louca.\nA neblina continua avançando, até que a cobre totalmente'],
        'proximos_estados': {
            '[sS]eguir?': 22,
            '[rR]etornar?': 20
        },
        'tempo_limite': 10
    },
    22: {
        'frases': ['Ela sai correndo da neblina e começa a atacar outra pessoa. Conforme mais pessoas entram em contato com aquela fumaça, todas ficam iguais a ela.'],
        'proximos_estados': {
            '[sS]eguir?': 22,
            '[rR]etornar?': 20
        },
        'tempo_limite': 10
    },
    21: {
        'frases': ['Reiniciar'],
        'proximos_estados': {
            'reiniciar': 2
        }
    }
}

# Dicionário com os estados correntes de cada jogador.
partidas = {}
