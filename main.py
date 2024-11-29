import sqlite3

def get_user_info(user_id):
    # Connect to the SQLite database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Vulnerable SQL query using string concatenation
    query = "SELECT * FROM users WHERE id = " + user_id
    cursor.execute(query)
    
    # Fetch and return the user information
    user_info = cursor.fetchone()
    conn.close()
    return user_info

# Example usage
user_id = input("Enter user ID: ")
print(get_user_info(user_id))

