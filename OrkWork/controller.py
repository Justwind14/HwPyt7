import view
import import_date
import export_date

def main_func():
    request = view.choise()
    test_list = list(request[0].split())
    if 1 == request[1]:      
        if (len(test_list) == 4):
            import_date.write_date(test_list)
        else:
            print('введены некорректные данные')

    else:
        view.out_put(export_date.exp(test_list))
            
