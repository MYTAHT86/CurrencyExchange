import sqlite3
from pathlib import Path

db_path = Path(__file__).resolve().parent / "database.db"
con = sqlite3.connect(db_path)
cur = con.cursor()
cur.execute("PRAGMA foreign_keys = ON;")
cur.execute("""
    CREATE TABLE IF NOT EXISTS Currencies (
        ID INTEGER PRIMARY KEY,
        Code VARCHAR NOT NULL UNIQUE,
        FullName VARCHAR NOT NULL,
        Sign VARCHAR NOT NULL
    );
""")
cur.execute("""
    CREATE TABLE IF NOT EXISTS ExchangeRates (
        ID INTEGER PRIMARY KEY,
        BaseCurrencyId INT NOT NULL,
        TargetCurrencyId INT NOT NULL,
        Rate DECIMAL(6) NOT NULL,
        FOREIGN KEY (BaseCurrencyId)
            REFERENCES Currencies(ID)
            ON DELETE CASCADE
            ON UPDATE CASCADE,
        FOREIGN KEY (TargetCurrencyId)
            REFERENCES Currencies(ID)
            ON DELETE CASCADE
            ON UPDATE CASCADE,

        UNIQUE (BaseCurrencyId, TargetCurrencyId)
    );
""")

cur.execute("""
    INSERT INTO Currencies (Code, Fullname, Sign) VALUES
        ('USD', 'US Dollar', '$'),
        ('EUR', 'Euro', '€'),
        ('RUB', 'Russian Ruble', '₽'),
        ('BYN', 'Belarusian Ruble', 'Б'),
        ('KZT', 'Tenge', '₸'),
        ('INR', 'Indian Rupee', '₹'),
        ('TRY', 'Turkish Lira', '₺')
""")

cur.execute("""
    INSERT INTO ExchangeRates (BaseCurrencyId, TargetCurrencyId, Rate) VALUES
        (1, 2, 0.91)
""")

con.commit()

con.close()