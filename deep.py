name = input ("What is the answer to the Great Question of Life, the Universe and Everything? ").lower().strip()
match name:
    case "42" |"forty two"|"forty-two":
        print ("Yes")

    case _:
        print ("NO")
