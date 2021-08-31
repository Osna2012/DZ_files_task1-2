from pprint import pprint
# открытие файла и создания словаря
cookbook = {}
grocery_list = []
count = 0     
with open('file.txt', encoding='UTF-8') as file:
    for line in file:
        grocery_list.append(line.strip()) 
while count < len(grocery_list):
    cookbook[grocery_list[count]] = [] 
    key = grocery_list[count]
    for i in range(int(grocery_list[count+1])):
        ing = grocery_list[count+2].strip().split(' | ')
        cookbook[key].append({'ingredient_name':ing[0],'quantity':ing[1],'measure':ing[2]})
        count = count + 1 
    count = count + 3   

#функция для подсчета кол-ва продуктов на кол-во персон
def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    cook_for_person = {}
    for dish in dishes:
        cook_for_person[dish] = cookbook[dish]

    for values in cook_for_person.values():
        for value in values:
            ing = value.get('ingredient_name')
            quantity = int(value.get('quantity')) * person_count
            measure = value.get('measure')
            if ing is not None:
                if ing not in result:
                    result[ing] = {'quantity':quantity, 'measure':measure}
                    
                else:
                    result[ing]['quantity'] = int(result[ing]['quantity']) + quantity

    for i, j in result.items():
        print(i,j)
                

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)