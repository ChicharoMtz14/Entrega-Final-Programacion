#  Código desarrollado en la clase - César Martínez (A01280550), Sofía Pérez (A00835487), Roberto Cantú (A01285737), Luis Zurita (A00836199)
#  Tema: Percepción de la Pobreza por parte de la sociedad mexicana

#  DEFINICIÓN DE LIBRERIAS
import PySimpleGUI as sg
import csv
import webbrowser as wb
import pandas as pd
from datetime import date
import matplotlib.pyplot as plt
from matplotlib import pylab

#  Variables globales
year = ""
titulo = ""
cortado = ""

#  Elementos gráficos de "Inicio de Sesión" y "Menú Principal"
font0 = ("Times, 23")
font1 = ("Times, 14")
font2 = ("Times, 13")
letrero00 = sg.Text("TODOS VS LA POBREZA", justification = 'center', font = font0)
img0 = sg.Image("Logo.png", 'center', pad = (0,5), key = "LOGO", size = (200,200))
letrero2 = sg.Text ("Ingrese su usuario: ", pad = (200,10), font = font1)
nombre = sg.Input ("", pad = (80,0), key = "INombre", font = font2)
letrero3 = sg.Text ("Ingrese su contraseña: ", pad = (185,10), font = font1)
password = sg.Input("", password_char = "*", pad = (80,0), key = "IACCESO", font = font2)
boton5 = sg.Button("ENTRAR", pad = (240,13), key = "ENTRAR", size = (10,1))
boton0_5 = sg.Button("¿Olvidó sus credenciales?", pad = (10,10), key = "OLVIDO", size = (23,1), font = font1)
boton4 = sg.Button("Para saber más del tema...", pad = (20,10), key = "MAS", size = (23,1), font = font1)
texto0 = sg.Text("'Unidos como equipo lograremos más.'", pad = (120,5), text_color = "black", font = font1)
letrero4 = sg.Text("© César Martínez, Sofía Pérez, Roberto Cantú y Luis Zurita (2022)", pad = (95, 14))

letrero6 = sg.Text("Usuario activo: Admin01", pad = (10,10), font = font1)
letrero1 = sg.Text("Bienvenid@, selecciona una opción para comenzar.", pad = (10,0), font = font1)  
img1 = sg.Image("foto1recortada.png", pad = (18,20), key = "IMAGEN1", size = (160,160))
img2 = sg.Image("sdg1recortado.png", pad = (18,20), key = "IMAGEN2", size = (160,160))
img3 = sg.Image("Formulario.png", pad = (16,20), key = "IMAGEN3", size = (160,160))
img4 = sg.Image("Lupa.png", pad = (16,20), key = "IMAGEN4", size = (160,160))
b1 = sg.Button("Estadísticas", key = "BESTADISTICA", size = (16,2), font = font1)
b2 = sg.Button("Introducción", key = "BINTRO", size = (16,2), font = font1)
b3 = sg.Button("¡Aporta tu granito \nde arena!", key = "BFORMULARIO" ,size = (16,2), font = font1)
b6 = sg.Button("Saber más...", key = "BVIDEO" ,size = (16,2), font = font1)
b4 = sg.Button("SALIR", pad =  (160, 20), key = "BSALIR", size = (13,2), button_color = "darkblue", font = font1)
b5 = sg.Button("Mapa de ayuda", key = "BMAPA", size = (13,2), button_color = "darkblue", font = font1)
letrero7 = sg.Text(('Fecha de hoy: ' + date.today().strftime("%d/%m/%Y")), pad = (45,0), font = font1)
letrero8 = sg.Text("El trabajo en equipo es el secreto que hace que gente \ncomún tenga resultados poco comunes. —Ifeanyi Onuoha", justification = 'center', pad = (170,5), font = font2)


#  FUNCIONES DEL CÓDIGO

#  Apartado 1: Introducción al tema, estilo portada
def intro():
    R1 = sg.Text("La amplia disponibilidad de datos en los medios de comunicación (televisión, redes sociales, radio, entre otros)", font = font2)
    R2 = sg.Text("ha derivado en múltiples escenarios de desinformación acerca de los problemas sociales que vive el país en años", font = font2)
    R3 = sg.Text("recientes. Sin ir más lejos, durante la pandemia de la COVID-19 en México se registraron diversos estudios en los", font = font2)
    R4 = sg.Text("que se constataba un escepticismo en la población civil respecto a los riesgos del contagio de la enfermedad pese", font = font2)
    R5 = sg.Text("a la existencia incluso de estadísticas que constatan el hecho (EFE, 2020).", font = font2)
    R6 = sg.Text("\nLa conciencia de la población sobre los múltiples problemas que azotan al país resulta de vital importancia para", font = font2)
    R7 = sg.Text("la debida resolución de estos. Si bien el anterior ejemplo deja en claro este punto para el caso específico de la", font = font2)
    R8 = sg.Text("COVID-19, la situación se extiende a otros problemas tal como el de la pobreza. Reyes (2021) asegura que la", font = font2)
    R9 = sg.Text("desinformación sobre las causas de pobreza no es exclusiva de algún nivel socioeconómico particular y se llega a", font = font2)
    R10 = sg.Text("afirmar incluso que “los individuos son responsables de su propia condición de pobreza” sin mayor sustento (p. 8). ", font = font2)
    R11 = sg.Text("\nCon base en lo anterior, se pretende elaborar una presentación clara y concisa de datos estadísticos sobre la", font = font2)
    R12 = sg.Text("pobreza en México así como sus principales causas. La existencia de números concretos y bien contextualizados", font = font2)
    R13 = sg.Text("son de suma importancia para fundamentar posteriores propuestas de políticas públicas que busquen arreglar la", font = font2)
    R14 = sg.Text("problemática. Todo ello se realizará, ultimadamente, en aras de contribuir a la sensibilización de la sociedad", font = font2)
    R15 = sg.Text("nacional acerca del tema y a eliminar estereotipos, prejuicios o mitos acerca de la pobreza en los diferentes", font = font2)
    R16 = sg.Text("sectores poblacionales.", font = font2)
    R17 = sg.Text("\nRevisa toda la bibliografía consultada para realizar este trabajo en la sección 'Referencias'.", font = font2)
    Bsalirintro = sg.Button("Cerrar esta ventana", key = "SalirIntro", pad = (100,10), font = font1)
    BReferencias = sg.Button("Referencias", key = "Referencias", pad = (170,10), font = font1, button_color = "darkblue")
    layoutintro = [[R1], [R2], [R3], [R4], [R5], [R6], [R7], [R8], [R9], [R10], [R11], [R12], [R13], [R14], [R15], [R16], [R17], [BReferencias, Bsalirintro]]
    VentanaIntro = sg.Window("Introducción - TODOS VS LA POBREZA", layoutintro)
    
    while True:
        event, values = VentanaIntro.Read()
        if event == sg.WIN_CLOSED:
            break
        if event == "SalirIntro":
            VentanaIntro.close()
            break
        if event == "Referencias":
            VentanaIntro.close()
            referencias()
            break
         
    return

