# decisão P4

idade = int(input('Digite sua idade:'))
if(idade < 18):
    print('Idade inferior a permitida')
elif(idade == 18):
    print('idade correta, pode se alistar')
else:
    print('idade superior a permitida')
