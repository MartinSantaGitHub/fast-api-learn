import time
import os
import colorama
from sys import stdout
from sqlalchemy.exc import OperationalError
from utils.connection import DatabaseConnection


def wait_for_db():
    """Function to wait for the database."""

    stdout.write("Waiting for the database...\n")

    db_up = False
    db_conn = DatabaseConnection(os.environ["DB_DRIVER"],
                                 os.environ["DB_USER"],
                                 os.environ["DB_PASSWORD"],
                                 os.environ["DB_HOST"],
                                 os.environ["DB_NAME"])

    while db_up is False:
        try:
            db_conn.execute("SELECT 1")
            db_up = True
        except OperationalError:
            stdout.write(colorama.Fore.YELLOW + "Database unavailable, waiting 1 second...\n")
            time.sleep(1)

    stdout.write(colorama.Fore.GREEN + "Database available!\n")


if __name__ == "__main__":
    wait_for_db()
