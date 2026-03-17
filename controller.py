from view import View
from model import Model
import flet as ft

class Controller(object):
    def __init__(self, view: View):
        self._view = view
        self._model = Model()


    def getNmax(self):
        return self._model.Nmax
    def getTmax(self):
        return self._model.Tmax


    def reset(self,e):
        self._model.reset() #resetto lo stato del gioco lato modello
        self._view._txtT.value=self._model.T
        self._view._lvOut.controls.clear()
        self._view._lvOut.controls.append(ft.Text("Inizia il gioco! Indovina il numero che sto pensando"))
        self._view.update()

    def play(self,e):
        tentativoStr = self._view._txtInTentativo.value
        try:
            tentativo = int(tentativoStr)
        except ValueError:
            self._view._lvOut.controls.append(ft.Text("Errore devi inserire un valore numerico"))
            self._view.update()
            return
        res = self._model.play(tentativo)
        if res == 0:
            self._view._lvOut.controls.append(ft.Text(f"Hai vinto! Il valore corretto era: {tentativo}", color = "green"))
            self._view.update()
            return
        elif res ==2:
            self._view._lvOut.controls.append(ft.Text(f"Hai perso! Il valore corretto era: {self._model.segreto}"))
            self._view.update()
        elif res ==-1:
            self._view._lvOut.controls.append(ft.Text(f"Ritenta! Il segreto è più piccolo di:  {tentativo}"),                         )
            self._view.update()
        else:
            self._view._lvOut.controls.append(ft.Text(f"Ritenta!Il segreto è più grande di:  {tentativo}"))
