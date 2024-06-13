import redis

redis_host = 'localhost'
redis_port = 6379

def connect_redis():
    return redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)

def add_data(r):
    key = input("Lütfen anahtarı girin: ")
    value = input("Lütfen değeri girin: ")
    r.set(key, value)
    print(f"'{key}' anahtarına '{value}' değeri eklendi.")

def delete_data(r):
    keys = r.keys()
    for key in keys:
        print(f"{key}: {r.get(key)}")
    key = input("Lütfen silmek istediğiniz anahtarı girin: ")
    r.delete(key)
    print(f"'{key}' anahtarı silindi.")

def update_data(r):
    keys = r.keys()
    if not keys:
        print("Güncellenecek veri yok.")
        return

    print("Mevcut veriler:")
    for key in keys:
        print(f"{key}: {r.get(key)}")

    key_to_update = input("Güncellemek istediğiniz anahtarın adını girin: ")
    if r.exists(key_to_update):
        new_value = input("Yeni değeri girin: ")
        r.set(key_to_update, new_value)
        print(f"'{key_to_update}' anahtarının değeri '{new_value}' olarak güncellendi.")
    else:
        print(f"'{key_to_update}' anahtarı bulunamadı.")

def menu():
    r = connect_redis()
    while True:
        print("\nSeçenekler:")
        print("1. Veri Ekleme")
        print("2. Veri Silme")
        print("3. Veri Güncelleme")
        print("4. Çıkış")
        
        choice = input("Bir seçenek seçin (1/2/3/4): ")

        if choice == '1':
            add_data(r)
        elif choice == '2':
            delete_data(r)
        elif choice == '3':
            update_data(r)
        elif choice == '4':
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçenek, lütfen tekrar deneyin.")

if __name__ == "__main__":
    menu()
