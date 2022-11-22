# Dicionário com as definições da máquina de estados do jogo.
frases = {
    'reiniciado': 'Jogo reiniciado (progresso do jogador apagado).',
    'saindo': 'Daisy\nDaisy',
    'canal_privado': 'Não é possível reproduzir áudio em canais privados.',
    'sem_canal_de_voz': 'Por favor, esteja em um canal de voz para ter a imersão completa do jogo.',
    'erro': 'Durante o jogo, digite "Seguir" para continuar a hostória, e "Retornar" para voltar a frase anterior.'
}
estados = {
    0: {
        'frases': ['Digite "iniciar" para começar o jogo.'],
        'proximos_estados': {
            '[iI]niciar?': 1
        }
    },
    1: {'frases': ['Durante o jogo, digite "Seguir" para continuar a hostória, e "Retornar" para voltar a frase anterior.'],
        'proximos_estados': {
            '[sS]eguir?': 2,
            '[rR]etornar?': 0
        }
    },
    2: {
        'frases': ['???: \n - ...droga...!'],
        'proximos_estados': {
            '[sS]eguir?': 3,
            '[rR]etornar?': 1
        }
    },
    3: {
        'frases': ['???: \n - Esqueci de desligar...'],
        'proximos_estados': {
            '[sS]eguir?': 4,
            '[rR]etornar?': 2
        }
    },
    4: {
        'frases': ['???: \n - Talvez eu deva dormir novamente... \n(ESCOLHA: "Levantar" ou "Dormir"' ],
        'proximos_estados': {
            '[lL]evantar?': 5,
            '[dD]ormir?': 6,
            '[rR]etornar?': 3
        }
    },
    5: {
        'frases': ['???:\nVocê levanta e vai até a cozinha. \n - Bom dia mãe!'],
        'proximos_estados': {
            '[sS]eguir?': 8, 
            '[rR]etornar?': 4
        }
    },
    6: {
        'frases': ['???:\n...'],
        'proximos_estados': {
            '[sS]eguir?': 7,
            '[rR]etornar?': 4
        }
    },
    7: {
        'frases': ['???: \n -Que droooga, agora não consigo dormir mais.'],
        'proximos_estados': {
            '[sS]eguir?': 5,
            '[rR]etornar?': 6
        }
    },
    8: {
        'frases': ['Mãe:\n - Bom dia!~'],
        'proximos_estados': {
            '[sS]eguir?': 9,
            '[rR]etornar?': 5
        }
    },
    9: {
        'frases': ['???:\nEla parece animada\n - Aconteceu alguma coisa?'],
        'proximos_estados': {
            '[sS]eguir?': 10,
            '[rR]etornar?': 8
        }
    },
    10: {
        'frases': ['Mãe:\n - Eu passei naquela entrevista, e começo hoje!'],
        'proximos_estados': {
            '[sS]eguir?': 11,
            '[rR]etornar?': 9
        }
    },
    11: {
        'frases': ['???:\n - Que bom! Vamos comemorar mais tarde?'],
        'proximos_estados': {
            '[sS]eguir?': 12,
            '[rR]etornar?': 10
        }
    },
    12: {
        'frases': ['Mãe:\n - Com certeza! Ah, mais uma coisa. Lucas, não chega muito tarde, sei que você se perde enquanto corre por ai.'],
        'proximos_estados': {
            '[sS]eguir?': 13,
            '[rR]etornar?': 11
        }
    },
    13: {
        'frases': ['Lucas:\n - OK! Não vou chegar tarde... Hoje.'],
        'proximos_estados': {
            '[sS]eguir?': 14,
            '[rR]etornar?': 12
        }
    },
    14: {
        'frases': ['Lucas:\nDe volta para o quarto. Você se arruma e vai correr'],
        'proximos_estados': {
            '[sS]eguir?': 15,
            '[rR]etornar?': 13
        }
    },
    15: {
        'frases': ['Lucas:\nO dia está realmente bonito hoje. Tenho uma sensação ótima.'],
        'proximos_estados': {
            '[sS]eguir?': 16,
            '[rR]etornar?': 14
        }
    },
    16: {
        'frases': ['Lucas:\nApós caminhar por um tempo você vê que já estou longe de casa, talvez seja hora de voltar. (ESCOLHER: "Voltar" ou "Continuar")'],
        'proximos_estados': {
            '[vV]oltar?': 17,
            '[cC]ontinuar?': 18,
            '[rR]etornar?': 15
        }
    },
    17: {
        'frases': ['Lucas:\nOu não. Conheço uma padaria muito boa por aqui, vou comer algo e depois volto.'],
        'proximos_estados': {
            '[sS]eguir?': 18,
            '[rR]etornar?': 16
        }
    },
    18: {
        'frases': ['Lucas:\n Voltando você espera no sinal, e percebe que uma neblina se aproxima. Não era um evento estranho. Esse fenômeno tende a acontecer bastante na região'],
        'proximos_estados': {
            '[sS]eguir?': 19,
            '[rR]etornar?': 16
        }
    },
    19: {
        'frases': ['Mas estranhamente a neblina se aproxima cada vez mais. Uma moça que estava perto acaba tendo contato'],
        'proximos_estados': {
            '[sS]eguir?': 20,
            '[rR]etornar?': 18
        }
    },
    20: {
        'frases': ['Ela começa a gritar. Aterrorizada pede por ajuda enquanto seus olhos ficam cada vez mais vermelhos'],
        'proximos_estados': {
            '[sS]eguir?': 21,
            '[rR]etornar?': 16
        }
    },
    21: {
        'frases': ['Todos ao redor entram em pânico e tentam fugir da neblina. Enquanto isso aquela mulher para de gritar, mas começa a falar sozinha. Parece estar ficando louca.\nA neblina continua avançando, até que a cobre totalmente'],
        'proximos_estados': {
            '[sS]eguir?': 22,
            '[rR]etornar?': 20
        }
    },
    22: {
        'frases': ['Ela sai correndo da neblina e começa a atacar outra pessoa, com arranhões e socos. Então começa a bater contra o chão a cabeça daquela pessoa, e então simplismente para, e corre atrás de outra pessoa'],
        'proximos_estados': {
            '[sS]eguir?': 23,
            '[rR]etornar?': 21
        }
    },
    23: {
        'frases': ['Outras pessoas que tentavam correr da neblina não tiveram sorte. Muitas acabaram se transtornando igual aquela mulher, e começaram a atacar os outros. Enquanto estavam atacando gritavam para que parasse. Mas parar o que?'],
        'proximos_estados': {
            '[sS]eguir?': 24,
            '[rR]etornar?': 22
        }
    },
    24: {
        'frases': ['Quando vi, já estavam por toda parte, muitos tiveram contato com a neblina, e eu não sabia para onde correr. A neblina avançava muito rápido então não adiantaria correr. Meu colégio é subindo o morro, lá devo ficar protegido.'],
        'proximos_estados': {
            '[sS]eguir?': 25,
            '[rR]etornar?': 23
        }
    },
    25: {
        'frases': ['Ao chegar lá você encontra outros que também estavam fugindo da neblina e daquelas pessoas. Mas a escola está trancada. Os portões estão fechados e não há entradas visíveis. Então você decide escalar os portões, dentro estará mais seguro.'],
        'proximos_estados': {
            '[sS]eguir?': 26,
            '[rR]etornar?': 24
        }
    },
    26: {
        'frases': ['Os demais te seguiram.'],
        'proximos_estados': {
            '[sS]eguir?': 27,
            '[rR]etornar?': 25
        }
    },
    25: {
        'frases': [''],
        'proximos_estados': {
            '[sS]eguir?': 26,
            '[rR]etornar?': 24
        }
    },
    21: {
        'frases': ['Reiniciar'],
        'proximos_estados': {
            'reiniciar': 2
        }
    }
}

# Dicionário com os estados correntes de cada jogador.
canais_de_voz = {}