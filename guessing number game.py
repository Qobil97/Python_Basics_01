secret_number=9

#here, i is renamed 

guess_count=0
guess_limit=3
while guess_count<guess_limit:
    guess=int(input('Guess: '))
    guess_count +=1
    if guess==secret_number:
        print('Yutding!')
        break
else:
    print("Ajab bo'ldi, qolding!")

