# 📦 MongoDB CRUD Operations in Python

This is a simple Python program to perform **CRUD** (Create, Read, Update, Delete) operations on a MongoDB collection using the **`pymongo`** library.

> 🔧 Ideal for beginners learning database handling with Python and MongoDB.

---

## 🧾 Features

- ✅ Create multiple documents
- 📄 Read and display all documents
- ✏️ Update a specific document's field
- ❌ Delete a document by name
- 🧭 Simple menu-driven interface for user interaction

---

## 📁 File Structure

```
mongodb_crud.py      # Main Python script
README.md            # Project documentation
```

⚙️ Prerequisites
Ensure you have the following installed:

- Python 3.x
- MongoDB (running locally)
- pymongo library

🚀 Setup Instructions
1. Clone the repository:
```
git clone https://github.com/yourusername/mongodb-crud.git
cd mongodb-crud
```
2. Install dependencies:
```
pip3 install pymongo
```
3. Start MongoDB service (Linux):
```
sudo systemctl start mongod
```
4. Run the script:
```
python3 mongodb_crud.py
```
📌 Usage
Once the program runs, you'll see a menu:
MongoDB CRUD Operations Menu
1. Create Documents
2. Read Documents
3. Update Document
4. Delete Document
5. Exit
Choose the option by entering the corresponding number.

🗃️ Database Details

```
Database: mydatabase
Collection: mycollection
```
The database and collection will be created automatically if they don’t already exist.