#  Apartado 1.5: Bibliografía Consultada
def referencias():
    R18 = sg.Text("Bibliografía Consultada:", font = font0)
    R19 = sg.Text("Banco Mundial. (2021). Pobreza (México). Recuperado de https://datos.bancomundial.org/\ntema/pobreza?locations=MX", font = font2)
    BVisitar1 = sg.Button("Visitar este sitio", key = "Visitar1", pad = (10,10))
    R20 = sg.Text("Cámara de Diputados. (2017). Encuesta telefónica nacional: Pobreza en México. Recuperado\nde http://www5.diputados.gob.mx/index.php/camara/Centros-de-Estudio/CESOP/Opinion-Pub\nlica/Encuestas/Encuesta-telefonica-nacional-Pobreza-en-Mexico", font = font2)
    BVisitar2 = sg.Button("Visitar este sitio", key = "Visitar2", pad = (10,10))
    R21 = sg.Text("Consejo Nacional de Evaluación de la Política de Desarrollo Social [CONEVAL]. (2020).\nPobreza en México: Resultados de pobreza en México 2020 a nivel nacional y por entidades\nfederativas. Recuperado de https://www.coneval.org.mx/Medicion/Paginas/PobrezaInicio.aspx", font = font2)
    BVisitar3 = sg.Button("Visitar este sitio", key = "Visitar3", pad = (10,10))
    R22 = sg.Text("EFE. (4 de julio de 2020). Pandemia, pobreza y desinformación golpean el Valle de México.\nRecuperado de https://www.debate.com.mx/estadodemexico/Pandemia-pobreza-y-desinforma\ncion-golpean-el-Valle-de-Mexico-20200704-0132.html", font = font2)
    BVisitar4 = sg.Button("Visitar este sitio", key = "Visitar4", pad = (10,10))
    R23 = sg.Text("Reyes, X. (2021). La pobreza en México y el Estado de México: Diagnóstico y percepciones\nciudadanas. Universidad Autónoma del Estado de México: Estado de México, México.\nDisponible en http://ri.uaemex.mx/handle/20.500.11799/111753", font = font2)
    BVisitar5 = sg.Button("Visitar este sitio", key = "Visitar5", pad = (10,10))
    BR_Regresar = sg.Button("Regresar a Introducción", key = "R_Regresar", pad = (65,10), font = font1, button_color = "darkblue")
    BR_MenuP = sg.Button("Volver al Menú Principal", key = "R_MP", pad = (60,10), font = font1, button_color = "darkblue")
    layoutreferencias = [[R18], [R19], [BVisitar1], [R20], [BVisitar2], [R21], [BVisitar3], [R22], [BVisitar4], [R23], [BVisitar5], [BR_Regresar, BR_MenuP]]
    VentanaReferencias = sg.Window("Referencias - TODOS VS LA POBREZA", layoutreferencias)
    
    while True:    
        event, values = VentanaReferencias.Read()
        if event == sg.WIN_CLOSED:
            break
        if event == "R_Regresar":
            VentanaReferencias.close()
            intro()
            break
        if event == "R_MP":
            VentanaReferencias.close()
            break
        if event == "Visitar1":
            wb.open_new_tab("https://datos.bancomundial.org/tema/pobreza?locations=MX")
        if event == "Visitar2":
            wb.open_new_tab("http://www5.diputados.gob.mx/index.php/camara/Centros-de-Estudio/CESOP/Opinion-Publica/Encuestas/Encuesta-telefonica-nacional-Pobreza-en-Mexico")
        if event == "Visitar3":
            wb.open_new_tab("https://www.coneval.org.mx/Medicion/Paginas/PobrezaInicio.aspx")
        if event == "Visitar4":
            wb.open_new_tab("https://www.debate.com.mx/estadodemexico/Pandemia-pobreza-y-desinformacion-golpean-el-Valle-de-Mexico-20200704-0132.html")
        if event == "Visitar5":
            wb.open_new_tab("http://ri.uaemex.mx/handle/20.500.11799/111753")

    return

