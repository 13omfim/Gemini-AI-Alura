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
### 📖 Aula 2 | Melhores técnicas em Engenharia de Prompt
```
- Aprender as melhores técnicas de como realizar um prompt;
- Conhecer o conceito de zero-shot prompting;
- Aprender a técnica de few-shot prompting;
- Conhecer a técnica Few-shot Chain-of-Thought prompting.
```
#### Desafios desta aula:

```
1. Use a técnica de Few-shot Chain-of-Thought para um problema da sua vida real;
2. Escolha 10 textos do seu site de notícias preferido. Apresente para o Google AI Studio o padrão dos títulos e das suas respectivas notícias e quando chegar no décimo primeiro texto, apresente somente a notícia e peça para ele gerar um título. Veja se existe alguma técnica ou padrão;
 ```

 #### Respostas:

1. Ação:
```
Acesse o site https://olhardigital.com.br/tag/tecnologia/ e selecione os 10 primeiras publicações, identifique o padrão dos títulos e das suas respectivas notícias e quando chegar no décima primeira publicação, apresente somente a notícia e gere um título. Informe se existiu alguma técnica ou padrão;
```
* Resolução:
```
Infelizmente, como um modelo de linguagem, não posso interagir diretamente com sites ou navegar na internet. Isso significa que não consigo acessar o site do Olhar Digital, ler as notícias, identificar padrões nos títulos ou gerar novos títulos para as publicações.
Para realizar essa tarefa, você precisaria de um programa que possa acessar a internet e processar as informações da página. Isso pode ser feito usando linguagens de programação como Python com bibliotecas como "requests" e "BeautifulSoup" para extrair os dados do site.
Aqui está um exemplo de como você pode fazer isso em Python:

import requests
from bs4 import BeautifulSoup

url = 'https://olhardigital.com.br/tag/tecnologia/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Encontre os artigos
articles = soup.find_all('article', class_='categoria-tecnologia')

# Analise os 10 primeiros artigos
for i in range(10):
  title = articles[i].find('h3').text.strip()
  link = articles[i].find('a')['href']
  print(f'Título: {title}\nLink: {link}\n')

# Analise o 11º artigo
article = articles[10]
link = article.find('a')['href']

# Acesse o link do artigo para extrair o texto da notícia

# Gere um título baseado no conteúdo da notícia
# ... 

print(f'Notícia: {news_text}\nTítulo gerado: {generated_title}') 

```
2. Ação:
```
Acesse o arquivo em anexo "Extract_tecmundo.csv" e selecione os 10 primeiras publicações, identifique o padrão dos títulos e das suas respectivas notícias e quando chegar no décima primeira publicação, apresente somente a notícia e gere um título. Informe se existiu alguma técnica ou padrão;
```
* Prompt:
```
Análise das 10 primeiras publicações do Tecmundo:
Observando os títulos e links do arquivo "Extract_tecmundo.csv", podemos identificar alguns padrões:
1. Notícias Diárias:
Título: "10 notícias de tecnologia para você começar o dia (XX/XX)"
XX/XX representa a data da publicação.
Indica um resumo diário com as principais notícias de tecnologia.
Link: https://www.tecmundo.com.br/internet/XXXXXXXX-10-noticias-tecnologia-voce-comecar-dia-XX-XX.htm
XXXXXXXX representa um ID único para a notícia.
XX-XX representa a data da publicação.
1. Notícias da Semana:
Título: "10 notícias mais importantes da semana (XX/XX a XX/XX)"
XX/XX a XX/XX representa o período da semana.
Indica um resumo semanal com as notícias mais relevantes.
Link: https://www.tecmundo.com.br/internet/XXXXXXXX-10-noticias-importantes-semana-XX-XX-XX-XX.htm
XXXXXXXX representa um ID único para a notícia.
XX-XX-XX-XX representa o período da semana.
1. Notícias Individuais:
Título: Variável, descrevendo o tema da notícia.
Link: https://www.tecmundo.com.br/categoria/XXXXXXXX-titulo-da-noticia.htm
categoria representa a categoria da notícia, como "ciencia", "mercado", "software", etc.
XXXXXXXX representa um ID único para a notícia.
titulo-da-noticia é o título da notícia em formato slug (separado por hífens).
Décima Primeira Publicação:
Notícia: (Acessar o link da décima primeira publicação no arquivo CSV para obter o texto completo da notícia)
Título Gerado: "Comece o dia atualizado: as 10 notícias de tecnologia mais importantes de 01/05".
Técnica/Padrão:
O título gerado segue o padrão das notícias diárias, incluindo a data (01/05) e a frase "Comece o dia atualizado" para torná-lo mais chamativo.
Conclusão:
O Tecmundo utiliza um padrão consistente para seus títulos e links, o que facilita a identificação do tipo de notícia e a navegação no site. As notícias diárias e semanais fornecem um resumo das principais notícias, enquanto as notícias individuais abordam temas específicos com mais detalhes.
```
  