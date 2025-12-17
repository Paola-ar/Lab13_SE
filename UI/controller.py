import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_graph(self, e):
        """ Handler per gestire creazione del grafo """""
        # TODO

        self._model.buildWeightedGraph()
        self._view.lista_visualizzazione_1.clear()
        self._view.lista_visualizzazione_1.append(ft.Text(f" Numero vertici: {self._model.G.number_of_nodes()}, numero archi: {self._model.G.number_of_edges()}"))
        min_p, max_p = self._model.get_edges_weight_min_max()
        self._view.lista_visualizzazione_1.append(ft.Text(f"Informazioni sui pesi degli archi - valore minimo: {min_p} e valore massimo: {max_p}"))

    def handle_conta_edges(self, e):
        """ Handler per gestire il conteggio degli archi """""
        # TODO

    def handle_ricerca(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del cammino """""
        # TODO