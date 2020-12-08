# -*- coding: utf-8 -*-
"""
Desarrollado por:
    Avila Zambrano ELlim
    Parado Sulca Yurgen
    Rodriguez Manuelo Jhoelver
"""
"""----------------------------------------------------------------------------------------------------LIBRERIAS"""
import json
import requests
import tkinter as tk
from importlib import reload
import gc
from tkinter import messagebox
"""---------------------------------------------------------------------------------INTERFAZ DE INICIO DE SESIÓN"""

            
login=tk.Tk()
login.geometry('400x300')
login.title('Huancayo Smart City')
login.configure(bg='#42C6CD')

"""----------------------------------------------------------------------------------------------EITQUETAS LOGIN"""

lblUsuario=tk.Label(login,text='Correo Electrónico: ')
lblUsuario.place(x=20,y=100)

lblContraseña=tk.Label(login,text='Contraseña: ')
lblContraseña.place(x=20,y=130)

"""-----------------------------------------------------------------------------------------CAJAS DE TEXTO LOGIN"""

tbUsuario=tk.Entry(login,width=38)
tbUsuario.place(x=150,y=100)

tbContrasena=tk.Entry(login,show='*',width=38)
tbContrasena.place(x=150,y=130)

"""----------------------------------------------------------------------------------INTERFAZ DEL MENU PRINCIPAL"""
def ventanaMenu():
    
    login.withdraw()
    menu=tk.Toplevel(login)
    menu.geometry("350x400")
    menu.title("Menú")
    menu.configure(bg='#42C6CD')
    
    """---------------------------------------------------------------------------INTERFAZ PARA CRUD DE USUARIOS"""

    def ventanaCrud():
        menu.withdraw()
        crudUsuarios=tk.Toplevel()
        crudUsuarios.geometry('400x550')
        crudUsuarios.title('CRUD Usuarios')
        crudUsuarios.configure(bg='#42C6CD')
        
        """------------------------------------------------------------------------------------------------LOCAL"""
        
        # urlInsert='http://localhost/SmartCity-main/Usuario/Insert_Usuario.php'
        # urlConsultaID='http://localhost/SmartCity-main/Usuario/Consulta_Usuario_ID.php'
        # urlUpdate='http://localhost/SmartCity-main/Usuario/Update_Usuario.php'
        
        """---------------------------------------------------------------------------------------------SERVIDOR"""
        
        urlInsert='http://smartcityhyo.tk/api/Usuario/Insert_Usuario.php'
        urlConsultaID='http://smartcityhyo.tk/api/Usuario/Consulta_Usuario_ID.php'
        urlUpdate='http://smartcityhyo.tk/api/Usuario/Update_Usuario.php'
        
        """---------------------------------------------------------------------------------------ETIQUETAS CRUD"""
        
        lblID=tk.Label(crudUsuarios,text=idUsuario)
        lblID.place(x=1,y=1)
        
        lblNombres = tk.Label(crudUsuarios,text='Nombres: ')
        lblNombres.place(x=10,y=40)

        lblApellidos = tk.Label(crudUsuarios,text='Apellidos: ')
        lblApellidos.place(x=10,y=70)

        lblDireccion = tk.Label(crudUsuarios,text='Dirección: ')
        lblDireccion.place(x=10,y=100)

        lblFechaNacimiento = tk.Label(crudUsuarios,text='Fecha de Nacimiento(aa-mm-dd): ')
        lblFechaNacimiento.place(x=10,y=130)
    
        lblNacionalidad = tk.Label(crudUsuarios,text='Nacionalidad: ')
        lblNacionalidad.place(x=10,y=160)

        lblTelefono = tk.Label(crudUsuarios,text='Teléfono: ')
        lblTelefono.place(x=10,y=190)

        lblEmail = tk.Label(crudUsuarios,text='Email: ')
        lblEmail.place(x=10,y=220)

        lblContraseña = tk.Label(crudUsuarios,text='Contraseña: ')
        lblContraseña.place(x=10,y=250)

        lblTipo = tk.Label(crudUsuarios,text='Tipo de Usuario: ')
        lblTipo.place(x=10,y=280)

        lblAreaAgregar = tk.Label(crudUsuarios,text='AGREGAR',font='helvetica 18')
        lblAreaAgregar.place(x=10,y=340)

        lblAreaActualizar = tk.Label(crudUsuarios,text='ACTUALIZAR',font='helvetica 15')
        lblAreaActualizar.place(x=10,y=400)
        
        lblIdBuscar = tk.Label(crudUsuarios,text='ID de Usuario')
        lblIdBuscar.place(x=150,y=390)

        """----------------------------------------------------------------------------------CAJAS DE TEXTO CRUD"""

        tbNombre = tk.Entry(crudUsuarios,width=40)
        tbNombre.place(x=150,y=40)

        tbApellidos=tk.Entry(crudUsuarios,width=40)
        tbApellidos.place(x=150,y=70)

        tbDireccion = tk.Entry(crudUsuarios,width=40)
        tbDireccion.place(x=150,y=100)

        tbFechaNacimiento = tk.Entry(crudUsuarios,width=31)
        tbFechaNacimiento.place(x=203,y=130)

        tbNacionalidad = tk.Entry(crudUsuarios, width=40)
        tbNacionalidad.place(x=150,y=160)

        tbTelefono = tk.Entry(crudUsuarios,width=40)
        tbTelefono.place(x=150,y=190)

        tbEmail = tk.Entry(crudUsuarios,width=40)
        tbEmail.place(x=150,y=220)

        tbContraseña = tk.Entry(crudUsuarios,width=40)
        tbContraseña.place(x=150,y=250)

        tbTipo = tk.Entry(crudUsuarios,width=40)
        tbTipo.place(x=150,y=280)
    
        tbBuscarId = tk.Entry(crudUsuarios,width=12)
        tbBuscarId.place(x=150,y=416)
    
        """-----------------------------------------------------------------------------------------BOTONES CRUD"""
        
        def volverMp():
            menu.deiconify()
            crudUsuarios.destroy()
        
        btnVolverMp=tk.Button(crudUsuarios,text='Volver',width=20,command=volverMp)
        btnVolverMp.place(x=120,y=470)
        
        def rellenarDatos():
            idBuscar=tbBuscarId.get()
            cuerpoJson={
                "ID_Usuario": idBuscar
                        }
            _headers={'Content-Type':'application/json; charset=UTF-8'}
            respuesta=requests.post(urlConsultaID, data=json.dumps(cuerpoJson), headers=_headers)
            desglozar=respuesta.json()
            
            tbNombre.delete(0,'end')
            tbApellidos.delete(0,'end')
            tbDireccion.delete(0,'end')
            tbFechaNacimiento.delete(0,'end')
            tbNacionalidad.delete(0,'end')
            tbTelefono.delete(0,'end')
            tbEmail.delete(0,'end')
            tbContraseña.delete(0,'end')
            tbTipo.delete(0,'end')
            
            tbNombre.insert(0,desglozar['US_Nombres'])
            tbApellidos.insert(0,desglozar['US_Apellidos'])
            tbDireccion.insert(0,desglozar['US_Direccion'])
            tbFechaNacimiento.insert(0,desglozar['US_Fecha_Nacimiento'])
            tbNacionalidad.insert(0,desglozar['US_Nacionalidad'])
            tbTelefono.insert(0,desglozar['US_Telefono'])
            tbEmail.insert(0,desglozar['US_Email'])
            
            
        btnRellenar=tk.Button(crudUsuarios,text='Rellenar',width=20,command=rellenarDatos)
        btnRellenar.place(x=245,y=388)
        
        def actualizarUsuario():
            idBuscar=tbBuscarId.get()
            cuerpoJson={
                "ID_Usuario": idBuscar,   
                "US_Nombres": tbNombre.get(),
                "US_Apellidos": tbApellidos.get(),
                "US_Direccion": tbDireccion.get(),
                "US_Fecha_Nacimiento": tbFechaNacimiento.get(),
                "US_Nacionalidad": tbNacionalidad.get(),
                "US_Telefono": tbTelefono.get(),
                "US_Email": tbEmail.get()
                }
            _headers={'Content-Type':'application/json; charset=UTF-8'}
            respuesta=requests.post(urlUpdate, data=json.dumps(cuerpoJson), headers=_headers)
            desglozar=respuesta.json()
            messagebox.showinfo(title="Mensaje",
                                message = desglozar['message'])
            tbNombre.delete(0,'end')
            tbApellidos.delete(0,'end')
            tbDireccion.delete(0,'end')
            tbFechaNacimiento.delete(0,'end')
            tbNacionalidad.delete(0,'end')
            tbTelefono.delete(0,'end')
            tbEmail.delete(0,'end')
            tbContraseña.delete(0,'end')
            tbTipo.delete(0,'end')
        
        btnActualizar=tk.Button(crudUsuarios,text='Actualizar',width=20,command=actualizarUsuario)
        btnActualizar.place(x=245,y=418)
        
        def agregarUsuario():
            cuerpoJson={"US_Nombres": tbNombre.get(),
                        "US_Apellidos": tbApellidos.get(),
                        "US_Direccion": tbDireccion.get(),
                        "US_Fecha_Nacimiento": tbFechaNacimiento.get(),
                        "US_Nacionalidad": tbNacionalidad.get(),
                        "US_Telefono": tbTelefono.get(),
                        "US_Email": tbEmail.get(),
                        "US_Contrasena": tbContraseña.get(),
                        "US_Tipo": tbTipo.get(),
                        "Estado": "Activo"
                        }
            _headers={'Content-Type':'application/json; charset=UTF-8'}
            respuesta=requests.post(urlInsert, data=json.dumps(cuerpoJson), headers=_headers)
            desglozar=respuesta.json()
            messagebox.showinfo(title="Registro exitoso",
                                message = desglozar['message'])
            tbNombre.delete(0,'end')
            tbApellidos.delete(0,'end')
            tbDireccion.delete(0,'end')
            tbFechaNacimiento.delete(0,'end')
            tbNacionalidad.delete(0,'end')
            tbTelefono.delete(0,'end')
            tbEmail.delete(0,'end')
            tbContraseña.delete(0,'end')
            tbTipo.delete(0,'end')
        
        btnAgregar=tk.Button(crudUsuarios,text='Agregar',width=20,command=agregarUsuario)
        btnAgregar.place(x=150,y=340)
        
        """-----------------------------------------------------------------------------------------------------"""
    
    btnAdministrarUsuarios = tk.Button(menu, text = "Administrar Usuarios", 
                                       width = 20,
                                       height = 2,
                                       command=ventanaCrud)
    
    btnAdministrarUsuarios.place(x=105,y = 50)
    
    """----------------------------------------------------------INTERFAZ DE ADMINISTRACIÓN DE FUENTE DE CÁMARAS"""
    
    def ventanaAdministrarCamaras():
        menu.withdraw()
        adminCamaras=tk.Toplevel()
        adminCamaras.geometry('800x300')
        adminCamaras.title('Adminitración de Cámaras')
        adminCamaras.configure(bg='#42C6CD')
        
        with open('Fuentes/fuentes.json') as file:
            fuentes = json.load(file)
        
        """------------------------------------------------------------------------ETIQUETAS ADMINISTRAR CAMARAS"""
        
        lblFuente=tk.Label(adminCamaras,text='FUENTE: ')
        lblFuente.place(x=40,y=80)
        
        lblLatitud=tk.Label(adminCamaras,text='LATITUD: ')
        lblLatitud.place(x=40,y=130)
        
        lblLongitud=tk.Label(adminCamaras,text='LONGITUD: ')
        lblLongitud.place(x=40,y=180)
        
        lblCamara1=tk.Label(adminCamaras,text='CAMARA 1',font='arial 14')
        lblCamara1.place(x=210,y=10)
        
        lblCamara2=tk.Label(adminCamaras,text='CAMARA 2',font='arial 14')
        lblCamara2.place(x=500,y=10)
        
        """-------------------------------------------------------------------CAJAS DE TEXTO ADMINISTRAR CAMARAS"""
        
        tbFuenteCamara1=tk.Entry(adminCamaras,width=35)
        tbFuenteCamara1.place(x=150,y=80)
        tbFuenteCamara1.insert(0, fuentes['fuenteCamara1'])
        
        tbLatitudCamara1=tk.Entry(adminCamaras,width=35)
        tbLatitudCamara1.place(x=150,y=130)
        tbLatitudCamara1.insert(0,fuentes['latCam1'])
        
        tbLongitudCamara1=tk.Entry(adminCamaras,width=35)
        tbLongitudCamara1.place(x=150,y=180)
        tbLongitudCamara1.insert(0,fuentes['lonCam1'])
        
        tbFuenteCamara2=tk.Entry(adminCamaras,width=35)
        tbFuenteCamara2.place(x=450,y=80)
        tbFuenteCamara2.insert(0,fuentes['fuenteCamara2'])
        
        tbLatitudCamara2=tk.Entry(adminCamaras,width=35)
        tbLatitudCamara2.place(x=450,y=130)
        tbLatitudCamara2.insert(0,fuentes['latCam2'])
        
        tbLongitudCamara2=tk.Entry(adminCamaras,width=35)
        tbLongitudCamara2.place(x=450,y=180)
        tbLongitudCamara2.insert(0,fuentes['lonCam2'])
        
        """--------------------------------------------------------------------------BOTONES ADMINISTRAR CAMARAS"""
        
        def volverMp2():
            menu.deiconify()
            adminCamaras.destroy()
        
        btnVolverMp=tk.Button(adminCamaras,text='Volver',width=20,command=volverMp2)
        btnVolverMp.place(x=300,y=260)  
        
        def guardarFuentes():
            fuenteCamara1 = tbFuenteCamara1.get()
            fuenteCamara2 = tbFuenteCamara2.get()
            latCam1 = tbLatitudCamara1.get()
            lonCam1 = tbLongitudCamara1.get()
            latCam2 = tbLatitudCamara2.get()
            lonCam2 = tbLongitudCamara2.get()
            fuentesJson = {
                "fuenteCamara1": fuenteCamara1,
                "fuenteCamara2": fuenteCamara2,
                "latCam1": latCam1,
                "lonCam1": lonCam1,
                "latCam2": latCam2,
                "lonCam2": lonCam2
                }
            with open('Fuentes/fuentes.json', 'w') as file:
                json.dump(fuentesJson, file, indent=4)
            print('Fuentes guardadas con exito')
        
        btnGuardarFuentes=tk.Button(adminCamaras,text='Guardar Cambios',width=20,command=guardarFuentes)
        btnGuardarFuentes.place(x=300,y=230) 
        """-----------------------------------------------------------------------------------------------------"""
            
    btnAdministrarCamaras= tk.Button(menu, text = "Administrar camaras", 
                                     width = 20,
                                     height = 2,
                                     command=ventanaAdministrarCamaras)
    btnAdministrarCamaras.place(x=105,y = 120)
    
    # def ventanaResumenDelitos():
    #     menu.withdraw()
    #     resumenDelitos=tk.Toplevel()
    #     resumenDelitos.geometry('500x600')
    #     resumenDelitos.title('Resumen de delitos cometidos')
    #     resumenDelitos.configure(bg='#42C6CD')
    
    #     def volverMp2():
    #         menu.deiconify()
    #         resumenDelitos.destroy()
        
    #     btnVolverMp=tk.Button(resumenDelitos,text='Volver',width=20,command=volverMp2)
    #     btnVolverMp.place(x=170,y=500)
    
    # btnResumenDelitos = tk.Button(menu, 
    #                               text = "Resumen de Delitos", 
    #                               width = 20,
    #                               height = 2, 
    #                               command=ventanaResumenDelitos)
    
    # btnResumenDelitos.place(x=105,y = 190)
    
    def llamarCamaras():
        import DeteccionArmasGUI
        reload(DeteccionArmasGUI)
    
    btniniciarCamaras = tk.Button(menu, 
                                  text = "Iniciar Cámaras", 
                                  width = 20,
                                  height = 2, 
                                  command=llamarCamaras)
    
    btniniciarCamaras.place(x=105,y = 190)
    gc.collect()
    def volver():
        login.deiconify()
        menu.destroy()
    
    btnVolver = tk.Button(menu, text = "Volver", width = 20,height = 2,command=volver)
    btnVolver.place(x=105,y = 260)
    
    