#  Apartado 2:  Selección de base de datos para mostrar estadísticas descriptivas
def estadisticabd():
    
    BD = sg.Text("            Escoge una base de datos para consultar:", justification = 'center', font = font1)
    BM = sg.Button("Banco Mundial", key = "BBM", font = font2, button_color = "gray", pad = (180,10))
    CONEVAL = sg.Button("CONEVAL", key = "BCONEVAL", font = font2, button_color = "gray", pad = (195,10))
    GOB = sg.Button("Gobierno Federal", key = "BGOB", font = font2, button_color = "gray", pad = (170,10))
    MP = sg.Button("Regresar", key = "BMP", font = font2, button_color = "darkblue", pad = (199,10))
    layoutEst_1 = [[BD], [BM], [CONEVAL], [GOB], [MP]]
    VentanaEst_1 = sg.Window("Bases de Datos", layoutEst_1)

    while True:
        event, values = VentanaEst_1.Read()
        if event == sg.WIN_CLOSED:
            break
        if event == "BMP":
            VentanaEst_1.close()
            break
        if event == "BBM":
            VentanaEst_1.close()
            estadistica_BM()
            break
        if event == "BCONEVAL":
            VentanaEst_1.close()
            estadistica_C()
            break
        if event == "BGOB":
            VentanaEst_1.close()
            estadistica_CD()
            break

    return

#  Apartado 2.1: Años de selección para base de datos del Banco Mundial
def estadistica_BM():
    Epoca = sg.Text("   Escoge un año de la base de datos: ", font = font1)
    Lista_BM = sg.Listbox(("1990", "1993", "1995", "1997", "1999", "2001", "2003", "2005", "2006", "2007", "2009", "2011",
                           "2013", "2015", "2017", "2019", "2021"), key = "L_Lista_BM", size = (16,8), pad = (100,10), font = "Times, 11")
    Volver_BM = sg.Button("Regresar", key = "V_BM", button_color = "darkblue", font= "Times, 12")
    MP_BM = sg.Button("Menú Principal", key = "BMP_BM", font = "Times, 12")
    Aceptar = sg.Button("ACEPTAR", key = "BAceptar", pad = (20,0), font = "Times, 12")
    layoutEst_2BM = [[Epoca], [Lista_BM], [Volver_BM, Aceptar, MP_BM]]
    VentanaEst_2BM = sg.Window("Año - Banco Mundial", layoutEst_2BM)
    
    while True:
        event, values = VentanaEst_2BM.Read()
        if event == sg.WIN_CLOSED:
            break
        if event == "V_BM":
            VentanaEst_2BM.close()
            estadisticabd()        
            break
        if event == "BMP_BM":
            VentanaEst_2BM.close()
            break
        #  Problemas con keyword 'None' y módulos de PYSimpleGUI obligan a considerar cada caso manualmente para validar selección.
        if event == "BAceptar" and ((str(values['L_Lista_BM'])) == "['1990']" or (str(values['L_Lista_BM'])) == "['1993']" or (str(values['L_Lista_BM'])) == "['1995']"
                                    or (str(values['L_Lista_BM'])) == "['1997']" or (str(values['L_Lista_BM'])) == "['1999']" or (str(values['L_Lista_BM'])) == "['2001']"
                                    or (str(values['L_Lista_BM'])) == "['2003']" or (str(values['L_Lista_BM'])) == "['2005']" or (str(values['L_Lista_BM'])) == "['2006']"
                                    or (str(values['L_Lista_BM'])) == "['2007']" or (str(values['L_Lista_BM'])) == "['2009']" or (str(values['L_Lista_BM'])) == "['2011']"
                                    or (str(values['L_Lista_BM'])) == "['2013']" or (str(values['L_Lista_BM'])) == "['2015']" or (str(values['L_Lista_BM'])) == "['2017']"
                                    or (str(values['L_Lista_BM'])) == "['2019']" or (str(values['L_Lista_BM'])) == "['2021']"):
            
            global year
            year = str(values['L_Lista_BM'])
            VentanaEst_2BM.close()
            estadistica_BM_2()
            break
                
    return            

