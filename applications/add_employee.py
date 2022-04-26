# INSERT SQL statement to insert a new row into animal table.
INSERT_EMPLOYEE = """
    INSERT INTO employees VALUES('{email}', '{first_name}', '{last_name}', '{dob}', '{state}', '{city}', '{hire_date}', {salary})
"""

INSERT_PERFORMER = """
    INSERT INTO performers VALUES('{email2}','{specialty}', {weight}, {height})
"""

INSERT_ANIMAL_TRAINER = """
    INSERT INTO animal_trainers VALUES('{email3}', '{animal_specialty}', {training_certification}, {max_animals})
"""

INSERT_CHOREOGRAPHER = """
    INSERT INTO choreographers VALUES('{email4}', '{performance_expertise}', {number_of_performances}, {years_in_industry})
"""
    
# Add an employee (with no specialization)
def add_employee(args):
    email = args['email'] # email is a primary key, it must be entered.
    first_name = args['first_name'] # First name is not null, it must be entered.
    hire_date = args['hire_date'] # Hire date is not null, it must be entered.
    last_name = "null"
    dob = "null"
    city = "null"
    state = "null"
    salary = "null"

    if args['last_name'] != '':
        last_name = args['last_name']
    if args['dob'] != '':
        dob = args['dob']
    if args['city'] != '':
        city = args['city']
    if args['state'] != '':
        state = args['state'] 
    if args['salary'] != '':
        salary = args['salary']

    add_employee = INSERT_EMPLOYEE.format(email = email, first_name = first_name, last_name = last_name, dob = dob, city = city, state = state, hire_date = hire_date, salary = salary)
    return add_employee
    
# Add a performer (ISA employee)
def add_performer(args):
    email = args['email'] # email is a primary key, it must be entered.
    first_name = args['first_name'] # First name is not null, it must be entered.
    hire_date = args['hire_date'] # Hire date is not null, it must be entered.
    last_name = "null"
    dob = "null"
    city = "null"
    state = "null"
    salary = "null"
    specialty = "null"
    weight = "null"
    height = "null"

    if args['last_name'] != '':
        last_name = args['last_name']
    if args['dob'] != '':
        dob = args['dob']
    if args['city'] != '':
        city = args['city']
    if args['state'] != '':
        state = args['state'] 
    if args['salary'] != '':
        salary = args['salary']
    if args['specialty'] != '':
        specialty = args['specialty']
    if args['weight'] != '':
        weight = args['weight'] 
    if args['height'] != '':
        height = args['height']
    add_employee = INSERT_EMPLOYEE.format(email=email, first_name=first_name, last_name=last_name, dob=dob, city=city, state=state, hire_date=hire_date, salary=salary)
    add_performer = INSERT_PERFORMER.format(email2=email, specialty=specialty, weight=weight, height=height)
    return (add_employee, add_performer)

# Add an animal trainer (ISA performer)
def add_animal_trainer(args):
    email = args['email'] # email is a primary key, it must be entered.
    first_name = args['first_name'] # First name is not null, it must be entered.
    hire_date = args['hire_date'] # Hire date is not null, it must be entered.
    last_name = "null"
    dob = "null"
    city = "null"
    state = "null"
    salary = "null"
    specialty = "null"
    weight = "null"
    height = "null"
    animal_specialty = "null"
    training_certification = "null"
    max_animals = "null"

    if args['last_name'] != '':
        last_name = args['last_name']
    if args['dob'] != '':
        dob = args['dob']
    if args['city'] != '':
        city = args['city']
    if args['state'] != '':
        state = args['state'] 
    if args['salary'] != '':
        salary = args['salary']
    if args['specialty'] != '':
        specialty = args['specialty']
    if args['weight'] != '':
        weight = args['weight'] 
    if args['height'] != '':
        height = args['height']
    if args['animal_specialty'] != '':
        animal_specialty = args['animal_specialty']
    if args['training_certification'] != '':
        training_certification = args['training_certification'] 
    if args['max_animals'] != '':
        max_animals = args['max_animals']

    add_employee = INSERT_EMPLOYEE.format(email=email, first_name=first_name, last_name=last_name, dob=dob, city=city, state=state, hire_date=hire_date, salary=salary)
    add_performer = INSERT_PERFORMER.format(email2=email, specialty=specialty, weight=weight, height=height)
    add_animal_trainer = INSERT_ANIMAL_TRAINER.format(email3 = email, animal_specialty = animal_specialty, training_certification = training_certification, max_animals = max_animals)
    return (add_employee, add_performer, add_animal_trainer)

# Add a choreographer (ISA employee)
def add_choreographer(args):
    email = args['email'] # email is a primary key, it must be entered.
    first_name = args['first_name'] # First name is not null, it must be entered.
    hire_date = args['hire_date'] # Hire date is not null, it must be entered.
    last_name = "null"
    dob = "null"
    city = "null"
    state = "null"
    salary = "null"
    performance_expertise = "null"
    number_of_performances = "null"
    years_in_industry = "null"

    if args['last_name'] != '':
        last_name = args['last_name']
    if args['dob'] != '':
        dob = args['dob']
    if args['city'] != '':
        city = args['city']
    if args['state'] != '':
        state = args['state'] 
    if args['salary'] != '':
        salary = args['salary']
    if args['performance_expertise'] != '':
        performance_expertise = args['performance_expertise']
    if args['number_of_performances'] != '':
        number_of_performances = args['number_of_performances'] 
    if args['years_in_industry'] != '':
        years_in_industry = args['years_in_industry']

    add_employee = INSERT_EMPLOYEE.format(email=email, first_name=first_name, last_name=last_name, dob=dob, city=city, state=state, hire_date=hire_date, salary=salary)
    add_choreographer = INSERT_CHOREOGRAPHER.format(email4 = email, performance_expertise = performance_expertise, number_of_performances = number_of_performances, years_in_industry = years_in_industry)
    return (add_employee, add_choreographer)