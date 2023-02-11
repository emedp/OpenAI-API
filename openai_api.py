import openai
import os

# Load your API key from an environment variable or secret management service
openai_api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = openai_api_key
# print(openai_api_key)

# VER LOS ID DE LOS ENGINES DISPONIBLES
# engines = openai.Engine.list().data
# for engine in engines:
#     print(engine.id)

print('Introduce FINALIZAR para salir del programa')
while True:
    # RECOGER PREGUNTA
    prompt = input("Escribe tu petición: ")

    if prompt == 'FINALIZAR':
        break

    # LANZAR PREGUNTA
    completion = openai.Completion.create(
        engine="text-davinci-003", 
        prompt=prompt,
        )
    print(completion.choices[0].text)
