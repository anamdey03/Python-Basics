import time

score = 0

name = str(input("What's your name? "))
print("Welcome, " + name + " to the quiz!\n")


def score_plus():
    global score
    score += 1
    print("Your score: ", score)


def score_minus():
    global score
    score -= 1
    print("Your score: ", score)


def q1():
    print("\n1. What is El Capitan?")
    time.sleep(1)
    print("a) An operating system for Windows")
    print("b) An operating system for MAC")
    print("c) A third-party application\n")

    answer = str(input("What's the right answer: "))
    if answer == "b":
        print("Well Done, that's correct!")
        score_plus()
    else:
        print("Sorry, that was the wrong answer!")
        score_minus()
    print()
    q2()


def q2():
    print("\n2. What is apple's latest device?")
    time.sleep(1)
    print("a) iPhone")
    print("b) MacBook Pro")
    print("c) iPod Touch\n")

    answer = str(input("What's the right answer: "))
    if answer == "b":
        print("Well Done, that's correct!")
        score_plus()
    else:
        print("Sorry, that was the wrong answer!")
        score_minus()
    print()
    q3()


def q3():
    print("\n3. Who is the CEO of Apple?")
    time.sleep(1)
    print("a) Anamitra Dey")
    print("b) Bill Gates")
    print("c) Steve Jobs\n")

    answer = str(input("What's the right answer: "))
    if answer == "c":
        print("Well Done, that's correct!")
        score_plus()
    else:
        print("Sorry, that was the wrong answer!")
        score_minus()


q1()

print("\nThank you for participating in the quiz!")
