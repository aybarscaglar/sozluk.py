None
meme_dict = {
            "ENGLİSH OR SHPANİS":"İNGİLİZLER YADA İSPANYOLLAR",
            "CHRINGE":"UTANDIRICI",
            }
word = input("anlamadığınız bir kelime yazınız ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("sözlükte yok")
