# 0 - 4 años cero  
# 5 - 18 años mesada, regalos, herencia  
# 19 - 63 años salario, emprendimiento, herencia, regalos, pareja, hijos, deudas
# 64 - 80 años emprendimiento, herencia, regalos, pensión, deudas, pareja 
# allowance = mesada
import questions as q
import life_money as lf

money_bag = []

if __name__ == '__main__':
    finished = True
    while finished: 
        int_age = int(input('Ingrese su edad actual en años: '))  
        child = range(5)
        teenager = range(5, 19)
        adult = range(19, 64)
        old_age = range(64, 81)

        if int_age in child:
            money_bag.append(0)
            print(money_bag)
            print('Usted es un bebé y no maneja dinero!')
        elif int_age in teenager:
            q.ask_for_inheritance(money_bag)
            q.ask_for_allowance(money_bag)
            q.ask_for_gifts(money_bag)
            print(money_bag)
            print(lf.life_money_calc(int_age, money_bag))
            print('La cantidad de dinero que usted tiene es', lf.life_money_calc(int_age, money_bag))

        elif int_age in adult:
            q.ask_for_inheritance(money_bag)
            q.ask_for_gifts(money_bag)
            q.ask_for_salary(money_bag)
            q.ask_for_entrepreneurship(money_bag)
            q.ask_for_couple(money_bag)
            q.ask_for_children(money_bag)
            q.ask_for_debt(money_bag)
            print(money_bag)
            print('La cantidad de dinero que usted tiene es', lf.life_money_calc(int_age, money_bag))
            
        elif int_age in old_age:
            q.ask_for_inheritance(money_bag)
            q.ask_for_gifts(money_bag)
            q.ask_for_entrepreneurship(money_bag)
            q.ask_for_couple(money_bag)
            q.ask_for_debt(money_bag)
            print(money_bag)
            print('La cantidad de dinero que usted tiene es', lf.life_money_calc(int_age, money_bag))
        
        else:
            print('Usted ya ha fallecido :(')
            print('Cerrrando el programa')
            finished = False          
