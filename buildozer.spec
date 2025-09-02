[app]
title = Financial Calculator
package.name = financialcalculator
package.domain = com.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0
requirements = python3,kivy,kivymd

android.permissions = INTERNET,ACCESS_NETWORK_STATE
android.api = 31
android.minapi = 21
android.ndk = 25b
android.sdk = 31
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1