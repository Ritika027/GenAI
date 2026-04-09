#we need to create a dictionary and store a student name
#pydantic khud se smjne ke kosish krta hai ke kya data bheja haii
from pydantic import BaseModel,EmailStr,Field
from typing import Optional


class Student(BaseModel):
    name: str = 'Ritika'
    age: Optional[int] = None
    email: Optional[EmailStr] = None
    cgpa:float = Field(gt=0,lt=10)
    sgpa:float = Field(gt=0,lt=10,default=5,description="Semester Grade Point Average, a measure of a student's academic performance in a specific semester, calculated as the average of the grades obtained in that semester's courses, weighted by the credit hours of each course. It provides insight into a student's performance during that particular semester and is often used for academic evaluations and progress tracking.")
#if no sgpa value given it will automatically take the default value of 5, but if we provide a value for sgpa it will validate it according to the constraints provided (greater than 0 and less than 10) and if the value is not valid it will raise a validation error.
#field constrain of cgpa is greater than 0 and less than 10, if we try to create a student object with cgpa less than or equal to 0 or greater than or equal to 10, it will raise a validation error.

#error because we are passing an integer instead of a string
new_student = {'name':32}

new_student = {'age':'22','email':'abc'}
#error raised because the email is not valid, pydantic is trying to convert the string to an email but it fails because it's not a valid email format
#implicit type conversion kr skta hai pydantic, but it will throw an error if the conversion is not possible(coerce)

new_student = {'age':'22','email':'abc@gmail.com','cgpa':9}


#using pydantic we can provide default values , constraints , descriptions , regex , expressions etc. to the fields in the model, and it will validate the data accordingly. It also provides useful error messages when the validation fails, making it easier to debug and understand what went wrong with the data being passed.

#creating a student object using the dictionary
student = Student(**new_student)

# print(student)
student_json = student.dict()
print(student_json)