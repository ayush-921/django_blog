from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Your account has been created. You can login now"
            )
            return redirect("login")
    else:
        form = UserRegistrationForm()
    return render(request, "users/register.html", {"form": form})


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Your account has been updated.")
            return redirect(
                "profile"
            )  # redirect uses get request and don perform resubmission
    else:
        u_form = UserUpdateForm(
            instance=request.user
        )  # user update form inported from forms.py
        p_form = ProfileUpdateForm(
            instance=request.user.profile
        )  # profile update form inported from forms.py
    context = {
        "u_form": u_form,
        "p_form": p_form,
    }  # context is used to pass the new form the profile.html
    return render(request, "users/profile.html", context)