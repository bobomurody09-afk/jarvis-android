[app]

# Ilova nomi
title = JARVIS

# Paket nomi (kichik harflar, bo'shliqsiz)
package.name = jarvis

# Domen (teskari format)
package.domain = org.jarvis

# Manba kodi joylashgan papka
source.dir = .

# Qo'shiladigan fayl kengaytmalari
source.include_exts = py,png,jpg,kv,atlas

# Versiya
version = 0.1

# Kerakli kutubxonalar (android va boshqa keraksiz so'zlar YO'Q)
requirements = python3,kivy,requests

# Ekran yo'nalishi
orientation = portrait

# To'liq ekran
fullscreen = 0

# Android ruxsatlari
android.permissions = INTERNET

# Android SDK/NDK sozlamalari
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a

# Presplash va icon (agar bo'lmasa, olib tashlanadi, xato bermaydi)
#icon.filename = %(source.dir)s/icon.png
#presplash.filename = %(source.dir)s/presplash.png

[buildozer]

# Log darajasi (2 = batafsil)
log_level = 2

# Root user ogohlantirishi
warn_on_root = 1
