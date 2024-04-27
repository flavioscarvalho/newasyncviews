import asyncio
import time
from django.http import HttpResponse, JsonResponse
import httpx  # Para chamadas HTTP assíncronas

# Função assíncrona para a view do contador de tempo
async def async_time_counter(request):
    await asyncio.sleep(5)  # Simula um atraso de 5 segundos
    return HttpResponse("Contador de tempo terminou após 5 segundos.")

# Função para a rota da API
def api(request):
    time.sleep(1)  # Simula um atraso de 1 segundo
    payload = {"message": "Hello World"}

    # Se "task_id" estiver nos parâmetros GET, adicione ao payload
    if "task_id" in request.GET:
        payload["task_id"] = request.GET["task_id"]

    return JsonResponse(payload)  # Retorna um JsonResponse com o payload

# Função para chamadas HTTP assíncronas
async def http_call_async():
    # Simula um contador de 1 a 5
    for num in range(1, 6):
        await asyncio.sleep(1)  # Simula atraso de 1 segundo
        print(num)  # Imprime o número

    # Chamada HTTP assíncrona com httpx
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org/get")  # Chama um endpoint de teste
        print(r.text)  # Imprime a resposta do endpoint HTTP

# Função assíncrona para criar uma tarefa não-bloqueante
async def async_view(request):
    loop = asyncio.get_event_loop()  # Obtém o loop de eventos
    loop.create_task(http_call_async())  # Cria uma tarefa assíncrona
    return HttpResponse("Non-blocking HTTP request")  # Retorna uma resposta
