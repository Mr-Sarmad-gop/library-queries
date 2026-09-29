import sqlite3

# Connect to (or create) library.db
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Create books table
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    genre TEXT NOT NULL,
    price REAL NOT NULL,
    stock INTEGER NOT NULL
)
""")

# Sample data with at least 8 rows
sample_books = [
    ("The Great Gatsby", "Fiction", 850.0, 10),
    ("To Kill a Mockingbird", "Fiction", 1200.0, 3),
    ("1984", "Fiction", 950.0, 2),
    ("Clean Code", "Technology", 2500.0, 12),
    ("The Pragmatic Programmer", "Technology", 2800.0, 4),
    ("Sapiens", "History", 1500.0, 7),
    ("Dune", "Fiction", 1800.0, 8),
    ("Atomic Habits", "Self-Help", 1100.0, 1)
]

# Insert sample data
cursor.executemany("""
INSERT INTO books (title, genre, price, stock)
VALUES (?, ?, ?, ?)
""", sample_books)

conn.commit()
conn.close()

print("Database 'library.db' created successfully with sample rows.")