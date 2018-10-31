import sqlite3


class DB:
    def __init__(self, filename='timestamps.db'):
        self.db = sqlite3.connect(filename)
        try:
            self.build_db()
        except sqlite3.OperationalError:
            pass

    def build_db(self):
        cursor = self.db.cursor()
        cursor.execute("CREATE TABLE parts (timestamp float, type text, distance int)")
        self.db.commit()

    def add_timestamp(self, timestamp):
        cursor = self.db.cursor()
        cursor.execute("INSERT INTO parts VALUES (" + timestamp.strftime('%s') + ", '', 0)")
        self.db.commit()

    def add_type(self, timestamp, part_type):
        cursor = self.db.cursor()
        cursor.execute("UPDATE parts SET type='" + part_type + "' WHERE timestamp=" + timestamp.strftime('%s'))
        self.db.commit()

    def add_distance(self, timestamp, distance):
        cursor = self.db.cursor()
        cursor.execute("UPDATE parts SET distance=" + str(distance) + " WHERE timestamp=" + timestamp.strftime('%s'))
        self.db.commit()

    def get_last_timestamp(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT MAX(timestamp) FROM parts")
        return cursor.fetchone()

    def get_entries(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT * from parts")
        return cursor.fetchall()

    def close_db(self):
        self.db.close()

