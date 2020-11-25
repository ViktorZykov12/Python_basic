goods = [] #Создаем структуру данных Товары
features = {'название': '', 'цена': '', 'количество': '', 'единица измерения': ''} #названия значений
analitics = {'название': [], 'цена': [], 'количество': [], 'единица измерения': []} #поидет в значение
num = 0 #переменная для выбора позиции в структуре данных товары
while True:
    if input('Выход - Q, \nЛюбая клавиша - продолжить: ').upper() == 'Q': #upper для случая если нажмут маленькую q и если введеное значение == q то break
        break
    num += 1
    for f in features.keys(): #для f передаем значение ключей списка features поочередно
        user_data = input(f'{f}: ') #пользователь вводит Название для первого прохода цикла
        features[f] = int(user_data) if (f == 'цена' or f == 'количество') else user_data #условие при котором определяем тип переменной, int если ключ == цена или количество в остальных случаях str
        analitics[f].append(features[f]) #добавляем введенное пользователем название товара в аналитический список
    goods.append((num, features.copy())) #добавляем на num соответственно первую позицию название
    #возвращаемся в начало условия for для заполнения цены количества ед измерения
    print('Текущая аналитика по товарам:\n')

    for key, value in analitics.items(): # для ключа и значения используем элементы словаля (пара ключ, значение) из списка аналитик
        print(key, value) #выводим на экран

    # и по новое предлагам повторить цикл while
