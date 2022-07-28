
from django.contrib import messages

def edit_user_data(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        user = User.objects.filter(username=username).first()
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username
        user.save()
        messages.success(request, 'User updated successfully!')
        context = {
            'user':user,
        }
    return render(request, 'edit_user_data.html', context)


def delete_user(request):
    username = request.POST.get('username')
    User.objects.get(username=username).delete()
    return redirect('edit_user')
