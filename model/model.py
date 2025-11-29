from database.dao import DAO
import networkx as nx

class Model:
    def __init__(self):
        #self._nodes = None
        #self._edges = None
        self.G = nx.Graph()
        self._lista_hub = []         #Nodes
        self._lista_tratte = []      #Edges
        self._dizionario_hub = {}

    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutti gli Hub (i nodi) presenti e filtrando le Tratte con
        guadagno medio per spedizione >= threshold (euro)
        """
        # TODO
        self.G.clear()                    #Pulisco il grafo in modo da non sovrascriverlo ogni volta
        self._lista_hub = DAO.get_hub()          #Lista di oggetti Hub
        self._lista_tratte = DAO.get_tratta()    #Lista di oggetti Tratta

        for hub in self._lista_hub:       #Ciclo sui nodi
            self.G.add_node(hub)                     #Aggiungo ogni hub alla lista dei nodi
            self._dizionario_hub[hub.id] = hub       #Creo il dizionario di hub per poter aggiungere più facilmente le tratte


        for tratta in self._lista_tratte:            #Ciclo sulle tratte
            if tratta.guadagno_medio >= threshold:   #Condizione sul guadagno minimo
                self.G.add_edge(self._dizionario_hub[tratta.id_hub_A], self._dizionario_hub[tratta.id_hub_B], weight=tratta.guadagno_medio)

        return self.G


    def get_num_edges(self):
        """
        Restituisce il numero di Tratte (edges) del grafo
        :return: numero di edges del grafo
        """
        # TODO
        return self.G.number_of_edges()

    def get_num_nodes(self):
        """
        Restituisce il numero di Hub (nodi) del grafo
        :return: numero di nodi del grafo
        """
        # TODO
        return self.G.number_of_nodes()

    def get_all_edges(self):
        """
        Restituisce tutte le Tratte (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """
        # TODO
        return self._lista_tratte

