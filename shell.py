# This is checkout_1_branch for testing
import basic

while True:
    text = input("basic terminal > ")
    result, error = basic.run("<File_name>", text)
    
    if error:
        print(error.as_string())
    else:
        print(result)