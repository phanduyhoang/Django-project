from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import Word
from random import sample
from random import sample
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def cards(request):
    words_list = Word.objects.all()
    paginator = Paginator(words_list, 20)  # Show 20 words per page

    page_number = request.GET.get('page')
    try:
        words = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        words = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        words = paginator.page(paginator.num_pages)

    return render(request, 'vocabulary/cards.html', {'words': words})


from django.shortcuts import render
from django.http import JsonResponse
from .models import Word
from random import sample
from users.models import TrainingHistory
def english_trainer(request):
    # Get a random English word
    #print('x')
    if request.user.is_authenticated:
        training_history = TrainingHistory.objects.get_or_create(user=request.user)[0]
    else:
        training_history = None
    random_word = Word.objects.order_by('?').first()

    # Get the correct translation for the random word
    correct_translation = random_word.russian_translation

    # Get three additional random incorrect translations (excluding the correct one)
    all_translations = list(Word.objects.exclude(english_word=random_word.english_word).values_list('russian_translation', flat=True))
    if len(all_translations) < 3:
        error_message = "Not enough translations available for this word"
        return render(request, 'vocabulary/english_trainer.html', {'error': error_message})

    incorrect_translations = sample(all_translations, 3)

    # Combine correct and incorrect translations to form options
    translations_choices = incorrect_translations + [correct_translation]

    # Shuffle the choices to display randomly
    random_translations = sample(translations_choices, 4)

    context = {
        'word': random_word,
        'translations': random_translations,
        'correct_translation': correct_translation,  # Pass correct translation to JavaScript
        'training_history': training_history 
    }

    return render(request, 'vocabulary/english_trainer.html', context)

def update_training_history(request):
    print('x')
    if request.method == 'POST':
        is_correct = request.POST.get('is_correct')  # Get the value of 'is_correct' from the POST data
        if is_correct == 'true':
            is_correct = True
        else:
            is_correct = False

        if request.user.is_authenticated:
            training_history, created = TrainingHistory.objects.get_or_create(user=request.user)
            if is_correct:
                training_history.correct_count += 1
            else:
                training_history.incorrect_count += 1
            training_history.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'message': 'User is not authenticated'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'})




from django.contrib.auth.decorators import login_required
@login_required
def check_answer(request):
    if request.method == 'POST':
        selected_translation = request.POST.get('selected_translation')
        correct_translation = request.POST.get('correct_translation')
        user = request.user

        training_history, created = TrainingHistory.objects.get_or_create(user=user)
        
        if selected_translation == correct_translation:
            result = 'correct'
            # Update correct count in training history
            training_history.correct_count += 1
        else:
            result = 'incorrect'
            # Update incorrect count in training history
            training_history.incorrect_count += 1

        # Save the changes to the training history
        training_history.save()

        return JsonResponse({'result': result})