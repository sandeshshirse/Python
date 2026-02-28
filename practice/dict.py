dict = {
    "key" : "value"
}


students = {
    "name"    : "Sandesh",
    "id"      : 12,
    "age"     : 20,
    "scores"  : {
        "phy"   : 45,
        "maths" : 64,
        "chem"  : 41
    }
}

print(students["name"])
students["college"] = "ICEM"

print(students)

print(students["scores"]["phy"])     #nested dict


            #dictonary meathods 


print(students.keys())               #to prints the keys of dict

print(list(students.keys()))         #type casting

print(students.items())              #to get the key values pairs

print(students.get("name"))          #to get values by using keys

      
      #get vs without get

print(students["name1"])             # ==> gives error
print(students.get("name1"))         # ==> gives null value