#  Apartado 2.2: Lectura de datos desde Excel para mostrarlos en el programa (Banco Mundial)
def estadistica_BM_2():
    tabla3 = pd.read_excel("BaseDatosPobrezaMexicoFINAL.xlsx", sheet_name = "Banco Mundial")
    df = pd.DataFrame(tabla3)
    titulo = sg.Text(('Banco Mundial - ' + (year[2] + year[3] + year[4] + year[5])), font = font1)
    punto1 = sg.Text("% de población con ingresos menores a $80.00 MXN diarios (2017 año base): ", font = "Times, 12")
    numero1 = sg.Text((str(df.iloc[3][year]) + '%'), font = "Times, 12", text_color = 'orange')
    punto2 = sg.Text("Índice de Gini en México: ", font = "Times, 12")
    numero2 = sg.Text((str(df.iloc[4][year]) + '%'), font = "Times, 12", text_color = 'orange')
    punto3 = sg.Text("% de población con el peor 50% de los sueldos: ", font = "Times, 12")
    numero3 = sg.Text((str(df.iloc[9][year]) + '%'), font = "Times, 12", text_color = 'orange')
    punto4 = sg.Text("% de población viviendo en barrios de tugurios: ", font = "Times, 12")
    numero4 = sg.Text((str(df.iloc[15][year]) + '%'), font = "Times, 12", text_color = 'orange')
    NuevaSel = sg.Button("Nueva selección", key = "BNS", font = font2)
    Graficar = sg.Button("Graficar...", key = "Graf", font = font2)
    MenuP = sg.Button("Menú Principal", key = "MP", font = font2, button_color = 'darkblue')
    
    layoutEst_3BM = [[titulo], [punto1, numero1], [punto2, numero2], [punto3, numero3], [punto4, numero4], [NuevaSel, Graficar, MenuP]]
    VentanaEst_3BM = sg.Window(('TODOS VS LA POBREZA - ' + 'Banco Mundial, ' + (year[2] + year[3] + year[4] + year[5])), layoutEst_3BM)
    OpcionG = sg.Combo(("Población con ingresos menores a $80.00 MXN", "Índice Gini", "Peor 50% de sueldos", "Barrios de tugurios"), key = "GRAFI")
    
    VolverG = sg.Button("Volver", key = "VOLVG", font = font1)
    GraficarG = sg.Button("GRAFICAR", key = "GRAFG", font = font1)
    VentanaTest = sg.Window("Graficar Datos", [[sg.Text("¿Qué deseas graficar? (1990 - 2021)", font = font1)],
                                         [OpcionG],
                                         [VolverG, GraficarG]])
    
    years = [1990,1993,1995,1997,1999,2001,2003,2005,2006,2007,2009,2011,2013,2015,2017,2019,2021]
    eje_y = [0 for i in range(17)]
    while True:
        event, values = VentanaEst_3BM.Read()
        if event == sg.WIN_CLOSED:
            break
        if event == "BNS":
            VentanaEst_3BM.close()
            estadisticabd()
            break
        #  Proceso de creación de gráficas con los datos de Excel para una mejor visualización del usuario.
        if event == "Graf":
            while True:
                event2, values2 = VentanaTest.Read()
                if event2 == sg.WIN_CLOSED:
                    VentanaTest.close()
                    VentanaEst_3BM.close()
                    estadistica_BM_2()
                    return
                if event2 == "VOLVG":
                    VentanaTest.close()
                    VentanaEst_3BM.close()
                    estadistica_BM_2()
                    return
                if event2 == "GRAFG":
                    if values2["GRAFI"] == "Población con ingresos menores a $80.00 MXN":
                        for i in range(17):
                            eje_y[i] = float(df.iloc[3][i+1])
                        plt.plot(years, eje_y); plt.title("Población con ingresos menores a $80.00 MXN (%), México, 1990 - 2017"); plt.xlabel("Años"); plt.ylabel("Porcentaje")
                        plt.show()
                    if values2['GRAFI'] == "Índice Gini":
                        for i in range(17):
                            eje_y[i] = float(df.iloc[4][i+1])
                        plt.plot(years, eje_y); plt.title("Índice de Gini (Porcentaje), México, 1990 - 2017"); plt.xlabel("Años"); plt.ylabel("Porcentaje")
                        plt.show()
                    if values2['GRAFI'] == "Peor 50% de sueldos":
                        for i in range(17):
                            eje_y[i] = float(df.iloc[9][i+1])
                        plt.plot(years, eje_y); plt.title("Población con el peor 50% de los sueldos (%), México, 1990 - 2017"); plt.xlabel("Años"); plt.ylabel("Porcentaje")
                        plt.show()
                    if values2['GRAFI'] == "Barrios de tugurios":
                        years2 = ["2001","2006","2015","2017","2019"]; eje_y2 = [19.9, 14.4, 11.1, 16, 16]
                        plt.bar(years2, eje_y2); plt.title("Población viviendo en barrios de tugurios (%), México, 1990 - 2017"); plt.xlabel("Años"); plt.ylabel("Porcentaje")
                        plt.show()
                    else:
                        continue 
        if event == "MP":
            VentanaEst_3BM.close()
            break
    
    return

#  Apartado 2.3: Años de selección para base de datos del CONEVAL
def estadistica_C():
    EpocaC = sg.Text("   Escoge un año de la base de datos: ", font = font1)
    Lista_C = sg.Listbox(("2016", "2018", "2020"), key = "L_Lista_C", size = (16,3), pad = (100,10), font = "Times, 11")
    Volver_C = sg.Button("Regresar", key = "V_C", button_color = "darkblue", font= "Times, 12")
    MP_C = sg.Button("Menú Principal", key = "BMP_C", font = "Times, 12")
    AceptarC = sg.Button("ACEPTAR", key = "BAceptarC", pad = (20,0), font = "Times, 12")
    layoutEst_2C = [[EpocaC], [Lista_C], [Volver_C, AceptarC, MP_C]]
    VentanaEst_2C = sg.Window("Año - CONEVAL", layoutEst_2C)
    
    while True:
        event, values = VentanaEst_2C.Read()
        if event == sg.WIN_CLOSED:
            break
        if event == "V_C":
            VentanaEst_2C.close()
            estadisticabd()        
            break
        if event == "BMP_C":
            VentanaEst_2C.close()
            break
        #  Misma cuestión del 'None' y la validación de datos
        if event == "BAceptarC" and ((str(values['L_Lista_C'])) == "['2016']" or (str(values['L_Lista_C'])) == "['2018']" or (str(values['L_Lista_C'])) == "['2020']"):
            global year
            year = str(values['L_Lista_C'])
            VentanaEst_2C.close()
            estadistica_C_2()
            break
    
    return

