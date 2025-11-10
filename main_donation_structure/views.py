from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.



def layout(request):
    return render(request, 'main_donation_structure/base.html')

def main_donation_structure(request):
    return render(request, 'main_donation_structure/main_text.html')



def GetInputValue(request):
  input_value = request.POST['quantity']
  return HttpResponse(input_value)