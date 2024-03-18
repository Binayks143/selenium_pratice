import base64

base_password="Binay456687"
encoded_password=base64.b64encode(base_password.encode("utf-8"))
print("encoded=",encoded_password)
#finding the element and decoading password
doc= base64.b64decode(encoded_password).decode("utf-8")
print("decoded=",doc)


