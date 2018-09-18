from .models import Category, Author, Image
from .forms import CategoryForm

# def categories(request):
#     # model = CategoryForm
#     model1 = Category.objects.all()
#     model = []
#     for ii in model1:
#         model.append(ii.category_name)
#     return {'model': model}

def categories(request):
    categories = Category.objects.all()
    return {'categories': categories}

def authors(request):
    authors = Author.objects.all()
    return {'authors': authors}

def logo(request):
    logo = Image.objects.get(name='logo')
    return {'logo': logo}