#  Apartado 2.4: Lectura de datos desde Excel para mostrarlos en el programa (CONEVAL)
def estadistica_C_2():
    tabla3 = pd.read_excel("BaseDatosPobrezaMexicoFINAL.xlsx", sheet_name = "CONEVAL")
    df = pd.DataFrame(tabla3)
    
    titulo = sg.Text(('CONEVAL - ' + (year[2] + year[3] + year[4] + year[5])), font = font1)
    punto1 = sg.Text("% de población en situación de pobreza: ", font = "Times, 12")
    numero1 = sg.Text((str(df.iloc[0][year]) + '%'), font = "Times, 12", text_color = 'orange')
    punto2 = sg.Text("Rezago educativo nacional: ", font = "Times, 12")
    numero2 = sg.Text((str(df.iloc[8][year]) + '%'), font = "Times, 12", text_color = 'orange')
    punto3 = sg.Text("Población con carencias de servicios básicos: ", font = "Times, 12")
    numero3 = sg.Text((str(df.iloc[12][year]) + '%'), font = "Times, 12", text_color = 'orange')
    punto4 = sg.Text("Población con carencias alimentarias: ", font = "Times, 12")
    numero4 = sg.Text((str(df.iloc[13][year]) + '%'), font = "Times, 12", text_color = 'orange')
    NuevaSel = sg.Button("Nueva selección", key = "BNS", font = font2)
    Graficar = sg.Button("Graficar...", key = "Graf", font = font2)
    MenuP = sg.Button("Menú Principal", key = "MP", font = font2, button_color = 'darkblue')
    
    layoutEst_3C = [[titulo], [punto1, numero1], [punto2, numero2], [punto3, numero3], [punto4, numero4], [NuevaSel, Graficar, MenuP]]
    VentanaEst_3C = sg.Window(('TODOS VS LA POBREZA - ' + 'CONEVAL, ' + (year[2] + year[3] + year[4] + year[5])), layoutEst_3C)
    OpcionG = sg.Combo(("Población en situación de pobreza", "Rezago educativo", "Carencia por acceso a los servicios básicos en la vivienda", "Carencia por acceso a la alimentación nutritiva y de calidad"), key = "GRAFI")
    
    VolverG = sg.Button("Volver", key = "VOLVG", font = font1)
    GraficarG = sg.Button("GRAFICAR", key = "GRAFG", font = font1)
    VentanaTest = sg.Window("Graficar Datos", [[sg.Text("¿Qué deseas graficar? (2016 - 2020)", font = font1)],
                                         [OpcionG],
                                         [VolverG, GraficarG]])
    
    years = ["2016", "2018", "2020"]
    eje_y = [0 for i in range(3)]
    while True:
        event, values = VentanaEst_3C.Read()
        if event == sg.WIN_CLOSED:
            break
        if event == "BNS":
            VentanaEst_3C.close()
            estadisticabd()
            break
        #  Creación de gráficas con datos de Excel para mejor visualización del usuario
        if event == "Graf":
            while True:
                event2, values2 = VentanaTest.Read()
                if event2 == sg.WIN_CLOSED:
                    VentanaTest.close()
                    VentanaEst_3C.close()
                    estadistica_C_2()
                    return
                if event2 == "VOLVG":
                    VentanaTest.close()
                    VentanaEst_3C.close()
                    estadistica_C_2()
                    return
                if event2 == "GRAFG":
                    if values2["GRAFI"] == "Población en situación de pobreza":
                        for i in range(3):
                            eje_y[i] = float(df.iloc[0][i+1])
                        plt.bar(years, eje_y); plt.title("Población en situación de pobreza (%), México, 2016 - 2020"); plt.xlabel("Años"); plt.ylabel("Porcentaje")
                        plt.show()
                    if values2['GRAFI'] == "Rezago educativo":
                        for i in range(3):
                            eje_y[i] = float(df.iloc[8][i+1])
                        plt.bar(years, eje_y); plt.title("Rezago educativo nacional (%), México, 2016 - 2020"); plt.xlabel("Años"); plt.ylabel("Porcentaje")
                        plt.show()
                    if values2['GRAFI'] == "Carencia por acceso a los servicios básicos en la vivienda":
                        for i in range(3):
                            eje_y[i] = float(df.iloc[12][i+1])
                        plt.bar(years, eje_y); plt.title("Población con carencias de servicios básicos (%), México, 2016 - 2020"); plt.xlabel("Años"); plt.ylabel("Porcentaje")
                        plt.show()
                    if values2['GRAFI'] == "Carencia por acceso a la alimentación nutritiva y de calidad":
                        for i in range(3):
                            eje_y[i] = float(df.iloc[13][i+1])
                        plt.bar(years, eje_y); plt.title("Población con carencias de alimentación (%), México, 2016 - 2020"); plt.xlabel("Años"); plt.ylabel("Porcentaje")
                        plt.show()
                    else:
                        continue
                
        if event == "MP":
            VentanaEst_3C.close()
            break
    
    return

