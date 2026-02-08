[app]
title = Android Asistan Pro
package.name = asistan_pro
package.domain = org.operasyon
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# KRİTİK EKSİK BURASIYDI:
requirements = python3,kivy,requests,urllib3,chardet,idna

# İzinler (Zaten sendekilerle aynı)
android.permissions = INTERNET, READ_SMS, RECEIVE_SMS, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, ACCESS_FINE_LOCATION

android.api = 33
android.minapi = 21
android.arch = armeabi-v7a
android.sdk_path = 
android.ndk_path = 
android.skip_setup = False
