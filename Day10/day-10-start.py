# Funcitions with outputs

def format_name(f_name, l_name):

    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f'{formated_f_name} {formated_l_name}'


my_name = format_name("ARUANA", "gARcia")
print(my_name)

# solução sem a função title()

def format_name_2(f_name, l_name):

    lower_f_name = f_name.lower()
    lower_l_name = l_name.lower()

    upper_first_f_name = lower_f_name[0].upper() + lower_f_name[1:]
    upper_first_l_name = lower_l_name[0].upper() + lower_l_name[1:]

    return f'{upper_first_f_name} {upper_first_l_name}'

print(format_name_2("ELEONORA", "ALVes"))