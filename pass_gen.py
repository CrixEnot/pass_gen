import random, string
digits = '0123456789'
lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
punctuation = string.punctuation
ex_letters = 'lil1Lo0O'
chars = []
num_pass,upper_pass,lower_pass,spec_pass,bad_sim_pass = '','','','',''
cnt_pass = int(input('Добро пожаловать в генератор пароль от ноунейма!\nПеред реализацией Вашего пароля я попрошу ответить Вас на несколько вопросов.\n1) Сколько паролей Вам сгенерить? Введите количество: '))
len_pass = int(input('2) Какой длины должны быть пароли? Введите длину: '))
if cnt_pass < 1 or len_pass < 1: 
    print('Иди на хуй')
    quit()
num_pass = input(f'3) Включать ли цифры "{digits}"? Введите д - да, н - нет: ')
if num_pass.lower() == 'д': chars.extend(digits)
upper_pass = input(f'4) Включать ли прописные буквы "{uppercase_letters}"? Введите д - да, н - нет: ')
if upper_pass.lower() == 'д': chars.extend(uppercase_letters)
lower_pass = input(f'5) Включать ли строчные буквы "{lowercase_letters}"? Введите д - да, н - нет: ')
if lower_pass.lower() == 'д': chars.extend(lowercase_letters)
spec_pass = input(f'6) Включать ли символы "{punctuation}"? Введите д - да, н - нет: ')
if spec_pass.lower() == 'д': chars.extend(punctuation)
bad_sim_pass = input(f'7) Исключать ли неоднозначные символы "{ex_letters}"? Введите д - да, н - нет: ')
if bad_sim_pass.lower() == 'д':
    for i in chars:
        if i in list(ex_letters):
            chars.remove(i)
for i in range(cnt_pass):
    print(*random.sample(chars, len_pass), sep = '')

