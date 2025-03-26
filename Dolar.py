#Aula Computational Thinking Using Python
#Programação
 
#Algoritmo: Converao_Reais_Dolares
 
reais = 0
cotacao_dolar = 0
conversao = 0
 
print("Bem vindo ao programa de conversão \n")
reais = float(input("Digite o valor que quer converter em reais:): \n")) #\n pula linha
cotacao_dolar = float(input("Digite a cotação do dólar de hoje:): \n"))
 
conversao = reais / cotacao_dolar
 
print("Com esta quantia é possivel comprar " + str (conversao)) #str é usado para converter um número em um texto. Pois o input não aceita números
print("Obrigado por usar nossos serviços")