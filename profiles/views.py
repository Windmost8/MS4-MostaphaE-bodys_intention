from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm

from products.models import Product, Comment, Contact
from checkout.models import Order
from products.forms import ProductForm, CommentForm, ContactForm


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def my_comments(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    comments = Comment.objects.filter(person__in=[profile])

    template = 'profiles/my_comments.html'
    context = {
        'form': form,
        'comments': comments,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def edit_comment(request, comment_id):
    """ Edit a comment in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('profile'))

    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated comment!')
            return redirect(reverse('my_comments'))
        else:
            messages.error(request, 'Failed to update comment. Please ensure the form is valid.')
    else:
        form = CommentForm(instance=comment)
        messages.info(request, f'You are editing {comment.product}')

    template = 'profiles/edit_comment.html'
    context = {
        'form': form,
        'comment': comment,
    }

    return render(request, template, context)


@login_required
def delete_comment(request, comment_id):
    """ Delete a comment from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    messages.success(request, 'Comment deleted!')
    return redirect(reverse('profile'))


@login_required
def my_contacts(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)
    contacts = Contact.objects.filter(person__in=[profile])

    template = 'profiles/my_contacts.html'
    context = {
        'contacts': contacts,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def delete_contact(request, contact_id):
    """ Delete a comment from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    contact = get_object_or_404(Contact, pk=contact_id)
    contact.delete()
    messages.success(request, 'Inquiry deleted from history!')
    return redirect(reverse('profile'))


@login_required
def edit_contact(request, contact_id):
    """ Edit a comment in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('profile'))

    contact = get_object_or_404(Contact, pk=contact_id)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated inquiry!')
            return redirect(reverse('my_contacts'))
        else:
            messages.error(request, 'Failed to update inquiry. Please ensure the form is valid.')
    else:
        form = ContactForm(instance=contact)
        messages.info(request, f'You are editing a previous inquiry.')

    template = 'profiles/edit_contact.html'
    context = {
        'form': form,
        'contact': contact,
    }

    return render(request, template, context)