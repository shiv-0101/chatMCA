import os
from openai import AzureOpenAI
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# This decorator is used to allow POST requests from the front-end without a CSRF token.
# In a production environment, you would use a proper Django form with a token.
@csrf_exempt
def chat_view(request):
    # Check if the chat history exists in the session. If not, initialize it.
    if 'chat_history' not in request.session:
        request.session['chat_history'] = []

    # Handle the API call on a POST request
    if request.method == 'POST':
        user_input = request.POST.get('message', '')

        # Add the user's message to the chat history
        request.session['chat_history'].append({"role": "user", "content": user_input})
        request.session.modified = True

        try:
            # Initialize the AzureOpenAI client
            client = AzureOpenAI(
            api_version="2024-12-01-preview",
            azure_endpoint="https://ldemo3838267452.cognitiveservices.azure.com/",
            api_key="vAIzaSyDDUv1XDDUV30CLlDYgOH6KLM9M9aZe4H0",
            )

            # Build the messages list for the API call
            messages = [{"role": "system", "content": "You are a helpful assistant."}]
            messages.extend(request.session['chat_history'])

            # Make the API call
            response = client.chat.completions.create(
                messages=messages,
                max_tokens=4096,
                temperature=1.0,
                top_p=1.0,
                model="gpt-4o-mini"
            )

            # Get the assistant's response
            assistant_response = response.choices[0].message.content

            # Add the assistant's response to the chat history
            request.session['chat_history'].append({"role": "assistant", "content": assistant_response})
            request.session.modified = True
            
            # Return the updated chat history as a JSON response
            return JsonResponse({"chat_history": request.session['chat_history']})

        except Exception as e:
            # Handle potential errors from the API call
            error_message = f"An error occurred: {str(e)}"
            return JsonResponse({"error": error_message}, status=500)

    return render(request, 'chat.html', {'chat_history': request.session['chat_history']})
