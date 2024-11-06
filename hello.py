#!C:\Users\tiago.yamaguti\python_base\python_base  python 
# esse comentario inicial colocando o caminho e a linguagem se chama SHEBANG

"""Hello Word Multi Linguas.

Dependendo da lingua configirado no ambiente o programa exibe a mensagem na lingua correspondente.

Como usar:
    -tenha a variavel LANG devidamente configurada. 
    Ex: export LANG=pt_BR
Execução:
    python hello.py
    ou
    ./hello.py
"""
__version__ = "0.0.'"
__name__ = "Tiago Yamaguti"
__license__ = "Unlicense"

import os 

#current_language = "en_US.UTF-8"
current_language = os.getenv ("LANG")

msg = "Hello, Word !"

if current_language == "pt_BR":
    msg = "Olá, Mundo !"
elif current_language == "it_IT":
    msg = "Ciao, Mondo"

print (msg)

#Este programa imprime Hello Word
#print ("Hello, Word !")