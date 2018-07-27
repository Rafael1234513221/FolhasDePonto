"""

PROGRAMA QUE DESCOBRE QUAIS HORÁRIOS COLOCAR NA FOLHA DE PONTO
DE TAL MODO QUE NÃO FIQUE HORÁRIO BRITÂNICO NEM DEVENDO HORA PRA
EMPRESA EM QUE PRESTA SERVIÇO.

"""

from random import randint


class Sistema:
    """Gestor de folha de ponto."""
    
    def __init__(self):
        """
        Apenas chama os modulos da classe
        """
        self.descobre_entrada()
        self.descobre_horario_de_almoço()
        self.descobre_saida()
        self.mostra_valores()
        
    
    def descobre_entrada(self):
        """
        Descobre o horário de entrada
        """
        self.entrada_hora = randint(7, 8)  
        if self.entrada_hora == 7:
            # Descobre os minutos pro caso de ter entrado as 7
            self.entrada_minuto = randint(50, 59)  
        
        elif self.entrada_hora == 8:
            # Descobre os minutos pro caso de ter entrado as 8
            self.entrada_minuto = randint(0, 10)  
        
        if self.entrada_hora < 10:
            # Coloca o 0 antes da hora, caso seja menor que 10
            self.entrada_hora = f'0{self.entrada_hora}'
        
        if self.entrada_minuto < 10:
            # Coloca o 0 antes da hora, caso seja menor que 10
            self.entrada_minuto = f'0{self.entrada_minuto}'
        
        # Return padrão
        return f'{self.entrada_hora}:{self.entrada_minuto}'
    

    def descobre_horario_de_almoço(self):
        """
        Descobre a ída e a vinda do horário de almoço.
        """
        # So pode ir pro almoço a parti de 12 horas
        self.ida_almoço_hora = 12
        
        self.ida_almoço_minuto = (randint(0, 10))
        
        if self.ida_almoço_minuto < 10:
            # Coloca o 0 antes do minuto, caso seja menor que 10
            self.ida_almoço_minuto = f'0{self.ida_almoço_minuto}'
        # Defina em formato hora a hora e minuto de ida pro almoço
        self.ida_almoço = f'{self.ida_almoço_hora}:{self.ida_almoço_minuto}'
        # So vai poder voltar do almoço depois das 13
        self.vinda_almoço_hora = 13
        # Sorteia um minuto entre 0 e 12
        self.vinda_almoço_minuto = (randint(0, 12))
        
        if self.vinda_almoço_minuto < 10:
            self.vinda_almoço_minuto = f'0{self.vinda_almoço_minuto}'
        # Define em formato Hora a volta do almoço
        self.vinda_almoço = f'{self.vinda_almoço_hora}:{self.vinda_almoço_minuto}'
        # Return padrão
        return f'Ida almoço = {self.ida_almoço} Vinda almoço= {self.vinda_almoço}'


    def descobre_saida(self):
        # Descobre o horario mínimo da saída
        self.saida = int(f'{self.entrada_hora}{self.entrada_minuto}') + 1000
        # Converte em string
        self.saida = str(self.saida)
        # Separa as HORAS
        self.saida_hora = int(self.saida[:2])
        # Sepera os MINUTOS
        self.saida_minuto = int(self.saida[2:])
        
        if self.saida_hora == 18:
            # Aumenta de 0 a 10 minutos no horário de saída
            self.saida_minuto += randint(0, 10)
        
        elif self.saida_hora == 17:
            self.saida_minuto += randint(0, 10)
            # Se com a soma os minutos passarem de 60 ele aumenta uma hora e zera os minutos
            if self.saida_minuto >= 60:
                # Aumento uma hora
                self.saida_hora += 1
                # Zero os minutos e acrescento o que sobrou dos 60
                self.saida_minuto -= 60
        
        # Coloca um 0 caso os minutos sejam menor que 10
        if self.saida_minuto < 10:
                self.saida_minuto = f'0{self.saida_minuto}'
        
        # Return padrão
        return f'{self.saida_hora}:{self.saida_minuto}'
    

    def mostra_valores(self):
        """
        Depois de adquirir os valores com as funções anteriores devemos repassar pro usuário.
        """
        return print(f'Entrada = {self.descobre_entrada()} Almoço = {self.descobre_horario_de_almoço()} Saida = {self.descobre_saida()}')


Sistema()
