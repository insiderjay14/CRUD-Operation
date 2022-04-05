from django.shortcuts import render
def sample(request):
    print(request)
    if request.method=='POST':
        print(request.POST)
        user=request.POST['username']
        pass1=request.POST['password']
        print(user,pass1)
    return render(request,'sample.html')