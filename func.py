import pandas as pd
import csv


def write_csv(input_list, path):

    with open(path, 'a') as f:
        writer = csv.writer(f)

        writer.writerows([input_list])

def read_csv(path):

    arr = []
    with open(path) as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            arr.append(row)

    return arr





def search(category, key):

    a = []

    data = pd.read_csv('database.csv')

    for i in data[category]:

        a.append(str(i))

    if key in a:

        num = a.index(key)

        return [data['object'][num], 
                data['id'][num], 
                data['img_URL'][num], 
                data['date'][num], 
                data['unit'][num], 
                data['unit_number'][num], 
                data['purchase_number'][num], 
                data['shelf'][num], 
                data['container'][num], 
                data['tag'][num], 
                data['subsidy'][num], 
                data['remark'][num]]

    else:
        return None

def renew_database():

    data_out = []

    name = []

    out = read_csv('data_log.csv')

    headers = out[0]
    data = out[1:]

    for i in data:

        if i[0] not in name:
            name.append(i[0])
            data_out.append(i)

        else:
            index = name.index(i[0])
            data_out[index][6] = int(data_out[index][6]) + int(i[6])

    with open('database.csv', 'w') as f:

        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(data_out)









if __name__ == '__main__':
    renew_database()
