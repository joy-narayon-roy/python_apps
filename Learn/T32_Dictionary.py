#If is a object

studentsId={
    101:"Joy",
    "102":"Narayon",
    103:"Roy"
}
print(studentsId[101])
print(studentsId["102"])
print(studentsId.get(103))
print(studentsId.get("201","Not found 201"))