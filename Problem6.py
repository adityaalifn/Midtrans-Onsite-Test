string1 = "abcde"
string2 = "bczah"

for i in string1:
    for j in string2:
        if i == j:
            string1 = string1.replace(i,"",1)
            string2 = string2.replace(j,"",1)

print(len(string1) + len(string2))