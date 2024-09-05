s1 = set()
s1.add("Rodrigo")
s1.add(1)
# s1.update("Carvalho")
s1.update(("Carvalho", 1, 2, 3, 4))
# s1.clear()
s1.discard("Rodrigo")
s1.discard("Carvalho")

print(s1)

s1 = (1, 2, 3)
s2 = (2, 3, 4)

s3 = s1 | s2
# s3 = s1 & s2
# s3 = s1 - s2
# s3 = s2 - s1
# s3 = s1 ^ s2

print(s3)
