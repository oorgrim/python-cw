
database = []

def new_employee(fullName: str, birth_date, position, salary):
    if not fullName:
        return {"id": -1, "error_desc": "Full Name not specified"}
    if not birth_date:
        return {"id": -1, "error_desc": "Birth Date not specified"}
    if not position:
        return {"id": -1, "error_desc": "Position not specified"}
    if salary <= 0:
        return {"id": -1, "error_desc": "Salary not valid"}
    first_name, last_name = fullName.split(" ", 1)

    newcome = {
        "id": len(database),
        "firstName": first_name,
        "lastName": last_name,
        "birthDate": birth_date ,
        "hiredDate": "yesterday",
        "firedDate": "",
        "position": position,
        "salary": salary
    }
    database.append(newcome)
    return {"id": newcome["id"], "error_desc": ""}

def fire_employee(id: int) -> dict:
    # database[id]
    if not (0 <= id < len(database)):
        return {"id": -1, "errorDesc": "No employee with this id "}
    if database[id]["fireDate"]: #!= " ":
        return {"id": -1, "errorDesc": "Employee already fired"}
    database[id]["fireDate"] = "tomorrow"
    return {"id": id, "errorDesc": ""}

def get_employee_id(full_name: str) -> int:
    try:
        first_name, last_name = full_name.split(" ", 1)            
    except ValueError:
        return -1
    for person in database:
        if first_name


        
    

def get_employee_record(id: str) -> int:
    pass

r1 = new_employee("Марк Марков", "2006-09-13", "просто Марк", 200)
r2 = new_employee("Сабина Кункаева", "2007-08-17", "радистка", 199)
r3 = new_employee("Ибраев Темирлан", "2005-08-30", "столяр", 300)
r4 = new_employee("Вова Новиков", "2009-01-29", "дотер", 190)     
r5 = new_employee("Имен Именов", "2009-01-29", "", 90)     
print(r1)
print(r2)
print(r3)
print(r4)
print(r5)
print(database)