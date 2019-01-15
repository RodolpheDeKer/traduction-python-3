#! /usr/bin/python3.6

from py_translator import Translator
import os
while True:
    text = input('ecri un message en français puis il sera tradui en Englai: ')
    restultat = Translator().translate(text=text, src="fr",  dest='en').text
    os.system("say "+restultat)
    print('')
    print(restultat)
    print("")
