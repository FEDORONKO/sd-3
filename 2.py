print("Таблиця множення від 1 до 10:")

# Верхній заголовок (1 2 3 ... 10)
print("    ", end="")
for i in range(1, 11):
    print(f"{i:>4}", end="")
print()  

print("    " + "-" * 40)  

for i in range(1, 11):
    print(f"{i:>2} |", end="")  
    for j in range(1, 11):
        print(f"{i * j:>4}", end="")
    print() 
