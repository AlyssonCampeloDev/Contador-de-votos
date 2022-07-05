import time

lula = 0
bolsonaro = 0
ciro = 0
branco = 0

while True:
    print('Escolha sua opção de voto:')
    print('1-lula.')
    print('2-bolsonaro.')
    print('3-ciro.')
    print('4-branco.')
    try:
        voto = int(input('Digite seu voto:\n'))
        time.sleep(1)
        if voto == 1:
            lula += 1
            print('Você votou no lula!')
        elif voto == 2:
            bolsonaro += 1
            print('Você votou no bolsonaro!')
        elif voto == 3:
            ciro += 1
            print('Você votou no ciro!')
        elif voto == 4:
            branco += 1 
            print('Você votou em branco!')
        else:
            print('Digite uma opção válida!')
            continue
        time.sleep(1)
        sair = str(input('Deseja finalizar a votação? [sim] para finalizar [nao] para continuar votando:'))
        if sair == 'sim':
            time.sleep(1)
            print('O Total de votos para o lula foi de:',lula)
            time.sleep(1)
            print('O Total de votos para o bolsonaro foi de:',bolsonaro)
            time.sleep(1)
            print('O Total de votos para o ciro foi de:',ciro)
            time.sleep(1)
            print('O Total de votos em branco foi de:',branco)
            time.sleep(1)
            
            if lula > bolsonaro and lula > ciro:
                print('Lula foi o vencedor das eleições!')
                time.sleep(1)
            
            elif bolsonaro > lula and bolsonaro > ciro:
                print('Bolsonaro foi o vencedor das eleições!')
                time.sleep(1)
            
            elif ciro > lula and ciro > bolsonaro:
                print('Ciro foi o vencendor das eleições!')
                time.sleep(1)
           
            elif branco > lula and branco > bolsonaro and branco > ciro:
                print('O voto em branco foi a opção mais votada')
                time.sleep(1)
            print('Saindo do sistema..')
            time.sleep(1)
            break
        
        elif sair == 'nao':
            continue
        else:
            print('Digite S ou N ')
            continue
        
    except(ValueError):
        print('Vote novamente digitando uma opção válida!') 