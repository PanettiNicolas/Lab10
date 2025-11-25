from model.hub import Hub

from database.DB_connect import DBConnect

class DAO:
    """
    Implementare tutte le funzioni necessarie a interrogare il database.
    """
    # TODO

    @staticmethod
    def get_hub():

        cnx = DBConnect.get_connection()
        result = {}

        if cnx is None:
            print("❌ Errore di connessione al database.")
            return None

        cursor = cnx.cursor(dictionary=True)
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

                result[hub.id] = hub

        except Exception as e:
            print(f"Errore di connessione al database: {e}")
            result = None

        finally:
            cursor.close()
            cnx.close()

        return result





