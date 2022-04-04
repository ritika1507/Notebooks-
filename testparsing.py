import sys
import re

def read_file():
    with open(sys.argv[1] , 'r' , encoding= 'utf-8') as file:
        myfile = file.read()

    return myfile



def parse_currency(file):
    curr = re.findall(r"([$₹£][0-9]+\.?[0-9]*\,?\d+(?=\s|$))", file)
    if curr == []:
        print('\nNo currency')
        return

    print("\nCurrencies in the file: " + str(curr))

    return


def parse_date_time(file):


    #ddmmyyyy
    date_type1 = re.findall(r'\b(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[012])\/([0-2]\d{3})\b', file)


    #ddmmyy
    date_type2 = re.findall(r'\b(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[012])\/(\d{2})\b' , file)


    #mmddyyyy
    date_type3 = re.findall(r"\b(0[1-9]|1[012])\/(0[1-9]|[12][0-9]|3[01])\/([0-2]\d{3})\b", file)


    #mmddyy
    date_type4 = re.findall(r"\b(0[1-9]|1[012])\/(0[1-9]|[12][0-9]|3[01])\/(\d{2})\b", file)


    if date_type1 == [] and date_type2 == [] and date_type3 == [] and date_type4 == []:
        print('\nNo dates')

    print('\nDates in the file: ')

    for date in date_type1:
        print(date)

    for date in date_type2:
        print(date)

    for date in date_type3:
        print(date)

    for date in date_type4:
        print(date)


def parse_vowels(file):
    reqd_words = re.findall(r"(\b[aeiouAEIOU]\w{3})(?![A-Za-z0-9])" , file)
    if reqd_words == []:
        print("\nNo four letter words starting with a vowel")
        return

    print("\nFour letter words starting with a vowel are :" + str(reqd_words))


def parse_cardinality(file):
    order_type1 = re.findall(r"\b([0-9]+(st|nd|th|rd))\b" , file)
    order_type2 = re.findall(r"\b(first|second|thir(d|teenth|tieth)|four(th|teenth|tieth)|fif(th|teenth|tieth)|six(th|teenth|tieth)|seven(th|teenth|tieth)|eight(th|teenth|ieth)|nin(th|eteenth|tieth)|hundredth|thousandth)\b", file)

    if order_type1 == [] and order_type2 == []:
        print("\nNo order words in file")
        return



    print('\nOrder words in file:')

    for order in order_type1:
        print(order[0])

    for order in order_type2:
       print(order[0])




if __name__ == '__main__':
    file = read_file()

    print("File contents:")
    print(format(file))

    parse_currency(file)
    parse_date_time(file)
    parse_vowels(file)
    parse_cardinality(file)