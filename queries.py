import sqlite3

def run_and_print(cursor, query_title, query):
    print(f"=== {query_title} ===")
    print(f"SQL: {query.strip()}\n")
    cursor.execute(query)
    rows = cursor.fetchall()
    
    # Print column names
    col_names = [description[0] for description in cursor.description]
    print(" | ".join(col_names))
    print("-" * 40)
    
    # Print rows
    for row in rows:
        print(" | ".join(str(val) for val in row))
    print("\n")

def main():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    # Query (a): Select title and price where price > 1000, sorted descending by price
    query_a = """
    SELECT title, price
    FROM books
    WHERE price > 1000
    ORDER BY price DESC;
    """
    run_and_print(cursor, "Query (a): Books with price > 1000 (Sorted Descending)", query_a)

    # Query (b): Query using AS to rename title as book_title
    query_b = """
    SELECT title AS book_title, price, genre
    FROM books;
    """
    run_and_print(cursor, "Query (b): Renamed title to book_title using AS", query_b)

    # Query (c): Select Fiction books with stock < 5 (Low-stock alert)
    query_c = """
    SELECT *
    FROM books
    WHERE genre = 'Fiction' AND stock < 5;
    """
    run_and_print(cursor, "Query (c): Fiction books with stock < 5 (Low-Stock Alert)", query_c)

    conn.close()

if __name__ == "__main__":
    main()