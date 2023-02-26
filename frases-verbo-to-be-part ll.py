from time import sleep

I_am_a_good_father = ('eu sou um bom pai'),
I_am_at_home = ('eu estou em casa'),
I_am_really_tall = 'eu sou muito alto/eu sou realmente alto', 'eu sou realmente alto/eu sou muito alto'
Im_Russian = 'eu sou russo/eu sou russa', 'eu sou russa/eu sou russo'
Im_an_actor = ('eu sou um ator'),
Relax_I_am_not_dangerous = ('relaxa! eu não sou perigoso'),
I_am_not_his_neighbor = ('eu não sou vizinho dele'),
I_am_not_a_lawyer = ('eu não sou um advogado'),
Im_not_an_artist = ('eu não sou um artista'),
I_m_not_the_author_of_that_book = ('eu não sou o autor daquele livro'),
Am_I_a_terrible_teacher = ('eu sou um professor terrível?'),
Am_I_wrong = ('eu estou errado?'),
Am_I_happy = ('eu sou feliz?'),
Am_I_too_short_for_that_part = ('eu sou baixo demais para aquele papel?'),
Am_I_a_lousy_husband = 'eu sou um marido horrível?/eu sou um marido merda?', 'eu sou um marido merda?/eu sou um marido horrível?'
Come_on_You_are_just_a_kid = ('ah para! você é somente uma criança'),
You_are_a_monster = ('você é um monstro!'),
You_are_my_best_customer = ('você é meu melhor cliente'),
Seriously_You_are_crazy_dude = ('sério! você é louco, cara!'),
You_are_so_cute = 'você é tão fofo/vocês são tão fofos/você é tão fofa/vocês são tão fofas', 'vocês são tão fofos/você é tão fofo/vocês são tão fofas/você é tão fofa', 'você é tão fofa/vocês são tão fofas/você é tão fofo/vocês são tão fofos', 'vocês são tão fofas/você é tão fofa/vocês são tão fofos/você é tão fofo'
You_are_right = 'você está certo/vocês estão certos/você está certa/vocês estão certas', 'vocês estão certos/você está certo/vocês estão certas/você está certa', 'você está certa/vocês estão certas/você está certo/vocês estão certos', 'vocês estão certas/você está certa/vocês estão certos/você está certo'
You_are_not_American = 'você não é americano/vocês não são americanos/você não é americana/vocês não são americanas', 'vocês não são americanos/você não é americano/vocês não são americanas/você não é americana', 'você não é americana/vocês não são americanas/vocês não são americanos/você não é americano', 'vocês não são americanas/você não é americana/você não é americano/vocês não são americanos'
You_are_not_a_bad_student = 'você não é um mau aluno/você não é uma má aluna', 'você não é uma má aluna/você não é um mau aluno'


