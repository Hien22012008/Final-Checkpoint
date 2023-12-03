n = int(input('Input n:'))

if n > 0:
   num_str = str(n)
   num_digits = len(num_str)
   print('This number has', num_digits,'(s)')
else:
   print('Please enter a number greater than 0')