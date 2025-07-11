def imei_check_digit(imei14: str) -> str:
    total = 0
    for i, char in enumerate(imei14):
        digit = int(char)
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit
    return str((10 - (total % 10)) % 10)

input_file = 'imei.txt'
output_file = 'kompletni_imei.txt'

with open(input_file, 'r', encoding='utf-8') as f_in, open(output_file, 'w', encoding='utf-8') as f_out:
    for line in f_in:
        imei14 = line.strip()
        if len(imei14) == 14 and imei14.isdigit():
            check_digit = imei_check_digit(imei14)
            full_imei = imei14 + check_digit
            f_out.write(full_imei + '\n')
        else:
            f_out.write(f'NEISPRAVAN: {imei14}\n')
