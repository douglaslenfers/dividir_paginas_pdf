from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .split_pdf import split_pdf
import os

@csrf_exempt
def index(request):
    try:
        if request.method == "POST":
            json_data = json.loads(request.body)
            input_path = json_data['input_path']
            pdf_name = input_path.replace(".pdf", "").split("/")[-1]
            output_path = json_data['output_path'] + pdf_name + "/"
            if not os.path.exists(output_path):
                os.makedirs(output_path)

            total_page_num = split_pdf(input_path, output_path)
            responseData = {
                'input_path': input_path,
                'output_path': output_path,
                'total_pages': int(total_page_num)
            }
        elif request.method == 'GET':
            responseData = {
                'ping':'pong'
            }
    except IOError:
            responseData = {
                'error': 'Ocorreu um erro ao tentar ler o arquivo'
            }
    except:
        responseData = {
            'error': 'Ocorreu um erro no sistema'
        }

    return JsonResponse(responseData)
