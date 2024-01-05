import itertools

 
characters = input("Denenecek karakterleri girin: ")

 
password_length = int(input("Şifre uzunluğunu girin: "))

 
allow_repeats = input("Karakterler tekrar kullanılsın mı? (Evet/Hayır): ").strip().lower() == "evet"

 
def brute_force(characters, password_length, allow_repeats):
    combinations = itertools.product(characters, repeat=password_length) if allow_repeats else itertools.permutations(characters, password_length)
    for password in combinations:
        guess = ''.join(password)
        print(guess)

# Şifre kombinasyonlarını ekranda gösteriyoruz
brute_force(characters, password_length, allow_repeats)

# şifre kombinasyonlarımızı kaydettiğimiz dosya adı
file_name = "sifreler.txt"

#   kombinasyonları dosyaya yazdırdığımız kod bloğu
def write_to_file(characters, password_length, allow_repeats):
    combinations = itertools.product(characters, repeat=password_length) if allow_repeats else itertools.permutations(characters, password_length)
    with open(file_name, 'w') as file:
        for password in combinations:
            guess = ''.join(password)
            file.write(guess + '\n')

# Şifre kombinasyonlarını   kaydediyoruz
write_to_file(characters, password_length, allow_repeats)

print(f"Şifre kombinasyonları {file_name} dosyasına kaydedildi.")
