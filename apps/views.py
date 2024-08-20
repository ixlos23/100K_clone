from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'apps/home.html'


"""
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/ixlos23/100K_clone.git
git push -u origin main
"""