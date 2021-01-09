# id_number = input("Please enter your ID number:")


def check_ID_number(id_number):
    if len(str(id_number)) != 11:
        return "ID number must be 11 digits!"
    else:
        if str(id_number)[0] == 0:
            return "First digit can not be 0"
        else:
            sum1 = (
                int(str(id_number))[0]
                + int(str(id_number))[2]
                + int(str(id_number))[4]
                + int(str(id_number))[6]
                + int(str(id_number))[8]
            )
            sum2 = (
                int(str(id_number))[1]
                + int(str(id_number))[3]
                + int(str(id_number))[5]
                + int(str(id_number))[7]
            )
            if ((sum1 * 7) - sum2) % 10 == str(id_number)[9]:
                return "Valid ID number"
            else:
                return "ID number invalid"


print(check_ID_number(10163081426))