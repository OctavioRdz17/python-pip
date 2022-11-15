import csv

def read_csv(path):
    with open(path,'r') as csvfile: # abre el archivo
        reader = csv.reader(csvfile,delimiter=',') # del import para leer csv

        # con la primera iteracion sacamos los keys del dict
        header = next(reader) 

        data = [] # creamos el diccionario a devolver
        # recorremos la lista con la info y le hacemos zip a tuplas con zip
        for row in reader:
            #se junta la clave con la info del row con un zip
            iterable = zip(header,row)
            # por cada row se crea un diccionario con todos los datos
            dict_country = {key:value for key, value in iterable}
            # se le hace append a una list que devuelva toda la data
            data.append(dict_country)
            # print(country)
        return data

if __name__ == '__main__':
    data = read_csv('./data.csv')
    print(data[0]) #devuelve el primer elemento
