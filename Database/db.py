import mysql.connector

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "event_ticket_db"
}

def get_connection():
    """Establishes and returns a new MySQL database connection."""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        return connection
    except mysql.connector.Error as error:
        print(f"[Error] Failed to connect to MySQL: {error}")
        return None

def init_db():
    """Ensures database exists upon startup."""
    try:
        conn = mysql.connector.connect(
            host=DB_CONFIG["host"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"]
        )
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_CONFIG['database']}")
        conn.close()
    except mysql.connector.Error as error:
        print(f"[Error] Initializing database: {error}")