perguntas = {
    'Pergunta 1': {
        'pergunta': '1 - I am a good father',
        'respostas': I_am_a_good_father
    },
    'Pergunta 2': {
        'pergunta': '2 - I am at home',
        'respostas': I_am_at_home
        },
    'Pergunta 3': {
        'pergunta': '3 - (2 traduções) I am really tall',
        'respostas': I_am_really_tall
        },
    'Pergunta 4': {
        'pergunta': "4 - (2 traduções) I'm Russian",
        'respostas': Im_Russian
        },
    'Pergunta 5': {
        'pergunta': "5 - I'm an actor",
        'respostas': Im_an_actor
    },
    'Pergunta 6': {
        'pergunta': '6 - Relax! I am not dangerous',
        'respostas': Relax_I_am_not_dangerous
    },
    'Pergunta 7': {
        'pergunta': '7 - I am not his neighbor',
        'respostas': I_am_not_his_neighbor
    },
    'Pergunta 8': {
        'pergunta': '8 - I am not a lawyer',
        'respostas': I_am_not_a_lawyer
    },
    'Pergunta 9': {
        'pergunta': "9 - I'm not an artist",
        'respostas': Im_not_an_artist
    },
    'Pergunta 10': {
        'pergunta': "10 - I'm not the author of that book",
        'respostas': I_m_not_the_author_of_that_book
    },
    'Pergunta 11': {
        'pergunta': '11 - Am I a terrible teacher?',
        'respostas': Am_I_a_terrible_teacher
    },
    'Pergunta 12': {
        'pergunta': '12 - Am I wrong?',
        'respostas': Am_I_wrong
    },
    'Pergunta 13': {
        'pergunta': '13 - Am I happy?',
        'respostas': Am_I_happy
    },
    'Pergunta 14': {
        'pergunta': '14 - Am I too short for that part?',
        'respostas': Am_I_too_short_for_that_part
    },
    'Pergunta 15': {
        'pergunta': '15 - (2 traduções) Am I a lousy husband?',
        'respostas': Am_I_a_lousy_husband
    },
    'Pergunta 16': {
        'pergunta': '16 - Come on! You are just a kid',
        'respostas': Come_on_You_are_just_a_kid
    },
    'Pergunta 17': {
        'pergunta': '17 - You are a monster!',
        'respostas': You_are_a_monster
    },
    'Pergunta 18': {
        'pergunta': '18 - You are my best customer',
        'respostas': You_are_my_best_customer
    },
    'Pergunta 19': {
        'pergunta': "19 - Seriously! You're crazy, dude!",
        'respostas': Seriously_You_are_crazy_dude
    },
    'Pergunta 20': {
        'pergunta': "20 - (4 traduções) You're so cute",
        'respostas': You_are_so_cute
    },
     'Pergunta 21': {
        'pergunta': "21 - (4 traduções) You're right",
        'respostas': You_are_right
    },
    'Pergunta 22': {
        'pergunta': '22 - (4 traduções) You are not American',
        'respostas': You_are_not_American
    },
    'Pergunta 23': {
        'pergunta': '23 - (2 traduções) You are not a bad student',
        'respostas': You_are_not_a_bad_student
    },
}

print("""
 Código 100% OpenSource(Código aberto) para ajudar a comunidade, caso queira retribuir de alguma forma,
 este é o pix: (11) 9 5939-2326, iria ajudar muito!! pois muito tempo foi gasto,
 tmj e obrigado por usar este software :)
 
 pressione (q) para sair do programa.
 
 Serão 23 Perguntas ao todo, bons estudos!
 
 """)

erros = acertos = 0
for chave, valor in perguntas.items():
    lista = []
    print('Traduz')
    print(f'{valor["pergunta"]} = ', end='')
    lista.append(valor['respostas'])

    resp_user = input('').lower().strip()

    if resp_user == 'q':
        exit()

    for c in lista:
        if resp_user == '':
            print('ERROU\n')
            for v in c:
                print(f'Resposta correta: {v}')
            erros += 1
            print()
            print(f'Acertos: {acertos}  Erros: {erros}\n\n')
        else:
            if resp_user in c:
                print('ACERTOU\n')
                for v in c:
                    print(f'Resposta correta: {v}')
                acertos += 1
                lista.clear()
                print()
                print(f'Acertos: {acertos}  Erros: {erros}\n')
            else:
                print('ERROU\n')
                for v in c:
                    print(f'Resposta correta: {v}')
                erros += 1
                lista.clear()
                print()
                print(f'Erros: {erros}  Acertos: {acertos}\n')


if erros > 3:
    print(f'Cara você errou {erros} perguntas, estuda mais cumpadi!!!')
elif erros == 0:
    print(f'PARBÉNSSSSSSSSSSSSS FDP VC ERROU {erros} PERGUNTAS, TU É BRABO E EU SEMPRE ACREDITEI EM VC, '
          'TO ORGULHOSO PELO SEU ESFORÇO <3 UM DIA VOCÊ SERÁ RECOMPENSADO POR ISSO!!\n')

sleep(5)
print('BOAAA FINALIZOU AS QUESTÕES ')
print('Em 30 segundos a janela fechará')
sleep(30)