"""------------------------------------------------------------------------------------------------BOTONES LOGIN"""
#LOCAL
# url="http://localhost/SmartCity-main/Usuario/login.php" 
# SERVIDOR
url='http://smartcityhyo.tk/api/Usuario/login.php'
def iniciarSesion():

    correcto=False
    
    while correcto == False:
        usuario=tbUsuario.get()
        contrasena=tbContrasena.get()
    
        cuerpoJson={
        "US_Email":usuario,
        "US_Contrasena":contrasena
        }
    
        _headers={'Content-Type':'application/json'}
        
        respuesta=requests.post(url, data=json.dumps(cuerpoJson), headers=_headers)
    
        extraerJson=respuesta.json()
        
        if extraerJson['status'] == True:
            global idUsuario
            idUsuario = extraerJson['ID_Usuario']
            correcto=True
            
            idJson = {
                "idUsuario": idUsuario
                }
            with open('Fuentes/id.json', 'w') as file:
                json.dump(idJson, file, indent=4)
            print('ID cargado con exito')
            
            ventanaMenu()
        else:
            print("Login fallido")
            messagebox.showinfo(title="inicio de sesion incorrecto",message = "Ingrese  un usuario o contraseña valida")
            break

btnIniciarSesion=tk.Button(login,text='Iniciar Sesión',command=iniciarSesion,width=16)
btnIniciarSesion.place(x=60,y=180)
btnSalir=tk.Button(login,text='Salir',command=login.destroy,width=16)
btnSalir.place(x=210,y=180)
login.mainloop()


