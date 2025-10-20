from django.shortcuts import render

def login(request):   
    
    context: dict[str, str] = {
        'title': 'Home - Авторизація',        
    }
    return render(request, 'users/login.html', context)


def registration(request):   
    
    context: dict[str, str] = {
        'title': 'Home - Реєстрація',        
    }
    return render(request, 'users/registration.html', context)


def profile(request):   
    
    context: dict[str, str] = {
        'title': 'Home - Кабінет',        
    }
    return render(request, 'users/profile.html', context)


def logout(request):   
    
    context: dict[str, str] = {
        'title': 'Home - Вихід', 
    }
    return render(request, '', context)