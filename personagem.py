from random import randint
import os


class Personagem():
    def __init__(self, fome, energia, saude):
        self.__fome = fome  # Declarando atributos necessários, fome: usada para medir o nível de fome do personagem,se for baixo demais, pode dar consequências
        self.__energia = energia  # Mostra a energia existente para continuar suas ações
        # Revela o estado do personagem com relação à ferimento, etc.
        self.__saude = saude
        self.enjoo = False
        self.contusao = False
        self.medicamento = 0
        self.kit = 0
        # self.__vida = 15

    def __str__(self):
        return f'{self.fomeEx()}\n{self.saudeEx()}\n{self.energiaEx()}'

    def get_saude(self): # Metodo dedicado para retornar o valor de saude, checar
        return self.__saude # se o jogo vai acabar por causa de morte;

    def set_energia(self, ch): # Metodo dedicado para alterar valores de Energia
        if ch == 6969:
            self.__energia = 200
        elif ch == 420420:
            self.__energia = 140
        else:
            self.__energia -= ch

    def set_saude(self,valor): # Metodo dedicado para alterar valores de Saude
        if self.__fome <= 0:
            self.__saude = 0
            print('Você morreu de fome!')
        self.__saude -= valor

    def set_fome(self, ch): # Metodo dedicado para alterar valores de Fome
        if self.__fome < 16:
            self.__fome += ch
        else:
            print('Você está cheio!')
            self.__fome -= 5

    def fomeEx(self): # Metodo dedicado para exibir status de fome
        if self.__fome >= 12:
            return 'Você não está com fome'
        elif self.__fome >= 8:
            return 'Você está ficando com fome'
        elif self.__fome >= 4:
            return 'Você está faminto!'
        elif self.__fome > 0:
            return 'Você está morrendo de fome!'
        else:
            return 'Você morreu de fome.'

    def saudeEx(self): # Metodo dedicado para exibir status de saude
        if self.enjoo == True:
            print('Você está com um enjôo forte! Comer coisas podres não é legal.')
        if self.contusao == True:
            print('Você está dolorido, e seu machucado não está melhorando...')
        if self.__saude >= 12:
            return f'Você não tem machucados.'
        elif self.__saude >= 8:
            return f'Você tem alguns machucados.'
        elif self.__saude >= 4:
            return f'Você não deveria estar vazando por ai! Procure se tratar.'
        elif self.__saude >= 1:
            return 'Já vi cadáveres mais saudáveis que você!!! Se trate imediatamente!!!'
        else:
            return 'Cabou-se o que era doce. Você morreu.'

    def energiaEx(self,): # Metodo dedicado para exibir status de energia
        if self.__energia >= 140:
            return 'Você não está cansado.'
        elif self.__energia >= 90:
            return 'Você está ficando cansado.'
        elif self.__energia >= 40:
            return 'Você está muito cansado.'
        elif self.__energia > 0:
            return 'Você está exausto.'
        else:
            return 'Você não tem mais como continuar o dia. Vá descansar.'

    def Cacar(self,noite=False): # Ação de caçar;
        os.system('cls')
        if self.__energia >= 35:
            if noite == False: # Se for de dia, poderá caçar tranquilamente :)
                if randint(0, 101) <= 30: # 30% de chance
                    print('Você conseguiu pescar um peixe.')
                    self.set_fome(2)
                    self.set_energia(20)
                    return 90
                elif randint(0, 101) <= 55: # 20% de chance
                    print('Você não conseguiu caçar nada')
                    self.set_fome(-1)
                    self.set_energia(15)
                    return 100
                elif randint(0, 101) <= 70: # 20% de chance
                    print('Você conseguiu caçar um coelho.')
                    self.set_fome(3)
                    self.set_energia(25)
                    return 80
                elif randint(0, 101) <= 90: # 20 % de chance
                    escolha = str(input('Você encontrou uma carcaça de animal. Deseja comer? [S/N] ')).upper().strip()[0]
                    if escolha == 'S':
                        taxa = randint(0, 10)
                        if taxa >= 5:
                            self.enjoo = True
                            print('Você começa a ponderar "Por que diabos eu comi essa carne podre?.')
                            self.set_fome(1)
                            self.set_energia(20)
                            return 25
                        else:
                            self.set_fome(1)
                            self.set_energia(20)
                            return 25
                    else:
                        self.set_fome(-1)
                        self.set_energia(25)
                        return 35
                else: # 10% de chance, Urso!
                    print('Você encontrou um urso. CORRE!')
                    self.contusao = True
                    self.set_fome(-2)
                    self.set_saude(3)
                    self.set_energia(35)
                    return 180
            elif randint(0,101) <= 50: # Sortudo, não aconteceu nada. 50% de chance
                print('Você não encontrou nada! Está escuro demais!')
                return 100
            elif randint(0,101) <= 90: # 40% de chance
                print('Você ouve um rugido... uma puma está indo atrás de você!')
                self.set_fome(-3)
                self.set_saude(5)
                self.set_energia(30)
                self.contusao = True
                return 180
            else: # 10% de chance de insta-death. Perfeição.
                print('Você achou uma matilha de lobos! Meus pêsames.')
                self.set_saude(15)
                return 0
        elif self.__energia == 0:
            print('Você está exausto. Vá descansar!')
            return 0
        else:
            print('Você não tem energia o suficiente para essa ação!')
            return 0

    def FrutasMet(self,noite): # Metodo dedicado para ação de procurar por frutas.
        os.system('cls')
        if self.__energia >= 15:
            if noite == False:
                if randint(0, 101) <= 50: # 50% de chance de achar uma fruta normal
                    escolha = str(input('Você encontra uma fruta exótica, deseja comer? [S/N] ').upper().strip()[0])
                    if escolha == 'S':
                        self.set_fome(1)
                        print('Muito gostosa!')
                        self.set_energia(5)
                        return 70
                    else:
                        print('Você decide não comer a fruta.')
                        self.set_fome(-1)
                        return 60
                elif randint(0, 101) <= 80: # 30% de chance de achar um tóxica
                    escolha = str(
                        input('Você encontra uma fruta exótica, deseja comer? [S/N] ')).upper().strip()[0]
                    if escolha == 'S':
                        self.set_fome(-1)
                        self.set_saude(1)
                        self.enjoo = True
                        print('Você vomita enlouquecidamente.')
                        self.set_energia(10)
                        return 70
                    else:
                        print('Você decide não comer a fruta.')
                        self.set_fome(-1)
                        return 60 
                else: # 20% de chande de achar um urso.
                    print(
                        'Você está colhendo frutas tranquilamente, então você ouve um barulho.\nUm urso resolveu catar frutar também!\n CORRA!!!')
                    self.contusao = True
                    self.set_fome(-2)
                    self.set_saude(3)
                    self.set_energia(15)
                    return 180
            elif randint(0,101) <= 50: # Sortudo. 50% de chance.
                print('Você não encontrou nada! Está escuro demais!')
                return 100
            elif randint(0,101) <= 90: # 40% de chance
                print('Você ouve um rugido... uma puma está indo atrás de você!')
                self.set_fome(-3)
                self.set_saude(5)
                self.set_energia(30)
                self.contusao = True
                return 180
            else: # 10% de chance de insta-death. Perfeição.
                print('Você achou uma matilha de lobos! Meus pêsames.')
                self.set_saude(15)
                return 0
        elif self.__energia == 0:
            print('Você está exausto. Vá descansar!')
            return 0
        else:
            print('Você não tem energia o suficiente para essa ação!')
            return 0

    def refresca(self): # Metodo dedicado para resetar valores importantes do personagem; Dormir.
        os.system('cls')
        if self.contusao == False or self.enjoo == False:
            self.set_energia(6969)  # Resetando energia ao fim do dia
            self.set_fome(-3) 
            self.set_saude(-2) # -1 pois set_saude usa -=, invertendo a operação para soma  
        else:
            self.set_energia(420420) # Resetando energia ao fim do dia
            self.set_fome(-3)

    def saudavel(self): # Metodo dedicado para tratar ferimentos
        os.system('cls')
        if self.enjoo == True and self.medicamento >= 1:
            self.enjoo = False
            self.medicamento -= 1
            print('Após tomar os medicamentos, você se sente melhor.')
        elif self.contusao == True and self.kit >= 1:
            self.contusao = False
            self.kit -= 1
            print('Você usa o kit de primeiros socorros e consegue aliviar a dor da contusão.')
        else:
            print('Você não está ferido, ou não tem medicamento! Vasculhe o avião!')

    def buscaMet(self,noite): # Metodo dedicado pra buscar medicamentos no avião
        os.system('cls')
        if noite == False:
            if randint(0, 300) <= 75 or randint(0, 300) > 225: # 50% de chance
                print('Você não encontra nada.')
                self.set_energia(15)
                self.set_fome(-1)
                return 30
            elif randint(0, 300) > 75 and randint(0, 300) <= 150: # 25% de chance
                print('Você encontrou um kit de primeiros socorros!')
                self.kit += 1
                self.set_energia(15)
                self.set_fome(-1)
                return 30
            else: # 25% de chance
                print('Você encontrou uma caixa com medicamentos!')
                self.medicamento += 1
                self.set_energia(15)
                self.set_fome(-1)
                return 30
        elif randint(0,101) <= 50: # Sortudo. 50% de chance.
            print('Você não encontrou nada! Está escuro demais!')
            return 100
        elif randint(0,101) <= 90: # 40% de chance.
            print('Você ouve um rugido... uma puma está indo atrás de você!')
            self.set_fome(-3)
            self.set_saude(5)
            self.set_energia(30)
            self.contusao = True
            return 180
        else: # 10% de chance de um insta-death. Perfeição.
            print('Você achou uma matilha de lobos! Meus pêsames.')
            self.set_saude(15)
            return 0
