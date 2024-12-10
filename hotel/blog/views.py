from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from datetime import datetime
from blog.models import Booking
from blog.forms import Book_in, Book_out



def cost_calculate(date_in, date_out):
    di = date_in.weekday()  # (0 = понедельник, 6 = воскресенье)
    delta = (date_out - date_in).days + 1
    full_weeks = delta // 7
    desc = {2: 0.9, 3: 0.85, 4: 0.8}
    cost = full_weeks * 1300 + sum([100 if 4 < i < 7 else 200 for i in range(di, di + delta % 7)])
    if 1 < full_weeks < 5:
        cost *= desc[full_weeks]
    elif full_weeks > 4:
        cost *= 0.75
    return cost


def index(request):
    template = 'blog/index.html'
    context = {'reservations': Booking.objects.all()}
    return render(request, template, context)


def reservation(request, reservation_id):
    template = 'blog/detail.html'
    try:
        resv = Booking.objects.filter(id=reservation_id).first()
        print(resv.date_out_fact)
        if resv.date_in_fact and resv.date_out_fact:

            cost = cost_calculate(resv.date_in_fact,
                                          resv.date_out_fact)
        else:
            cost = cost_calculate(resv.date_in,
                                          resv.date_out)
        print(cost)
        context = {'reservation': resv,
                   'cost': cost}
    except AttributeError:
        raise Http404(f'reservation {reservation_id} Not Found')
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    context = {'category_slug': category_slug}
    return render(request, template, context)


def delete_obj(request, reservation_id):
    obj = get_object_or_404(Booking, id=reservation_id)
    obj.delete()
    return redirect('blog:index')


def book_in(request, reservation_id):
    # Получаем объект бронирования по ID, если объект не найден, выбрасываем 404
    booking = get_object_or_404(Booking, id=reservation_id)

    # Если запрос POST, обновляем объект
    if request.method == 'POST':
        form = Book_in(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('blog:reservation', reservation_id=booking.id)

    else:
        # Если запрос GET, показываем текущие данные в форме
        form = Book_in(instance=booking)

    return render(request, 'blog/edit_booking.html', {'form': form, 'booking': booking})


def book_out(request, reservation_id):
    # Получаем объект бронирования по ID, если объект не найден, выбрасываем 404
    booking = get_object_or_404(Booking, id=reservation_id)

    # Если запрос POST, обновляем объект
    if request.method == 'POST':
        form = Book_out(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('blog:reservation', reservation_id=booking.id)

    else:
        # Если запрос GET, показываем текущие данные в форме
        form = Book_out(instance=booking)

    return render(request, 'blog/edit_booking.html', {'form': form, 'booking': booking})
