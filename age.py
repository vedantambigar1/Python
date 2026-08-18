from datetime import datetime

user_input = (input("enter your birth_year YYYY-MM-DD:"))

birth_year = datetime.strptime(user_input,"%Y-%m-%d").date()
today = datetime.today().date()
age = today.year - birth_year.year - ((today.month, today.month) < (birth_year.month, birth_year.day))
print(f"you are {age} years old.")