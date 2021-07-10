a = "david"
b = 'ask\"arian'
aa = "david" \
    "askarian"
aaa = "david\naskarian"
aaaa = "david\taskarian"
# \r pulls all the row to the begning so it can cause it to override
aaaaa = "david asasd \raskarian \r asd"
print(b)
print(aa)
print(aaa)
print(aaaa)
print(aaaaa)
c = 3
if c >= 4:
    print("blah")
