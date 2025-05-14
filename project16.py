def hide_message(secret,cover_text):
    binary =  ''.join(format(ord(c),'08b') for c in secret)
    zwc_map = {'0': '\u200b', '1' : '\u200c'}

    encoded = ''.join(zwc_map[bit] for bit in binary)
    return cover_text + encoded 

secret= "hello"
cover = "This is a normal message ."
result = hide_message(secret,cover)
with open ("secret_text", "w", encoding= "utf -8" )as f:
    f.write(result)
    print("Secret hidden in text !")