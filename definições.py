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
            '[lL]evantar?': 8,
            '[dD]ormir?': 5,
            '[rR]etornar?': 3
        }
    },
    5: {
        'frases': ['??? - Melhor voltar a dormir. Não é levantando cedo que se aproveita uma folga.'],
        'proximos_estados': {
            '[sS]eguir?': 6, 
            '[rR]etornar?': 4
        }
    },
    6: {
        'frases': ['…'],
        'proximos_estados': {
            '[sS]eguir?': 7,
            '[rR]etornar?': 5
        }
    },
    7: {
        'frases': ['??? - Que droga Aaahhh. Agora não consigo dormir.'],
        'proximos_estados': {
            '[sS]eguir?': 8,
            '[rR]etornar?': 6
        }
    },
    8: {
        'frases': ['Você levanta e vai até a cozinha.'],
        'proximos_estados': {
            '[sS]eguir?': 9,
            '[rR]etornar?': 7
        }
    },
    9: {
        'frases': ['??? - Bom dia mãe!'],
        'proximos_estados': {
            '[sS]eguir?': 10,
            '[rR]etornar?': 8
        }
    },
    10: {
        'frases': ['Mãe - Bom dia!~'],
        'proximos_estados': {
            '[sS]eguir?': 11,
            '[rR]etornar?': 9
        }
    },
    11: {
        'frases': ['Ela parece animada.'],
        'proximos_estados': {
            '[sS]eguir?': 12,
            '[rR]etornar?': 10
        }
    },
    12: {
        'frases': ['??? - Aconteceu alguma coisa?'],
        'proximos_estados': {
            '[sS]eguir?': 13,
            '[rR]etornar?': 11
        }
    },
    13: {
        'frases': ['Mãe - Eu passei na primeira etapa naquela entrevista que te contei. Estou indo para a segunda etapa daqui a pouco.'],
        'proximos_estados': {
            '[sS]eguir?': 14,
            '[rR]etornar?': 12
        }
    },
    14: {
        'frases': ['??? - Sério?! Que bom! Vamos comemorar mais tarde?'],
        'proximos_estados': {
            '[sS]eguir?': 15,
            '[rR]etornar?': 13
        }
    },
    15: {
        'frases': ['Mãe - Com certeza! Ah, mais uma coisa.'],
        'proximos_estados': {
            '[sS]eguir?': 16,
            '[rR]etornar?': 14
        }
    },
    16: {
        'frases': ['Mãe - Lucas, não chegue muito tarde, sei que você perde a noção do tempo enquanto corre por aí.'],
        'proximos_estados': {
            '[sS]eguir?': 17,
            '[rR]etornar?': 15
        }
    },
    17: {
        'frases': ['Lucas - OK!'],
        'proximos_estados': {
            '[sS]eguir?': 18,
            '[rR]etornar?': 16
        }
    },
    18: {
        'frases': ['Lucas - Não vou chegar tarde… Hoje.'],
        'proximos_estados': {
            '[sS]eguir?': 19,
            '[rR]etornar?': 17
        }
    },
    19: {
        'frases': ['De volta para o quarto. Você se prepara e vai correr.'],
        'proximos_estados': {
            '[sS]eguir?': 20,
            '[rR]etornar?': 18
        }
    },
    20: {
        'frases': ['Lucas - O dia está realmente bonito hoje. Tenho uma sensação ótima.'],
        'proximos_estados': {
            '[sS]eguir?': 21,
            '[rR]etornar?': 19
        }
    },
    21: {
        'frases': ['Na cidade:'],
        'proximos_estados': {
            '[sS]eguir?': 22,
            '[rR]etornar?': 20
        }
    },
    22: {
        'frases': ['Após caminhar por um tempo você vê que já está longe de casa, talvez seja hora de voltar.'],
        'proximos_estados': {
            '[sS]eguir?': 23,
            '[rR]etornar?': 21
        }
    },
    23: {
        'frases': ['ESCOLHA:\n "Voltar" ou "Continuar"'],
        'proximos_estados': {
            '[vV]oltar?': 35,
            '[cC]ontinuar?': 24,
            '[rR]etornar': 22
        }
    },
    24: {
        'frases': ['Ou não. Você conhece uma padaria muito boa por aqui, então decide comer algo e depois voltar.'],
        'proximos_estados': {
            '[sS]eguir?': 25,
            '[rR]etornar?': 23
        }
    },
    25: {
        'frases': ['Na padaria:'],
        'proximos_estados': {
            '[sS]eguir?': 26,
            '[rR]etornar?': 24
        }
    },
    26: {
        'frases': ['Padeiro - Lucas! Como você tá meu filho?'],
        'proximos_estados': {
            '[sS]eguir?': 27,
            '[rR]etornar?': 25
        }
    },
    27: {
        'frases': ['Lucas - Estou bem. Como vai, Sr. Antônio?'],
        'proximos_estados': {
            '[sS]eguir?': 28,
            '[rR]etornar?': 26
        }
    },
    28: {
        'frases': ['Sr. Antônio - Muito bem! Recebi um grande pedido, terei que fechar daqui a pouco para a entrega.'],
        'proximos_estados': {
            '[sS]eguir?': 29,
            '[rR]etornar?': 27
        }
    },
    29: {
        'frases': ['Lucas - Oh, o senhor está indo bem então.'],
        'proximos_estados': {
            '[sS]eguir?': 30,
            '[rR]etornar?': 28
        }
    },
    30: {
        'frases': ['Sr. Antônio - Hahaha. E o que você vai querer hoje? O de sempre?'],
        'proximos_estados': {
            '[sS]eguir?': 31,
            '[rR]etornar?': 29
        }
    },
    31: {
        'frases': ['Lucas - Isso mesmo. Estava dando uma volta, já estou voltando pra casa.'],
        'proximos_estados': {
            '[sS]eguir?': 32,
            '[rR]etornar?': 30
        }
    },
    32: {
        'frases': ['Sr. Antônio - Então volte logo, sua mãe sempre se preocupa com você zanzando por ai.'],
        'proximos_estados': {
            '25[sS]eguir?': 33,
            '[rR]etornar?': 31
        }
    },
    33: {
        'frases': ['Lucas - Já estou indo. Obrigado!'],
        'proximos_estados': {
            '[sS]eguir?': 34,
            '[rR]etornar?': 32
        }
    },
    34: {
        'frases': ['Sr. Antônio - Tchau!'],
        'proximos_estados': {
            '[sS]eguir?': 35,
            '[rR]etornar?': 33
        }
    },
    35: {
        'frases': ['Voltando você espera no sinal, e percebe que uma neblina se aproxima. Dias assim eram comuns devido a região.'],
        'proximos_estados': {
            '[sS]eguir?': 36,
            '[rR]etornar?': 23
        }
    },
    36: {
        'frases': ['Mas estranhamente, essa se aproximava muito rápido, o normal era uma névoa que surgia lentamente até que não se via mais nada.'],
        'proximos_estados': {
            '[sS]eguir?': 37,
            '[rR]etornar?': 35
        }
    },
    37: {
        'frases': ['Uma moça que estava perto acaba entrando em contato com aquele estranho nevoeiro.'],
        'proximos_estados': {
            '[sS]eguir?': 38,
            '[rR]etornar?': 36
        }
    },
    38: {
        'frases': ['Ela começa a se inclinar como se algo estivesse incomodando seus olhos, e conforme tinha mais contato com a névoa, mais ela se contorcia e coçava os olhos.'],
        'proximos_estados': {
            '[sS]eguir?': 39,
            '[rR]etornar?': 37
        }
    },
    39: {
        'frases': ['O que parecia uma leve incômodo passou a ser desespero. A mulher começou a gritar enquanto se contorcia em sua caminhada para fora daquela neblina.'],
        'proximos_estados': {
            '[sS]eguir?': 40,
            '[rR]etornar?': 38
        }
    },
    40: {
        'frases': ['Ela estava aterrorizada, seu medo era quase palpável, mas ninguém se atrevia a chegar perto dela.'],
        'proximos_estados': {
            '[sS]eguir?': 41,
            '[rR]etornar?': 39
        }
    },
    41: {
        'frases': ['Todos começaram a correr assim que os gritos daquela moça começaram. Ninguém tinha coragem para ajudá-la, não havia ninguém que quisesse se expor a seja lá o que era aquilo.'],
        'proximos_estados': {
            '[sS]eguir?': 42,
            '[rR]etornar?': 40
        }
    },
    42: {
        'frases': ['Conforme a moça ia desaparecendo pela neblina, seus gritos iam diminuindo. Mas já não haviam muitos por perto para testemunhar isso.'],
        'proximos_estados': {
            '[sS]eguir?': 43,
            '[rR]etornar?': 41
        }
    },
    43: {
        'frases': ['Então foi possível ouvir uns resmungos vindo da sua direção. Ela parecia discutir sobre algo, foi quando começou a gritar.'],
        'proximos_estados': {
            '[sS]eguir?': 44,
            '[rR]etornar?': 42
        }
    },
    44: {
        'frases': ['Moça na neblina- VOCÊ NÃO TEM ESSE DIREITO, VOU FAZER VOCÊ PAGAR!'],
        'proximos_estados': {
            '[sS]eguir?': 45,
            '[rR]etornar?': 43
        }
    },
    45: {
        'frases': ['ELA PULA PARA FORA DA NEBLINA EM DIREÇÃO ÀS OUTRAS PESSOAS.'],
        'proximos_estados': {
            '[sS]eguir?': 46,
            '[rR]etornar?': 44
        }
    },
    46: {
        'frases': ['Todos estavam muito assustados, gritavam para todos os lados tentando fugir da névoa, e agora dela.'],
        'proximos_estados': {
            '[sS]eguir?': 47,
            '[rR]etornar?': 45
        }
    },
    47: {
        'frases': ['Essa mulher estava com seus olhos tão vermelhos, que quase não se podia notar suas pupilas. Com toda sua fúria conseguiu alcançar um homem que estava tentando fugir desesperado.'],
        'proximos_estados': {
            '[sS]eguir?': 48,
            '[rR]etornar?': 46
        }
    },
    48: {
        'frases': ['Essa mulher estava com seus olhos tão vermelhos, que quase não se podia notar suas pupilas. Com toda sua fúria conseguiu alcançar um homem que estava tentando fugir desesperado.'],
        'proximos_estados': {
            '[sS]eguir?': 49,
            '[rR]etornar?': 47
        }
    },
    49: {
        'frases': ['Ela pula em suas costas e começa a morder sua orelha, até que a arranca fora.'],
        'proximos_estados': {
            '[sS]eguir?': 50,
            '[rR]etornar?': 48
        }
    },
    50: {
        'frases': ['Ele caiu se contorcendo enquanto a mulher o atacava. Ela dava socos e puxava seu cabelo.'],
        'proximos_estados': {
            '[sS]eguir?': 51,
            '[rR]etornar?': 49
        }
    },
    51: {
        'frases': ['Sem que ele conseguisse se defender, possivelmente pela dor, ela começa a puxar sua cabeça, e então bater contra o chão, com tanta força que os gritos dele não duraram muito, até que parou de reagir.'],
        'proximos_estados': {
            '[sS]eguir?': 52,
            '[rR]etornar?': 50
        }
    },
    52: {
        'frases': ['Você estava lá, a alguns metros a frente, paralizado pelo medo. Até que a mulher se aproxima e começa a correr em sua direção.'],
        'proximos_estados': {
            '[sS]eguir?': 53,
            '[rR]etornar?': 51
        }
    },
    53: {
        'frases': ['Mas ela apenas passa por você e pula em outra pessoa que estava gritando desesperada.'],
        'proximos_estados': {
            '[sS]eguir?': 54,
            '[rR]etornar?': 52
        }
    },
    54: {
        'frases': ['Foi nesse momento que você começou a correr. Já não conseguia pensar direito, e estava longe de casa. A neblina se aproximava cada vez mais e outras pessoas tinham contato com ela. Quando você percebeu já haviam muitos conturbados ao entrar em contato com aquela névoa.'],
        'proximos_estados': {
            '[sS]eguir?': 55,
            '[rR]etornar?': 53
        }
    },
    55: {
        'frases': ['Não!'],
        'proximos_estados': {
            '[sS]eguir?': 56,
            '[rR]etornar?': 54
        }
    },
    56: {
        'frases': ['Com aquela estranha fumaça. Não tinha como ser como os antigos nevoeiros, aquilo não tinha como ser apenas um fenômeno da natureza. Era outra coisa.'],
        'proximos_estados': {
            '[sS]eguir?': 57,
            '[rR]etornar?': 55
        }
    },
    57: {
        'frases': ['Um carro atravessa em sua frente e então bate em uma árvore, que por sua vez cai impedindo a passagem. Tudo o que você pode fazer é voltar.'],
        'proximos_estados': {
            '[sS]eguir?': 58,
            '[rR]etornar?': 56
        }
    },
    58: {
        'frases': ['Mas espera. Sua escola é subindo o morro, a movimentação por lá deve ser menor, além de que a altura deve dificultar a subida daquela fumaça. Ao ir em direção da escola você precisa desviar de alguns acidentes que ocorrem à sua volta, até que finalmente está em uma localização mais afastada e então chega na escola.'],
        'proximos_estados': {
            '[sS]eguir?': 59,
            '[rR]etornar?': 57
        }
    },
    59: {
        'frases': ['Como planejado, a fumaça parece ter dificuldades para se expandir até o topo daquele morro.'],
        'proximos_estados': {
            '[sS]eguir?': 60,
            '[rR]etornar?': 58
        }
    },
    60: {
        'frases': ['Chegando ao destino, você encontra outras pessoas, aparentemente também perturbadas buscando abrigo.'],
        'proximos_estados': {
            '[sS]eguir?': 61,
            '[rR]etornar?': 59
        }
    },
    61: {
        'frases': ['Como é um dia sem aulas, a escola está com os portões fechados, mas você dá a ideia de escalar os muros e invadir.'],
        'proximos_estados': {
            '[sS]eguir?': 62,
            '[rR]etornar?': 61
        }
    },
    62: {
        'frases': ['Felizmente você encontra as chaves da porta principal na portaria, e consegue abrir para que todos entrem.'],
        'proximos_estados': {
            '[sS]eguir?': 63,
            '[rR]etornar?': 61
        }
    },
    63: {
        'frases': ['Estranho 1 - O que está acontecendo?!\nEstranho 2 - Que loucura é essa?!\nEstranho 3 - Como a neblina pôde deixá-los tão perigosos?!'],
        'proximos_estados': {
            '[sS]eguir?': 64,
            '[rR]etornar?': 62
        }
    },
    64: {
        'frases': ['Todos estão assustados, tentando entender o que acabou de acontecer. Uma moça se coloca na frente de todos e começa a falar.'],
        'proximos_estados': {
            '[sS]eguir?': 65,
            '[rR]etornar?': 63
        }
    },
    65: {
        'frases': ['Moça - Por favor, peço que prestem atenção por um momento.'],
        'proximos_estados': {
            '[sS]eguir?': 66,
            '[rR]etornar?': 64
        }
    },
    66: {
        'frases': ['Surpreendentemente os demais realmente pararam por um momento para ouvi-la.'],
        'proximos_estados': {
            '[sS]eguir?': 67,
            '[rR]etornar?': 65
        }
    },
    67: {
        'frases': ['Moça - Eu me chamo Sara, e sou cientista na empresa farmacêutica próxima daqui.'],
        'proximos_estados': {
            '[sS]eguir?': 68,
            '[rR]etornar?': 66
        }
    },
    68: {
        'frases': ['Moça - O que vocês viram não era neblina. Infelizmente…'],
        'proximos_estados': {
            '[sS]eguir?': 69,
            '[rR]etornar?': 37
        }
    },
    69: {
        'frases': ['Ela parecia nervosa, com medo.'],
        'proximos_estados': {
            '[sS]eguir?': 70,
            '[rR]etornar?': 68
        }
    },
    70: {
        'frases': ['Moça - Ocorreu um vazamento de um produto químico que estávamos trabalhando. A solução se tornou instável por conta de um pequeno desequilíbrio na composição das substâncias, o que acabou causando um acidente, e como puderam ver, o vazamento de um gás.'],
        'proximos_estados': {
            '[sS]eguir?': 71,
            '[rR]etornar?': 69
        }
    },
    71: {
        'frases': ['Estranho 2 - Tinha que ser culpa do laboratório pra variar. E o que vocês vão fazer quanto a isso? O que você tá fazendo aqui? Deveria resolver essa bagunça, por que ainda tá aqui?!'],
        'proximos_estados': {
            '[sS]eguir?': 72,
            '[rR]etornar?': 70
        }
    },
    72: {
        'frases': ['Muitos ali começaram a discutir sobre como o laboratório era perigoso, nada de útil para o momento. Até que ela levantou a voz para falar novamente.'],
        'proximos_estados': {
            '[sS]eguir?': 73,
            '[rR]etornar?': 71
        }
    },
    73: {
        'frases': ['Sara - Por favor! Não discutam em um momento como esse. Precisamos achar um jeito de nos proteger, ainda há muito produto químico para se espalhar, e não estamos seguros aqui.'],
        'proximos_estados': {
            '[sS]eguir?': 74,
            '[rR]etornar?': 72
        }
    },
    74: {
        'frases': ['Estranho 1 - E o que você sugere? Que a gente saia daqui e vá até o meio da confusão?'],
        'proximos_estados': {
            '[sS]eguir?': 75,
            '[rR]etornar?': 73
        }
    },
    75: {
        'frases': ['Lucas - Deixem que ela termine, não temos muito tempo para ficar discutindo.'],
        'proximos_estados': {
            '[sS]eguir?': 76,
            '[rR]etornar?': 74
        }
    },
    76: {
        'frases': ['Sara - Obrigada. O gás é sim perigoso, eu sei bem disso, mas precisamos achar um jeito de sair daqui e ir para um lugar seguro.'],
        'proximos_estados': {
            '[sS]eguir?': 77,
            '[rR]etornar?': 75
        }
    },
    77: {
        'frases': ['Sara - Minha casa fica na região, se conseguirmos-'],
        'proximos_estados': {
            '[sS]eguir?': 78,
            '[rR]etornar?': 76
        }
    },
    78: {
        'frases': ['Estranho 2 - O que você está insinuando?! Realmente planeja sair daqui? Só pode estar louca. Estamos protegidos nessa altura, seria impossível aquela fumaça toda vir para essa escola.'],
        'proximos_estados': {
            '[sS]eguir?': 79,
            '[rR]etornar?': 77
        }
    },
    79: {
        'frases': ['Sara - Estou dizendo que é possível. A solução é muito abundante, não levará muito tempo até que sejamos engolidos por ela.'],
        'proximos_estados': {
            '[sS]eguir?': 80,
            '[rR]etornar?': 78
        }
    },
    80: {
        'frases': ['Não!'],
        'proximos_estados': {
            '[sS]eguir?': 81,
            '[rR]etornar?': 79
        }
    },
    81: {
        'frases': ['Não!'],
        'proximos_estados': {
            '[sS]eguir?': 82,
            '[rR]etornar?': 80
        }
    },
    82: {
        'frases': ['Não!'],
        'proximos_estados': {
            '[sS]eguir?': 83,
            '[rR]etornar?': 81
        }
    },
    83: {
        'frases': ['Não!'],
        'proximos_estados': {
            '[sS]eguir?': 84,
            '[rR]etornar?': 82
        }
    },
    84: {
        'frases': ['Não!'],
        'proximos_estados': {
            '[sS]eguir?': 85,
            '[rR]etornar?': 83
        }
    },
    85: {
        'frases': ['Não!'],
        'proximos_estados': {
            '[sS]eguir?': 86,
            '[rR]etornar?': 84
        }
    },
    86: {
        'frases': ['Não!'],
        'proximos_estados': {
            '[sS]eguir?': 87,
            '[rR]etornar?': 85
        }
    },
    87: {
        'frases': ['Não!'],
        'proximos_estados': {
            '[sS]eguir?': 88,
            '[rR]etornar?': 86
        }
    },
    88: {
        'frases': ['Não!'],
        'proximos_estados': {
            '[sS]eguir?': 89,
            '[rR]etornar?': 87
        }
    },
    89: {
        'frases': ['Não!'],
        'proximos_estados': {
            '[sS]eguir?': 90,
            '[rR]etornar?': 88
        }
    },
    90: {
        'frases': ['Não!'],
        'proximos_estados': {
            '[sS]eguir?': 91,
            '[rR]etornar?': 89
        }
    },
    91: {
        'frases': ['Não!'],
        'proximos_estados': {
            '[sS]eguir?': 92,
            '[rR]etornar?': 90
        }
    },
    92: {
        'frases': ['Não!'],
        'proximos_estados': {
            '[sS]eguir?': 93,
            '[rR]etornar?': 91
        }
    },
    93: {
        'frases': ['Não!'],
        'proximos_estados': {
            '[sS]eguir?': 94,
            '[rR]etornar?': 92
        }
    },
    94: {
        'frases': ['Não!'],
        'proximos_estados': {
            '[sS]eguir?': 95,
            '[rR]etornar?': 93
        }
    },
    95: {
        'frases': ['Não!'],
        'proximos_estados': {
            '[sS]eguir?': 96,
            '[rR]etornar?': 94
        }
    },
    96: {
        'frases': ['Não!'],
        'proximos_estados': {
            '[sS]eguir?': 81,
            '[rR]etornar?': 79
        }
    },
    97: {
        'frases': ['Não!'],
        'proximos_estados': {
            '[sS]eguir?': 81,
            '[rR]etornar?': 79
        }
    },
    98: {
        'frases': ['Não!'],
        'proximos_estados': {
            '[sS]eguir?': 81,
            '[rR]etornar?': 79
        }
    },
    99: {
        'frases': ['Não!'],
        'proximos_estados': {
            '[sS]eguir?': 81,
            '[rR]etornar?': 79
        }
    },
    100: {
        'frases': ['Não!'],
        'proximos_estados': {
            '[sS]eguir?': 81,
            '[rR]etornar?': 79
        }
    },
    80: {
        'frases': ['Não!'],
        'proximos_estados': {
            '[sS]eguir?': 81,
            '[rR]etornar?': 79
        }
    },
    80: {
        'frases': ['Não!'],
        'proximos_estados': {
            '[sS]eguir?': 81,
            '[rR]etornar?': 79
        }
    },
    80: {
        'frases': ['Não!'],
        'proximos_estados': {
            '[sS]eguir?': 81,
            '[rR]etornar?': 79
        }
    },
    80: {
        'frases': ['Não!'],
        'proximos_estados': {
            '[sS]eguir?': 81,
            '[rR]etornar?': 79
        }
    },
    80: {
        'frases': ['Não!'],
        'proximos_estados': {
            '[sS]eguir?': 81,
            '[rR]etornar?': 79
        }
    },
    80: {
        'frases': ['Não!'],
        'proximos_estados': {
            '[sS]eguir?': 81,
            '[rR]etornar?': 79
        }
    },
    80: {
        'frases': ['Não!'],
        'proximos_estados': {
            '[sS]eguir?': 81,
            '[rR]etornar?': 79
        }
    },
    80: {
        'frases': ['Não!'],
        'proximos_estados': {
            '[sS]eguir?': 81,
            '[rR]etornar?': 79
        }
    },
    80: {
        'frases': ['Não!'],
        'proximos_estados': {
            '[sS]eguir?': 81,
            '[rR]etornar?': 79
        }
    },
    80: {
        'frases': ['Não!'],
        'proximos_estados': {
            '[sS]eguir?': 81,
            '[rR]etornar?': 79
        }
    },
    80: {
        'frases': ['Não!'],
        'proximos_estados': {
            '[sS]eguir?': 81,
            '[rR]etornar?': 79
        }
    },
    80: {
        'frases': ['Não!'],
        'proximos_estados': {
            '[sS]eguir?': 81,
            '[rR]etornar?': 79
        }
    },
    80: {
        'frases': ['Não!'],
        'proximos_estados': {
            '[sS]eguir?': 81,
            '[rR]etornar?': 79
        }
    },
    80: {
        'frases': ['Não!'],
        'proximos_estados': {
            '[sS]eguir?': 81,
            '[rR]etornar?': 79
        }
    },
    80: {
        'frases': ['Não!'],
        'proximos_estados': {
            '[sS]eguir?': 81,
            '[rR]etornar?': 79
        }
    },
    80: {
        'frases': ['Não!'],
        'proximos_estados': {
            '[sS]eguir?': 81,
            '[rR]etornar?': 79
        }
    },
    80: {
        'frases': ['Não!'],
        'proximos_estados': {
            '[sS]eguir?': 81,
            '[rR]etornar?': 79
        }
    },
    80: {
        'frases': ['Não!'],
        'proximos_estados': {
            '[sS]eguir?': 81,
            '[rR]etornar?': 79
        }
    },
    80: {
        'frases': ['Não!'],
        'proximos_estados': {
            '[sS]eguir?': 81,
            '[rR]etornar?': 79
        }
    },
    80: {
        'frases': ['Não!'],
        'proximos_estados': {
            '[sS]eguir?': 81,
            '[rR]etornar?': 79
        }
    },
    
}

# Dicionário com os estados correntes de cada jogador.
canais_de_voz = {}