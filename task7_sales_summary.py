
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def main():
    # Connect to or create the SQLite database
    conn = sqlite3.connect("sales_data.db")
    cursor = conn.cursor()

    # Create table
    cursor.execute("DROP TABLE IF EXISTS sales;")
    cursor.execute("""
    CREATE TABLE sales (
        product TEXT,
        quantity INTEGER,
        price REAL
    );
    """)

    # Insert sample data
    data = [
        ("Product A", 10, 5.0),
        ("Product B", 7, 8.0),
        ("Product C", 12, 6.5),
    ]
    cursor.executemany("INSERT INTO sales VALUES (?, ?, ?);", data)
    conn.commit()

    # Run SQL query
    query = "SELECT product, SUM(quantity) AS total_qty, SUM(quantity * price) AS revenue FROM sales GROUP BY product"
    df = pd.read_sql_query(query, conn)

    # Print results
    print("\nSales Summary:")
    print(df)

    # Plot revenue chart
    plt.figure(figsize=(6,4))
    df.plot(kind='bar', x='product', y='revenue')
    plt.title("Revenue by Product")
    plt.tight_layout()
    plt.savefig("sales_chart.png")
    plt.show()

    conn.close()

if __name__ == "__main__":
    main()
