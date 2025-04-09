def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text


with open('text.txt', "r", encoding="utf-8") as file:
    lines = file.readlines()

encrypted_lines = [caesar_cipher(line.strip(), i + 1) for i, line in enumerate(lines)]

encrypted_file_path = "encrypted_text.txt"
with open(encrypted_file_path, "w", encoding="utf-8") as file:
    file.write("\n".join(encrypted_lines))

