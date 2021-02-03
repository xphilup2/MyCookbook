mutable_bytes = bytearray(b'\xDE\xAd\xEF')
mutable_bytes[0] = 0
mutable_bytes.append(255)

print(mutable_bytes)
# print(type(mutable_bytes))
print(mutable_bytes[0:2])

