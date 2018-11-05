from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect


from .models import Question, Choice

# Create your views here.
def index(request):
  last_question_list = Question.objects.order_by('-pub_date')[:5]
  context = {
    'latest_question_list': last_question_list
  }

  return render(request, 'polls/index.html', context)
  
# Detail of the question
def detail(request, question_id):
  question = get_object_or_404(Question,pk = question_id)
  
  return render(request, 'polls/detail.html', { 'question': question })


# Vote for question
def vote(request, question_id) :
  question = get_object_or_404(Question, pk= question_id)
  try:
    selected_choice = question.choice_set.get(pk = request.POST['choice'])
  except (KeyError, Choice.DoesNotExist):
    return render(request, 'polls/detail.html', {
      'question': question,
      'error_message': "You didn't select a choice"
    })
  else:
    selected_choice.votes += 1
    selected_choice.save()

    return HttpResponseRedirect(reversed("polls:results", args =(question_id,)))
  

# Results
def results(request, question_id):
  question = get_object_or_404(Question, pk=question_id)

  return render(request, 'polls/results.html', {'question': question})
