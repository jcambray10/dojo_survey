from django.urls import path, include

urlpatterns = [
    path('', include('dojo_survery_app.urls')),
]

# echo "# dojo_survey" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/jcambray10/dojo_survey.git
# git push -u origin main