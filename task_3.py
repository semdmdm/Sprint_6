world_champions = {
    2002: 'Бразилия',
    2006: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
}

world_champions[2022] = 'Аргентина'
country = 'Италия'

world_champions_list = (world_champions.keys())
for world_champions_list in world_champions.keys():
    print(world_champions_list, '-', world_champions[world_champions_list])

if country in world_champions.values():
    print(f'{country} cтановилась чемпионом мира по футболу в 21 веке!')
else:
    print(f'{country} не выигрывала чемпионат мира по футболу в 21 веке.')