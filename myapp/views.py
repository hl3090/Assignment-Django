from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import ProductMst, ProductSubCat
from .forms import ProductMstForm, ProductSubCatForm

def admin_dashboard(request):
    return render(request, 'base.html')

def add_product(request):
    if request.method == 'POST':
        form = ProductMstForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = ProductMstForm()
    return render(request, 'add_product.html', {'form': form})

def add_product_subcategory(request, product_id):
    product = ProductMst.objects.get(pk=product_id)
    if request.method == 'POST':
        form = ProductSubCatForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = ProductSubCatForm(initial={'product': product})
    return render(request, 'add_product_subcategory.html', {'form': form, 'product': product})

def view_products(request):
    products = ProductMst.objects.all()
    return render(request, 'view_products.html', {'products': products})

def view_product_subcategory(request, product_id):
    product = ProductMst.objects.get(pk=product_id)
    subcategories = ProductSubCat.objects.filter(product=product)
    return render(request, 'view_product_subcategory.html', {'subcategories': subcategories, 'product': product})

def update_product_subcategory(request, subcategory_id):
    subcategory = ProductSubCat.objects.get(pk=subcategory_id)
    if request.method == 'POST':
        form = ProductSubCatForm(request.POST, request.FILES, instance=subcategory)
        if form.is_valid():
            form.save()
            return redirect('view_product_subcategory', subcategory.product.pk)
    else:
        form = ProductSubCatForm(instance=subcategory)
    return render(request, 'update_product_subcategory.html', {'form': form, 'subcategory': subcategory})

def delete_product_subcategory(request, subcategory_id):
    subcategory = ProductSubCat.objects.get(pk=subcategory_id)
    subcategory.delete()
    return redirect('view_product_subcategory', subcategory.product.pk)

def product_manager_dashboard(request):
    return render(request, 'dashboard.html')

def search_product(request):
    query = request.GET.get('q')
    products = ProductMst.objects.filter(product_name__icontains=query)
    return render(request, 'search_product.html', {'products': products})