import xlrd


book = xlrd.open_workbook('city_data.xlsx')

sheet = book.sheet_by_index(0)

main_data_list = []

score = 10

for row in range(3, sheet.nrows):

    temp_dict = {}

    print(sheet.row_values(row))

    sheet_value = sheet.row_values(row)

    temp_dict['city'] = sheet_value[0]
    temp_dict['gdp'] = sheet_value[1]
    temp_dict['people'] = sheet_value[2]
    temp_dict['price'] = sheet_value[3]
    temp_dict['salary'] = sheet_value[4]
    temp_dict['underground'] = sheet_value[5]
    temp_dict['school'] = sheet_value[6]
    temp_dict['hospi'] = sheet_value[7]
    temp_dict['students'] = sheet_value[8]
    temp_dict['score'] = score
    temp_dict['pr/sa'] = format(sheet_value[3] / sheet_value[4], '.2f')

    score -= 1

    main_data_list.append(temp_dict)


print(main_data_list)


# 将每个城市按照10条数据分别进行排名，除房价外，排名第一得10分，排名最后得1分
def desc_cities(cities_list, kw='2019GDP'): 
    if kw != 'price':
        cities_bykey = sorted(cities_list, key=lambda x:x.get(kw), reverse=True)

        for i in range(len(cities_bykey)):
            cities_list[i]['score'] += (len(cities_bykey) - i)
    else:
        cities_bykey = sorted(cities_list, key=lambda x:x.get(kw), reverse=False)

        for i in range(len(cities_bykey)):
            cities_list[i]['score'] += (i + 1)

    return 0


def print_res(cities_list):
    cities_byscore = sorted(cities_list, key=lambda x:x.get('score'), reverse=True)

    for i in range(len(cities_byscore)):
        print('第' + str(i+1) + '名')
        print(cities_byscore[i]['city'], cities_byscore[i]['score'])

        print('-'*10)

if __name__=='__main__':
    for key in main_data_list[0].keys():
        desc_cities(main_data_list, key)

    print_res(main_data_list)
 


    


