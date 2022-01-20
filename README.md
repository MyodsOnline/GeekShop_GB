# GeekShop_GeekBrains

Training project on creating an online store on the Django framework  
### To use project your environment pip list must contains:  
Django==3.2.9.   
Pillow==8.4.0.    
django-environ==0.8.1   
requests==2.27.1   
social-auth-app-django==5.0.0

You can install it from requirements.txt using: pip install requirements.txt. 

### To see the project abilities please make sure you have done:

python manage.py makemigrations  
python manage.py migrate  

### To load some data in database:  
1. python manage.py createsuperuser  
2. python manage.py loaddata products/fixtures/categories.json
3. python manage.py loaddata products/fixtures/products.json
4. python manage.py loaddata mainapp/fixtures/promo.json
5. python manage.py update_db

