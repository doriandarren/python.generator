import asyncio
import aiohttp


# Función asíncrona para consultar el modelo
async def query_ollama(prompt):
    ##url = "http://localhost:11434/api/generate"
    url = "http://192.168.1.100:11434/v1/completions"
    payload = {
        "model": "llama3",  # Puedes cambiar por cualquier modelo que tengas instalado
        "prompt": prompt,
        "stream": False
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload) as response:
            if response.status == 200:
                data = await response.json()
                return data.get("choices")
            else:
                return f"Error: {response.status}"



# Función principal para ejecutar múltiples consultas asíncronas
async def main():
    prompts = [
        # "¿dame un código que sume 2 números en pyhton?",
        # "Explica la teoría de la relatividad de forma simple.",
        # "¿Cuál es el significado de la vida?"
        #"¿que día es hoy?"
        "Me puedes crear una historia de un dectective en la edad medieval?"
    ]

    tasks = [query_ollama(prompt) for prompt in prompts]
    results = await asyncio.gather(*tasks)

    for idx, result in enumerate(results):
        ## print(type(result))

        ##print(f"Respuesta {idx + 1}: {result[0]['text']}")

        for r in result:
            print(f"Respuesta {idx + 1}: {r['text']}")
            print(f"----")



# Ejecutar el bucle de eventos
if __name__ == "__main__":
    asyncio.run(main())