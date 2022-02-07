import json
from timeit import default_timer as timer
from unicodedata import name

start = timer() #start of operations timer
#opens .json file, please add directory for your specific file
with open("combined.json", "r") as json_file:
	data = json.load(json_file)

#all variables
total_messages = 0
calls = 0
call_time = 0
person_1 = ""
person_2 = ""

#identifies participants of the chat
for item in data["participants"]:
    person_1 = str(item["name"])

for item in data["messages"]:
    if "call_duration" in item:
        call_time += int(item["call_duration"])
    if "type" in item:
        if item["type"] == "Call":
            calls += 1
        if item["type"] == "Generic" or item["type"] == "Share":
            total_messages += 1
    
end = timer()
print(f"Chat participants are {person_1} and {person_2}")
print(f"Total Messages: {total_messages}\nTotal Calls: {calls}\nTotal Call Time: {round(call_time / 3600000, 2)} hours\nOperations took {round((end - start), 5)} seconds")
