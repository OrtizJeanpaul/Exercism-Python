def commands(binary_str):
    ACTIONS = ["Reverse","jump","close your eyes","double blink","wink"]

    binary_list = [binary_str]
    should_reverse = True
    handshake = list()
    for index in range(len(binary_list)):
        if binary_list[index] == 1:
            temp = ACTIONS[index]
            if(temp == "Reverse"):
                should_reverse = False
            else:
                handshake.append(ACTIONS[index])
    
    return handshake.reverse() if should_reverse == True else handshake
