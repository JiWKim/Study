##p.223 q46
#InsertingName

f3=open("Names.txt", 'r')
f3_data=f3.read()
f3_data_list=f3_data.split("\n")

new_name=input("Enter a name: ")

for name in f3_data_list:
      if name.upper()==new_name.upper():
            break
      elif name.upper()>new_name.upper():
            new_index=f3_data_list.index(name)
            f3_data_list.insert(new_index, new_name)
            break
      elif ((new_name.upper()>name.upper()) & (name==f3_data_list[-1])):
            f3_data_list.insert(len(f3_data_list), new_name)

f3.close()


f3_write=open("Names.txt", 'w')
for names in f3_data_list:
      f3_write.write(names)
      f3_write.write("\n")
f3_write.close()      
