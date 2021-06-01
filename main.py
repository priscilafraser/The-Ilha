# Jogo de sobrevivência; Objetivo: Sobreviver 7 dias em uma ilha deserta
# Sobreviver caçando, bebendo água, dormindo, etc
from personagem import Personagem  # Importando os objetos;
from relogio import Relogio
from time import sleep

if (__name__ == "__main__"):
    persona = Personagem(10, 200, 15)  # Instanciando o personagem
    relogio = Relogio()  # Instanciando o tempo
    resultado = 0
    print('-=' * 30)
    print('Bem vindo ao The Ilha;')
    print('-=' * 30)
    sleep(3)
    print('Você está fazendo uma viagem de negócios, num jatinho fretado por sua empresa.')
    print('Porém, no meio do trajeto, uma tempestade horrivel se forma e acaba derrubando seu avião, \nque cai em uma ilha no meio do oceano.')
    sleep(3)
    print('Por algum milagre, você sobrevive a queda (o piloto não teve a mesma sorte), e agora,')
    print('você deverá sobreviver por 7 dias nessa ilha, que é o tempo necessário para sua empresa rastrear o local da queda e enviar o resgate.')
    sleep(3)
    print('Boa sorte, e tente não morrer!"')
    print('Cace, ou procure por frutas, e evite morrer.')
    while True:  # While infinito para repetir quantas vezes quiser
        print('-=' * 30)
        persona.set_saude(0)
        if persona.get_saude() == 0:
            print('Fim de jogo, cabou.')
            exit()
        print('Seus status:')
        print(persona)
        
        NoiteOuNao = relogio.get_noite()
        print("Horário: " + str(relogio))
        ch = int(
            input('''
Deseja:
    [1] - Caçar/Pescar
    [2] - Colher frutas
    [3] - Vasculhar escombros do avião
    [4] - Tratamento
    [5] - Dormir
    [6] - Sair do Jogo
            '''))
        if ch == 1: # Caçar
            resultado = persona.Cacar(NoiteOuNao)
            relogio.avancaTempo(resultado)

        elif ch == 2: # Colher frutas
            resultado = persona.FrutasMet(NoiteOuNao)
            relogio.avancaTempo(resultado)

        elif ch == 3: # Vasculhar escombros
            resultado = persona.buscaMet(NoiteOuNao)
            relogio.avancaTempo(resultado)

        elif ch == 4: # Tratar feridas
            persona.saudavel()

        elif ch == 5: # Dormir, passar o dia
            persona.refresca()
            relogio.passarDia()
            relogio.avancaTempo(0)

        elif ch == 6: # Sair do jogo :(
            final = str(input(
                'Você deseja sair do jogo? Todo seu progresso será perdido! [S/N]')).upper().strip()[0]
            if final == 'S':
                break
            elif final != 'S' or final != 'N':
                print('Opção inválida')
        resultado = relogio.get_data()
        if resultado == 1: # Caso o jogador seja salvo, termine o while.
            print('Você foi salvo! Muito bom!!')
            break

print('-=' * 30)
print('Fim de jogo!')
