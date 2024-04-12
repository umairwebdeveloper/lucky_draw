from django.shortcuts import render
from app.models import PrizeProbability, WinGiftEmail
from .forms import WinGiftEmailForm
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
import random 


def generate_prize():
    # Fetch all prizes from the database
    prizes = PrizeProbability.objects.all()

    # Check if the total probability is 100%
    total_percentage = sum(prize.percentage for prize in prizes)
    if total_percentage != 100:
        raise ValueError("Total probability does not sum up to 100%")

    # Randomly choose a prize based on the probabilities
    chosen_prize = random.choices(
        population=[prize for prize in prizes],
        weights=[prize.percentage for prize in prizes],
        k=1
    )

    return str(chosen_prize[0].id), str(chosen_prize[0].money)


@csrf_exempt  # Temporarily disable CSRF
@require_http_methods(["POST"])
def add_email(request):
    form = WinGiftEmailForm(request.POST)
    if form.is_valid():
        instance = form.save()
        return JsonResponse({'status': 'success', 'message': 'Email added successfully', 'id': instance.id})
    else:
        return JsonResponse({'status': 'fail', 'errors': form.errors, 'message': 'Invalid data'})
    
@csrf_exempt
@require_http_methods(["POST"])
def get_prize(request):
    try:
        selected_index = request.POST.get('selectedIndex')
        model_id = request.POST.get('modelId')
        id, selected_prize = generate_prize()
        WinGiftEmail.objects.filter(id=model_id).update(prize_won=selected_prize, number_selected=selected_index)
        remianing_prizes = PrizeProbability.objects.exclude(id=id).all()
        remaining_prizes_money = [prize.money for prize in remianing_prizes]
        random.shuffle(remaining_prizes_money)
        

        return JsonResponse({
            'selectedPrize': selected_prize,
            'otherPrizes': remaining_prizes_money,
            'status': 'success',
            'message': 'Prize selected successfully'
        })
    except ValueError as e:
        return JsonResponse({'status': 'fail', 'message': str(e)})

# Create your views here.
def home(request):
    return render(request, 'home.html')