a=list(input('Чотирицифрове натуральне число - '))
print(f'Добуток цифр - {int(a[0])*int(a[1])*int(a[2])*int(a[3])}')
print(f'В реверсному порядку - {"".join(a[::-1])}')
print(f'Сортовані цифри - {"".join(sorted(a))}')