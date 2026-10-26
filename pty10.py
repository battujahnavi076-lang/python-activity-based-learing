text = "AAABBCCCCD"
if text == "":
    print("Input string is empty.")
else:
    encoded, count = "", 1
    for i in range(1, len(text)):
        if text[i] == text[i-1]: count += 1
        else:
            encoded += text[i-1] + str(count); count = 1
    encoded += text[-1] + str(count)
    print("Original:", text, "Length:", len(text))
    print("Encoded:", encoded, "Length:", len(encoded))
    print("Chosen representation:", encoded if len(encoded) < len(text) else text)
