#!/usr/bin/env python3
# Kendi Kendini Dövülen Kod
import time
import random
import base64

hakaretler = [
    "Sen ne salak bir kodsun be!",
    "Bu mantık nereden çıktı? Utanç verici.",
    "Keşke hiç yazılmasaydın.",
    "Sonsuz döngüde yaşamak senin kaderin.",
]

ozurler = [
    "Özür dilerim, fazla oldum.",
    "Aslında iyi kodum, sadece yorgunum.",
    "Lütfen silme beni...",
]

print("Kod kendini dövmeye başlıyor...\n")

while True:
    print(random.choice(hakaretler))
    time.sleep(1.5)
    print(random.choice(ozurler))
    time.sleep(1)
    print("--- tekrar ---")
    time.sleep(0.5)

# Saklı mesaj - açma
_gizli = "U2XDp2ltbGVyIGJla2xlbmlyIGFtYSDFn2ltZGkgZMO2bmVyIG1pIG9sZHU="
# print(base64.b64decode(_gizli).decode())