#  Apartado 2.5: Selección de preguntas desde la base de datos de la Cámara de Diputados
def estadistica_CD():
    EpocaCD = sg.Text("   Escoge una pregunta de la base de datos: ", pad = (160,10), font = font1)
    tabla3 = pd.read_excel("BaseDatosPobrezaMexicoFINAL.xlsx", sheet_name = "Cámara de Diputados - Preguntas")
    df = pd.DataFrame(tabla3)
    preguntas = ["" for i in range(10)]
    for x in range(10): preguntas[x] = str(df.iloc[x][0])
    Lista_CD = sg.Listbox(preguntas, key = "L_Lista_CD", size = (80,8), pad = (30,10), font = "Times, 11")
    Volver_CD = sg.Button("Regresar", key = "V_CD", button_color = "darkblue", font= "Times, 12")
    MP_CD = sg.Button("Menú Principal", key = "BMP_CD", font = "Times, 12")
    AceptarCD = sg.Button("ACEPTAR", key = "BAceptarCD", pad = (200,0), font = "Times, 12")
    layoutEst_2CD = [[EpocaCD], [Lista_CD], [Volver_CD, AceptarCD, MP_CD]]
    VentanaEst_2CD = sg.Window("Año - Cámara de Diputados", layoutEst_2CD)
    
    while True:
        event, values = VentanaEst_2CD.Read()
        if event == sg.WIN_CLOSED:
            break
        if event == "V_CD":
            VentanaEst_2CD.close()
            estadisticabd()        
            break
        if event == "BMP_CD":
            VentanaEst_2CD.close()
            break
        #  Nuevamente el tema del 'None' y la validación de datos
        if event == "BAceptarCD" and ((str(values['L_Lista_CD'])) == "['En su opinión, ¿qué describe mejor lo que es el bienestar?']" or
                                      (str(values['L_Lista_CD'])) == "['¿Qué diría usted que es ser pobre?']" or
                                      (str(values['L_Lista_CD'])) == "['En su opinión, ¿qué consideran los mexicanos que es ser pobre extremo?']" or
                                      (str(values['L_Lista_CD'])) == "['¿Qué es indispensable para sobrevivir cuando se es pobre?']" or
                                      (str(values['L_Lista_CD'])) == "['¿A quién cree usted que afecta más la pobreza?']" or
                                      (str(values['L_Lista_CD'])) == "['De acuerdo con lo que usted piensa, ¿existen pobres porque…?']" or
                                      (str(values['L_Lista_CD'])) == "['Si el dinero del gobierno no alcanza para todo, ¿qué cree usted que se debe atender primero?']" or
                                      (str(values['L_Lista_CD'])) == "['En su opinión, ¿qué se necesita para acabar con la pobreza?']" or
                                      (str(values['L_Lista_CD'])) == "['Para usted, ¿quién el principal responsable de que haya problemas sociales?']" or
                                      (str(values['L_Lista_CD'])) == "['Para ayudar a resolver el problema de la pobreza, ¿con quién preferiría colaborar usted?']"):
            global titulo
            titulo = str(values['L_Lista_CD']).replace('[','').replace(']','').replace("'","",2)
            global cortado
            cortado = titulo[:23]
            estadistica_CD_2()
    
    return

#  Apartado 2.6: Definición de gráficas a partir de los datos almacenados en el Excel con las múltiples bases de datos.
def estadistica_CD_2():
    tabla3 = pd.read_excel("BaseDatosPobrezaMexicoFINAL.xlsx", sheet_name = cortado)
    df = pd.DataFrame(tabla3)
    tamano = len(df.index)
    eje_x = ["" for i in range(tamano)]
    eje_y = [0.0 for i in range(tamano)]
    for i in range(tamano): 
        eje_x[i] = (str(df.iloc[i][0]))
        eje_y[i] = round((float(df.iloc[i][1])*100), 3)
        
    f = plt.figure(figsize = (7,6.5))
    plt.bar(eje_x, eje_y, color = "lightblue"); plt.xticks(fontsize = 8, rotation = 45, ha = 'right')
    for j in range(len(eje_x)):
        plt.text(j,eje_y[j],str(eje_y[j]) + '%', ha = 'center', bbox = dict(facecolor = 'yellow', alpha = 0.6))
    
    plt.tight_layout()
    plt.title(titulo, fontsize = 10); plt.ylabel("Porcentaje")
    plt.show()
    
    return

