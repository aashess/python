# import required function
import random

# use required input for user and computer.
def inpuut():
    user = int(input("Choose Your Number: "))
    computer1 = random.randint(1, 10)
    computer2 = random.randint(1, 10)
    computer3 = random.randint(1, 10)
    leader = random.randint(1, 5)
    print(f"l={leader} u={user} c1={computer1} c2={computer2} c3={computer3}")
    return user, computer1, computer2, computer3, leader

# make required function 
# user, computer1, computer2, computer3, leader
def gameplay():
    user_total = 0
    computer1_total = 0
    computer2_total = 0
    computer3_total = 0
    
    for i in range(4):
        # Call inpuut() once per iteration, store the results
        user, computer1, computer2, computer3, leader = inpuut()

        if user == leader:
            user_total += 1
            continue 
        elif computer1 == leader:
            computer1_total += 1
            continue
        elif computer2 == leader:
            computer2_total += 1
            continue
        elif computer3 == leader:
            computer3_total += 1

    print(f"User total: {user_total}")
    print(f"Computer 1 total: {computer1_total}")
    print(f"Computer 2 total: {computer2_total}")
    print(f"Computer 3 total: {computer3_total}")

gameplay()
