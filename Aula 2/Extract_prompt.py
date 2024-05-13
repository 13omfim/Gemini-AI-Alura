from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import csv

# Configurar o Selenium
driver = webdriver.Chrome()
driver.get('https://www.tecmundo.com.br/tecnologia')

# Esperar que os elementos da página carreguem
wait = WebDriverWait(driver, 10)

# Rolando a página para carregar mais notícias
for i in range(3): 
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
  wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.tec--list__item'))) # Seletor CSS para artigos

# Obter o HTML completo após rolar a página
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

# Encontrar os artigos
articles = soup.find_all('div', class_='tec--list__item')

# Listas para armazenar os dados
titulos_links = []

# Analisar os artigos (considerando apenas os 11 primeiros)
for i in range(11):
    title_tag = articles[i].find('a', class_='tec--card__title__link')
    title = title_tag.text.strip() if title_tag else "Título não encontrado"
    link = title_tag['href'] if title_tag else "Link não encontrado"

    # Adicionar dados às listas
    titulos_links.append({'titulo': title, 'link': link})

    print(f'Título: {title}\nLink: {link}\n')

# Fechar o navegador
driver.quit()

# Salvar em arquivo .txt
with open('Extract_tecmundo.txt', 'w', encoding='utf-8') as f:
  for item in titulos_links:
    f.write(f"Título: {item['titulo']}\nLink: {item['link']}\n\n")

# Salvar em arquivo .csv
with open('Extract_tecmundo.csv', 'w', newline='', encoding='utf-8') as f:
  writer = csv.writer(f)
  writer.writerow(['Título', 'Link'])
  for item in titulos_links:
    writer.writerow([item['titulo'], item['link']])

print("Dados salvos em 'Extract_tecmundo.txt' e 'Extract_tecmundo.csv'")