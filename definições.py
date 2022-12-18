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
            '[sS]eguir?': 33,
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
        'frases': ['Sara - O gás é sim perigoso, mas deve ter algo que possa nos proteger, precisamos de máscaras e óculos de proteção. Algo resistente que nos proteja.'],
        'proximos_estados': {
            '[sS]eguir?': 81,
            '[rR]etornar?': 79
        }
    },
    81: {
        'frases': ['Lucas - Simples máscaras poderiam nos ajudar?'],
        'proximos_estados': {
            '[sS]eguir?': 82,
            '[rR]etornar?': 80
        }
    },
    82: {
        'frases': ['Ela para por um momento, com uma expressão preocupada, não parece ter fé nessa ideia.'],
        'proximos_estados': {
            '[sS]eguir?': 83,
            '[rR]etornar?': 81
        }
    },
    83: {
        'frases': ['Lucas - Nossa escola recebeu uns mergulhadores um tempo atrás para uma convenção, e eles guardavam alguns tanques de oxigênio para mergulho por aqui, soube que não levaram todos, se tivermos sorte eles devem estar em algum lugar pelo prédio. Devem ser mais eficazes que máscaras pra gripe.'],
        'proximos_estados': {
            '[sS]eguir?': 84,
            '[rR]etornar?': 82
        }
    },
    84: {
        'frases': ['Sua expressão muda em um passe de mágica.'],
        'proximos_estados': {
            '[sS]eguir?': 85,
            '[rR]etornar?': 83
        }
    },
    85: {
        'frases': ['Sara - Isso seria ótimo! Não podemos ter contato com o gás de forma alguma. Se encontrarmos os tanques, então poderemos sair daqui.'],
        'proximos_estados': {
            '[sS]eguir?': 86,
            '[rR]etornar?': 84
        }
    },
    86: {
        'frases': ['Estranho 1 - Mas para onde iríamos? Não podemos permanecer aqui, porque aquelas pessoas podem entrar, mas não podemos sair e nos jogar direto na cova dos leões.'],
        'proximos_estados': {
            '[sS]eguir?': 87,
            '[rR]etornar?': 85
        }
    },
    87: {
        'frases': ['Estranho 2 - Você pensa que é o que? Daniel? Se liguem, essa doida deve estar querendo esse lugar só pra ela enquanto empurra a gente morro a baixo, deveríamos expulsá-la daqui, e deixar que ela morra sozinha lá fora.'],
        'proximos_estados': {
            '[sS]eguir?': 88,
            '[rR]etornar?': 86
        }
    },
    88: {
        'frases': ['Lucas - Acredito que os tanques estejam no depósito do laboratório de química. Devem ter outros equipamentos por lá também. (Você se dirige à cientista)'],
        'proximos_estados': {
            '[sS]eguir?': 89,
            '[rR]etornar?': 87
        }
    },
    89: {
        'frases': ['Estranho 2 - Com licença garoto, eu estou falando.'],
        'proximos_estados': {
            '[sS]eguir?': 90,
            '[rR]etornar?': 88
        }
    },
    90: {
        'frases': ['Sara - Ótimo, precisamos ir buscá-los. Devem ser pesados então todos que quiserem sair venham conosco.'],
        'proximos_estados': {
            '[sS]eguir?': 91,
            '[rR]etornar?': 89
        }
    },
    91: {
        'frases': ['Estranho 2 - Mas pra onde vocês iriam?!'],
        'proximos_estados': {
            '[sS]eguir?': 92,
            '[rR]etornar?': 90
        }
    },
    92: {
        'frases': ['Lucas - Você(Sara) deu a ideia, deve saber de um local seguro, do contrário apenas permaneceria quieta por aqui.'],
        'proximos_estados': {
            '[sS]eguir?': 93,
            '[rR]etornar?': 91
        }
    },
    93: {
        'frases': ['Sara - Eu moro não muito longe, por conta do trabalho tenho um laboratório no subsolo, ele funciona como um bunker, pode nos proteger até que a situação seja revertida.'],
        'proximos_estados': {
            '[sS]eguir?': 94,
            '[rR]etornar?': 92
        }
    },
    94: {
        'frases': ['Lucas - Vou confiar em você, não temos muitas opções, e você deve ter mais conhecimento que nós sobre o caso. Vamos logo, não nos resta muito tempo.'],
        'proximos_estados': {
            '[sS]eguir?': 95,
            '[rR]etornar?': 93
        }
    },
    95: {
        'frases': ['Estranho 2 - Vocês vão todos morrer, tenho certeza.'],
        'proximos_estados': {
            '[sS]eguir?': 96,
            '[rR]etornar?': 94
        }
    },
    96: {
        'frases': ['Com exceção desse senhor nervoso, o resto te seguiu. Vendo que ficaria sozinho ele não ficou para trás'],
        'proximos_estados': {
            '[sS]eguir?': 97,
            '[rR]etornar?': 95
        }
    },
    97: {
        'frases': ['Ao chegar na sala vocês se deparam com uma trava eletrônica, para abrir precisaríamos de uma tag de acesso.'],
        'proximos_estados': {
            '[sS]eguir?': 98,
            '[rR]etornar?': 96
        }
    },
    98: {
        'frases': ['Estranho 1 - E agora? Como vamos abrir isso?'],
        'proximos_estados': {
            '[sS]eguir?': 99,
            '[rR]etornar?': 97
        }
    },
    99: {
        'frases': ['Estranho 2 - Eu disse que não daria certo.'],
        'proximos_estados': {
            '[sS]eguir?': 100,
            '[rR]etornar?': 98
        }
    },
    100: {
        'frases': ['Lucas - Deve ter alguma tag pela escola, talvez na portaria ou pela secretaria. Se não me engano tinham algumas no almoxarifado. Podemos nos separar e procurar.'],
        'proximos_estados': {
            '[sS]eguir?': 101,
            '[rR]etornar?': 99
        }
    },
    101: {
        'frases': ['Sara - Mas não conhecemos a escola tão bem.'],
        'proximos_estados': {
            '[sS]eguir?': 102,
            '[rR]etornar?': 100
        }
    },
    102: {
        'frases': ['Lucas - Se voltarem para a entrada, a secretaria é logo à direita, a portaria vocês já sabem onde é, o almoxarifado eu conheço, é mais complicado de explicar então posso ir lá.'],
        'proximos_estados': {
            '[sS]eguir?': 103,
            '[rR]etornar?': 101
        }
    },
    103: {
        'frases': ['Estranho 2 - Você realmente tem muita coragem em.'],
        'proximos_estados': {
            '[sS]eguir?': 104,
            '[rR]etornar?': 192
        }
    },
    104: {
        'frases': ['No total haviam 6 pessoas, 7 se contar com aquele senhor chato, mas ninguém estava ouvindo o que ele falava.'],
        'proximos_estados': {
            '[sS]eguir?': 105,
            '[rR]etornar?': 103
        }
    },
    105: {
        'frases': ['Vocês se separam, Sara vai com você até o almoxarifado. Aquele senhor chato acompanha o que parece ser um carteiro e um taxista, pelo que contaram estavam em horário de trabalho, juntos eles vão para a portaria. Também havia uma senhora acompanhada de seu cachorro, segundo ela não o largaria mesmo em meio a essa confusão, uma jovem optou por acompanhá-la até a secretaria, já que parecia ser um caminho mais simples para a velhinha.'],
        'proximos_estados': {
            '[sS]eguir?': 105,
            '[rR]etornar?': 104
        }
    },
    106: {
        'frases': ['Ninguém ficou só, até mesmo aquele senhor irritadiço seguiu em grupo, não importava o que dissesse parecia assustado, diria que é o mais covarde.'],
        'proximos_estados': {
            '[sS]eguir?': 107,
            '[rR]etornar?': 105
        }
    },
    107: {
        'frases': ['Lucas - Optou por me seguir pra não arriscar ser expulsa por aquele senhor?'],
        'proximos_estados': {
            '[sS]eguir?': 108,
            '[rR]etornar?': 106
        }
    },
    108: {
        'frases': ['Sara - Em parte sim, mas como você vai no almoxarifado achei melhor te seguir, pode ter algo útil por lá.'],
        'proximos_estados': {
            '[sS]eguir?': 109,
            '[rR]etornar?': 107
        }
    },
    109: {
        'frases': ['Lucas - Não sei sobre isso, mas você pode estar certa.'],
        'proximos_estados': {
            '[sS]eguir?': 110,
            '[rR]etornar?': 108
        }
    },
    110: {
        'frases': ['Chegando no almoxarifado, por sorte estava aberto.'],
        'proximos_estados': {
            '[sS]eguir?': 111,
            '[rR]etornar?': 109
        }
    },
    111: {
        'frases': ['Lucas - Nunca fui tão grato pelo senhor esquecer essa sala aberta.'],
        'proximos_estados': {
            '[sS]eguir?': 112,
            '[rR]etornar?': 110
        }
    },
    112: {
        'frases': ['Vocês começam a procurar por tags, ela também procura por “algo útil” como havia falado.'],
        'proximos_estados': {
            '[sS]eguir?': 113,
            '[rR]etornar?': 111
        }
    },
    113: {
        'frases': ['Sara - Isso era recorrente?'],
        'proximos_estados': {
            '[sS]eguir?': 114,
            '[rR]etornar?': 112
        }
    },
    114: {
        'frases': ['Lucas - oi?'],
        'proximos_estados': {
            '[sS]eguir?': 115,
            '[rR]etornar?': 113
        }
    },
    115: {
        'frases': ['Sara - A sala ficar destrancada.'],
        'proximos_estados': {
            '[sS]eguir?': 116,
            '[rR]etornar?': 114
        }
    },
    116: {
        'frases': ['Ela está tentando puxar assunto, por algum motivo não parece ser por simples simpatia.'],
        'proximos_estados': {
            '[sS]eguir?': 117,
            '[rR]etornar?': 115
        }
    },
    117: {
        'frases': ['Lucas - Lembro de ver ele levando bronca de tempos em tempos, até que começou a programar um despertador pro final do seu expediente. Ele melhorou depois disso, não sei como acabou deixando aberto de novo.'],
        'proximos_estados': {
            '[sS]eguir?': 118,
            '[rR]etornar?': 116
        }
    },
    118: {
        'frases': ['Sara - Hahaha. Me lembro de quando cheguei no laboratório, eu sempre esquecia algum detalhe nos procedimentos, nada que pudesse matar alguém, mas sempre levei bronca dos supervisores.'],
        'proximos_estados': {
            '[sS]eguir?': 119,
            '[rR]etornar?': 117
        }
    },
    119: {
        'frases': ['Ela esbarra em algo e derruba uma pilha de pastas no chão, você vai até ela ajudar, e percebe que suas mãos estavam tremendo tentando guardar aqueles documentos no lugar. Por isso estava puxando assunto?'],
        'proximos_estados': {
            '[sS]eguir?': 118,
            '[rR]etornar?': 118
        }
    },
    120: {
        'frases': ['ESCOLHA:\n "Continuar conversando" ou "Voltar a procurar"'],
        'proximos_estados': {
            '[cC]ontinuar conversando?': 121,
            '[vV]oltar a procurar?': 138,
            '[rR]etornar': 119
        }
    },
    121: {
        'frases': ['Lucas - Também costumava esquecer meu material quando cheguei aqui.'],
        'proximos_estados': {
            '[sS]eguir?': 122,
            '[rR]etornar?': 120
        }
    },
    122: {
        'frases': ['Você junta todas as pastas e coloca no lugar.'],
        'proximos_estados': {
            '[sS]eguir?': 123,
            '[rR]etornar?': 121
        }
    },
    123: {
        'frases': ['Lucas - Minha mãe sempre me dava bronca também. No fundamental sempre tinha que assinar bilhetes por eu esquecer meus livros ou algum material, hahaha. Me lembro de uma vez que tinhamos que levar cartolina para uma atividade em grupo, e eu fiquei responsável por isso, e adivinha.'],
        'proximos_estados': {
            '[sS]eguir?': 124,
            '[rR]etornar?': 122
        }
    },
    124: {
        'frases': ['Sara - Você esqueceu?'],
        'proximos_estados': {
            '[sS]eguir?': 125,
            '[rR]etornar?': 123
        }
    },
    125: {
        'frases': ['Lucas - Eu lembrei! Fiquei com o trabalho pronto e esqueci de trazer na apresentação'],
        'proximos_estados': {
            '[sS]eguir?': 126,
            '[rR]etornar?': 124
        }
    },
    126: {
        'frases': ['Sara - Hahaha. E o que aconteceu?'],
        'proximos_estados': {
            '[sS]eguir?': 127,
            '[rR]etornar?': 125
        }
    },
    127: {
        'frases': ['Lucas - Como você pode imaginar, levei bronca, não só da professora mas dos meus colegas. Lembro que nunca mais me deram responsabilidade sobre material.'],
        'proximos_estados': {
            '[sS]eguir?': 128,
            '[rR]etornar?': 126
        }
    },
    128: {
        'frases': ['Sara - É, ainda recebi responsabilidade mesmo com meus erros, querendo ou não você pode aprender com isso, mas se continuar sendo isento nada nunca vai mudar.'],
        'proximos_estados': {
            '[sS]eguir?': 129,
            '[rR]etornar?': 127
        }
    },
    129: {
        'frases': ['Lucas - Acho que esse não é o caso do senhor responsável por essa sala, hahaha.'],
        'proximos_estados': {
            '[sS]eguir?': 130,
            '[rR]etornar?': 128
        }
    },
    130: {
        'frases': ['Sara - Hahaha.'],
        'proximos_estados': {
            '[sS]eguir?': 131,
            '[rR]etornar?': 129
        }
    },
    131: {
        'frases': ['Lucas - SÉRIO? Que ótimo, agora podemos voltar. Olha isso.'],
        'proximos_estados': {
            '[sS]eguir?': 132,
            '[rR]etornar?': 130
        }
    },
    132: {
        'frases': ['Você mostra para ela alguns bastões de ferro.'],
        'proximos_estados': {
            '[sS]eguir?': 133,
            '[rR]etornar?': 131
        }
    },
    133: {
        'frases': ['Sara - O que é isso?'],
        'proximos_estados': {
            '[sS]eguir?': 134,
            '[rR]etornar?': 132
        }
    },
    134: {
        'frases': ['Lucas - Algo útil.'],
        'proximos_estados': {
            '[sS]eguir?': 135,
            '[rR]etornar?': 133
        }
    },
    135: {
        'frases': ['Sara - Você quer bater com isso nas pessoas lá fora.'],
        'proximos_estados': {
            '[sS]eguir?': 136,
            '[rR]etornar?': 134
        }
    },
    136: {
        'frases': ['Lucas - Não é para sairmos batendo em todo mundo, mas se nos atacarem e não conseguimos fugir podemos ao menos bater uma vez para que percam a consciência ou caiam. Só para que a gente consiga fugir.'],
        'proximos_estados': {
            '[sS]eguir?': 137,
            '[rR]etornar?': 135
        }
    },
    137: {
        'frases': ['Sara - Não queria ter que fazer isso, parte da responsabilidade de eles estarem assim é minha, mas não podemos dar brechas'],
        'proximos_estados': {
            '[sS]eguir?': 138,
            '[rR]etornar?': 148
        }
    },
    138: {
        'frases': ['Você ajuda e continua procurando pela tag.'],
        'proximos_estados': {
            '[sS]eguir?': 139,
            '[rR]etornar?': 120
        }
    },
    139: {
        'frases': ['Lucas - Achei.'],
        'proximos_estados': {
            '[sS]eguir?': 140,
            '[rR]etornar?': 138
        }
    },
    140: {
        'frases': ['Sara - É sério? Que bom.'],
        'proximos_estados': {
            '[sS]eguir?': 141,
            '[rR]etornar?': 139
        }
    },
    141: {
        'frases': ['Lucas - Podemos voltar agora.'],
        'proximos_estados': {
            '[sS]eguir?': 142,
            '[rR]etornar?': 140
        }
    },
    142: {
        'frases': ['Sara - Espera!'],
        'proximos_estados': {
            '[sS]eguir?': 143,
            '[rR]etornar?': 141
        }
    },
    143: {
        'frases': ['Ela se abaixou para pegar algo. São bastões de ferro.'],
        'proximos_estados': {
            '[sS]eguir?': 144,
            '[rR]etornar?': 142
        }
    },
    144: {
        'frases': ['Lucas - O que é isso?'],
        'proximos_estados': {
            '[sS]eguir?': 145,
            '[rR]etornar?': 143
        }
    },
    145: {
        'frases': ['Sara - Algo útil.'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    146: {
        'frases': ['Lucas - Não queria fazer isso, mas realmente pode ser útil se formos atacados.'],
        'proximos_estados': {
            '[sS]eguir?': 147,
            '[rR]etornar?': 145
        }
    },
    147: {
        'frases': ['Sara - Penso o mesmo, parte da culpa pode ser minha por essa bagunça, mas precisamos nos defender.'],
        'proximos_estados': {
            '[sS]eguir?': 148,
            '[rR]etornar?': 146
        }
    },
    148: {
        'frases': ['Vocês voltam até onde estavam antes. A senhora e a garota já voltaram, mas o outro grupo não.'],
        'proximos_estados': {
            '[sS]eguir?': 149,
            '[rR]etornar?': 147
        }
    },
    149: {
        'frases': ['Você entrega um bastão para cada e vai atrás dos demais na portaria, Sara te segue.'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    150: {
        'frases': ['Lucas - Aconteceu alguma coisa?'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    151: {
        'frases': ['Você se dirige aos senhores, mas vê o senhor chato tentando trancar a saída.'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    152: {
        'frases': ['Sara - O que você está fazendo?!'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    153: {
        'frases': ['Senhor chato - trancando a saída, não quero que nenhum de vocês volte infectado tentando me matar.'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    154: {
        'frases': ['Lucas - A decisão de sair ou não, é nossa. O senhor não pode fazer nada!'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    155: {
        'frases': ['Senhor chato - E o que você vai fazer? Me bater com o bastão? Quando isso acabar, se acabar, chamarei a polícia e irei denunciar vocês por tentativa de homicídio!'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    156: {
        'frases': ['Lucas - Faça o que quiser!'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    157: {
        'frases': ['Você grita, e aquele senhor se assusta.'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    158: {
        'frases': ['Senhor chato - E você tá falando com quem nesse tom? Eu deveria te dar um bom tapa pra aprender a ter respeito.'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    159: {
        'frases': ['Ele levanta a mão e vai em sua direção. A jovem que estava com a senhora chega e o empurra para longe com um chute bem no meio da barriga. Ele se desequilibra e cai. Então começamos a desfazer a bagunça dele enquanto a Sara o amarra.'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    160: {
        'frases': ['Lucas - Vamos voltar para dentro e ir atrás das máscaras e dos óculos.'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    161: {
        'frases': ['Voltando, a jovem fica responsável pelo senhor amarrado, levando ele aos puxões pela corda que o segurava como um prisioneiro. Ela finalmente se apresenta como Júlia.'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    162: {
        'frases': ['Os senhores também acharam uma tag.'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    163: {
        'frases': ['No total vocês conseguiram 5 chaves. Ao tentar abrir a porta com uma das tags, o acesso é negado, e aparece a mensagem de que você tem mais 2 tentativas.'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    164: {
        'frases': ['Graças a presença dos tanques dos mergulhadores a segurança foi reforçada nas travas, já que é um equipamento caro.'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    165: {
        'frases': ['Senhor chato - Vai explodir se vocês errarem?'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    166: {
        'frases': ['Ele solta uma risada com tom de deboche.'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    167: {
        'frases': ['Júlia - Se eu pudesse, te jogaria no gás só pra testar esse brinquedo.'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    168: {
        'frases': ['Ela balança o bastão de ferro, o deixando quieto rapidinho.'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    169: {
        'frases': ['Sara - Foco. O senhor deveria ajudar, e não incomodar. Todos estamos assustados com a situação, não é como se fosse nosso maior desejo sair daqui num momento como esse. Então apenas cale a boca por favor.'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    170: {
        'frases': ['Ele parece inconformado, mas se vira para Júlia e se acalma rapidinho.'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    171: {
        'frases': ['ESCOLHA ENTRE AS TAGS RESTANTES:\n"Tag 1"\n"Tag 2"\n"Tag 3"\n"Tag 4"'],
        'proximos_estados': {
            '[tT]ag 1?': 172,
            '[tT]ag 2?': 219,
            '[tT]ag 3?': 229,
            '[tT]ag 4?': 224,
            '[rR]etornar?': 170
        }
    },
    172: {
        'frases': ['A tag é recusada'],
        'proximos_estados': {
            '[tT]ag 2?': 173,
            '[tT]ag 3?': 229,
            '[tT]ag 4?': 221,
            '[rR]etornar?': 171
        }
    },
    173: {
        'frases': ['Não funcionou'],
        'proximos_estados': {
            '[tT]ag 3?': 229,
            '[tT]ag 4?': 174,
            '[rR]etornar?': 144
        }
    },
    174: {
        'frases': ['Infelizmente não era essa'],
        'proximos_estados': {
            '[sS]eguir?': 175,
            '[rR]etornar?': 173
        }
    },
    175: {
        'frases': ['O alarme é acionado!'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    176: {
        'frases': ['Sara - Droga e agora?'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    177: {
        'frases': ['É possível ouvir os gritos daquelas pessoas se aproximando.'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    178: {
        'frases': ['Todos entram em pânico. Estão indo cada um para um lado.'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    179: {
        'frases': ['Lá estão eles! Já podemos vê-los correndo em nossa direção.'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    180: {
        'frases': ['Todos estavam apavorados, gritando e tentando fugir. Júlia tenta ajudar a velhinha a se defender e tenta levá-la para um local seguro. Sem sucesso. Os infectados puxam a senhora enquanto Júlia tenta ajudar, mas nada funciona, até que ela é empurrada e a solta. A senhora então, apavorada, tenta lutar por sua vida, mas enquanto é atacada o gás a cobre. Cheia de lágrimas e revoltada com a situação, a jovem começa a atacar os infectados com o bastão de ferro. Um cai no chão enquanto outro alcança seu cabelo, puxando e a derrubando. Mesmo no chão ela ainda tenta lutar, mas recebe socos e arranhões, até que para de reagir quando é arrastada e se desequilibra na escadaria.'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    181: {
        'frases': ['Os senhores tentam fugir, mas não são velozes o suficiente. Um infectado pula no senhor chato e acaba empurrando os demais. Todos tentando levantar novamente, mas com a atual idade já não conseguem agir rapidamente, todos são pegos e recebem um fim triste. Você nem soube o nome deles.'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    182: {
        'frases': ['Sara e você tentando fugir subindo as escadas. Ela tropeça e cai, mas felizmente ainda se recupera com sua ajuda e vocês continuam.'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    183: {
        'frases': ['Mais a frente um dos infectados a puxa pelo pé, e ela cai novamente. Você tenta ajudá-la, mas outros surgem e ela te empurra para longe, mandando que você corra. Você está receoso mas obedece.'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    184: {
        'frases': ['Parece que você está seguro, mas eles aparecem na sua frente e você precisa voltar. Buscando um local seguro nada se resolve, até que você se vê encurralado, então decide subir nos pilares do pátio'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    185: {
        'frases': ['Finalmente longe de todos você pode respirar, mas não por muito tempo, o gás se aproxima, então você continua subindo até que não tem para onde ir.'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    186: {
        'frases': ['Não há saída. O gás te alcança, você começa a sentir irritação na garganta e nos olhos. De repente, é como se pusessem fogo em seus olhos, eles ardem tanto que você se solta e cai do pilar. Tudo está nebuloso e você vê alguém mais à frente, é sua mãe!'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    187: {
        'frases': ['Como ela veio para aqui? Sua casa é distante o suficiente para ela estar segura. Quando se vira, seus olhos estão tão vermelhos quanto o fogo, parece que tem sangue saindo deles. Ela está completamente atordoada, você se aproxima.'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    188: {
        'frases': ['Lucas - Isso é sangue?'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    189: {
        'frases': ['Ela se vira para te observar, calmamente se aproxima. Ainda é difícil ver, a sensação dos olhos já não é mais a mesma.'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    190: {
        'frases': ['Mãe - Lucas?'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    200: {
        'frases': ['Ela diz com uma voz aconchegante.'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    201: {
        'frases': ['Lucas - Sou eu mãe.'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    202: {
        'frases': ['Você corre para um abraço, mas ela te empurra.'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    203: {
        'frases': ['Mãe - Você é uma decepção, por que nunca me ouve?'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    204: {
        'frases': ['Você não entende o que está acontecendo.'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    205: {
        'frases': ['Lucas - Está tudo bem? A senhora está estranha.'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    206: {
        'frases': ['Mãe - Eu não sou o problema. Olha pra você tão grande, e tão imaturo. Não foi isso que eu planejei,você é pura decepção.'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    207: {
        'frases': ['Seus olhos já estão cheios de lágrimas perante tais palavras. Mas o que está acontecendo? Ela nunca disse algo assim.'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    208: {
        'frases': ['Mãe - Você devia apenas morrer!'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    209: {
        'frases': ['Ela te empurra. Você já não vê nada.'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    210: {
        'frases': ['Sara - Lucas?'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    211: {
        'frases': ['Uma voz meio trêmula surge, Sara está viva?'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    212: {
        'frases': ['Sara - Lucas…\nMãe - Você está bem?'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    213: {
        'frases': ['Espera não parece com ela.'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    214: {
        'frases': ['Mãe - Apenas morra!'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    215: {
        'frases': ['Sara - LUCAS!'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    216: {
        'frases': ['Mãe - MORRA!'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    217: {
        'frases': ['Você a ataca, começa a bater desordenadamente nela. Até que as vozes param. Mas você já não vê, não entende, não parece estar vivo. Tudo é turbulento e vazio, não há nada, nem ninguém.'],
        'proximos_estados': {
            '[sS]eguir?': 146,
            '[rR]etornar?': 144
        }
    },
    218: {
        'frases': ['FIM 1\nEscreva "Retornar" para voltar as escolhas de tags e continuar o jogo'],
        'proximos_estados': {
            '[rR]etornar?': 171
        }
    },
    219: {
        'frases': ['Não funcionou'],
        'proximos_estados': {
            '[tT]ag 1?': 220,
            '[tT]ag 3?': 229,
            '[tT]ag 4?': 222,
            '[rR]etornar?': 171
        }
    },
    220: {
        'frases': ['A tag é recusada'],
        'proximos_estados': {
            '[tT]ag 3?': 229,
            '[tT]ag 4?': 174,
            '[rR]etornar?': 219
        }
    },
    221: {
        'frases': ['Infelizmente não era essa'],
        'proximos_estados': {
            '[tT]ag 3?': 229,
            '[tT]ag 2?': 226,
            '[rR]etornar?': 172
        }
    },
    222: {
        'frases': ['Infelizmente não era essa'],
        'proximos_estados': {
            '[tT]ag 3?': 229,
            '[tT]ag 1?': 223,
            '[rR]etornar?': 171
        }
    },
    223: {
        'frases': ['A tag é recusada'],
        'proximos_estados': {
            '[sS]eguir': 175,
            '[rR]etornar?': 171
        }
    },
    224: {
        'frases': ['Infelizmente não era essa'],
        'proximos_estados': {
            '[tT]ag 3?': 229,
            '[tT]ag 2?': 227,
            '[tT]ag 1?': 225,
            '[rR]etornar?': 171
        }
    },
    225: {
        'frases': ['Infelizmente não era essa'],
        'proximos_estados': {
            '[tT]ag 3?': 229,
            '[tT]ag 2?': 226,
            '[rR]etornar?': 171
        }
    },
    226: {
        'frases': ['Não funcionou'],
        'proximos_estados': {
            '[sS]eguir?': 175,
            '[rR]etornar?': 225
        }
    },
    227: {
        'frases': ['Não funcionou'],
        'proximos_estados': {
            '[tT]ag 3?': 229,
            '[tT]ag 1?': 228,
            '[rR]etornar?': 171
        }
    },
    228: {
        'frases': ['A tag é recusada'],
        'proximos_estados': {
            '[sS]eguir?': 175,
            '[rR]etornar?': 227
        }
    },
    229: {
        'frases': ['Deu certo!'],
        'proximos_estados': {
            '[sS]eguir?': 230,
            '[rR]etornar?': 170
        }
    },
    230: {
        'frases': ['Lucas - Deu certo!'],
        'proximos_estados': {
            '[sS]eguir?': 231,
            '[rR]etornar?': 229
        }
    },
    231: {
        'frases': ['Todos entram rapidamente e começam a vasculhar a área, Sara fecha a porta para que possam estar seguros de possíveis perigos.'],
        'proximos_estados': {
            '[sS]eguir?': 232,
            '[rR]etornar?': 230
        }
    },
    232: {
        'frases': ['Finalmente encontram as máscaras.'],
        'proximos_estados': {
            '[sS]eguir?': 234,
            '[rR]etornar?': 231
        }
    },
    233: {
        'frases': ['Júlia - Viu? Deveria ter um pouco mais de fé.'],
        'proximos_estados': {
            '[sS]eguir?': 234,
            '[rR]etornar?': 232
        }
    },
    234: {
        'frases': ['Senhor chato - Ainda não estamos seguros.'],
        'proximos_estados': {
            '[sS]eguir?': 235,
            '[rR]etornar?': 233
        }
    },
    235: {
        'frases': ['Ele empina o nariz e vira o rosto enquanto pega uma das máscaras, logo ele, que não queria participar . No final só está com medo como todos os outros.'],
        'proximos_estados': {
            '[sS]eguir?': 236,
            '[rR]etornar?': 234
        }
    },
    236: {
        'frases': ['Sara - Que bom que encontramos.'],
        'proximos_estados': {
            '[sS]eguir?': 237,
            '[rR]etornar?': 235
        }
    },
    237: {
        'frases': ['Lucas - Realmente, parte de mim estava duvidando que ainda teríamos elas aqui.'],
        'proximos_estados': {
            '[sS]eguir?': 238,
            '[rR]etornar?': 236
        }
    },
    238: {
        'frases': ['Sara - Agora só precisamos nos arrumar e seguir caminho.'],
        'proximos_estados': {
            '[sS]eguir?': 239,
            '[rR]etornar?': 237
        }
    },
    239: {
        'frases': ['Senhor chato - E sobreviver.'],
        'proximos_estados': {
            '[sS]eguir?': 240,
            '[rR]etornar?': 238
        }
    },
    240: {
        'frases': ['Lucas - Escuta aqui senhor.'],
        'proximos_estados': {
            '[sS]eguir?': 241,
            '[rR]etornar?': 239
        }
    },
    241: {
        'frases': ['Senhor chato - Tenho nome. Antônio!'],
        'proximos_estados': {
            '[sS]eguir?': 242,
            '[rR]etornar?': 240
        }
    },
    242: {
        'frases': ['Tudo para. Antônio… Péssimo nome, péssimo momento.'],
        'proximos_estados': {
            '[sS]eguir?': 243,
            '[rR]etornar?': 241
        }
    },
    243: {
        'frases': ['Sara - Tudo bem?'],
        'proximos_estados': {
            '[sS]eguir?': 244,
            '[rR]etornar?': 242
        }
    },
    244: {
        'frases': ['Você volta a si.'],
        'proximos_estados': {
            '[sS]eguir?': 245,
            '[rR]etornar?': 243
        }
    },
    245: {
        'frases': ['Lucas - Sr. Antônio. Não temos tempo para ficar discutindo. Precisamos encontrar um local seguro. Sei que está com medo mas não podemos duvidar de nada nesse momento, essa pode ser nossa única chance.'],
        'proximos_estados': {
            '[sS]eguir?': 246,
            '[rR]etornar?': 244
        }
    },
    246: {
        'frases': ['Ele faz uma cara de desinteresse mas parece ter compreendido a situação. Talvez agora colabore.'],
        'proximos_estados': {
            '[sS]eguir?': 247,
            '[rR]etornar?': 245
        }
    },
    247: {
        'frases': ['Todos começam a se preparar, colocam as máscaras, apoiam os tanques com suportes e põem os óculos de mergulho.'],
        'proximos_estados': {
            '[sS]eguir?': 248,
            '[rR]etornar?': 246
        }
    },
    248: {
        'frases': ['Júlia - O gás já está aqui!'],
        'proximos_estados': {
            '[sS]eguir?': 249,
            '[rR]etornar?': 247
        }
    },
    249: {
        'frases': ['Todos entram em choque. Sara já abre a porta para evitar barulhos que chamem os infectados.'],
        'proximos_estados': {
            '[sS]eguir?': 250,
            '[rR]etornar?': 248
        }
    },
    250: {
        'frases': ['Sara - Todos permaneçam em silêncio e me acompanhem, talvez eles não nos vejam com todo esse gás.'],
        'proximos_estados': {
            '[sS]eguir?': 251,
            '[rR]etornar?': 249
        }
    },
    251: {
        'frases': ['Já prontos vocês seguem caminho. Sara vai na frente enquanto todos a acompanham em fila, tentando fazer o mínimo de barulho possível. Você está junto dela para que possam encontrar a saída da escola.'],
        'proximos_estados': {
            '[sS]eguir?': 252,
            '[rR]etornar?': 250
        }
    },
    252: {
        'frases': ['Todos saem sem problema, parece que aquelas pessoas ainda não chegaram.'],
        'proximos_estados': {
            '[sS]eguir?': 253,
            '[rR]etornar?': 251
        }
    },
    253: {
        'frases': ['Descendo o morro vocês avistam o primeiro infectado, mesmo com todo o gás ainda é possível vê-lo.'],
        'proximos_estados': {
            '[sS]eguir?': 254,
            '[rR]etornar?': 252
        }
    },
    254: {
        'frases': ['O cãozinho da senhora começa a ficar agitado, até que consegue pular dos braços dela e correr até um dos infectados, onde começa a correr. Ele não o tinha notado até começar a latir. A senhora corre até ele gritando para que volte, isso claramente chama a atenção daquelas pessoas. Mas antes que possamos segurá-la, um infectado aparece da direção oposta e pula em cima da velhinha, outros surgem em meio aos gritos dela. Já não é possível alcançá-la.'],
        'proximos_estados': {
            '[sS]eguir?': 255,
            '[rR]etornar?': 253
        }
    },
    255: {
        'frases': ['Foi um susto muito grande para todos, que estavam em choque ainda, ninguém esperava que ela realmente fosse atrás do cãozinho, era uma situação triste porém perigosa. Júlia tenta ir até ela mas Sara a segura, não podemos fazer mais nada. As lágrimas de Júlia descem em abundância, mas dela não sai um som, ainda não estamos seguros, então continuamos caminho até chegar na rua principal, enquanto Júlia segue tentando se acalmar, os óculos com certeza não ajudam nada.'],
        'proximos_estados': {
            '[sS]eguir?': 256,
            '[rR]etornar?': 254
        }
    },
    256: {
        'frases': ['Nos aproximando da praça, Sara parece confusa.'],
        'proximos_estados': {
            '[sS]eguir?': 257,
            '[rR]etornar?': 255
        }
    },
    257: {
        'frases': ['Diálogo entre sussurros:'],
        'proximos_estados': {
            '[sS]eguir?': 258,
            '[rR]etornar?': 256
        }
    },
    258: {
        'frases': ['Lucas - O que aconteceu?'],
        'proximos_estados': {
            '[sS]eguir?': 259,
            '[rR]etornar?': 257
        }
    },
    259: {
        'frases': ['Sara - Não consigo me localizar, me mudei não tem muito tempo. Minha casa fica entrando em alguma dessas ruas.'],
        'proximos_estados': {
            '[sS]eguir?': 260,
            '[rR]etornar?': 258
        }
    },
    260: {
        'frases': ['O senhor que parecia um carteiro entrou na conversa.'],
        'proximos_estados': {
            '[sS]eguir?': 261,
            '[rR]etornar?': 259
        }
    },
    261: {
        'frases': ['Carteiro - Você sabe o nome da rua? Algum ponto de referência?'],
        'proximos_estados': {
            '[sS]eguir?': 262,
            '[rR]etornar?': 260
        }
    },
    262: {
        'frases': ['Sara - Não sem o nome da rua, ainda não me acostumei, eu ainda estava voltando pra casa pelo GPS.'],
        'proximos_estados': {
            '[sS]eguir?': 263,
            '[rR]etornar?': 261
        }
    },
    263: {
        'frases': ['Lucas - Você não lembra de nenhuma particularidade da rua?'],
        'proximos_estados': {
            '[sS]eguir?': 264,
            '[rR]etornar?': 262
        }
    },
    264: {
        'frases': ['Sara - Não consigo pensar. Eu acho que tinha um bar na esquina, é uma bifurcação.'],
        'proximos_estados': {
            '[sS]eguir?': 265,
            '[rR]etornar?': 263
        }
    },
    265: {
        'frases': ['Lucas - Acho que é mais a frente!'],
        'proximos_estados': {
            '[sS]eguir?': 266,
            '[rR]etornar?': 264
        }
    },
    266: {
        'frases': ['Todos seguem tentando encontrar esse ponto de referência.'],
        'proximos_estados': {
            '[sS]eguir?': 267,
            '[rR]etornar?': 265
        }
    },
    267: {
        'frases': ['Lucas - Olhe!'],
        'proximos_estados': {
            '[sS]eguir?': 268,
            '[rR]etornar?': 266
        }
    },
    268: {
        'frases': ['Um bar logo à frente pode ser nossa referência.'],
        'proximos_estados': {
            '[sS]eguir?': 269,
            '[rR]etornar?': 267
        }
    },
    269: {
        'frases': ['Carteiro - Se acalmem, vejam.'],
        'proximos_estados': {
            '[sS]eguir?': 270,
            '[rR]etornar?': 268
        }
    },
    270: {
        'frases': ['É possível ver do outro lado da rua outro bar, quase que idêntico.'],
        'proximos_estados': {
            '[sS]eguir?': 271,
            '[rR]etornar?': 269
        }
    },
    271: {
        'frases': ['Júlia - Que porcaria é essa?'],
        'proximos_estados': {
            '[sS]eguir?': 272,
            '[rR]etornar?': 270
        }
    },
    272: {
        'frases': ['Carteiro - Dois amigos abriram esse bar, mas um descobriu que a mulher estava dormindo com o outro, esse ficou com o bar e com a mulher, que mais pra frente o traiu com outro e o deixou. Mas o amigo que foi traído abriu esse outro bar para acabar com o negócio do antigo amigo. Eles ficavam nessa implicação para ver quem conseguia gerenciar melhor o bar.'],
        'proximos_estados': {
            '[sS]eguir?': 273,
            '[rR]etornar?': 271
        }
    },
    273: {
        'frases': ['Lucas - Que maravilha. O que fazemos agora?'],
        'proximos_estados': {
            '[sS]eguir?': 274,
            '[rR]etornar?': 272
        }
    },
    274: {
        'frases': ['Carteiro - Uma das ruas é sem saída, a outra pode ser a casa dela.'],
        'proximos_estados': {
            '[sS]eguir?': 275,
            '[rR]etornar?': 273
        }
    },
    275: {
        'frases': ['Sara - Eu não sei dizer, entrando na rua eu preciso virar em outra, mas nunca fui até o final então não sei se a rua é sem saída.'],
        'proximos_estados': {
            '[sS]eguir?': 276,
            '[rR]etornar?': 275
        }
    },
    276: {
        'frases': ['Lucas - Tente lembrar de mais alguma referência que tenha perto da sua casa, pode ser mais fácil achar.'],
        'proximos_estados': {
            '[sS]eguir?': 277,
            '[rR]etornar?': 275
        }
    },
    277: {
        'frases': ['Sara - Acho que tinha uma igreja próxima, mas não tenho certeza.'],
        'proximos_estados': {
            '[sS]eguir?': 278,
            '[rR]etornar?': 276
        }
    },
    278: {
        'frases': ['Carteiro - Estou em dúvida de qual das ruas tem a igreja. Já tem um tempo que não entrego nada aqui.'],
        'proximos_estados': {
            '[sS]eguir?': 279,
            '[rR]etornar?': 277
        }
    },
    279: {
        'frases': ['Júlia - Podemos seguir por um caminho, se ela não se lembrar de nada voltamos.'],
        'proximos_estados': {
            '[sS]eguir?': 280,
            '[rR]etornar?': 278
        }
    },
    280: {
        'frases': ['Parece que não se tem outra opção. Mas para onde o grupo deveria seguir?'],
        'proximos_estados': {
            '[sS]eguir?': 281,
            '[rR]etornar?': 279
        }
    },
    282: {
        'frases': ['Carteiro - Estou em dúvida de qual das ruas tem a igreja. Já tem um tempo que não entrego nada aqui.'],
        'proximos_estados': {
            '[sS]eguir?': 282,
            '[rR]etornar?': 280
        }
    },
    283: {
        'frases': ['ESCOLHA ENTRE AS VIAS:\n"Esquerda" ou "Direita"'],
        'proximos_estados': {
            '[eD]squerda?': 284,
            '[dD]ireita': 302,
            '[rR]etornar?': 282
        }
    },
    284: {
        'frases': ['Todos entram em acordo para tentar ir pela esquerda.'],
        'proximos_estados': {
            '[sS]eguir?': 285,
            '[rR]etornar?': 283
        }
    },
    285: {
        'frases': ['Parece haver uma movimentação mais à frente. Todos buscam manter a calma, podemos vê-los perdidos, atordoados, um gato passa a frente deles como se nada estivesse acontecendo, até subir em um muro e miar. É quando todos tentam alcançá-lo, expulsando o bichinho ao susto.'],
        'proximos_estados': {
            '[sS]eguir?': 286,
            '[rR]etornar?': 284
        }
    },
    286: {
        'frases': ['Todos passam pelo outro lado e seguem caminho. Após um tempo você começa a sussurrar.'],
        'proximos_estados': {
            '[sS]eguir?': 287,
            '[rR]etornar?': 285
        }
    },
    287: {
        'frases': ['Lucas - Vocês também viram?'],
        'proximos_estados': {
            '[sS]eguir?': 288,
            '[rR]etornar?': 286
        }
    },
    288: {
        'frases': ['Sara - Parece que não conseguem ver.'],
        'proximos_estados': {
            '[sS]eguir?': 289,
            '[rR]etornar?': 287
        }
    },
    289: {
        'frases': ['Júlia - Devemos ser cuidadosos, mesmo se algum passar por nós não podemos deixá-los perceber, não sabemos em que grau não podem enxergar.'],
        'proximos_estados': {
            '[sS]eguir?': 290,
            '[rR]etornar?': 288
        }
    },
    290: {
        'frases': ['Todos consentem e seguem caminho.'],
        'proximos_estados': {
            '[sS]eguir?': 291,
            '[rR]etornar?': 289
        }
    },
    291: {
        'frases': ['Sara - Não reconheço esse caminho, não é por aqui.'],
        'proximos_estados': {
            '[sS]eguir?': 292,
            '[rR]etornar?': 290
        }
    },
    292: {
        'frases': ['Os demais parecem chateados e assustados, se o grupo por onde passamos tiver voltado a se espalhar, será difícil atravessar.'],
        'proximos_estados': {
            '[sS]eguir?': 293,
            '[rR]etornar?': 291
        }
    },
    293: {
        'frases': ['Antônio - Que merda.'],
        'proximos_estados': {
            '[sS]eguir?': 294,
            '[rR]etornar?': 292
        }
    },
    294: {
        'frases': ['Lucas - Cuidado com o tom de voz, eles podem nos ouvir.'],
        'proximos_estados': {
            '[sS]eguir?': 295,
            '[rR]etornar?': 293
        }
    },
    295: {
        'frases': ['Ele começa a sussurrar.'],
        'proximos_estados': {
            '[sS]eguir?': 296,
            '[rR]etornar?': 294
        }
    },
    296: {
        'frases': ['Antônio - O que faremos?'],
        'proximos_estados': {
            '[sS]eguir?': 297,
            '[rR]etornar?': 295
        }
    },
    297: {
        'frases': ['Lucas - Obviamente voltar, não tem outra saída.'],
        'proximos_estados': {
            '[sS]eguir?': 298,
            '[rR]etornar?': 296
        }
    },
    298: {
        'frases': ['Todos parecem receosos, mas não podemos continuar parados ali.'],
        'proximos_estados': {
            '[sS]eguir?': 299,
            '[rR]etornar?': 297
        }
    },
    299: {
        'frases': ['Na volta o grupo havia se espalhado.'],
        'proximos_estados': {
            '[sS]eguir?': 300,
            '[rR]etornar?': 298
        }
    },
    300: {
        'frases': ['Antônio encontrou uma pedra pelo caminho, acenou com a mão para todos irem para um lado e ele jogou a pedra para o outro lado da rua.'],
        'proximos_estados': {
            '[sS]eguir?': 301,
            '[rR]etornar?': 299
        }
    },
    301: {
        'frases': ['O grupo de infectados seguiu o som no maior alvoroço, graças a isso podemos voltar e entrar na outra rua.'],
        'proximos_estados': {
            '[sS]eguir?': 302,
            '[rR]etornar?': 300
        }
    },
    302: {
        'frases': ['Sara parece receosa mas parece estar encontrando semelhanças com seu caminho.'],
        'proximos_estados': {
            '[sS]eguir?': 303,
            '[rR]etornar?': 301
        }
    },
    303: {
        'frases': ['Ela nos guia virando em uma esquina e seguindo caminho.'],
        'proximos_estados': {
            '[sS]eguir?': 304,
            '[rR]etornar?': 302
        }
    },
    304: {
        'frases': ['Sara - É logo à frente!'],
        'proximos_estados': {
            '[sS]eguir?': 305,
            '[rR]etornar?': 303
        }
    },
    305: {
        'frases': ['Ela parece animada, não parecem haver infectados à frente.'],
        'proximos_estados': {
            '[sS]eguir?': 306,
            '[rR]etornar?': 304
        }
    },
    306: {
        'frases': ['Seguindo é possível ver alguém cambaleando, deveriamos nos preocupar?'],
        'proximos_estados': {
            '[sS]eguir?': 307,
            '[rR]etornar?': 305
        }
    },
    307: {
        'frases': ['A pessoa parece atordoada mas parece nos ver, como ela faz isso em meio a neblina sem proteção? Será que na verdade eles conseguem ver?'],
        'proximos_estados': {
            '[sS]eguir?': 308,
            '[rR]etornar?': 306
        }
    },
    308: {
        'frases': ['Estranho - Vocês aí!'],
        'proximos_estados': {
            '[sS]eguir?': 309,
            '[rR]etornar?': 307
        }
    },
    309: {
        'frases': ['A pessoa fala em alto e bom som, chamando a atenção de infectados.'],
        'proximos_estados': {
            '[sS]eguir?': 310,
            '[rR]etornar?': 308
        }
    },
    310: {
        'frases': ['Estranho - Não me abandonem.'],
        'proximos_estados': {
            '[sS]eguir?': 311,
            '[rR]etornar?': 209
        }
    },
    311: {
        'frases': ['Cada fala dessa pessoa parece de alguém embriagado, será que ainda não foi infectado?'],
        'proximos_estados': {
            '[sS]eguir?': 312,
            '[rR]etornar?': 310
        }
    },
    312: {
        'frases': ['Estranho - Eu to com medo.'],
        'proximos_estados': {
            '[sS]eguir?': 313,
            '[rR]etornar?': 311
        }
    },
    313: {
        'frases': ['Ela fala se aproximando, podemos ver uma mulher, os olhos estão vermelhos assim como os outros, mas não parece estar cem por cento como eles, parece ter consciência, devemos tomar cuidado.'],
        'proximos_estados': {
            '[sS]eguir?': 314,
            '[rR]etornar?': 312
        }
    },
    314: {
        'frases': ['Estranha - Por que não me ouvem? Vão me deixar aqui?'],
        'proximos_estados': {
            '[sS]eguir?': 315,
            '[rR]etornar?': 313
        }
    },
    315: {
        'frases': ['Ela vem se aproximando aos poucos, tentando andar normalmente.'],
        'proximos_estados': {
            '[sS]eguir?': 316,
            '[rR]etornar?': 314
        }
    },
    316: {
        'frases': ['Estranha - Eu disse que to com medo...'],
        'proximos_estados': {
            '[sS]eguir?': 317,
            '[rR]etornar?': 315
        }
    },
    317: {
        'frases': ['Estranha - POR QUE VOCÊS NÃO ME OUVEM?!'],
        'proximos_estados': {
            '[sS]eguir?': 318,
            '[rR]etornar?': 316
        }
    },
    318: {
        'frases': ['Era o que estava faltando para chamar os infectados, que começam a correr em direção dela, mas vocês estão no caminho. Tentam subir o muro mas nada é efetivo, eles se aproximam depressa e vocês parecem presos.'],
        'proximos_estados': {
            '[sS]eguir?': 319,
            '[rR]etornar?': 317
        }
    },
    319: {
        'frases': ['Antônio - Para a parede.'],
        'proximos_estados': {
            '[sS]eguir?': 320,
            '[rR]etornar?': 318
        }
    },
    320: {
        'frases': ['Ele manda nosso grupo encostar na parede enquanto nos empurra. Então corre para o outro lado.'],
        'proximos_estados': {
            '[sS]eguir?': 321,
            '[rR]etornar?': 319
        }
    },
    321: {
        'frases': ['Antônio - VOCÊS IMBECIS, VENHAM AQUI DESGRAÇADOS!'],
        'proximos_estados': {
            '[sS]eguir?': 322,
            '[rR]etornar?': 320
        }
    },
    322: {
        'frases': ['Ele os chama! E continua gritando para chamar sua atenção.'],
        'proximos_estados': {
            '[sS]eguir?': 323,
            '[rR]etornar?': 321
        }
    },
    323: {
        'frases': ['Lucas - NÃO!'],
        'proximos_estados': {
            '[sS]eguir?': 324,
            '[rR]etornar?': 322
        }
    },
    324: {
        'frases': ['Todos se assustam com seu grito e o puxam, correm em disparada até a casa de Sara, que consegue abrir e nos colocar para dentro em segurança.'],
        'proximos_estados': {
            '[sS]eguir?': 325,
            '[rR]etornar?': 323
        }
    },
    325: {
        'frases': ['Sr. Antônio morreu tentando nos ajudar, mesmo se dizendo contra a ideia e tentando nos provocar.'],
        'proximos_estados': {
            '[sS]eguir?': 326,
            '[rR]etornar?': 324
        }
    },
    326: {
        'frases': ['Ela nos leva até o porão, onde está a entrada do bunker.'],
        'proximos_estados': {
            '[sS]eguir?': 327,
            '[rR]etornar?': 325
        }
    },
    327: {
        'frases': ['Coloca sua senha e nos deixa entrar. A porta se fecha e as luzes acendem, ainda não podemos tirar a proteção pois o gás é sugado e outro é espirrado em nós, finalmente podemos tirar todo aquele peso e a porta se abre.'],
        'proximos_estados': {
            '[sS]eguir?': 328,
            '[rR]etornar?': 326
        }
    },
    328: {
        'frases': ['Na entrada ainda não temos acesso ao laboratório, temos que entrar em banheiros, tinham feminino e masculino, onde devemos nos limpar e colocar roupas limpas que se encontravam lá. Parece que o trabalho dela é realmente perigoso e delicado.'],
        'proximos_estados': {
            '[sS]eguir?': 329,
            '[rR]etornar?': 327
        }
    },
    329: {
        'frases': ['O banho é reconfortante, em meio a toda a situação é realmente muito bom estar aqui.'],
        'proximos_estados': {
            '[sS]eguir?': 330,
            '[rR]etornar?': 328
        }
    },
    330: {
        'frases': ['Todos conseguem comer e beber, e finalmente podemos tentar relaxar, o que não é tão simples já que infelizmente acompanhamos diversas mortes e cenas assustadoras hoje.'],
        'proximos_estados': {
            '[sS]eguir?': 331,
            '[rR]etornar?': 329
        }
    },
    331: {
        'frases': ['Cada momento parecia um filme de terror.'],
        'proximos_estados': {
            '[sS]eguir?': 332,
            '[rR]etornar?': 330
        }
    },
    332: {
        'frases': ['Sara conseguiu contactar outras pessoas, que após um período conseguiram “limpar” a situação.'],
        'proximos_estados': {
            '[sS]eguir?': 333,
            '[rR]etornar?': 331
        }
    },
    333: {
        'frases': ['Não tem como reviver aqueles que se foram, e aqueles que foram infectados lutam para voltar ao normal, alguns nunca mais foram vistos.'],
        'proximos_estados': {
            '[sS]eguir?': 334,
            '[rR]etornar?': 332
        }
    },
    334: {
        'frases': ['No noticiário pudemos ver outros sobreviventes que conseguiram fugir para longe de tudo por estarem mais afastados.'],
        'proximos_estados': {
            '[sS]eguir?': 335,
            '[rR]etornar?': 333
        }
    },
    335: {
        'frases': ['O laboratório foi “processado”, foi o que disseram. Fecharam as portas e não tinham permissão para trabalhar nunca mais.'],
        'proximos_estados': {
            '[sS]eguir?': 336,
            '[rR]etornar?': 334
        }
    },
    336: {
        'frases': ['O laboratório não poderia mais causar problemas, nem poderia atuar.'],
        'proximos_estados': {
            '[sS]eguir?': 337,
            '[rR]etornar?': 335
        }
    },
    337: {
        'frases': ['Isso era o que pensávamos, mas o silêncio deles apenas durou o suficiente para o episódio ser arquivado e camuflado. Ninguém mais lembrava do ocorrido, foi quando aconteceu novamente.'],
        'proximos_estados': {
            '[sS]eguir?': 338,
            '[rR]etornar?': 336
        }
    },
    338: {
        'frases': ['Nenhum gás foi vazado, nenhum infectado voltou, foi a última vez que algo assim aconteceu.'],
        'proximos_estados': {
            '[sS]eguir?': 339,
            '[rR]etornar?': 337
        }
    },
    339: {
        'frases': ['Porque o vírus por eles criado, não pôde ser revertido.'],
        'proximos_estados': {
            '[sS]eguir?': 340,
            '[rR]etornar?': 338
        }
    },
    340: {
        'frases': ['FIM 2\nObrigada por jogar!\nDeseja "Reiniciar"?'],
        'proximos_estados': {
            '[rR]einiciar?': 2
        }
    },


}

# Dicionário com os estados correntes de cada jogador.
canais_de_voz = {}
