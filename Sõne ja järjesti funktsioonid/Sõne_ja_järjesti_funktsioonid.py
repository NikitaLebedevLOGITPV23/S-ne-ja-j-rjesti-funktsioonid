   #1 Литералы строк

S="str"
index = 0
while True:
    print(S[index])
    index += 1
    if index == len(S):
        break
   
   #2 Экранированные последовательности

S="s\np\ta\nbbb"
count = 0
while True:
    if count >= len(S):
        break
    count += 1
print("Sümbolite arv reas :", count)
   
   #3 Повторение строки
S1="Rida kordamine"
count = 0
while True:
    if count < 3:
        print(S1 * 3)
        count += 1
    else:
        break

   #4 Длина строки
S="Joone pikkus"
pikkus=0
while True:
    if pikkus<len(S):
        pikkus+=1
    else:
        break
print("Joone pikkus:", pikkus)