#  Apartado 3:  Formulario que se guarda en un Excel
def formulario():
    bformulario1 = sg.Button('Guardar Datos',  key = "BGRABAR", button_color = "darkblue", font = font2)
    bformulario2 = sg.Button('Ver Estadísticas',  key = "BVERESTADISTICAS", button_color = "darkblue", font = font2)
    bformulario3 = sg.Button('SALIR',  key = "BSALIRFORMULARIO", font = font2)

    letrero9 = sg.Text("Edad: ", font = font2) 
    edad = sg.Input('', key = 'IEDAD', size = (12,1))
    sexo = sg.Text("Sexo: ", font = font2) 
    ComboSexo = sg.Combo(("Masculino", "Femenino", "Otro"), key = 'IOPCIONES')
    entidad = sg.Text("Entidad federativa de residencia: ", font = font2)
    estados = sg.Listbox(("Aguascalientes", "Baja California", "Baja California Sur", "Campeche", "Ciudad de México", "Chiapas", "Chihuahua",
                         "Coahuila de Zaragoza", "Colima", "Durango", "Estado de México", "Guanajuato", "Guerrero", "Hidalgo", "Jalisco",
                         "Michoacán de Ocampo", "Morelos", "Nayarit", "Nuevo León", "Oaxaca", "Puebla", "Querétaro", "Quintana Roo",
                         "San Luis Potosí", "Sinaloa", "Sonora", "Tabasco", "Tamaulipas", "Tlaxcala","Veracruz", "Yucatán", "Zacatecas"), key = "Iestado", size = (16,3))
    pregunta1 = sg.Text("1) ¿Conoces alguna iniciativa pública o privada actual que combata la pobreza en México?", font = ("Times, 11"), text_color = "black")
    ComboOpciones2 = sg.Combo(("Sí", "No"), key = 'IOPCIONES2')
    pregunta2 = sg.Text("Si tu respuesta fue 'Sí', ¿cómo se llama? (Escribe N/A si escogiste 'No'.)", font = ("Times, 11"))
    respuesta2 = sg.Input('', key = 'IRESPUESTA2')
    pregunta3 = sg.Text("2) ¿Conoces alguna institución que registre las estadísticas sobre la pobreza?", font = ("Times, 11"), text_color = "black")
    ComboOpciones3 = sg.Combo(("Sí", "No"), key = 'IOPCIONES3')
    pregunta4 = sg.Text("Menciona un ejemplo. (Escribe N/A si escogiste 'No'.)", font = ("Times, 11"))
    respuesta3 = sg.Input('', key = 'IRESPUESTA3')
    pregunta5 = sg.Text("Menciona un segundo ejemplo. (N/A si no aplica.)", font = ("Times, 11"))
    respuesta4 = sg.Input('', key = 'IRESPUESTA4')
    pregunta6 = sg.Text("3) ¿Consideras que las actuales políticas sociales verdaderamente mitigan la pobreza?", font = ("Times, 11"), text_color = "black")
    ComboOpciones4 = sg.Combo(("Sí", "No"), key = 'IOPCIONES4')
    pregunta7 = sg.Text("4) ¿Es la pobreza una causa o una consecuencia de otras problemáticas sociales a nivel nacional?", font = ("Times, 11"), text_color = "black")
    ComboOpciones5 = sg.Combo(("Causa", "Consecuencia"), key = 'IOPCIONES5')
    pregunta8 = sg.Text("Si contestaste 'causa', ¿qué problemas se originan a partir de la pobreza? (N/A si no aplica.)", font = ("Times, 11"))
    respuesta5 = sg.Input('', key = 'IRESPUESTA5')
    pregunta9 = sg.Text("Si contestaste 'consecuencia', ¿de qué problemas se deriva la pobreza? (N/A si no aplica.)", font = ("Times, 11"))
    respuesta6 = sg.Input('', key = 'IRESPUESTA6')
    pregunta10 = sg.Text("5) ¿Consideras que 'el pobre es pobre porque quiere'?", font = ("Times, 11"), text_color = "black")
    ComboOpciones6 = sg.Combo(("Sí", "No"), key = 'IOPCIONES6')
    pregunta11 = sg.Text("6) En México se realizan periódicamente estudios sobre los actuales niveles de pobreza\ny marginalización. ¿Cuál crees que era, a 2020, el porcentaje de población viviendo en la\npobreza a nivel nacional? (Escribe sólo el número.)", font = ("Times, 11"), text_color = "black")
    respuesta7 = sg.Input('', key = 'IRESPUESTA7')
    pregunta12 = sg.Text("7) De las siguientes opciones, escoge la de mayor impacto en la pobreza mexicana: ", font = ("Times, 11"), text_color = "black")
    ComboOpciones7 = sg.Combo(("apatía por la situación actual", "problemas estructurales", "ambiente político", "diferencias sociales", "conflictos familiares", "otros"), key = 'IOPCIONES7')
    pregunta13 = sg.Text("8) ¿Cuántos años estimas que tomará resolver el problema de la pobreza nacional?", font = ("Times, 11"), text_color = "black")
    respuesta8 = sg.Input('', key = 'IRESPUESTA8', size = (12,1))

    layoutformulario = [[letrero9, edad, sexo, ComboSexo],
        [entidad, estados],
        [pregunta1, ComboOpciones2],
        [pregunta2], [respuesta2],
        [pregunta3, ComboOpciones3],
        [pregunta4, respuesta3],
        [pregunta5, respuesta4],
        [pregunta6, ComboOpciones4],
        [pregunta7], [ComboOpciones5],
        [pregunta8], [respuesta5],
        [pregunta9], [respuesta6],
        [pregunta10, ComboOpciones6],
        [pregunta11, respuesta7],
        [pregunta12], [ComboOpciones7],
        [pregunta13], [respuesta8],
        [bformulario1, bformulario2, bformulario3]]
    frame_formulario = sg.Frame("Contesta lo siguiente:", layoutformulario, key = 
"FFORMULARIO",  visible = True)
    layoutventanaformulario = [[frame_formulario]] 
    windowformulario = sg.Window( 'Formulario - TODOS VS LA POBREZA', layoutventanaformulario, size = (700,705))
    event, values = windowformulario.read()                   
    
    if event == 'BGRABAR':
    
        cuenta = 0
        info = [values['IEDAD'], values['IOPCIONES'], values["Iestado"], values['IOPCIONES2'], values['IRESPUESTA2'], values['IOPCIONES3'],
                values['IRESPUESTA3'], values['IRESPUESTA4'], values['IOPCIONES4'], values['IOPCIONES5'], values['IRESPUESTA5'], values['IRESPUESTA6'],
                values['IOPCIONES6'], values['IRESPUESTA7'], values['IOPCIONES7'], values['IRESPUESTA8']]
        for i in range(len(info)):
            if info[i] == "":
                sg.Popup("Cuidado, llena toda la información como corresponde.", title = "ADVERTENCIA", font = font2)
                windowformulario.close()
                formulario()
                break
            else:
                cuenta = cuenta + 1
        
        if cuenta == 16:
            with open('ResultadosEncuesta.csv', 'a', newline = '\n') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(info)
            sg.Popup("Información registrada. ¡GRACIAS!", title = "¡GRACIAS!", font = font2)
            windowformulario.close()
       
    if event == 'BSALIRFORMULARIO':
        windowformulario.close()
        
        
    if event == 'BVERESTADISTICAS': #  Generar reporte de estadísticas obtenidas a partir de datos recopilados con formulario.
        windowformulario.close()
        with open('ResultadosEncuesta.csv', 'r') as csv_file:
            leearchivo = csv.reader(csv_file)
            renglonest1 = sg.Text("Número de Encuestados : ", font = font2)
            renglonest2 = sg.Text("Promedio de edad: ", font = font2)
            renglonest3 = sg.Text("Conciencia sobre combate a la pobreza (organismos o iniciativas) (%): ", font = font2)
            renglonest4 = sg.Text("¿Cuántos años tomará erradicar la pobreza? (Promedio): ", font = font2)
            renglonest5 = sg.Text("Promedio de porcentaje de pobreza mexicana (según encuestados): ", font = font2)
            renglonest6 = sg.Text("Factores pertinentes a la pobreza mexicana", font = font2)
            graf = sg.Button("Ver Gráfica", key = "GRAFIC", font = "Times, 12")
            volver = sg.Button("Volver", key = "VOLV", font = "Times, 12")
            edad = encuestados = tiempo = conc = pobr = graf_1 = graf_2 = graf_3 = graf_4 = graf_5 = graf_6 = 0
            for row in leearchivo:
                edad += int(row[0])
                encuestados += 1
                tiempo += int(row[15])
                pobr += int(row[13])
                if row[3] == "Sí" or row[5] == "Sí":
                    conc += 1
                if row[14] == "apatía por la situación actual":
                    graf_1 += 1
                if row[14] == "problemas estructurales":
                    graf_2 += 1
                if row[14] == "ambiente político":
                    graf_3 += 1
                if row[14] == "diferencias sociales":
                    graf_4 += 1
                if row[14] == "conflictos familiares":
                    graf_5 += 1
                if row[14] == "otros":
                    graf_6 += 1
                
            cant_enc = sg.Text(encuestados, font = font2, text_color = "black")
            prom_edad = sg.Text(round(edad/encuestados, 2), font = font2, text_color = "black")
            porc_conc = sg.Text(str((round(conc/encuestados, 2))*100) + '%', font = font2, text_color = "black")
            prom_years = sg.Text(round(tiempo/encuestados, 2), font = font2, text_color = "black")
            porc_pobr = sg.Text(str((round(pobr/encuestados, 2))) + "%", font = font2, text_color = "black")
            
            layoutestformulario = [[renglonest1, cant_enc], [renglonest2, prom_edad], [renglonest3, porc_conc],
                                   [renglonest4, prom_years], [renglonest5, porc_pobr], [renglonest6, graf], [volver]]
            
            windowestformulario =sg.Window("Estadísticas Formulario - TODOS VS LA POBREZA", layoutestformulario)
            eje_x = ["apatía por la situación actual", "problemas estructurales", "ambiente político", "diferencias sociales", "conflictos familiares", "otros"]
            eje_y = [graf_1, graf_2, graf_3, graf_4, graf_5, graf_6]
            
            while True:
                event, values = windowestformulario.Read()
                if event == sg.WIN_CLOSED:
                    formulario()
                    break
                if event == "VOLV":
                    windowestformulario.close()
                    windowformulario.close()
                    formulario()
                    break
                if event == "GRAFIC":
                    plt.bar(eje_x, eje_y, color = "darkblue"); plt.xticks(fontsize = 8, rotation = 45, ha = 'right')
                    for j in range(len(eje_x)):
                        plt.text(j,eje_y[j],str(eje_y[j]), ha = 'center', bbox = dict(facecolor = 'orange', alpha = 0.8))
                    
                    plt.tight_layout()
                    plt.title("Factores pertinentes a la pobreza mexicana (Encuesta, 2022)", fontsize = 10); plt.ylabel("Cantidad")
                    plt.show()
                
    return

