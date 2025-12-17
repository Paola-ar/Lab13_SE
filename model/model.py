import networkx as nx
from database.dao import  DAO



class Model:
    def __init__(self):
        self.G = nx.DiGraph()

        self.id_map = {}


        self.lista_cromosomi = []
        self.lista_geni = []
        self.lista_geni_connessi = []

        self.load_cromosomi ()
        self.load_geni()
        self.load_geni_connessi()

    def load_cromosomi(self):
        self.lista_cromosomi = DAO.getCromosomi()

    def load_geni(self ):
        self.lista_geni = DAO.getGeni()

    def load_geni_connessi(self):
        self.lista_geni_connessi = DAO.getGeniConnessi()

        self.corr = []
        self.pesi = []



    def buildWeightedGraph(self):
        # peso = 0

        self.geniCromosomi = DAO.readCromosomi()
        self.id_gene = {g.id: g for g in self.geniCromosomi}

        self.corr = DAO.readIterazioni()
        self.edges = {}
        """for i in self.iterazioni:

            i1 = self.id_gene[i].gene1
            r2 = self.id_gene[i].gene2
            peso = self.id_gene[i].correlazione
            self.pesi.append(peso)
            edges.append((r1, r2,peso))"""
        """cromosomi = DAO.readCromosomi()
        for a in range(len(cromosomi)+1):
            c1 = cromosomi[a]
            c2 = cromosomi[a+1]
            if c1.id != c2.id and c1.cromosoma != c2.cromosoma:
                for id in self.id_gene:
                    if id in self.iterazioni:

                        if id == c1.id or id == c2.id:

                            peso = self.id_gene[c1].correlazione"""

        """for i in range(1,len(self.corr)+1):
            gc = self.geniCromosomi[i]
            gc2 = self.geniCromosomi[i+1]
            if gc.id == self.corr[i].gene1 and gc.id == self.corr[i+1].gene2:
                c1 = gc.cromosoma
                c2 = gc2.cromosoma
                cromosomi = (c1,c2)
                for cromosomi in self.corr:
                    p = self.corr[i][cromosomi]
                    peso += p
                    edges.append((cromosomi, peso))"""
        # possibile soluzione
        for g1,g2,corr in self.lista_geni_connessi:
            if (self.id_map[g1], self.id_map[g2]) not in edges: # se non è presente coppia cromosomi
                edges [(self.id_map[g1], self.id_map[g2]) ] = float(corr)
            else:
                edges [(self.id_map[g1], self.id_map[g2]) ] += float(corr)

        for k,v in edges.items(): # per chiavi valori
            self.edges.append([k[0],k[1],v])






        self.G.add_edges_from(edges)
        print(self.G)

    def get_edges_weight_min_max(self):

        return min(self.pesi), max(self.pesi)


    def ricerca_cammino(self,t):
        self.soluzione_best.clear()

        for n in self.get_nodes():
            partial = []
            partial_Edge = []

            partial.append(n)
            self.ricorsione(partial,partial_Edge,n)

        print("final", len(self.soluzione_best),[i[2]["weight"]for i in self])

    def ricorsione(self, partial_nodes, partial_edges, t):
        n_last = partial_nodes[-1]
        neigh = self._get_admissible_neighbors(n_last, partial_edges,t)



        for n in neigh:
            print("...")
            partial_nodes.append(n)
            partial_edges.append((n_last,n,self.G.get_edge_data(n_last,n)))


    def _get_admissible_neighbors(self,node,partial_edges, soglia):
        result = []
        for u,v,data in self.G.edges(node, data=True):
            if data["weight"] > soglia:
                # controllo     SOLO arco diretto
        if (u,v) not in [(x[0]),(x,[1])