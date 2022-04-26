# DEFAULT_FETCH Gives the default information stored in an employee.
DEFAULT_FETCH = """
    SELECT 
        e.email,
        e.first_name,
        e.last_name,
        e.dob,
        e.city,
        e.state,
        e.hire_date
    FROM 
        employees e
    WHERE
        e.email = e.email
""" # Last line is default to true since we need something we can AND with.

# SENSITIVE_FETCH gives all the information in DEFAULT_FETCH, but also include sensitive information
# such as their salary and insurance information.
SENSITIVE_FETCH = """
    SELECT 
        e.email,
        e.first_name,
        e.last_name,
        e.dob,
        e.city,
        e.state,
        e.hire_date,
        e.salary,
        i.renewal_date,
        i.insurance_plan,
        i.cost
    FROM 
        employees e,
        insurance i
    WHERE 
        e.email = i.employee_email
"""

# queryMap stores the potential specifications a user can make about their search.
queryMap = {
    'first_name': " AND e.first_name LIKE '%%{}%%'", # Two % needed to write %
    'last_name': "AND e.last_name LIKE '%%{}%%'",
    'email': " AND e.email LIKE '%%{}%%'",
    'choreographer': """\n INTERSECT \n (SELECT e1.email, e1.first_name, e1.last_name, 
        e1.dob, e1.city, e1.state, e1.hire_date FROM choreographers c1, employees e1 
        WHERE c1.email = e1.email)""",
    'choreographer_sensitive': """\n INTERSECT \n (SELECT e1.email, e1.first_name, 
        e1.last_name, e1.dob, e1.city, e1.state, e1.hire_date, e1.salary, i1.renewal_date, 
        i1.insurance_plan, i1.cost FROM choreographers c1, employees e1, insurance i1 
        WHERE c1.email = e1.email AND i1.employee_email = e1.email)""",
    'animal_trainer': """\n INTERSECT \n (SELECT e2.email, e2.first_name, e2.last_name, 
        e2.dob, e2.city, e2.state, e2.hire_date FROM animal_trainers a1, employees e2 
        WHERE a1.email = e2.email)""",
    'animal_trainer_sensitive': """\n INTERSECT \n (SELECT e3.email, e3.first_name, 
        e3.last_name, e3.dob, e3.city, e3.state, e3.hire_date, e3.salary, i2.renewal_date, 
        i2.insurance_plan, i2.cost FROM animal_trainers a1, employees e3, insurance i2 
        WHERE a1.email = e3.email AND i2.employee_email = e3.email)""",
    'performer': """\n INTERSECT \n (SELECT e4.email, e4.first_name, e4.last_name, 
        e4.dob, e4.city, e4.state, e4.hire_date FROM performers p1, employees e4 
        WHERE p1.email = e4.email)""",
    'performer_sensitive': """\n INTERSECT \n (SELECT e5.email, e5.first_name, 
        e5.last_name, e5.dob, e5.city, e5.state, e5.hire_date, e5.salary, i3.renewal_date, 
        i3.insurance_plan, i3.cost FROM performers p1, employees e5, insurance i3 
        WHERE p1.email = e5.email AND i3.employee_email = e5.email)""",
    'recent_hires': "AND to_char(now(), 'YYYY') = to_char(e.hire_date, 'YYYY')", # Everyone hired in the same year as search
    'sort_by_hire_date': "\n ORDER BY hire_date"

}

# Run whenever a user wants to search for an employee.
def fetch(args):
    if "sensitive_information" not in args:
        query = DEFAULT_FETCH
    else:
        query = SENSITIVE_FETCH

    if 'first_name' in args: # Search by first name
        query += queryMap['first_name'].format(args['first_name'])
    if 'last_name' in args: # Search by last name
        query += queryMap['last_name'].format(args['last_name'])
    if 'email' in args: # Search by email
        query += queryMap['email'].format(args['email'])
    if 'choreographer' in args and "sensitive_information" not in args: # Search only choreographers, not sensitive
        query += queryMap['choreographer']  
    if 'choreographer' in args and "sensitive_information" in args: # Search only choreographers, sensitive
        query += queryMap['choreographer_sensitive']  
    if 'animal_trainer' in args and "sensitive_information" not in args: # Search only animal trainers, not sensitive
        query += queryMap['animal_trainer'] 
    if 'animal_trainer' in args and "sensitive_information" in args: # Search only choreographers, sensitive
        query += queryMap['animal_trainer_sensitive']
    if 'performer' in args and "sensitive_information" not in args: # Search only performers, not sensitive
        query += queryMap['performer']
    if 'performer' in args and "sensitive_information" in args: # Search only performers, sensitive
        query += queryMap['performer_sensitive']
    if 'recent_hires' in args: # Search hires within the same year
        query += queryMap['recent_hires']
    if 'sort_by_hire_date' in args: # Sort by hire date
        query += queryMap['sort_by_hire_date']
    return query