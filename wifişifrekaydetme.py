import subprocess
import pandas as pd
import re

# Wi-Fi ağlarını bulmak için bir komut çalıştır
command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True, text=True, encoding='utf-8')

# SSID'leri al
wifi_names = re.findall(r":\s(.*)", command_output.stdout)

# Her ağın şifresini al ve bir DataFrame'e kaydet
wifi_data = []
failed_profiles = []  # Şifresi olmayan ağları takip etmek için bir liste
for name in wifi_names:
    profile_info = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output=True, text=True, encoding='utf-8')
    if profile_info.stdout:
        wifi_password = re.search(r"Key Content\s+:\s(.*)", profile_info.stdout)
        if wifi_password:
            wifi_data.append({"SSID": name, "Password": wifi_password.group(1)})
        else:
            failed_profiles.append(name)
    else:
        failed_profiles.append(name)

# Verileri DataFrame'e kaydet
df = pd.DataFrame(wifi_data)

# Şifre uzunluğunu gösteren yeni bir sütun ekle
df['Password Length'] = df['Password'].apply(lambda x: len(x) if x else None)

# Şifresi olmayan ağları gösteren bir dosya oluştur
with open("failed_profiles.txt", "w") as file:
    file.write("\n".join(failed_profiles))

# Excel dosyasına kaydet
df.to_excel("wifi_passwords_with_length.xlsx", index=False)
