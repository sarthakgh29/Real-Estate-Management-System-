import mysql.connector
import tkinter as tk
from tkinter import messagebox

# Function to connect to the MySQL database
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            user='ss6801',
            password='@Shivsar1829',
            host='localhost',
            database="realestate"
        )
        return connection
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Failed to connect to database: {err}")
        return None

# Function to create tables if they do not exist
def create_tables(connection):
    try:
        cursor = connection.cursor()

        # Table: properties
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS properties (
                id INT AUTO_INCREMENT PRIMARY KEY,
                address VARCHAR(255) NOT NULL,
                price DECIMAL(10, 2) NOT NULL,
                bedrooms INT,
                bathrooms INT
            )
        """)

        # Table: owners
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS owners (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                contact_number VARCHAR(15)
            )
        """)

        # Table: buyers
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS buyers (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                contact_number VARCHAR(15)
            )
        """)

        # Table: agents
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS agents (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                contact_number VARCHAR(15)
            )
        """)

        # Table: transactions
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id INT AUTO_INCREMENT PRIMARY KEY,
                property_id INT,
                buyer_id INT,
                agent_id INT,
                transaction_date DATE,
                FOREIGN KEY (property_id) REFERENCES properties(id),
                FOREIGN KEY (buyer_id) REFERENCES buyers(id),
                FOREIGN KEY (agent_id) REFERENCES agents(id)
            )
        """)

        connection.commit()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Failed to create tables: {err}")

# Function to add a new property to the database
def add_property(connection, address, price, bedrooms, bathrooms):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO properties (address, price, bedrooms, bathrooms)
            VALUES (%s, %s, %s, %s)
        """, (address, price, bedrooms, bathrooms))
        connection.commit()
        messagebox.showinfo("Success", "Property added successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Failed to add property: {err}")

# Function to add a new owner to the database
def add_owner(connection, name, contact_number):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO owners (name, contact_number)
            VALUES (%s, %s)
        """, (name, contact_number))
        connection.commit()
        messagebox.showinfo("Success", "Owner added successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Failed to add owner: {err}")

# Function to add a new buyer to the database
def add_buyer(connection, name, contact_number):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO buyers (name, contact_number)
            VALUES (%s, %s)
        """, (name, contact_number))
        connection.commit()
        messagebox.showinfo("Success", "Buyer added successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Failed to add buyer: {err}")

# Function to add a new agent to the database
def add_agent(connection, name, contact_number):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO agents (name, contact_number)
            VALUES (%s, %s)
        """, (name, contact_number))
        connection.commit()
        messagebox.showinfo("Success", "Agent added successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Failed to add agent: {err}")

# Function to add a new transaction to the database
def add_transaction(connection, property_id, buyer_id, agent_id, transaction_date):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO transactions (property_id, buyer_id, agent_id, transaction_date)
            VALUES (%s, %s, %s, %s)
        """, (property_id, buyer_id, agent_id, transaction_date))
        connection.commit()
        messagebox.showinfo("Success", "Transaction added successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Failed to add transaction: {err}")

# Function to handle GUI interactions
def handle_choice(choice):
    if choice == 'Add Property':
        address = address_entry.get()
        price = float(price_entry.get())
        bedrooms = int(bedrooms_entry.get())
        bathrooms = int(bathrooms_entry.get())
        add_property(connection, address, price, bedrooms, bathrooms)
    elif choice == 'Add Owner':
        owner_name = owner_name_entry.get()
        owner_contact = owner_contact_entry.get()
        add_owner(connection, owner_name, owner_contact)
    elif choice == 'Add Buyer':
        buyer_name = buyer_name_entry.get()
        buyer_contact = buyer_contact_entry.get()
        add_buyer(connection, buyer_name, buyer_contact)
    elif choice == 'Add Agent':
        agent_name = agent_name_entry.get()
        agent_contact = agent_contact_entry.get()
        add_agent(connection, agent_name, agent_contact)
    elif choice == 'Add Transaction':
        prop_id = int(prop_id_entry.get())
        buyer_id = int(buyer_id_entry.get())
        agent_id = int(agent_id_entry.get())
        trans_date = transaction_date_entry.get()
        add_transaction(connection, prop_id, buyer_id, agent_id, trans_date)

