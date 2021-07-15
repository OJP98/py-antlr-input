from tkinter import filedialog as fd, messagebox
import os
import tkinter as tk

def SelectFile():
    return fd.askopenfilename()

def GetGrammarFile():
    # Get the grammar file for the user
    grammar_file = SelectFile()
    while not grammar_file:
        retry_box = messagebox.askretrycancel(
            title='Gramática',
            message='Por favor, seleccione el archivo de gramática'
        )
        if not retry_box: exit()
        grammar_file = SelectFile()

    g_file = grammar_file
    return os.path.normpath(g_file)

def GetTestFile():
    # Get the test file from the user
    test_file = SelectFile()
    while not test_file:
        retry_box = messagebox.askretrycancel(
            title='Archivo de Entrada',
            message='Por favor, seleccione el archivo de entrada'
        )
        if not retry_box: exit()
        test_file = SelectFile()

    t_file = test_file
    return os.path.normpath(t_file)

def CompileAndExecute(grammar_path, grammar_name, start_rule, file_path):
    g_command = f'antlr4 -o . -lib . {grammar_path}'
    j_command = f'javac *.java'
    t_command = f'grun {grammar_name} {start_rule} -gui {file_path}'

    os.system(g_command)
    os.system(j_command)
    os.system(t_command)

def GetTextInput(label):
    master = tk.Tk()

    def GetInput():
        master.withdraw()
        master.quit()

    tk.Label(master, text=label).pack()
    # Ask for the user to input the grammar name
    text_input = tk.Entry(
        master,
        justify=tk.LEFT,
        width=50
    )
    text_input.pack()
    
    button = tk.Button(
        master,
        text='Aceptar',
        command=GetInput
    )
    button.pack()

    master.mainloop()

    return text_input.get()

if __name__ == "__main__":

    root = tk.Tk()
    root.withdraw()

    # Ask for required preparations
    requirements = messagebox.askyesno(
        title='Requerimientos',
        message='¿Está configurado java y ANTLR, junto con los comandos antlr4 y grun?')
    
    # If he doesn't have them, then exit
    if not requirements:
        messagebox.showerror(
            title='Error de Requerimientos',
            message='Por favor, instale los requerimientos para utilizar el programa'
        )
        exit()

    grammar_name = GetTextInput('Nombre de la gramática: ')

    # Ask for the user to select the grammar file
    grammar_box = messagebox.askokcancel(
        title='Gramática',
        message='Por favor, seleccione el archivo de gramática'
    )
    # exit out if he cancels
    if not grammar_box: exit()

    grammar_file = GetGrammarFile()

    start_rule = GetTextInput('Nombre de la regla de inicio (para Decaf, es "program"):')
    # start_rule = 'program'

    # Ask for the user to select the input file
    input_file = messagebox.askokcancel(
        title='Archivo de entrada',
        message='Por favor, seleccione el archivo de entrada'
    )
    # exit out if he cancels
    if not input_file: exit()

    test_file = GetTestFile()

    CompileAndExecute(grammar_file, grammar_name, start_rule, test_file)