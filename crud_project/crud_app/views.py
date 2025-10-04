from django.shortcuts import render

# Create your views here.
from .models import Student
from .forms import StudentForm


def student_list(request):
    students = Student.objects.all()
    query = request.GET.get('q')
    if query:
        students = students.filter(name__icontains = query)
    return render(request, 'student_list.html',{'students': students})


def student_create(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'student_form.html',{'form':form})


def student_update(request):
    student = get_object_or_404(Student, id = id)
    form = StudentForm(request.POST or None, instance = student)
    if form.is_valid():
        form.save()
        return redirect('studnet_list')
    return render(request, 'student_form.html',{'form':form})

def student_delete(request,id):
    student = get_object_or_404(Student, id = id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_form.html')
    return render(request,'student_confirm_delete.html',{'student':student})
