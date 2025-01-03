from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import quote  # P garantir que a mensagem seja codificada corretamente

# Função p enviar uma mensagem para um nmr
def enviar_mensagem(numero, mensagem):
    # Codificando a mensagem p garantir que não haja problemas com caracteres especiais
    mensagem_codificada = quote(mensagem)

    # Abrindo a conversa com o nmr no WhatsApp Web
    link = f"https://web.whatsapp.com/send?phone={numero}&text={mensagem_codificada}"
    driver.get(link)
    
    # Aguardar até que o campo de mensagem esteja visível
    try:
        # Espera a caixa de texto se tornar visível
        caixa_texto = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="1"]'))
        )
        # Clica na caixa de texto para garantir que o foco está lá
        caixa_texto.click()  
        # Envia a mensagem
        caixa_texto.send_keys(mensagem)  # Digita a mensagem
        caixa_texto.send_keys(Keys.RETURN)  # Simula pressionamento da tecla Enter para enviar a mensagem
        
        print(f"Mensagem enviada para {numero}")
        time.sleep(5)  # Espera para garantir que a mensagem foi enviada
    except Exception as e:
        print(f"Erro ao enviar mensagem para {numero}: {e}")

# Configurando o driver e abrindo o WhatsApp Web
driver = webdriver.Chrome(service=webdriver.chrome.service.Service(ChromeDriverManager().install()))
driver.get('https://web.whatsapp.com/')
time.sleep(30)  # Aguarde até que o WhatsApp Web carregue e você escaneie o QR code

# Lista de nmr de telefone e mensagem
numeros = ['5547996752886', '554488346775'] 
mensagem = "Mensagem teste"

# Enviando mensagens
for numero in numeros:
    enviar_mensagem(numero, mensagem)
    
# Fechando o navegador
driver.quit()
