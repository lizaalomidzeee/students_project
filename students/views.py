from django.shortcuts import render
import random



def get_random_students():
    first_names = ['Alex', 'Maria', 'John', 'Sophia', 'Michael', 'Emma']
    last_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis']

    students = []
    for _ in range(100):
        student = {
            'name': random.choice(first_names),
            'surname': random.choice(last_names),
            'gpa': round(random.uniform(1.0, 4.0), 2),
            'course': random.randint(1, 4)
        }
        students.append(student)
    return students


def main_page_view(request):
    students = get_random_students()
    selected_student = random.choice(students)
    return render(request, 'students/main_page.html', {'student': selected_student})

def students_page_view(request):
    students = get_random_students()
    return render(request, 'students/students_page.html', {'students': students})

def home_view(request):
    return render(request, 'students/main_page.html')
