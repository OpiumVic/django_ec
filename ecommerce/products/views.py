from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category
from .forms import CategoryForm
from django.forms import modelform_factory

ProductForm = modelform_factory(Product, fields='__all__')

def home(request):
    return render(request, "products/home.html")

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            # pass message
            return redirect("products:add_category")
    else:
        form = CategoryForm()
    return render(request,"products/category_form.html",{'form':form})

def category_list(request):
    categories = Category.objects.all()
    return render(request,"products/category_list.html",{'categories':categories})

# Added: view to add a product
def add_product(request):
    """
    Shows a product form and saves a new Product on POST.
    Uses a dynamic ModelForm so you don't need to create a separate form class.
    """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('products:product_list')
    else:
        form = ProductForm()
    return render(request, 'products/product_form.html', {'form': form})

# Added: view to list all products
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def product_loop(request):
    products = Product.objects.all()
    return render(request, "products/product_loop.html", {'products': products})

def product_detail(request, pk):
    """
    Show full product information including full description and larger image.
    """
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_details.html', {'product': product})