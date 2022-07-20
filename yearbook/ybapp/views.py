import uuid
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import  Memories, Year, Branch, Comments, Student
from django.contrib.auth import authenticate, login as dj_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from .decorators import allowed_users, unauthenticated_user
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def index(request):                
        if request.method == 'POST':
                search = request.POST.get('search')
                searchx = search.lower()
                students = Student.objects.all()
                passarr=[]
                for s in students:                        
                        sname = s.fname.lower()+' '+s.lname.lower()
                        result = sname.find(searchx)
                        if(result != -1):
                                passarr.append(s)
                return render(request, 'searchr.html', {'stus': passarr})        
        year = Year.objects.all()     
        stu = Student.objects.all()        
        return render(request,'index.html', {'year': year, 'student': stu})


@login_required(login_url='login')
def student(request):
        br = Branch.objects.all()
        return render(request, 'student.html',{'branch': br})

def createyear(request):
        if request.method == 'POST':
                year = Year()
                yearx = request.POST.get('year')
                year.ybyear = yearx
                year.save()
                messages.info(request, 'Year added')
                return redirect('/student')
        return redirect('/student')

def createbranch(request):
        if request.method == 'POST':
                branch = Branch()
                branchx = request.POST.get('branch')
                branch.branch = branchx
                branch.save()
                messages.info(request, 'Branch added')
                return redirect('/student')
        return redirect('/student')

def createstudent(request):
        if request.method == 'POST':                
                username = request.POST.get('username')

                if User.objects.filter(username = username).first():
                        messages.info(request, 'Username Taken')
                        return redirect('/student') 
                email = request.POST.get('email')

                if User.objects.filter(email = email).first():
                        messages.info(request, 'Email is already in use')
                        return redirect('/student')

                password = request.POST.get('password')                                
                if len(password) < 6:
                        messages.info(request, 'Password should have minimum 6 characters')
                        return redirect('/student')

                user_obj = User(username = username, email = email)    
                user_obj.set_password(password)        
                user_obj.save()
                
                fname = request.POST.get('fname')
                lname = request.POST.get('lname')                                                
                year = request.POST.get('year')                                                
                branch = request.POST.get('branch')

                i=1
                while True:
                        if(Student.objects.filter(id=i)):
                                i=i+1
                        else:
                                break  
                student_obj = Student.objects.create(id = i, user = user_obj, is_verified = True ,username = username, email = email, fname = fname, lname = lname, year = year, branch = branch)        
                student_obj.save()
                send_mail_after_creation(email, username, password)
                messages.info(request, 'Email with details sent')
                return redirect('/student')
        return redirect('/student')    


def vstudent(request, pk, sk):
        student = Student.objects.all()
        mm = Memories.objects.filter(memuname = sk)
        cc = Comments.objects.filter(recieveruname = sk, is_approved = False)
        xx = Comments.objects.filter(recieveruname = sk, is_approved = True)
        return render(request, 'vstudent.html',{'student': student, 'memories': mm, 'username': sk,'commentsnot': cc, 'commentsis': xx})

def creatememory(request, pk, sk):
        if request.method == 'POST':                               
                memory = Memories()                    
                text = request.POST.get('text')                               
                username = request.POST.get('username')
                i=1
                while True:
                        if(Memories.objects.filter(id=i)):
                                i=i+1
                        else:
                                break
                memory.id=i
                memory.memuname = username                                               
                memory.text = text                
                memory.save()        
                messages.info(request, 'Memory added')
        return redirect('/year/branch/'+str(pk)+'/viewstudent/'+username)

def deletemem(request, pk, sk, mk):
        Memories.objects.filter(id=mk).delete()             
        messages.info(request, 'Memory Deleted')
        return redirect('/year/branch/'+str(pk)+'/viewstudent/'+sk)

@unauthenticated_user
def register(request):        
        if request.method == 'POST':                   
                username = request.POST.get('username') 
                z = len(username)
                if len(username) < 6:
                        messages.info(request, 'Username should have minimum 6 characters')
                        return redirect('/register')    

                if User.objects.filter(username = username).first():
                        messages.info(request, 'Username Taken')
                        return redirect('/register')    

                email = request.POST.get('email')                 
                strx = '@'
                result = email.find(strx)
                if result == -1:        
                        messages.info(request,'Invalid Email')
                        return redirect('/register')                

                if User.objects.filter(email = email).first():
                        messages.info(request, 'Email is already in use')
                        return redirect('/register')
                
                password = request.POST.get('password') 
                if len(password) < 6:
                        messages.info(request, 'Password should have minimum 6 characters')
                        return redirect('/register')

                user_obj = User(username = username, email = email)    
                user_obj.set_password(password)        
                user_obj.save()
                auth_token = str(uuid.uuid4())
                i=1
                while True:
                        if(Student.objects.filter(id=i)):
                                i=i+1
                        else:
                                break  
                profile_obj = Student.objects.create(id = i, user = user_obj, auth_token = auth_token, username = username, email = email)        
                profile_obj.save()   
                send_mail_afterregi(email, auth_token)
                return redirect('/token')

        return render(request, 'register.html')

