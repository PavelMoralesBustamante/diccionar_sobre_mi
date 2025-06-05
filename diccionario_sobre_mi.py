from colorama import Style, Fore, Back
#Diccionario con 20 datos sobre mi
yo = {
    "pnombre":"Pavel",
    "appaterno": "Morales",
    "fecha_nacimiento":{
        "dia":2,
        "mes":6,
        "anio":1989
    },
    "signo":"♊"
}

#Mostrar Ficha
print(f""" {Style.BRIGHT}{Fore.YELLOW}
===========================================
         {yo['pnombre']} {yo['appaterno']} {yo['signo']}
==========================================={Style.RESET_ALL}

Fecha Nacimiento : {yo['fecha_nacimiento']['dia']}-{yo['fecha_nacimiento']['mes']}-{yo['fecha_nacimiento']['anio']}      Nacionalidad:
      
      """)