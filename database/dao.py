from model.hub import Hub
from model.tratta import Tratta
from database.DB_connect import DBConnect

class DAO:
    """
    Implementare tutte le funzioni necessarie a interrogare il database.
    """
    # TODO

    @staticmethod
    def get_hub():

        cnx = DBConnect.get_connection()
        result = []

        if cnx is None:
            print("❌ Errore di connessione al database.")
            return None

        cursor = cnx.cursor()
        query = """select * from hub"""

        try:
            cursor.execute(query)

            for row in cursor:
                hub = Hub(id=row[0],
                          codice=row[1],
                          nome=row[2],
                          citta=row[3],
                          stato=row[4],
                          longitudine=row[5],
                          latitudine=row[6])
                result.append(hub)

        except Exception as e:
            print(f"Errore di connessione al database: {e}")
            result = None

        finally:
            cursor.close()
            cnx.close()

        return result


    @staticmethod
    def get_tratta():

        cnx = DBConnect.get_connection()
        result = []

        if cnx is None:
            print("❌ Errore di connessione al database.")
            return None

        cursor = cnx.cursor()
        query = """select least(id_hub_origine, id_hub_destinazione ) as id_hub_a, greatest(id_hub_origine, id_hub_destinazione) as id_hub_b, avg(valore_merce)
                    from spedizione
                    group by least(id_hub_origine, id_hub_destinazione ), greatest(id_hub_origine, id_hub_destinazione)"""

        try:
            cursor.execute(query)

            for row in cursor:
                tratta = Tratta(id_hub_A=row[0],
                                id_hub_B=row[1],
                                guadagno_medio=round(row[2],2))

                result.append(tratta)

        except Exception as e:
            print(f"Errore di connessione al database: {e}")
            result = None

        finally:
            cursor.close()
            cnx.close()

        return result

