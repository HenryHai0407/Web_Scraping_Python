str="""
name,age,address,gender,mark,class,teacher
Le Hoang,20,Ha Noi,M,10,A2,Alice
Nguyen Ngoc Quynh,26,Ho Chi Minh,F,6,A1,Alice
Tran Minh Tuan,21,Ha Noi,M,9,A3,Alice
Nguyen Bao Hoang,23,Ho Chi Minh,M,8,A1,Mark
Le Van Do,27,Ha Noi,M,9,A6,Alice
Do Tan,19,Ha Noi,M,7,A7,Mark&Alice
Tran Le Nguyen Anh,22,Ho Chi Minh,F,9,A5,Ben
Le Ngoc,20,Ha Noi,M,10,A2,Alice
Le Lan,20,Ha Noi,M,10,A2,Mark
Le Long,20,Ha Noi,M,10,A2,Alice
Pham The Hien,26,Ho Chi Minh,F,5,A3,Alice
"""

def get_last_first_name(name):
    # Le Hoang
    last_name = name
    first_name = name
    first_space_index = name.find(" ")
    if first_space_index != -1:
        last_name = name[:first_space_index].strip().upper()
        first_name = name[first_space_index+1:].strip().title()
    return last_name, first_name


def get_sv_info(sv_str):
    sv_str = sv_str.strip()
    sv_str_list = sv_str.split(",")
    full_name = sv_str_list[0].strip()
    last_name, first_name = get_last_first_name(full_name)
    return {
        "name": full_name
        ,"age": int(sv_str_list[1].strip())
        ,"address": sv_str_list[2].strip()
        ,"gender": sv_str_list[3].strip()
        ,"mark": int(sv_str_list[4].strip())
        ,"class": sv_str_list[5].strip()
        ,"teacher": sv_str_list[6].strip()
        ,"last_name": last_name
        ,"first_name": first_name
    }

def get_sv_info_from_str():
    str_list = str.strip().splitlines()
    sv_list = []
    index = 0
    for sv_str in str_list:
        if index > 0:
            sv = get_sv_info(sv_str)
            sv_list.append(sv)
        index += 1
    print(sv_list)


if __name__ == "__main__":
    get_sv_info_from_str()