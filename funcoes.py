class FuncoesCronometro:
    def __init__(self): segundos, minutos, horas = 0, 0, 0
    
    def inicializar_tempo(self, horas, minutos, segundos):
    	self.segundos = segundos
    	self.minutos = minutos
    	self.horas = horas

    def resetar(self):
    	self.segundos = 0
    	self.minutos = 0
    	self.horas = 0

    def atualizar_tempo(self, incremento):
        self.segundos += incremento

        if self.segundos == 60:
            self.segundos = 0
            self.minutos += 1
        elif self.segundos == -1:
            self.segundos = 59
            self.minutos -= 1

        if self.minutos == 60:
            self.minutos = 0
            self.horas += 1
        elif self.minutos == -1:
            self.minutos = 59
            self.horas -= 1
            if self.horas == -1: self.horas = 23
