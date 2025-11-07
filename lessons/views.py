from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.


def layout(request):
    return render(request, 'lessons/layout.html')

def lessons1(request):
    return render(request, 'lessons/lesson1.html')

def lessons2(request):
    return render(request, 'lessons/lesson2.html')

#@ oz_book_1 (Я знаю, насколько это не оптимально с точки зрения кода, зато работает здесь и сейчас. Станет проблемой, потом починю. По уму это должна быть автоматика все таки)
def oz_book_1(request):
    return render(request, 'lessons/oz_book_1.html')
def oz_book_2(request):
    return render(request, 'lessons/oz_book_2.html')
def oz_book_3(request):
    return render(request, 'lessons/oz_book_3.html')
def oz_book_4(request):
    return render(request, 'lessons/oz_book_4.html')
def oz_book_5(request):
    return render(request, 'lessons/oz_book_5.html')
def oz_book_6(request):
    return render(request, 'lessons/oz_book_6.html')
def oz_book_7(request):
    return render(request, 'lessons/oz_book_7.html')
def oz_book_8(request):
    return render(request, 'lessons/oz_book_8.html')
def oz_book_9(request):
    return render(request, 'lessons/oz_book_9.html')
def oz_book_10(request):
    return render(request, 'lessons/oz_book_10.html')
def oz_book_11(request):
    return render(request, 'lessons/oz_book_11.html')
def oz_book_12(request):
    return render(request, 'lessons/oz_book_12.html')
def oz_book_13(request):
    return render(request, 'lessons/oz_book_13.html')
def oz_book_14(request):
    return render(request, 'lessons/oz_book_14.html')
def oz_book_15(request):
    return render(request, 'lessons/oz_book_15.html')
def oz_book_16(request):
    return render(request, 'lessons/oz_book_16.html')
def oz_book_17(request):
    return render(request, 'lessons/oz_book_17.html')


#@csrf_exempt
def GetInputValue(request):
  input_value = request.POST['quantity']
  return HttpResponse(input_value)