# Main function
def main():
    global connection
    connection = connect_to_database()

    if connection:
        create_tables(connection)

        root = tk.Tk()
        root.title("Real Estate Management System")

        choices = ['Add Property', 'Add Owner', 'Add Buyer', 'Add Agent', 'Add Transaction']

        for i, choice in enumerate(choices):
            tk.Button(root, text=choice, command=lambda ch=choice: handle_choice(ch)).grid(row=i, column=0, pady=5)

        # Entry fields for adding property
        global address_entry, price_entry, bedrooms_entry, bathrooms_entry
        address_label = tk.Label(root, text="Address:")
        address_label.grid(row=0, column=1)
        address_entry = tk.Entry(root)
        address_entry.grid(row=0, column=2)

        price_label = tk.Label(root, text="Price:")
        price_label.grid(row=1, column=1)
        price_entry = tk.Entry(root)
        price_entry.grid(row=1, column=2)

        bedrooms_label = tk.Label(root, text="Bedrooms:")
        bedrooms_label.grid(row=2, column=1)
        bedrooms_entry = tk.Entry(root)
        bedrooms_entry.grid(row=2, column=2)

        bathrooms_label = tk.Label(root, text="Bathrooms:")
        bathrooms_label.grid(row=3, column=1)
        bathrooms_entry = tk.Entry(root)
        bathrooms_entry.grid(row=3, column=2)

        # Entry fields for adding owner
        global owner_name_entry, owner_contact_entry
        owner_name_label = tk.Label(root, text="Owner Name:")
        owner_name_label.grid(row=4, column=1)
        owner_name_entry = tk.Entry(root)
        owner_name_entry.grid(row=4, column=2)

        owner_contact_label = tk.Label(root, text="Owner Contact:")
        owner_contact_label.grid(row=5, column=1)
        owner_contact_entry = tk.Entry(root)
        owner_contact_entry.grid(row=5, column=2)

        # Entry fields for adding buyer
        global buyer_name_entry, buyer_contact_entry
        buyer_name_label = tk.Label(root, text="Buyer Name:")
        buyer_name_label.grid(row=6, column=1)
        buyer_name_entry = tk.Entry(root)
        buyer_name_entry.grid(row=6, column=2)

        buyer_contact_label = tk.Label(root, text="Buyer Contact:")
        buyer_contact_label.grid(row=7, column=1)
        buyer_contact_entry = tk.Entry(root)
        buyer_contact_entry.grid(row=7, column=2)

        # Entry fields for adding agent
        global agent_name_entry, agent_contact_entry
        agent_name_label = tk.Label(root, text="Agent Name:")
        agent_name_label.grid(row=8, column=1)
        agent_name_entry = tk.Entry(root)
        agent_name_entry.grid(row=8, column=2)

        agent_contact_label = tk.Label(root, text="Agent Contact:")
        agent_contact_label.grid(row=9, column=1)
        agent_contact_entry = tk.Entry(root)
        agent_contact_entry.grid(row=9, column=2)

        # Entry fields for adding transaction
        global prop_id_entry, buyer_id_entry, agent_id_entry, transaction_date_entry
        prop_id_label = tk.Label(root, text="Property ID:")
        prop_id_label.grid(row=10, column=1)
        prop_id_entry = tk.Entry(root)
        prop_id_entry.grid(row=10, column=2)

        buyer_id_label = tk.Label(root, text="Buyer ID:")
        buyer_id_label.grid(row=11, column=1)
        buyer_id_entry = tk.Entry(root)
        buyer_id_entry.grid(row=11, column=2)

        agent_id_label = tk.Label(root, text="Agent ID:")
        agent_id_label.grid(row=12, column=1)
        agent_id_entry = tk.Entry(root)
        agent_id_entry.grid(row=12, column=2)

        transaction_date_label = tk.Label(root, text="Transaction Date:")
        transaction_date_label.grid(row=13, column=1)
        transaction_date_entry = tk.Entry(root)
        transaction_date_entry.grid(row=13, column=2)

        root.mainloop()

        connection.close()

if __name__ == "__main__":
    main()
