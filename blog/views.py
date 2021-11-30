from django.shortcuts import render, redirect 

from django.http import HttpResponse
from .forms import StudentRegistration 
from .models import Student
from django.http import HttpResponseRedirect 
'''
def function1(request): # this is the object of HttpResponse
	data = "<html> <body> <h1> Hello All </h1> </body> </html>"
	return HttpResponse(data)


def function2(request): # this is the object of HttpResponse
	data = "<html> <body> <h1> Home Page </h1> </body> </html>"
	return HttpResponse(data)

# Create your views here.
'''

def home(request): # this is the object of HttpResponse
	
	return render(request, 'blog/home.html', {'title': 'Batch1'})



posts = [{'author': 'Munesh', 
         'title': 'solar energy', 
         'content':'Renewable energy source', 
         'date1': 'July 22, 2021'},

         {'author': 'joel', 
         'title': 'Health', 
         'content':'Health is wealth', 
         'date1': 'July 21, 2021'},

          ]


def all_post(request):
	context = { 'posts' : posts }
	return render(request, 'blog/all_posts.html', context)


#def showformdata(request):
#	fm = StudentRegistration()
#	return render(request, 'blog/register.html', {'form':fm})

def thankyou(request):
	return render(request, 'blog/success.html')

def showformdata(request):
	if request.method== 'POST':
		fm = StudentRegistration(request.POST)
		if fm.is_valid():
			print ("form validated ")
			fmdict=fm.cleaned_data
			print ("Name:", fm.cleaned_data.items())
			fm_model=Student(stuid=fmdict.get('stuid'), stuname= fmdict.get('stuname'), stupass=fmdict.get('stupass'), stmail=fmdict.get('stmail') )
			fm_model.save()
			#return render(request, 'blog/success.html', {'name': fmdict.get('stuid')} )
			return redirect('dis-success')
	
	else:
		fm = StudentRegistration()
	return render(request, 'blog/register.html', {'form':fm})