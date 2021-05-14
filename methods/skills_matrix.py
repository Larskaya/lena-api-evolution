
class Matrix:
    def get_skill_matrix(skill): 
        matrix = {
            '0': { 'eat': 1, 'fight': 1, 'fertile': 1, 'friend': 0, 'hide': -1 }, # движение
            '1': { 'eat': 1, 'fight': 0, 'fertile': 0, 'friend': 1, 'hide': 0 }, # кушать растения
            '2': { 'eat': 0, 'fight': 1, 'fertile': 0, 'friend': 0, 'hide': 0 }, # кушать существ
            '3': { 'eat': 1, 'fight': 0, 'fertile': 0, 'friend': 0, 'hide': 0 }, # быстрый обмен веществ
            '4': { 'eat': 0, 'fight': 0, 'fertile': 0, 'friend': 0, 'hide': 0 }, # крылья/плавники
            '5': { 'eat': -1, 'fight': 0, 'fertile': 0, 'friend': 0, 'hide': 1 }, # прятать запасы (только для кушоющих растения)
            '6': { 'eat': 1, 'fight': 1, 'fertile': 0, 'friend': 0, 'hide': -1 }, # крупный размер
            '7': { 'eat': 0, 'fight': 1, 'fertile': 0, 'friend': 0, 'hide': 0 }, # броня (повышает вес)
            '8': { 'eat': 0, 'fight': 0, 'fertile': 1, 'friend': 1, 'hide': 0 }, # половое размножение (увеличивает количество мутаций)
            '9': { 'eat': 0, 'fight': 0, 'fertile': 0, 'friend': 0, 'hide': 1 }, # впадать в спячку (если еды не хватает)
            '10': { 'eat': 0, 'fight': 1, 'fertile': 1, 'friend': 1, 'hide': -1 }, # стайность (плюс к обороне, минус к плодовитости)
            '11': { 'eat': 0, 'fight': 0, 'fertile': 0, 'friend': 0, 'hide': 0 }, # нервная система для дружбы (пользователь  может предложить дружбу)
            '12': { 'eat': 0, 'fight': 0, 'fertile': 0, 'friend': 0, 'hide': 0 } # нервная система для еды (пользователь может замедлить питание)
        }

        a = matrix[skill]
        return a

