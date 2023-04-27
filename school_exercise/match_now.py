language = input("Enter prefered language: ")

match language:
    case "java":
        print("you are a hardcore programmer")
    case "javascript":
        print("you are a full stack developer")
    case "python":
        print("you are an amazing programmer")
    case _:
        print("if you are learning programming for the first time, learn python")

if language == "java":
    print("you are a hardcore programmer")
elif language == "javascript":
    print("you are a full stack developer")
elif language == "python":
    print("you are an amazing programmer")
else:
    print("if you are learning programming for the first time, learn python")