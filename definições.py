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
    1: {'frases': ['Durante o jogo, digite "Seguir" para continuar a história, e "Retornar" para voltar a frase anterior.'],
        'proximos_estados': {
            '[sS]eguir?': 2,
            '[rR]etornar?': 0
        }
    },
    2: {
        'frases': ['???: \n - ...droga...'],
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
        'frases': ['???: \n - Talvez eu devesse levantar…\n(ESCOLHA: "Levantar" ou "Dormir")'],
        'proximos_estados': {
            '[lL]evantar?': 5,
            '[dD]ormir?': 6,
            '[rR]etornar?': 3
        }
    },
    5: {
        'frases': ['Você levanta e vai até a cozinha.'],
        'proximos_estados': {
            '[sS]eguir?': 6, 
            '[rR]etornar?': 4
        }
    },
    6: {
        'frases': ['??? \n - Bom dia mãe!'],
        'proximos_estados': {
            '[sS]eguir?': 7,
            '[rR]etornar?': 5
        }
    },
    7: {
        'frases': ['Mãe: \n - Bom dia!'],
        'proximos_estados': {
            '[sS]eguir?': 8,
            '[rR]etornar?': 6
        }
    },
    8: {
        'frases': ['Ela parece animada.'],
        'proximos_estados': {
            '[sS]eguir?': 9,
            '[rR]etornar?': 7
        }
    },
    9: {
        'frases': ['???\n - Aconteceu alguma coisa?'],
        'proximos_estados': {
            '[sS]eguir?': 10,
            '[rR]etornar?': 8
        }
    },
    10: {
        'frases': ['???\n - Aconteceu alguma coisa?'],
        'proximos_estados': {
            '[sS]eguir?': 11,
            '[rR]etornar?': 9
        }
    },
}

# Dicionário com os estados correntes de cada jogador.
canais_de_voz = {}