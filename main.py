# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#Reads file from path and returns the content
def get_file_contents(path):
    file = open(path, 'r')
    content = file.read()
    file.close()
    return content

# parse the first n lines in str and returns dict count of rejected, pos, and neg samples
def parse_n(str, n):
    count_dict = {
        "rej": 0,
        "pos": 0,
        "neg":0
    }
    samples = str.splitlines()
    for i in range(n):
        if samples[i] == '-1':
            count_dict['rej'] += 1
        elif samples[i] == '1':
            count_dict['pos'] += 1
        elif samples[i] == '2':
            count_dict['neg'] += 1

    return count_dict


def main():
    content = get_file_contents('./rs_1.csv')
    print(parse_n(content,21424))



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
