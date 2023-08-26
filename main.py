import g4f
from tika import parser  # pip install tika

raw = parser.from_file("resume.pdf")
resume_text = (
    str(raw["content"].encode("utf-8", errors="ignore"))
    .replace("\n", "")
    .replace("\\", "")
)

print(resume_text)


def main():
    completion = g4f.ChatCompletion.create(
        model=g4f.models.gpt_35_turbo_16k_0613,
        messages=[
            {
                "role": "user",
                "content": "O seguinte texto é extraído diretamente de um PDF de currículo. Leve em consideração os seguintes detalhes:"
                + "\n\n- Esse currículo pode estar escrito em qualquer linguagem, não necessariamente em portugues."
                + "\n\n- Ao ler o currículo, dê sugestões de melhoria e cite diretamente as partes que devem ser corrigidas (faça citaçöes diretas, sem traduzir o que está escrito)."
                + "\n\n- Caso encontre símbolos aleatórios ou palavras que não existem, sinalize como grave e indique quais são essas palavras ou símbolos."
                + "\n\n- Caso encontre erros de digitação, escreva como a palavra deve ser escrita corretamente."
                + "\n\n- Dependendo da fonte utilizada, o currículo pode conter espaços entre as letras, caso isso ocorra apenas considere que esses espaços não existem e não sugira uma correção relacionada a isso."
                + "\n\n- Para cada ponto levantado, adicione um dos seguintes prefixos para classificar e organizar: [GRAVÍSSIMO] [GRAVE] [MÉDIO] [OPCIONAL]."
                + "\n\nSegue o currículo:"
                + "\n\n"
                + resume_text
                + "\n\nDETALHE: Separe cada sugestão por uma linha em branco.",
            }
        ],
        provider=g4f.Provider.You,
    )

    for message in completion:
        print(message, flush=True, end="")


if __name__ == "__main__":
    main()
