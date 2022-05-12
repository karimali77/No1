import json

# Opening JSON file
result = 0
name = input("Enter yout name: ")
with open('questions.json') as json_file:
    data = json.load(json_file)
    for question in data:
        print(question+": ")
        answer = input()
        if answer == data[question]:
            result = result + 1

resultFile = open("result.txt", "w")
resultFile.write(name+": ")
resultFile.write("result is: " + str(result)+"/20")
resultFile.close()