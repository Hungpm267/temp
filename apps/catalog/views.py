from django.shortcuts import render

# Create your views here.
# apps/catalog/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Category, Product, ProductImage
from .forms import CategoryForm, ProductForm

# Hiển thị danh sách Category (Read)
class CategoryListView(ListView):
    model = Category
    template_name = 'catalog/category_list.html'
    context_object_name = 'categories'
    paginate_by = 10

# Hiển thị chi tiết một Category (Read)
class CategoryDetailView(DetailView):
    model = Category
    template_name = 'catalog/category_detail.html'
    context_object_name = 'category'

# Tạo Category mới (Create)
class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'catalog/category_form.html'
    success_url = reverse_lazy('category-list')

# Cập nhật Category (Update)
class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'catalog/category_form.html'
    success_url = reverse_lazy('category-list')

# Xóa Category (Delete)
class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'catalog/category_confirm_delete.html'
    success_url = reverse_lazy('category-list')
    
    # =======================================================================
    

# ======== THÊM CÁC PRODUCT VIEWS DƯỚI ĐÂY ========

# Hiển thị danh sách Product (Read)
class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'
    paginate_by = 2 # Phân trang, mỗi trang 8 sản phẩm

# Hiển thị chi tiết Product (Read)
class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

# Tạo Product mới (Create)
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('product-list')

    def form_valid(self, form):
    # Dòng 1: Lấy danh sách các file ảnh phụ
        images = self.request.FILES.getlist('more_images')

    # Dòng 2: Chạy bước lưu tự động đầu tiên
        self.object = form.save()

    # Dòng 3: Lặp qua từng file ảnh phụ
        for image in images:
        # Dòng 4: Tạo và lưu từng ảnh vào model ProductImage
            ProductImage.objects.create(product=self.object, image=image)
        
    # Dòng 5: Quay lại quy trình tự động để nó làm nốt việc cuối
        return super().form_valid(form)

# Cập nhật Product (Update)
class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('product-list')

    def form_valid(self, form):
        images = self.request.FILES.getlist('more_images')
        self.object = form.save()
        for image in images:
            ProductImage.objects.create(product=self.object, image=image)
        return super().form_valid(form)

# Xóa Product (Delete)
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('product-list')