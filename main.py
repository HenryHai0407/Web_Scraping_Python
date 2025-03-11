from util.common import *
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


def get_last_name_mark_list(str):
    last_name_mark_list = []
    sv_list = get_sv_info_from_str(str)
    last_name_mark = {}
    for sv in sv_list:
        last_name = sv["last_name"]
        mark = sv["mark"]
        if last_name not in last_name_mark:
            last_name_mark[last_name] = []
        last_name_mark[last_name].append(mark)
  # print(last_name_mark)

    last_name_mark_avg = {}
    for k,v in last_name_mark.items():
        last_name_mark_avg[k] = get_avg_mark(v)
  # print(last_name_mark_avg)

    max_avg_mark = max(last_name_mark_avg.values())
    
    for k,v in last_name_mark_avg.items():
        if v == max_avg_mark:
            last_name_mark_list.append(k)
    print(last_name_mark_list)
    return last_name_mark_list     

if __name__ == "__main__":
    get_last_name_mark_list(str)
    pass