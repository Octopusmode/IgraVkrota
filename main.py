from time import sleep;
import os
done = False;
inv_list = [];
backpack = [];
i = 0;
print('Появился крот. Он готов рыть землю. Нажми любую цифру.');
key = input ('Копать');
while not done:
    import random;
    loot = ["Корень рябины", 'Белый гриб',"Железная руда","Монетка","Подкова","Пластиковый мусор","Камешек"];
    item = random.choice(loot);
    print("Тебе попался(ась):",(item));
    inv = [];
    inv.append(item);
    inv_list.append(item);

    for variant in loot:
        for item in inv_list:
            if variant == item: 
                i = i + 1;
        if i > 0:
            backpack.append(f'{variant} = {str(i)} шт.');
        i = 0;

    print ("В твоей корзине \n",*backpack, sep='\n');

    print('Крот копает...');
    # sleep(1)
    if input('Хочешь копать ещё? (1 - Нет) ') == '1':
            done = True;
    else:
        backpack = []
        os.system('cls||clear');

backpack = [];
for variant in loot:
    for item in inv_list:
        if variant == item: 
            i = i + 1;
    if i > 0:
        backpack.append(f'{variant} = {str(i)} шт.');
    i = 0;

os.system('cls||clear');
print(f'Итак в твоей корзине:');
print(*backpack, sep='\n')