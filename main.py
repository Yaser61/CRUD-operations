import hazelcast

def list_records(my_map):
    print("List of records:")
    for key, value in my_map.entry_set():
        print(f"ID: {key}, Value: {value}")

def add_record(my_map):
    record_id = input("Enter the ID of the new record: ")
    record_value = input("Enter the value of the new record: ")
    my_map.put(record_id, record_value)
    print("Record added successfully!")

def update_record(my_map):
    record_id = input("Enter the ID of the record you want to update: ")
    if my_map.contains_key(record_id):
        new_value = input("Enter the new value: ")
        my_map.put(record_id, new_value)
        print("Record updated successfully!")
    else:
        print("Record not found!")

def delete_record(my_map):
    record_id = input("Enter the ID of the record you want to delete: ")
    if my_map.remove(record_id):
        print("Record deleted successfully!")
    else:
        print("Record not found!")

def main():
    cluster_name = "hello-world"  # Hazelcast küme adı

    client = hazelcast.HazelcastClient(
        cluster_name=cluster_name
    )

    my_map = client.get_map("my-distributed-map").blocking()

    while True:
        print("\nSelect an operation:")
        print("1. List records")
        print("2. Add a record")
        print("3. Update a record")
        print("4. Delete a record")
        print("5. Exit")

        operation = input("Enter the operation number: ")

        if operation == "1":
            list_records(my_map)
        elif operation == "2":
            add_record(my_map)
        elif operation == "3":
            update_record(my_map)
        elif operation == "4":
            delete_record(my_map)
        elif operation == "5":
            break
        else:
            print("Invalid operation number")

    client.shutdown()

if __name__ == "__main__":
    main()