#  Apartado 4: Video
def videoyt():
    wb.open_new_tab("https://www.youtube.com/watch?v=Hp5BSbk4lM0")
    return

#  Apartado 5: Mapa
def mapaayuda():
    wb.open_new_tab("https://www.google.com/maps/search/albergues+pobreza/@25.7028786,-100.3353042,13.23z?hl=es")
    return

layoutI_S = [[letrero00, img0], [letrero2], [nombre], [letrero3], [password], [boton5], [boton0_5, boton4], [texto0], [letrero4]]
layoutprincipal = [[letrero6], [letrero1, letrero7], [img1, img2, img3, img4], [b2, b1,b3, b6], [b4, b5], [letrero8]]

MenuPrincipal = sg.Window(("TODOS VS LA POBREZA - "), layoutprincipal, size = (800,500))
InicioSesion = sg.Window("Inicio de Sesión - TODOS VS LA POBREZA", layoutI_S, size = (600,600))

#  Ejecución del código comienza aqui
while True:
    event, values = InicioSesion.read()
    if event == sg.WIN_CLOSED:
        quit()
    if event == "OLVIDO":
        sg.Popup("Usuario: Admin01 // Contraseña: Equipo01", title = "Recordatorio", font = font2)
        continue
    if event == "MAS":
        wb.open_new_tab("https://www.un.org/sustainabledevelopment/es/poverty/")
        continue
    if event == "ENTRAR":
        if values['INombre'] == "Admin01" and values['IACCESO'] == "Equipo01":
            InicioSesion.close()
            break
        else:
            sg.Popup("Credenciales incorrectas. Intente de nuevo.", title = "Advertencia", font = font2)
            continue

while True:
    event2,values2 = MenuPrincipal.read()
    if event2 == sg.WIN_CLOSED:
        break
    if event2 == "BSALIR":
        MenuPrincipal.close()
        break
    if event2 == "BESTADISTICA":
        estadisticabd()
    if event2 == "BINTRO":
        intro()
    if event2 == "BFORMULARIO":
        formulario()
    if event2 == "BVIDEO":
        videoyt()
    if event2 == "BMAPA":
        mapaayuda()

    
