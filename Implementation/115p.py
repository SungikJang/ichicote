loc = str(input())
i = int(loc[1])
alph = loc[0]
if (alph == "a"):
    loc_num = 10 + i
if (alph == "b"):
    loc_num = 20 + i
if (alph == "c"):
    loc_num = 30 + i
if (alph == "d"):
    loc_num = 40 + i
if (alph == "e"):
    loc_num = 50 + i
if (alph == "f"):
    loc_num = 60 + i
if (alph == "g"):
    loc_num = 70 + i
if (alph == "h"):
    loc_num = 80 + i

count = 0
def is_good(fin_loc):
    if fin_loc // 10 == 0:
        return False
    if (fin_loc % 10 == 9) | (fin_loc % 10 == 0):
        return False
    if fin_loc // 90 != 0:
        return False
    else:
        return True





if is_good(loc_num + 21) == True:
    count += 1
if is_good(loc_num + 19) == True:
    count += 1
if is_good(loc_num + 12) == True:
    count += 1
if is_good(loc_num + 8) == True:
    count += 1
if is_good(loc_num - 21) == True:
    count += 1
if is_good(loc_num - 19) == True:
    count += 1
if is_good(loc_num - 12) == True:
    count += 1
if is_good(loc_num - 8) == True:
    count += 1

print(count)


#풀긴풀음
# 내풀이가 뭔가 더 직관적이고 1차원적인듯
#
