from django.shortcuts import render,redirect,get_object_or_404
# from .models import department
from django.contrib import messages
from .form import ReportForm
from RepairReportMaker.models import Report


# Create your views here.
def index(request):
    all_report = Report.objects.all().order_by('-Date').values()
    if request.method == "POST":
        Topic = request.POST.get("Topic")
        User = request.POST.get("User")
        Department = request.POST.get("Department")
        Computer_Equipment = request.POST.get("Computer_Equipment")
        Details = request.POST.get("Details")
        report = Report.objects.create(
            Topic = Topic,
            Department = Department,
            User = User,
            Computer_Equipment = Computer_Equipment,
            Details = Details 
        )
        # return HttpResponse("<h1> แบบฟอร์มบันทึกข้อมูล </H1>")
        messages.success(request, 'บันทึกข้อมูลเรียบร้อยแล้ว!')
        return render(request,"index.html",{"all_report":all_report})
    else:
        
        return render(request,"index.html",{"all_report":all_report})
def about(request):
    return render(request,"about.html")

def admin_index(request):
    all_report = Report.objects.all().order_by('-Date').values()
    return render(request,"Admin_index.html",{"all_report":all_report})

def admin_edit(request):
    all_report = Report.objects.all()
    
    return render(request,"Admin_edit.html",{"all_report":all_report})

def admin_form(request):
    if request.method == "POST":
        Topic = request.POST.get("Topic")
        User = request.POST.get("User")
        Department = request.POST.get("Department")
        Computer_Equipment = request.POST.get("Computer_Equipment")
        Details = request.POST.get("Details")
        report = Report.objects.create(
            Topic = Topic,
            Department = Department,
            User = User,
            Computer_Equipment = Computer_Equipment,
            Details = Details 
        )
        messages.success(request, 'บันทึกข้อมูลเรียบร้อยแล้ว!')
        return redirect("/admin_index")
    else:
        return render(request,'Admin_form.html')
    
# def edit_department(request,pk):
#     Department = get_object_or_404(department,pk=pk)
#     if request.method == "POST":
#         form = DepartmentForm(request.POST , instance=Department)
#         if form.is_valid():
#             form.save()
#             return redirect("/admin_index")
#     else:
#         form = DepartmentForm(instance=Department)
#     return render(request,'Admin_edit_department.html',{'form':form, 'Department':Department,})

# def del_department(request,pk):
#     Department = get_object_or_404(department,pk=pk)
#     Department.delete()
#     return redirect("/admin_index")

def edit_report(request,pk):
    report = get_object_or_404(Report,pk=pk)
    if request.method == "POST":
        form = ReportForm(request.POST , instance=report)
        if form.is_valid():
            form.save()
            messages.success(request, 'บันทึกข้อมูลเรียบร้อยแล้ว!')
            return redirect("/admin_index")
    else:
        form = ReportForm(instance=report)
    return render(request,'Admin_edit_Report.html',{'form':form, 'Report':report})

def del_report(request,pk):
    report = get_object_or_404(Report,pk=pk)
    report.delete()
    messages.success(request, 'ลบข้อมูลเรียบร้อยแล้ว!')
    return redirect("/admin_index")
