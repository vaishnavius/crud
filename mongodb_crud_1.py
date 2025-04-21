#Question Write a program to implement MongoDB CRUD operations.
#Steps: gedit mongodb_crud.py--Save the Program.
#pip3 install pymongo
#sudo systemctl start mongod
#python3 mongodb_crud.py




from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["mycollection"]


# Create (Insert multiple documents)
def create_documents():
    count = int(input("How many documents do you want to insert? "))
    for i in range(count):
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        city = input("Enter city: ")
        document = {"name": name, "age": age, "city": city}
        collection.insert_one(document)
    print("Documents inserted successfully.")

# Read (Fetch and display documents)
def read_documents():
    documents = list(collection.find())
    if not documents:
        print("Collection is empty.")
    else:
        for doc in documents:
            print(doc)

# Update (Modify a document)
def update_document():
    name = input("Enter the name of the document to update: ")
    field = input("Which field do you want to update? (name/age/city): ")
    
    if field not in ["name", "age", "city"]:
        print("Invalid field. Please enter 'name', 'age', or 'city'.")
        return
    
    if field == "age":
        new_value = int(input("Enter new age: "))
    else:
        new_value = input(f"Enter new value for {field}: ")
    
    query = {"name": name}
    new_values = {"$set": {field: new_value}}
    result = collection.update_one(query, new_values)
    if result.modified_count > 0:
        print("Document updated successfully.")
    else:
        print("No matching document found.")

# Delete (Remove a document)
def delete_document():
    name = input("Enter the name of the document to delete: ")
    query = {"name": name}
    result = collection.delete_one(query)
    if result.deleted_count > 0:
        print("Document deleted successfully.")
    else:
        print("No matching document found.")

# Menu Loop
def menu():
    while True:
        print("\nMongoDB CRUD Operations Menu")
        print("1. Create Documents")
        print("2. Read Documents")
        print("3. Update Document")
        print("4. Delete Document")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            create_documents()
        elif choice == "2":
            read_documents()
        elif choice == "3":
            update_document()
        elif choice == "4":
            delete_document()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Run Menu
if __name__ == "__main__":
    menu()
