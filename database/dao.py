from database.DB_connect import DBConnect
from model.cromosoma import Cromosoma
from model.iterazione import Iterazione



class DAO:
    # soluzione

    #

    @staticmethod
    def getGeni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT i.id_gene1 AS gene1, i.id_gene2 AS gene2, i.correlazione
                    FROM interazione i"""

        cursor.execute(query)

        for row in cursor:
            r = Iterazioni(row["gene1"], row["gene2"],row["correlazione"])
            result.append(r)

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getCromosomi():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        # query = """ SELECT id,cromosoma
        #             FROM gene
        #             WHERE cromosoma !=0
        #             GROUP BY id,cromosoma"""

        cursor.execute(query)

        for row in cursor:
            r = Cromosoma(row["id"],row["cromosoma"])
            result.append(r)

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getGeniConnessi():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT g1.id AS gene1, g2.id AS gene2, i.correlazione
                    FROM gene AS g1, gene AS g2, interazione i
                    WHERE g1.id = i.id_gene1 AND g2.id = i.id_gene2
                        AND g1.cromosoma != g2.cromosoma
                        AND g1.cromosoma >  0
                        AND g2.cromosoma > 0
                    GROUP BY g1.id, g2.id
                    ...."""

        cursor.execute(query)

        for row in cursor:
            r = Iterazione(**row) #(row["gene1"],row["gene2"], row["correlazione"])
            result.append(r)

        cursor.close()
        conn.close()
        return result


