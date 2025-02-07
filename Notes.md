 
 Create Virtual Env -------------

 python -m venv .venv  

To Activate --------------->

.venv\Scripts\activate


Install Django ------- ----->

pip install django

python.exe -m pip install --upgrade pip

Freeze Pip ----------->

pip freeze > requirement.txt

Create Project ----------->

django-admin startproject twiterClone

16 : 09

To Run Server ----------->

 python manage.py runserver



To make Migration ----------->

python manage.py makemigrations

python manage.py migrate



To Create Admin / Super User --------->

python manage.py createsuperuser

User Name :  Rmohit
rmohit21264@gmail.com
Password : Rmohit@21
Rmohit@21


To Use Image Field Need Pillow Lib ---------->

python -m pip install Pillow


Add Static And Media to Settings and Url


Media_URL = '/media/'
Media_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

Add App ----------->

python manage.py startapp tweet









