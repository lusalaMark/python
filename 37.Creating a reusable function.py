def emoji_counter(message):
    words = message.split(" ")
    emojis = {
        ":)": "happy",
        ":(": "sad"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = ">>>"
print(emoji_counter(message))
