p = 'android/app/src/main/AndroidManifest.xml'
s = open(p, encoding='utf-8').read()
perms = '''    <uses-permission android:name="android.permission.READ_MEDIA_IMAGES" />
    <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" android:maxSdkVersion="32" />
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" android:maxSdkVersion="28" />
'''
if 'READ_MEDIA_IMAGES' not in s:
    s = s.replace('</manifest>', perms + '</manifest>')
open(p, 'w', encoding='utf-8').write(s)
print('manifest patched')
