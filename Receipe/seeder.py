from faker import Faker
from django.conf import settings
import random
from Receipe.models import Student, StudentID, Department,StudentMarks,Subject

fake = Faker()

def create_sub_marks(n=100)->True:
    try:
            Student_objs  = Student.objects.all()
            for student in Student_objs:
                subjects = Subject.objects.all()
                for subject in subjects:
                     StudentMarks.objects.create(
                          subject =  subject,
                          student = student,
                          marks = random.randint(0,100)
                     )
    except Exception as e:
        print(e)

def seed_db(n=10) -> None:
    try:
        for _ in range(0, n):
            departments_obj_id = Department.objects.all()
            random_index = random.randint(0, len(departments_obj_id) - 1)
            student_id = f'STU-0{random.randint(100, 999)}'
            department = departments_obj_id[random_index]
            student_name = fake.name()
            student_age = random.randint(20, 30)
            student_email = fake.email()
            student_address = fake.address()

            student_id_obj = StudentID.objects.create(student_id=student_id)
            student_id_obj.save()
            Student.objects.create(
                student_id=student_id_obj,
                department=department,
                student_name=student_name,
                student_age=student_age,
                student_email=student_email,
                student_address=student_address
            )
    except Exception as e:
        print(e)