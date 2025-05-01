import tkinter as tk
from tkinter import messagebox

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x320')
        self.resizable(0, 0)
        self.title('Calculadora')
        self.iconbitmap('icono.ico')
        # Atributos de clase
        self.expresion = ''
        # Caja de texto (input)
        self.entrada = None
        # StringVar lo utilizamos para obtener el valor del input
        self.entrada_texto = tk.StringVar()
        # Creamos los componentes
        self._creacion_componentes()
        
    # Métodos de clase
    # Método para crear los componentes
    def _creacion_componentes(self):
        # Creamos un primer Frame para el texto
        entrada_frame = tk.Frame(self, width=400, height=50, bg='grey')
        entrada_frame.pack(side=tk.TOP)
        # Caja de Texto
        entrada = tk.Entry(entrada_frame, font=('arial', 18, 'bold'), fg='white',
                    textvariable=self.entrada_texto, width=30, justify=tk.RIGHT, bg='#353535')
        entrada.grid(row=0, column=0, ipady=10)
        
        # Creamos otro frame para la parte inferior)
        botones_frame = tk.Frame(self, width=400, height=450, bg='grey')
        botones_frame.pack(fill='both', expand=True, ipady=10)
        
        # Primer row
        boton_limpiar = tk.Button(botones_frame, text='Limpiar', width='38', height=3,
                                    bd=0, bg='#d9d9d9', cursor='hand2', command=self._evento_limpiar)
        boton_limpiar.grid(row=0, column=0, columnspan=3, padx=1, pady=1, sticky=tk.W+tk.E)
        boton_dividir = tk.Button(botones_frame, text='/', width='17', height=3, bd=0,
                                  bg='#eee', cursor='hand2', 
                                  command=lambda: self._evento_click('/')
                                  ).grid(row=0, column=3, padx=1, pady=1)
        #boton_dividir.grid(row=0, column=3, padx=1, pady=1)
        
        #Segundo row
        boton_7 = tk.Button(botones_frame, text='7', width=12, height=3, bd=0,
                                  bg='#eee', cursor='hand2', 
                                  command=lambda: self._evento_click(7)
                                  ).grid(row=1, column=0, padx=1, pady=1)
        boton_8 = tk.Button(botones_frame, text='8', width=12, height=3, bd=0,
                                  bg='#eee', cursor='hand2', 
                                  command=lambda: self._evento_click(8)
                                  ).grid(row=1, column=1, padx=1, pady=1)
        boton_9 = tk.Button(botones_frame, text='9', width=12, height=3, bd=0,
                                  bg='#eee', cursor='hand2', 
                                  command=lambda: self._evento_click(9)
                                  ).grid(row=1, column=2, padx=1, pady=1)
        boton_multiplicar = tk.Button(botones_frame, text='*', width=17, height=3, bd=0,
                                  bg='#eee', cursor='hand2', 
                                  command=lambda: self._evento_click('*')
                                  ).grid(row=1, column=3, padx=1, pady=1)
        
        #Tercero row
        boton_4 = tk.Button(botones_frame, text='4', width=12, height=3, bd=0,
                                  bg='#eee', cursor='hand2', 
                                  command=lambda: self._evento_click(4)
                                  ).grid(row=2, column=0, padx=1, pady=1)
        boton_5 = tk.Button(botones_frame, text='5', width=12, height=3, bd=0,
                                    bg='#eee', cursor='hand2', 
                                    command=lambda: self._evento_click(5)
                                    ).grid(row=2, column=1, padx=1, pady=1)
        boton_6 = tk.Button(botones_frame, text='6', width=12, height=3, bd=0,
                                    bg='#eee', cursor='hand2', 
                                    command=lambda: self._evento_click(6)
                                    ).grid(row=2, column=2, padx=1, pady=1)
        boton_restar = tk.Button(botones_frame, text='-', width=17, height=3, bd=0,
                                  bg='#eee', cursor='hand2', 
                                  command=lambda: self._evento_click('-')
                                  ).grid(row=2, column=3, padx=1, pady=1)
        
        #Cuarto row
        boton_1 = tk.Button(botones_frame, text='1', width=12, height=3, bd=0,
                                  bg='#eee', cursor='hand2', 
                                  command=lambda: self._evento_click(1)
                                  ).grid(row=3, column=0, padx=1, pady=1)
        boton_2 = tk.Button(botones_frame, text='2', width=12, height=3, bd=0,
                                    bg='#eee', cursor='hand2', 
                                    command=lambda: self._evento_click(2)
                                    ).grid(row=3, column=1, padx=1, pady=1)
        boton_3 = tk.Button(botones_frame, text='3', width=12, height=3, bd=0,
                                    bg='#eee', cursor='hand2', 
                                    command=lambda: self._evento_click(3)
                                    ).grid(row=3, column=2, padx=1, pady=1)
        boton_sumar = tk.Button(botones_frame, text='+', width=17, height=3, bd=0,
                                  bg='#eee', cursor='hand2', 
                                  command=lambda: self._evento_click('+')
                                  ).grid(row=3, column=3, padx=1, pady=1)
        ##Quinto row
        boton_0 = tk.Button(botones_frame, text='0', width=12, height=3, bd=0,
                                  bg='#eee', cursor='hand2', 
                                  command=lambda: self._evento_click(0)
                                  ).grid(row=4, column=0, padx=1, pady=1)
        boton_parentesis_izq = tk.Button(botones_frame, text='(', width=12, height=3, bd=0,
                                    bg='#eee', cursor='hand2', 
                                    command=lambda: self._evento_click('(')
                                    ).grid(row=4, column=1, padx=1, pady=1)
        boton_parentesis_der = tk.Button(botones_frame, text=')', width=12, height=3, bd=0,
                                    bg='#eee', cursor='hand2', 
                                    command=lambda: self._evento_click(')')
                                    ).grid(row=4, column=2, padx=1, pady=1)
        boton_igual = tk.Button(botones_frame, text='=', width=17, height=3, bd=0,
                                  bg='#eee', cursor='hand2', 
                                  command=self._evento_igual
                                  ).grid(row=4, column=3, padx=1, pady=1)
        
    def _evento_igual(self):
        # Evaluar la expresión matemática
        try:
            resultado = eval(self.expresion)
            self.entrada_texto.set(resultado)
            self.expresion = str(resultado)  # Actualizamos la expresión con el resultado
        except ZeroDivisionError:
            messagebox.showerror('Error', 'No se puede dividir entre cero')
            self.expresion = ''
            self.entrada_texto.set(self.expresion)
        except Exception as e:
            messagebox.showerror('Error', f'Error en la expresión: {e}')
            self.expresion = ''
            self.entrada_texto.set(self.expresion)
        
        
    def _evento_click(self, elemento):
        # Concatenamos el nuevo elemento a la expresión ya existente
        self.expresion = f'{self.expresion}{elemento}'
        self.entrada_texto.set(self.expresion)
        
    def _evento_limpiar(self):
        self.expresion = ''
        self.entrada_texto.set(self.expresion)
    
    
if __name__ == '__main__':
    calculadora = Calculadora()
    calculadora.mainloop()
