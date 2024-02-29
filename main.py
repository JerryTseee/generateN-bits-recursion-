def generate_n_bit_strings(n, bit_string=''):
    if len(bit_string) == n:
        print(bit_string)
        return
    else:
        #Append '0' and explore to the deep
        generate_n_bit_strings(n, bit_string + '0')
        #Append '1' and explore to the deep
        generate_n_bit_strings(n, bit_string + '1')

# Example usage:
n = 3
generate_n_bit_strings(n)
