from .models import Category, Product, Author, Comment
from .forms import CategoryForm, ProductForm, SearchForm, CommentAddForm, SignUpForm
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth import authenticate
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from bookshop.serializers import ProductSerializer
from rest_framework import generics
from cart.forms import CartAddProductForm
from orders.models import OrderItem
from django.contrib.auth.forms import UserCreationForm





class IndexView(View):
    def get(self, request):
        categories = Category.objects.all().order_by('category_name')
        tab = []
        top = []
        count_id = OrderItem.objects.all().latest('id')
        for i in range(count_id.id, count_id.id -10, -1):
            tab.append(OrderItem.objects.get(id=i))
        for a in tab:
            top.append(Product.objects.get(id=a.product_id))
        return render(request, 'bookshop/index.html', {'categories': categories, 'top': top})


class CategoryView(View):
    def get(self, request, slug):
        categories = Category.objects.all().order_by('category_name')
        products = Product.objects.filter(categories__slug=slug).order_by('name')
        return render(request, 'bookshop/category_products.html', {'products': products, 'categories': categories})


class CategoryCreate(CreateView):
    model = Category
    fields = '__all__'
    success_url = reverse_lazy('index')


class CategoryUpdate(UpdateView):
    model = Category
    fields = '__all__'
    success_url = reverse_lazy('index')


class ProductsView(generic.ListView):
    template_name = 'bookshop/products_list.html'
    def get_queryset(self):
        return Product.objects.all().order_by('name')


class Login(View):
    def get(self, request):
        return render(request, "bookshop/login.html", {'user': request.user})
    def post(self, request):
        login1 = request.POST.get("login")
        password = request.POST.get("password")
        user = authenticate(username=login1, password=password)
        if user:
            login(request, user)
            return redirect('index')
        return HttpResponse("ERROR %s %s" % (login1, password))


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect("index")


class Search(View):
    def get(self, request):
        form = SearchForm()
        return render(request, 'bookshop/search.html', {'form': form})

    def post(self, request):
        form = SearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            search_ch = request.POST.get('search_ch')
            products = []
            categories = []
            authors = []
            if search_ch == 'Kategoria':
                categories = Product.objects.filter(categories__category_name=name).order_by('name')
            elif search_ch == 'Książka':
                products = Product.objects.filter(name__icontains=name)
            elif search_ch == 'Author':
                authors = Product.objects.filter(author__author_last_name=name).order_by('name')
            else:
                products = Product.objects.filter(name__icontains=name)
                categories = Product.objects.filter(categories__slug=name).order_by('name')
                authors = Product.objects.filter(author__author_last_name=name).order_by('name')
            return render(request, 'bookshop/search.html', {'products': products, 'categories': categories,
                                                            'authors': authors, 'name': name})

class ProductCreate(CreateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('products')


class ProductUpdate(UpdateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('products')


class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('products')


class AuthorView(generic.ListView):
    template_name = 'bookshop/authors_list.html'

    def get_queryset(self):
        return Author.objects.all().order_by('category_name')


class BookShopView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class BookView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class Product_detail(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        cart_product_form = CartAddProductForm()
        comments = Comment.objects.filter(book=pk)
        form = CommentAddForm()
        return render(request, "bookshop/book_details.html", {"form": form, "product": product, 'comments': comments, 'cart_product_form': cart_product_form})

    def post(self, request, pk):
        form = CommentAddForm(request.POST)
        book = Product.objects.get(pk=pk)
        if form.is_valid():
            Comment.objects.create(
                text=form.cleaned_data['text'],
                book=book
            )
            return redirect("detail", pk)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'bookshop/signup.html', {'form': form})



class Authors_list(View):
    def get(self, request):
        authors = Author.objects.all().order_by('author_last_name')
        return render(request, 'bookshop/authors.html', {'authors': authors})



class Authors_products(View):
    def get(self, request, id):
        authors = Author.objects.all().order_by('author_last_name')
        products = Product.objects.filter(author__id=id).order_by('name')
        return render(request, 'bookshop/authors_products.html', {'products': products, 'authors': authors})


class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'
    success_url = reverse_lazy('author-list')


class AuthorUpdate(UpdateView):
    model = Author
    fields = '__all__'
    success_url = reverse_lazy('author-list')


