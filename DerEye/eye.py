import os
from os import system, name
import colorama
from colorama import Fore
import socket
import sys
from datetime import datetime
import time
colorama.init()

os.system("cls")


print(f'''{Fore.MAGENTA}

       ....                                        ..      .                             
   .xH888888Hx.                                 x88f` `..x88. .>   ..                    
 .H8888888888888:                  .u    .    :8888   xf`*8888%   @L                     
 888*"""?""*88888X        .u     .d88B :@8c  :8888f .888  `"`    9888i   .dL       .u    
'f     d8x.   ^%88k    ud8888.  ="8888f8888r 88888' X8888. >"8x  `Y888k:*888.   ud8888.  
'>    <88888X   '?8  :888'8888.   4888>'88"  88888  ?88888< 888>   888E  888I :888'8888. 
 `:..:`888888>    8> d888 '88%"   4888> '    88888   "88888 "8%    888E  888I d888 '88%" 
        `"*88     X  8888.+"      4888>      88888 '  `8888>       888E  888I 8888.+"    
   .xHHhx.."      !  8888L       .d888L .+   `8888> %  X88!        888E  888I 8888L      
  X88888888hx. ..!   '8888c. .+  ^"8888*"     `888X  `~""`   :    x888N><888' '8888c. .+ 
 !   "*888888888"     "88888%       "Y"         "88k.      .~      "88"  888   "88888%   
        ^"***"`         "YP'                      `""*==~~`              88F     "YP'    
                                                                        98"              
                                                                      ./"                
                                                                     ~`                  


''')


time.sleep(1)
print(" ")
scan = input(str(f"{Fore.YELLOW}>> {Fore.GREEN}Introduce la IP a escanear:{Fore.WHITE} "))
print("_" * 50)
time.sleep(1)
print(" ")
print(f"{Fore.WHITE}Escaneando: ", scan)
time.sleep(1)
print(" ")
print(f"{Fore.WHITE}Iniciado a las: ", str(datetime.now()))
print(" ")
print("_" * 50)
print(" ")

try:
    for port in range(1, 8000):
        sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        resultado = sck.connect_ex((scan,port))
        if resultado == 0:
            print(f"[{Fore.GREEN}*{Fore.WHITE}] El puerto", port, "está abierto.")
        sck.close()
    
except KeyboardInterrupt:
    print(" ")
    print(f"{Fore.RED}Saliendo del programa...")
    print(" ")

except socket.error:
    print(f"{Fore.RED}El host no ha respondido...")
    sys.exit()