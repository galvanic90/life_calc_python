def ask_for_pension(mb):
    pension = float(input('Ingrese la cantidad recibida por pensión: ')) 
    total = pension * 12
    return mb.append(total)


def ask_for_salary(mb):
    salary = float(input('Ingrese la cantidad recibida por salario: '))
    total = salary * 12 
    return mb.append(total)


def ask_for_debt(mb):
    debt = float(input('Ingrese la cantidad que adeuda: ')) 
    return mb.append(-debt)


def ask_for_children(mb):
    couple = input('Tiene usted hijos? S/N')
    if couple == 'S':
        value = float(input('Ingrese el valor invertido en su (sus) hijo(s): '))
        return mb.append(-value)
    else: 
        value = 0
        return mb.append(value)


def ask_for_couple(mb):
    couple = input('Tiene usted pareja? S/N')
    if couple == 'S':
        value = float(input('Ingrese el valor invertido en su pareja: '))
        return mb.append(-value)
    else: 
        value = 0
        return mb.append(value)


def ask_for_entrepreneurship(mb):
    entrepreneurship = input('Tiene usted algún emprendimiento? S/N')
    if entrepreneurship == 'S':
        value = float(input('Ingrese el valor generado por la empresa: '))
        return mb.append(value)
    else: 
        value = 0
        return mb.append(value)


def ask_for_inheritance(mb):
    inheritance = input('Ha recibido usted alguna herencia? S/N')
    if inheritance == 'S':
        value = float(input('Ingrese el valor heredado: '))
        return mb.append(value)
    else: 
        value = 0
        return mb.append(value)


def ask_for_allowance(mb):
    allowance = float(input('Ingrese la mesada asignada por sus padres ')) 
    return mb.append(allowance)


def ask_for_gifts(mb):
    gifts = input('Ha recibido usted algun regalo? S/N')
    if gifts == 'S':
        value = float(input('Ingrese el valor del regalo: '))
        return mb.append(value)
    else: 
        value = 0
        return mb.append(value)
    

def ask_for_close():
    close = input('O pulse X para salir')
    return False