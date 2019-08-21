from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from .models import *
import os, sys
import math 


# Create your views here.

def example_get(request, var_a, var_b):
	try:
		var_b = var_b*var_b
		returnob = {
		"data": "%s: %s" %(var_a, var_b),
		}
		return JsonResponse(returnob)
	except Exception as e:
		exc_type, exc_obj, exc_tb = sys.exc_info()
		other = sys.exc_info()[0].__name__
		fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
		errorType = str(exc_type)
		return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})

@csrf_exempt
def example_post(request):
	log = []
	if request.method == "POST":
		try:
			data = request.POST["data"]
			jsob = json.loads(data)
			print(jsob)
			print(type(jsob))
			square = 0 

			sqaured = int(jsob['i1']) * int(jsob['i1'])
			cubed = int(jsob['i1']) * int(jsob['i1'])
			cubed = cubed * int(jsob['i1'])

			return JsonResponse({"number squared":squared})

		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			other = sys.exc_info()[0].__name__
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			errorType = str(exc_type)
			return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
	else:
		return HttpResponse("ONLY POST REQUESTS")



@csrf_exempt
def fib(request):
	jsob = {'startnumber': 0, 'length': 10}
	log = []
	if request.method == "POST":
		try:
			data = request.POST["data"]
			received = json.loads(data)
			jsob.update(received)



			startnumber = int(jsob['startnumber'])
			length = int(jsob['length'])
			loop = range(length)
			numlist = []

			fibnum = startnumber
			addnum = 1

			for l in loop:
				numlist.append(fibnum)
				fibnum = fibnum + addnum
				addnum = fibnum - addnum 

			return JsonResponse({"fib":numlist})

		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			other = sys.exc_info()[0].__name__
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			errorType = str(exc_type)
			return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
	else:
		return HttpResponse("ONLY POST REQUESTS")





@csrf_exempt
def pythag(request):
	jsob = {'sideone': 3, 'sidetwo': 5}
	log = []
	if request.method == "POST":
		try:
			data = request.POST["data"]
			received = json.loads(data)
			jsob.update(received)



			sideone = int(jsob['sideone'])
			sidetwo = int(jsob['sidetwo'])


			side_one_squared = sideone*sideone
			side_two_squared = sidetwo*sidetwo
			sides_added = side_one_squared+side_two_squared
			sidethree = math.sqrt(sides_added)
			 

			return JsonResponse({"sidethree":sidethree})

		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			other = sys.exc_info()[0].__name__
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			errorType = str(exc_type)
			return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
	else:
		return HttpResponse("ONLY POST REQUESTS")