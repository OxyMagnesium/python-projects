
def func_menu(name, **kwargs):
    code = f'void {name}()\n'
    code += '{\n'
    code += '    int opt, cont = 1;\n'
    code += '    while (cont)\n'
    code += '    {\n'
    code += '        cout << "MENU\\n";\n'
    i = 1
    for key, val in kwargs.items():
        code += f'        cout << "{i}. {key}\\n";\n'
        i += 1
    code += f'        cout << "{i}. Exit\\n";\n'
    code += f'        cout << "Enter your choice: "; cin >> opt;\n'
    code += '        switch(opt)\n'
    code += '        {\n'
    i = 1
    for key, val in kwargs.items():
        code += f'            case {i}: {val};\n                break;\n'
        i += 1
    code += f'            case {i}: cont = 0;\n'
    code += '        }\n'
    code += '    }\n'
    code += '}\n'
    return code

def input_var(name, var):
    return f'cout << "{name}: "; cin >> {var};'

def class_input(name, param_class, **kwargs):
    pass