@unauthenticated_user
def loginuser(request):
        if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(username = username, password = password)
                if user is None:
                        messages.info(request, 'Invalid Credentials')
                        return redirect('/login')                
                if user.is_staff:
                        dj_login(request, user)
                        return redirect('/')
                else:
                        logout(request)
                user_obj = User.objects.filter(username = username).first()
                if user_obj is None:
                        messages.info(request, 'Invalid Username')
                        return redirect('/login')
                        
                profile_obj = Student.objects.filter(user = user_obj).first()
                if not profile_obj.is_verified:
                        messages.info(request, 'Verify your profile from mail')
                        return redirect('/login')

                user = authenticate(username = username, password = password)
                if user is None:
                        messages.info(request, 'Invalid Credentials')
                        return redirect('/login')
                per = Student.objects.get(username = username)
                dj_login(request, user)
                if per.fname == '':
                        return redirect('/edit_detail/'+username)     
                else:   
                        return redirect('/')

        return render(request, 'login.html')

def loginadmin(request):
        if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(username = username, password = password)

                if user is None:
                        messages.info(request, 'Invalid Credentials')
                        return redirect('/loginadmin')

                if user.is_staff == False:
                        messages.info(request, 'Not Admin Credentials')
                        return redirect('/login')
                
                dj_login(request, user)
                return redirect('/')
        return render(request, 'login_admin.html')
def logoutuser(request):
        logout(request)
        messages.info(request, 'Logged out')
        return redirect('/')

def yourprofile(request):
        st = Student.objects.all()
        return render(request,'yourprofile.html', {'student': st})

def edit_detail(request, pk):
        st = Student.objects.filter(username = pk).first()
        yr = Year.objects.all()
        br = Branch.objects.all()
        return render(request, 'edit_details.html',{'student': st, 'year': yr, 'branch': br})

def edit_detail_admin(request, sk, pk):
        st = Student.objects.filter(username = pk).first()
        yr = Year.objects.all()
        br = Branch.objects.all()
        return render(request, 'edit_details.html',{'student': st, 'year': yr, 'branch': br})

def edituserdetail(request, pk):                                
        if request.method == 'POST':                                
                student = Student.objects.get(id=pk)                                                        
                fname = request.POST.get('first_name')
                lname = request.POST.get('last_name')      
                email = request.POST.get('email') 
                year = request.POST.get('year')   
                branch = request.POST.get('branch')                   
                username = request.POST.get('username')        
                fname = fname[:1].upper() + fname[1:]
                lname = lname[:1].upper() + lname[1:]
                student.email=email
                student.fname = fname   
                student.lname = lname                                
                student.year = year
                student.username=username  
                student.branch=branch                                
                student.save()        
        return redirect('/yourprofile') 

def edituserdetail_admin(request, sk, pk):                                
        if request.method == 'POST':                                
                student = Student.objects.get(id=pk)                                                        
                fname = request.POST.get('first_name')
                lname = request.POST.get('last_name')      
                email = request.POST.get('email') 
                year = request.POST.get('year')   
                branch = request.POST.get('branch')                   
                username = request.POST.get('username')        
                fname = fname[:1].upper() + fname[1:]
                lname = lname[:1].upper() + lname[1:]
                student.email=email
                student.fname = fname   
                student.lname = lname                                
                student.year = year
                student.username=username  
                student.branch=branch                                
                student.save()        
        return redirect('/year/branch/'+str(sk)+'/viewstudent/'+username)

def profpic(request):
        st = Student.objects.all()
        if request.method == 'POST':
                img = request.FILES.get('image')
                username = request.POST.get('username')
                stu = Student.objects.filter(username = username).first()
                stu.image = img
                stu.save()
                return redirect('/yourprofile')
        return render(request, 'profpic.html', {'student':st})

def year(request, pk):        
        br = Branch.objects.all()
        return render(request, 'year.html', {'branch': br, 'year': int(pk) })

def branch(request, pk, sk):
        st = Student.objects.filter(year = pk, branch = sk)
        return render(request,'branch.html', {'student': st})

def createcomment(request, pk, sk):
        if request.method == 'POST':                
                comment = Comments()
                content = request.POST.get('content')
                senderuname = request.POST.get('senderuname')      
                recieveruname = request.POST.get('recieveruname')                                                                                                                 
                comment.content = content
                comment.senderuname = senderuname
                comment.recieveruname = recieveruname
                student = Student.objects.filter(username = recieveruname).first()
                comment.save()
                messages.info(request, 'Comment Sent to '+ student.fname +' for approval')
        return redirect('/year/branch/'+str(pk)+'/viewstudent/'+sk) 
        
def approve(request, pk, sk, mk):   
        comment = Comments.objects.get(id=mk)     
        comment.is_approved = True
        comment.save()
        messages.info(request, 'Comment Approved')
        return redirect('/year/branch/'+str(pk)+'/viewstudent/'+sk) 

def decline(request, pk, sk, mk):
        Comments.objects.filter(id=mk).delete()             
        messages.info(request, 'Comment Deleted')
        return redirect('/year/branch/'+str(pk)+'/viewstudent/'+sk) 

def send_mail_afterregi(email, token):
    subject = 'Please Verify your account'
    message = f'Hi! Click on the link to verify your account http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)

def send_mail_after_creation(email, username, password):
        subject = 'Your Login Details for Yearbook Website'
        message = f'Your username - "{username}"  Your password - "{password}"'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, email_from, recipient_list)


def verify(request, auth_token):    
    profile_obj = Student.objects.get(auth_token = auth_token)
    if profile_obj:
        if profile_obj.is_verified:
            messages.info(request, 'Already verified')
            return redirect('/login')

        profile_obj.is_verified = True
        profile_obj.save()
        messages.info(request, 'Email verified')
        return redirect('/login')
    else:
        return redirect('/error')

def token(request):    
    return render(request, 'token.html')

def error(request):
    return render(request, 'error.html')