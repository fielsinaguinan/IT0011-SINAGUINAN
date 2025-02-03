def pattern_a(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()  

pattern_a(5)  
