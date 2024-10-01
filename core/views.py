from django.shortcuts import render
# View for the home page
from django.shortcuts import render
from core .models import About, Education, RecentWork,Experience,CV  # Adjust as necessary
from django.shortcuts import render


def home_view(request):
    
    about = About.objects.first()  # Fetch the first About instance
    educations=Education.objects.first()
    experience=Experience.objects.first()
    works=RecentWork.objects.all()
    cv=CV.objects.first()

    return render(request, 'home_view.html',{'cv':cv,'experience':experience,'about':about,'educations':educations,'works':works})



# View for the About form
from django.shortcuts import render, redirect
from .forms import AboutForm
from django.core.files.storage import FileSystemStorage

def about_form(request):
    if request.method == 'POST':
        form = AboutForm(request.POST, request.FILES)
        if form.is_valid():
            # Process the form data
            short_description = form.cleaned_data['short_description']
            description = form.cleaned_data['description']
            image = form.cleaned_data['image']

            # Save the uploaded image
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            image_url = fs.url(filename)

            # Save the data to the database
            about_instance = About(
                short_description=short_description,
                description=description,
                image=image_url,  # Save the image URL if you're saving it like this
            )
            about_instance.save()  # Save the instance to the database

            # Redirect to education form after saving
            return redirect('education_form')
    else:
        form = AboutForm()
    
    return render(request, 'about_form.html', {'form': form})

from .forms import EducationForm
from .models import Education  # Import your Education model
from django.contrib.auth.decorators import login_required  # Import the login_required decorator

@login_required  # Ensure that only authenticated users can access this view
def education_form(request):
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            # Process the form data
            title = form.cleaned_data['title']
            year = form.cleaned_data['year']
            course = form.cleaned_data['course']
            description = form.cleaned_data['description']

            # Create an instance of the Education model and save it to the database
            education_instance = Education(
                user=request.user,  # Associate the education instance with the logged-in user
                title=title,
                year=year,
                course=course,
                description=description
            )
            education_instance.save()  # Save the instance

            # Redirect to the recent work form
            return redirect('recentwork_form')
    else:
        form = EducationForm()
    
    return render(request, 'education_form.html', {'form': form})



from django.shortcuts import render, redirect
from .forms import RecentWorkForm
from django.core.files.storage import FileSystemStorage

def recentwork_form(request):
    if request.method == 'POST':
        form = RecentWorkForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form data to the database
            form.save()
            return redirect('home_view')
    else:
        form = RecentWorkForm()
    
    return render(request, 'recentwork_form.html', {'form': form})
