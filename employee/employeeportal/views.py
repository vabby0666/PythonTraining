import csv
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from models import AddEmployee
from django.views.decorators.csrf import csrf_exempt
import io
from django.http import HttpResponseRedirect,HttpResponse
from django.core.validators import email_re
from time import sleep
from django.db.models import Q


@csrf_exempt
def showTable(request):
	table = AddEmployee.objects.all()
	context={'table':table}
	return render(request,'jsonex.html', context)

@csrf_exempt
def add(request):
	if request.is_ajax():
		username = request.POST.get('username')
		emailId = request.POST.get('emailId')
		mobileNumber=request.POST.get('mobileNumber')
		saving=AddEmployee(username=username,emailId=emailId,mobileNumber=mobileNumber)
		if(saving.save()):
			return HttpResponse(200)
	return render(request, 'failed.html')

@csrf_exempt
def objectDelete(request, item_id):
	if request.is_ajax():
		object = get_object_or_404(AddEmployee, pk=item_id)
		object.delete()
		return HttpResponse(200)
	return render(request, 'failed.html')

def objectUpdate(request, item_id):
	a = AddEmployee.objects.get(id=item_id)
	context={'username':a.username,'emailId':a.emailId,'mobileNumber':a.mobileNumber}
	return render(request,'update.html',context)

@csrf_exempt
def update(request):
	if request.is_ajax():
		AddEmployee.objects.filter(emailId = request.POST.get('updemailId')).update(username = request.POST.get('updusername'), mobileNumber= request.POST.get('updmobileNumber'))
		return HttpResponse(200)
	return redirect("/employee/")



def upload(request):
	error = ""
	success=""
	try:
		csv_file = request.FILES['file']
		data_set = csv_file.read().decode('utf-8')
		io_string = io.StringIO(data_set)
		next(io_string)
		i = 0
		for column in csv.reader(io_string, delimiter=','):
				i += 1
				name = column[0]
				emailId = column[1]
				mobile = column[2]

				def emailcheck(e):
					if email_re.match(e):
						return True
					return False

				if mobile.isdigit() and not name.isdigit() and emailcheck(emailId) and len(mobile) == 10:
					try:
						created = AddEmployee(username=name, emailId=emailId, mobileNumber=mobile)
						created.save()
						error+="<br/>row-"+str(i)+":added to database."
						success+="<br/>row-"+str(i)+":added to database."

					except:
						error += "<br/> row-" + str(i) + ": email already exists: " + emailId
				else:
					error += "<br/> row-" + str(i) + ": Not a valid data"
		if (error == success):
			error = "Upload Successful!!"
	except:
		messages.error(request, "No file selected!!")

	messages.error(request, error)
	sleep(0.2)
	return HttpResponseRedirect("/employee/")


def objectSearch(request):
	sitem=request.GET['searchdata']
	table = AddEmployee.objects.filter( Q(username__contains=sitem) | Q(emailId__contains=sitem) | Q(mobileNumber__contains=sitem))
	context1 = {'table': table , 'sitem': sitem}
	return render(request, 'searcheddata.html',context1)