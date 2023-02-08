from django.shortcuts import render
import openai
from chat.models import Chat
from django.conf import settings

# Create your views here.

openai.api_key = getattr(settings, "API_KEY")

def generate_response(prompt):

  completions = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
  )

  message = completions.choices[0].text
  return message.strip()


def index(request):
  chats = Chat.objects.all()
  if request.method == 'POST':
    user_input = request.POST.get('message')

    response = generate_response(user_input)
    chat = Chat.objects.create(
      question=user_input,
      answer=response,
    )

  context = {
    'chats': chats
  }

  return render(request, 'index.html', context)