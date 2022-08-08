import random

random_number = random.randint(1,100)
print(random_number)


game_count = 1
while True:
    try:
        my_number = int(input("1~100 숫자 중에 하나만 입력하세요>>> "))
        if my_number > random_number:
            print("정답은 숫자가 더 작아요")
        elif my_number < random_number:
            print("정답은 숫자가 더 큽니다.")
        elif my_number == random_number:
            print(f"정답입니다. {game_count}회 만에 맞추셨습니다")
            break
        game_count += 1
    except:
        print("에러 발생, 숫자를 입력하세요")