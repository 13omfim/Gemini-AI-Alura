<!-- DICA P/ - EDIÇÂO | Inicio -->

<!--
<p align="center">
<img loading="lazy" src="https://github.com/13omfim/Gemini-AI-Alura/assets/169212815/e1903626-9e4e-472c-9dac-fa1da0d384d6"/>
</p>
-->

<!-- Abaixo, cria uma caixa sobressalente para destacar o texto
```
```
Fim -->

<!-- Abaixo, modelos sem alinhamento
![gemini](https://github.com/13omfim/Gemini-AI-Alura/assets/169212815/e1903626-9e4e-472c-9dac-fa1da0d384d6)
-->

<!-- Abaixo, modelos sem alinhamento 
![Static Badge](https://img.shields.io/badge/Status-Em%20Constru%C3%A7%C3%A3o-orange)
-->

<!-- Selecione todo o texto Abaixo "Imersão..." e Segure "ctrl"+ "enter" que cria linha abaixo "Gemini-Ai-Alura" que fica acima -->

<!-- DICA P/ - EDIÇÂO | Fim -->

<!-- Imagem Cabeçalho -->
![google](/assets/images/sab.jpeg)

<!--  Badges -->
<p align="center">
<img loading="lazy" src="https://img.shields.io/badge/Status-Em%20Constru%C3%A7%C3%A3o-orange"/>
</p>

![Static Badge](https://img.shields.io/badge/Prompt-Script-blue?logo=googlegemini) ![GitHub License](https://img.shields.io/github/license/mashape/apistatus?logo=github) ![GitHub followers](https://img.shields.io/github/followers/13omfim?style=social) ![GitHub language count](https://img.shields.io/github/languages/count/13omfim/Gemini-AI-Alura)

<!-- Cabeçalho -->
# <h1 align="center">Gemini-Ai-Alura<h1>

## 👩‍💻 Imersão em AI Gemini, Google Studio fornecida pela Alura em parceria com o Google
<!-- Indices -->
### 📖 Aula 3 | Explorando os Parametros do Google AI Studio
#### Assuntos abordados:
```
- Conhecer os 3 tipos de prompts do Google AI Studio: chat prompts, freeform prompts e structured prompts;
- Explorar os parâmetros do Google AI Studio;
- Conhecer mais sobre os tokens e PLN;
- Iniciar o contato com Python pelo Google Colab.
```
#### Desafios desta aula:

```
1. Criar seu próprio áudio e realizar um prompt para análise pelo Google AI Studio;
2. Pesquise como colocar a imagem do Google AI Studio dentro do código de Pyhton no Google Colab;
3. Pegue os códigos que não contenham imagens do AI Studio e exporte para o Google Colab.;
```

 #### Respostas:

* Resolução:
```
-	Baixar as 3 imagens e fazer upload delas no ícone de pasta que fica na barra lateral esquerda do Google Colab;
-	Ao passar o mouse por cima do nome da imagem, aparecerão 3 pontinhos do lado direito do mesmo. Ao clicar nesses 3 pontinhos, selecionar a opção "Copiar caminho". Depois, ir no código, e dentro da lista de nome "prompt parts", substituir a linha "*upload_if_needed("<path>/image0.jpeg")" por "*upload_if_needed("CAMINHO_DA_SUA_IMAGEM")";
-	Fazer o mesmo para as outras duas imagens dentro das outras funções "*upload_if_needed" que estão nesta lista. O código ficará mais ou menos assim:

-	Na linha "genai.configure(api_key="YOUR_API_KEY")", substituir "YOUR_API_KEY" pela sua API Key, obtida no Google AI Studio.

```
* Prompt:
```
prompt_parts = [
  "Given an image of a product and its target audience, write an engaging marketing description",
  "Product Image: ",
  *upload_if_needed("/content/image0.jpg"),
  "Target Audience: Mid-aged men",
  "Marketing Description: Introducing the epitome of power and sophistication - the sleek and captivating sports car. It's more than just a car; it's a symbol of your passion for life and your unwavering commitment to excellence. Embrace the thrill and indulge in the ultimate driving pleasure.",
  "Product Image: ",
  *upload_if_needed("/content/image1.jpg"),
  "Target Audience: Environmentalists",
  "Marketing Description: Looking for a sustainable and eco-friendly way to get around? Look no further than this black bicycle. Biking is a great way to reduce your carbon footprint and improve your health at the same time. If you're an environmentalist, there's no better way to get around than by bike!",
  "Product Image: ",
  *upload_if_needed("/content/image2.jpg"),
  "Target Audience: Athletes",
  "Marketing Description: ",
]
```




  