import pymongo
from pymongo import MongoClient
from bson import ObjectId  # ObjectId'yi bson modülünden import ediyoruz
import pprint

# MongoDB'ye bağlan
client = MongoClient("mongodb://localhost:27017/")

# Veritabanını ve koleksiyonu seç
db = client["foy6"]
collection = db["persons"]

def add_person():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    city = input("Enter city: ")
    person = {
        "name": name,
        "age": age,
        "city": city
    }
    collection.insert_one(person)
    print("Person added successfully!")

def update_person():
    list_persons()  # Update işleminden önce kişileri listele
    person_id = input("Enter the ID of the person to update: ")
    person = collection.find_one({"_id": ObjectId(person_id)})  # ObjectId'yi bson modülünden kullanıyoruz
    if person:
        print("Current data: ")
        pprint.pprint(person)
        
        new_name = input("Enter new name (leave blank to keep current): ") or person['name']
        new_age = input("Enter new age (leave blank to keep current): ") or person['age']
        new_city = input("Enter new city (leave blank to keep current): ") or person['city']
        
        collection.update_one(
            {"_id": ObjectId(person_id)},
            {"$set": {"name": new_name, "age": int(new_age), "city": new_city}}
        )
        print("Person updated successfully!")
    else:
        print("Person not found!")

def delete_person():
    list_persons()  # Delete işleminden önce kişileri listele
    person_id = input("Enter the ID of the person to delete: ")
    result = collection.delete_one({"_id": ObjectId(person_id)})  # ObjectId'yi bson modülünden kullanıyoruz
    if result.deleted_count > 0:
        print("Person deleted successfully!")
    else:
        print("Person not found!")
    list_persons()  # Delete işleminden sonra kişileri tekrar listele

def list_persons():
    persons = collection.find()
    for person in persons:
        pprint.pprint(person)

def main():
    while True:
        print("\n--- MongoDB CRUD Operations ---")
        print("1. Add Person")
        print("2. Update Person")
        print("3. Delete Person")
        print("4. List Persons")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            add_person()
        elif choice == '2':
            update_person()
        elif choice == '3':
            delete_person()
        elif choice == '4':
            list_persons()
        elif choice == '5':
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
