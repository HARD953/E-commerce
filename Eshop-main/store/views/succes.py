from django.shortcuts import render

def success(request):
    name = request.POST.get('cpm_trans_id')
    print(name)