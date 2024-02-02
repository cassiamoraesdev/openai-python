import openai

# Configure a sua chave da API da OpenAI
openai.api_key = 'SUA_CHAVE_DA_API_OPENAI'

def gerar_texto_IA(prompt):
    try:
        # Chame a API da OpenAI para gerar texto com base no prompt fornecido
        resposta = openai.Completion.create(
            engine="text-davinci-003",  # Escolha o motor de geração de texto (pode variar)
            prompt=prompt,
            max_tokens=150  # Limite máximo de tokens no texto gerado
        )

        # Retorne o texto gerado
        return resposta.choices[0].text.strip()

    except Exception as e:
        print(f"Erro ao chamar a API da OpenAI: {e}")
        return None

def main():
    # Exemplo de prompt
    prompt = "Escreva um parágrafo sobre inteligência artificial."

    # Gere texto usando a IA da OpenAI
    texto_gerado = gerar_texto_IA(prompt)

    # Exiba o texto gerado
    if texto_gerado:
        print(f"Texto gerado pela IA:\n{texto_gerado}")

if __name__ == "__main__":
    main()
