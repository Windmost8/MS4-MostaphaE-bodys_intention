from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.views.generic.edit import CreateView

from .models import Product, Category, Comment, Contact, UserProfile
from .forms import ProductForm, CommentForm

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
            
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    #is_favorite = False
    #if product.favorite.filter(id=request.user.id).exists():
    #    is_favorite = True

    context = {
        'product': product,
    #    'is_favorite': is_favorite,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


def contact(request):
    """ view for contact us page"""
    profile = None
    if request.user.is_authenticated:
        profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        inquiry = request.POST.get('inquiry')
        instance = Contact(name=name, email=email, inquiry=inquiry)
        if profile:
            instance.person = profile
        instance.save()

    context = {
        'contact': contact,
    }

    return render(request, 'products/contact.html', context)


@login_required
def add_comment(request, product_id):
    profile = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            comment.person = profile
            comment.product = product
            comment.save()
            messages.success(request, 'Successfully added comment!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add comment. Please try again.')
    else:
        form = CommentForm()
        
    template = 'products/add_comment.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


#class AddCommentView(CreateView):
#    model = Comment
#    form_class = CommentForm
#    template_name = "products/add_review.html"
#    # fields = '__all__'
#    success_url = reverse_lazy('products')

#    def form_valid(self, form):
#        form.instance.product_id = self.kwargs['pk']
#        return super().form_valid(form)


#def reviews_stars(request):
#    """view for reviews"""
#    if request.method == "GET":
#        product_id = request.GET.get('product_id')
#        product = Product.objects.get(id=product_id)
#        comment = request.GET.get('comment')
#        stars = request.GET.get('stars')
#        person = request.user
#        Reviews(person=person, product=product, comment=comment, stars=stars).save()
#        return redirect('product_detail', id=product_id)
