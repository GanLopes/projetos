print ('Promoção atacadão')
valor = float(input('digite o valor do produto: '))
quantidade = float(input('quantidade de produto comprado: '))

final = valor * quantidade
desconto_1 = final * 0.1
desconto_2 = final * 0.2
desconto_3 = final * 0.3
desconto_4 = final * 0.4
if final < 100:
    print ('O valor da conta é de R$ ' ,(final))
elif final > 100 and final < 199:
    print ('O valor da conta é de R$ ' ,(final - desconto_1))
elif final > 200 and final < 299:
    print ('O valor da conta é de R$ ',(final - desconto_2))
elif final > 300 and final < 400:
    print ('O valor da conta é de R$ ' ,(final - desconto_3))
else:
    print ('O valor da conta é de R$ ' , (final - desconto_4))
