import pyautogui
from time import sleep  

# -Passos manuais para realizar esse processo


# 1- Clicar e digitar meu usuário
pyautogui.click(1003,546,duration=2)
pyautogui.write('roger')
# 2- clicar e digitar minha senha
pyautogui.click (977,566,duration=2)
pyautogui.write('123456')
# 3- clicar em entrar
pyautogui.click (878,599,duration=2)
# 4- extair cada produto
with open ('produtos.txt','r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]

# 	1 CLICAR E DIGITAR PRODUTO
pyautogui.click(691,526,duration=0.5)
pyautogui.write(produto)
# 	2 CLICAR E DIGITAR QUANTIDADE
pyautogui.click(674,553,duration=0.5)
pyautogui.write(quantidade)
#  	3 CLICAR E DIGITAR O PRECO
pyautogui.click(680,579,duration=0.5)
pyautogui.write(preco)

# 	4 clicar em registrar
pyautogui.click (603,743,duration=0.5)
sleep(1)
 