import re

if __name__ == "__main__":
    with open('./data.txt', encoding='utf-8', mode='r') as f_in:
        data = f_in.read()

    # Don't use the following syntax
    # f_in = open('./data.txt', encoding='utf-8', mode='r')
    # data = f_in.read()
    # needs to close the file

    # cleaned = data.replace('\n', '').replace('\t', '')

    cleaned_data = re.sub(r'[\n\t]', '', data)

    data_dict = eval(cleaned_data)
    #print(data_dict.keys())
    #print(data_dict['data'])

    file_contents = "id,title,price\n"

    for k in data_dict:
        if not re.match(r'data_\d', k):
            continue
        v = data_dict[k]
        for each_book in v:
            file_contents += f"\"{each_book['id']}\", \"{each_book['title']}\", \"{each_book['price']}\"\n"

    #print(file_contents)
    file_contents = file_contents.strip('\n')

    with open('clean.csv', encoding='utf-8', mode='w') as f_out:
        f_out.write(file_contents)

