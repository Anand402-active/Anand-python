Name_list=[]
Massage_list=[]
import csv
with open('./Files/contacts.csv','r') as file :
    data=csv.reader(file,delimiter=' ')
    for i in data:
        print(i)
        with open('anand5.txt','a') as new_file :
            new_writer=new_file.write(str(i))
#         name = i[0].split('\t')[0]
#         msg  = i[0].split('\t')[1]
#         Name_list.append(name)
#         Massage_list.append(msg)
#
# print(Name_list)
# print(Massage_list)



