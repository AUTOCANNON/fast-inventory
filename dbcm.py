import psycopg2

class UseDatabase:

    def __init__(self, config: dict) -> None:
        self.configuration = config

    def __enter__(self) -> 'cursor':
        self.conn = psycopg2.connect(self.configuration)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, *args) -> None:
        self.cursor.close()
        self.conn.commit()
        self.conn.close()