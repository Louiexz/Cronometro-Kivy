from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from funcoes import FuncoesCronometro

class Cronometro(BoxLayout):
    def __init__(self, **kwargs):
        super(Cronometro, self).__init__(**kwargs)
        self.funcoes = FuncoesCronometro()

    def atualizar_valores(self):
        self.ids.segundos.text = f"{self.funcoes.segundos:02d}"
        self.ids.minutos.text = f"{self.funcoes.minutos:02d}"
        self.ids.horas.text = f"{self.funcoes.horas:02d}"

    def obter_valores_iniciais(self):
        horas = int(self.ids.horas.text)
        minutos = int(self.ids.minutos.text)
        segundos = int(self.ids.segundos.text)
        return horas, minutos, segundos

    def cronometro_iniciar(self, incremento=1):
        self.cronometro_parar()
        horas, minutos, segundos = self.obter_valores_iniciais()
        self.funcoes.inicializar_tempo(horas, minutos, segundos)
        self.cronometro_event = Clock.schedule_interval(lambda dt: self.atualizar_tempo(incremento), 1)

    def cronometro_reverter(self): self.cronometro_iniciar(incremento=-1)

    def cronometro_parar(self):
        if hasattr(self, 'cronometro_event'):
            Clock.unschedule(self.cronometro_event)
            del self.cronometro_event

        self.funcoes.resetar()

    def atualizar_tempo(self, incremento):
        self.atualizar_valores()
        self.funcoes.atualizar_tempo(incremento)

class CronometroApp(App):
    icon = "img/ampulheta.png"
    def build(self): return Cronometro()
