import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def mostra_tratte(self, e):
        """
        Funzione che controlla prima se il valore del costo inserito sia valido (es. non deve essere una stringa) e poi
        popola "self._view.lista_visualizzazione" con le seguenti info
        * Numero di Hub presenti
        * Numero di Tratte
        * Lista di Tratte che superano il costo indicato come soglia
        """
        # TODO
        self._view.lista_visualizzazione.controls.clear()

        threshold_str = self._view.guadagno_medio_minimo.value

        try:
            if  not threshold_str:
                threshold = 0.0
            else:
                threshold = float(threshold_str)

        except ValueError:
            self._view.show_alert("Inserire un valore numerico valido")
            self._view.page.update()
            return

        grafo = self._model.costruisci_grafo(threshold)
        tratte = grafo.edges(data=True)
        self._view.lista_visualizzazione.controls.append(ft.Row(controls=[ft.Text("Numero di tratte: "), ft.Text(str(self._model.get_num_edges()))]))
        self._view.lista_visualizzazione.controls.append(ft.Row(controls=[ft.Text("Numero di nodi: "), ft.Text(str(self._model.get_num_nodes()))]))

        for u, v, data in tratte:
            guadagno = data.get('weight', 'N/D')
            self._view.lista_visualizzazione.controls.append(ft.Text(f"Hub {u} --> Hub {v} : {guadagno}"))


        self._view.page.update()


