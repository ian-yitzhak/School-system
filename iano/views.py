from django.shortcuts import render




from . models import Contact ,Post, techer,department,schools 

from django.http import HttpResponse

from django.shortcuts import redirect

from mainapp.forms import student , teacher
from django.shortcuts import render





def home(request):

    posts = Post.objects.all()




    if request.method =="POST":

       
        email = request.POST.get('email')
        
        subject = request.POST.get('subject')
       
        contact.email=email
        
        contact.subject=subject
        contact.save()

        return render( request , 'iano/contact.html')

    return render( request , 'iano/index.html'  , {'posts' : posts})



def teachl(request):

    posts = teacher.objects.all()




    return render( request , 'iano/teach.html'  , {'posts' : posts})





def school(request):

    posts = school.objects.all()




    return render( request , 'iano/school.html'  , {'posts' : posts})



def department(request):

    posts = departments.objects.all()



    return render( request , 'iano/dep.html'  , {'posts' : posts})




class PastorSignUpView(CreateView):
    model = User
    form_class = PastorSignupForm
    template_name = 'form/login.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'pastor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('form/login.html')









