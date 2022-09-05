import sqlite3
from tkinter import ttk
from tkinter import *


class Producto:

    def __init__(self, ventana):
        self.vent = ventana
        self.vent.title('Aplicacion de productos')

        # CREAR un contenedor o frame
        contenedor = LabelFrame(self.vent, text="Registrar un nuevo producto")
        contenedor.grid(row=0, column=0, columnspan=3, pady=20)

        # Entrada nombre del producto
        Label(contenedor, text="Nombre: ").grid(row=1, column=0)
        self.nombreProd = Entry(contenedor)
        self.nombreProd.focus()
        self.nombreProd.grid(row=1, column=1, )

        # Entrada descripcion del producto
        Label(contenedor, text="Descripcion: ").grid(row=2, column=0)
        self.descripcionProd = Entry(contenedor)
        self.descripcionProd.grid(row=2, column=1, )

        # Entrada descripcion del producto
        Label(contenedor, text="id_proveedor: ").grid(row=3, column=0)
        self.id_proveedorProd = Entry(contenedor)
        self.id_proveedorProd.grid(row=3, column=1, )

        # Agregar un boton
        ttk.Button(contenedor, text='Crear producto', command=self.agregar_producto).grid(row=4, columnspan=2,
                                                                                          sticky=W + E)

        # Output Messages
        self.message = Label(text='', fg='red')
        self.message.grid(row=3, column=0, columnspan=2, sticky=W + E)

        ######################## Contenedor Proveedor
        # CREAR un contenedor o frame
        contenedorProve = LabelFrame(self.vent, text="Registrar un nuevo proveedor")
        contenedorProve.grid(row=5, column=0, columnspan=30, pady=20)

        # Entrada nombre del proveedor
        Label(contenedorProve, text="Nombre: ").grid(row=1, column=0)
        self.nombreProve = Entry(contenedorProve)
        self.nombreProve.focus()
        self.nombreProve.grid(row=1, column=1, )

        # Entrada direccion del producto
        Label(contenedorProve, text="Direccion: ").grid(row=2, column=0)
        self.direccionProve = Entry(contenedorProve)
        self.direccionProve.grid(row=2, column=1, )

        # Agregar un boton
        ttk.Button(contenedorProve, text='Crear proveedor').grid(row=4, columnspan=4, sticky=W + E)

        # Tabla
        self.tabla = ttk.Treeview(height=10, columns=('#0', '#1'))
        self.tabla.grid(row=7, column=0, columnspan=2)
        self.tabla.heading('#0', text='Nombre', anchor=CENTER)
        self.tabla.heading('#1', text='Descripcion', anchor=CENTER)

        self.traer_productos()

    nombre_bd = 'base_de_datos.db'

    def ejecutar_query(self, query, parameters=()):
        with sqlite3.connect(self.nombre_bd) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    def traer_productos(self):
        records = self.tabla.get_children()
        for element in records:
            self.tabla.delete(element)
        query = 'Select * from PRODUCTO'
        db_rows = self.ejecutar_query(query)
        for row in db_rows:
            self.tabla.insert('', 0, text=row[1], values=row[2])

    def validacion(self):
        return len(self.nombreProd.get()) != 0 and len(self.descripcionProd.get()) != 0 and len(
            self.id_proveedorProd.get()) != 0

    def agregar_producto(self):
        if self.validacion():
            query = 'INSERT INTO PRODUCTO VALUES(NULL,?,?,?)'
            parametros = (self.nombreProd.get(), self.descripcionProd.get(), self.id_proveedorProd.get())
            self.ejecutar_query(query, parametros)
            self.message['text'] = 'Product {} added Successfully'.format(self.nombreProd.get())
            self.nombreProd.delete(0, END)
            self.id_proveedorProd.delete(0, END)
            self.descripcionProd.delete(0, END)
        else:
            self.message['text'] = 'Todos los campos son requeridos'
        self.traer_productos()


if __name__ == '__main__':
    ventana = Tk()
    aplicacion = Producto(ventana)
    ventana.mainloop()
