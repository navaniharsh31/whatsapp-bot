def format():
    with open("message.txt", "r", encoding="utf8") as message:
        message_line = message.readlines()

    for i in range(len(message_line)):
        message_line[i] = message_line[i].rstrip('\n')
        message_line[i] = message_line[i]+ " "+"\\n"

    with open("message_formatted.txt", "w", encoding="utf8") as final:
        final.writelines(message_line)

    print("Message format complete")