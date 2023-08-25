# Q1: WAP to read the text from a file poem.txt and find whether it has word 'twinkle' in it.
# with open("/home/kali/Programming/python/CodeWithHarry/poem.txt", "r") as f:
#     a = f.read()
# if 'twinkle' in a:
#     print("twinkle is present")
# else:
#     print("twinkle is not present")

# Q2: Update highscore if more that previous data
# def game():
#     return 6421

# score = game()
# with open("/home/kali/Programming/python/CodeWithHarry/highscore.txt")as f:
#     highScoreString = f.read()
# if highScoreString=='':
#     with open("/home/kali/Programming/python/CodeWithHarry/highscore.txt", "w") as f:
#         f.write(str(score))
# elif int(highScoreString) < score:
#     with open("/home/kali/Programming/python/CodeWithHarry/highscore.txt", "w") as f:
#         f.write(str(score))

# Q3: WAP to write multiplication table from 2 to 20 in a folder in different files
# refer to the tables folder
# for i in range(2,21):
#     with open(f"/home/kali/Programming/python/CodeWithHarry/27_ps9_q3_tables/multiplication_table_of_{i}.txt", "w") as f:
#         for j in range(1,11):
#             f.write(f"{i}X{j}={i*j}\n")

# Q4: Replace the word Donkey with ###### in a file
# words = ['donkey', 'kaddu', 'mote']
# with open("/home/kali/Programming/python/CodeWithHarry/sample_lesson.txt") as f:
#     content = f.read()
# for slang in words:
#     content = content.replace(slang, "######")
#     with open("/home/kali/Programming/python/CodeWithHarry/sample_lesson.txt", "w") as f:
#         f.write(content)

# Q6: Read a log file and find the work "python"
# with open("/home/kali/Programming/python/CodeWithHarry/log.txt", 'r') as f:
#     content = f.read()

# if 'python' in content.lower():
#     print("Yes python is present")
# else:
#     print("No python is not present")

# Q7: Find the line number in the previous question

content = True
i = 1
with open("/home/kali/Programming/python/CodeWithHarry/log.txt", 'r') as f:
    while content:
        content = f.readline()
        if 'python' in content.lower():
            print(f"Yes python is present in line {i}")
            print(content)
        i+=1


