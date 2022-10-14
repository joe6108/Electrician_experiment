import random

if __name__ == "__main__":
    x = True
    while x == True :
        #取得使用者輸入
        user_input = input("Type a word:")
        print("Your input is", user_input)
        #正確答案(隨機取得)
        dictionary = None
        with open('word.txt') as f:
            dictionary = f.read().splitlines()
        answer = random.sample(dictionary, 1)[0]
        print(answer)
        #確認答案
        for i in range(5):
            if user_input[i] == answer[i]:
                print("🟩", end='')
            elif user_input[i] in answer:
                print("🟨", end='')
            else:
                print("⬛", end='')

        break