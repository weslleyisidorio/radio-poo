estacoes = {89.5:'Cocais', 91.5: 'mix', 94.1: "Boa", 99.1:'Clube'}
freqEstacoes =  list(estacoes.keys())
nomeEstacoes = list(estacoes.values())

class RadioFM:
    def __init__(self, vol_max, estacoes):
        self.volume_min = 0
        self.volume_max = vol_max
        self.freq_min = 88
        self.freq_max = 108
        self.estacoes = estacoes
        self.volume = None
        self.ligado = False
        self.estacao_atual = None
        self.frequencia_atual = None
        self.antena_habilitada = False

    def ligar(self):
        self.ligado = True
        self.volume = self.volume_min
        if self.antena_habilitada == True:
            self.frequencia_atual = freqEstacoes[0]
            self.estacao_atual = nomeEstacoes[0]


    def desligar(self):
        self.ligado = False
        self.volume = None
        self.frequencia_atual = None
        self.estacao_atual = None

    def aumentar_volume(self, vol = 1):
        if self.volume + vol <= self.volume_max:
            self.volume += vol

    def diminuir_volume(self, vol = 1):
        if self.volume - vol >= self.volume_min:
            self.volume -= vol
        
    def mudar_frequencia(self, est = 0):
        if est != 0:
            self.frequencia_atual = est
            self.estacao_atual = estacoes.get(est,'estação inexistente')

        else:
            if self.frequencia_atual != freqEstacoes[len(freqEstacoes)-1]:
                    
                self.frequencia_atual = freqEstacoes[freqEstacoes.index(self.frequencia_atual) + 1]

                self.estacao_atual = nomeEstacoes[nomeEstacoes.index(self.estacao_atual) + 1]

            else:
                self.frequencia_atual = freqEstacoes[0]
                self.estacao_atual = nomeEstacoes[0]

            
def main():
    radio1 = RadioFM(100, estacoes)
    radio1.antena_habilitada = True #Caso a antena não esteja habilitada ocorrerá um erro no rograma
    radio1.ligar()
    

    radio1.aumentar_volume()
    radio1.aumentar_volume(10)
    print('-------------- Radio 01 --------------')
    print(f'Volume: {radio1.volume}')
    print('--------------------------------------')

    
    print(f'Frequencia: {radio1.frequencia_atual}')
    print('--------------------------------------')

    radio1.mudar_frequencia()
    print(f'Estação: {radio1.estacao_atual}')
    print(f'Frequência: {radio1.frequencia_atual}')

    radio1.mudar_frequencia(94.1)
    print(f'Estação: {radio1.estacao_atual}')
    print(f'Frequência: {radio1.frequencia_atual}')

    radio1.mudar_frequencia(88.1)
    print(f'Estação: {radio1.estacao_atual}')
    print(f'Frequência: {radio1.frequencia_atual}')
    print('--------------------------------------')

    radio1.desligar()
    print(f'Ligado: {radio1.ligado}')
    print('--------------------------------------')
    
    print('-------------- Radio 02 --------------')
    radio2 = RadioFM(120, estacoes)
    radio2.antena_habilitada = True 
    radio2.ligar()

    radio2.diminuir_volume(5)
    print(f'Volume: {radio2.volume}') #volume não diminui do limite

    radio2.mudar_frequencia()
    print(f'Frequência: {radio2.frequencia_atual}')
    print(f'Estação: {radio2.estacao_atual}')

    radio2.aumentar_volume(130) #Volume não é atualizado
    print(f'Volume: {radio2.volume}')

    radio2.aumentar_volume(50)
    print(f'Volume: {radio2.volume}')

    radio2.desligar()
    print(f'Ligado: {radio2.ligado}')
    print('--------------------------------------')
    
    print('-------------- Radio 03 --------------')
    radio3 = RadioFM(60, estacoes)
    radio3.antena_habilitada = True
    radio3.ligar()
    print(f'Ligado: {radio3.ligado}')

    radio3.mudar_frequencia(1.1) # A rádio consegue ir para frequencias mais baixas que o minimo
    print(f'Frequencia: {radio3.frequencia_atual}')
    print(f'Estação: {radio3.estacao_atual}')

    radio3. mudar_frequencia(200.5) # A radio consegue ir para frequencias mais altas que o máximo
    print(f'Frequencia: {radio3.frequencia_atual}')
    print(f'Estação: {radio3.estacao_atual}')

if __name__ == '__main__':
    main()