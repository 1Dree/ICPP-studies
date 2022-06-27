# printar um par de numeros root e pwr tal que 1 < pwr < 6 e root**pwr
# resulte no numero dado como input.
x = int(input(""));
abs_x = abs(x);
root = 0;
pwr = None;
pwr_guess_range = range(2, 6);

while root < abs_x:
    if (abs_x%2 != 0 and abs_x%5 != 0) or pwr: break;
    root += 1;
    for pwr_guess in pwr_guess_range:
        if root**pwr_guess == abs_x:
            if x < 0: root = -root;
            print("hello");
            pwr = pwr_guess;
            break;
            
print(root, pwr) if pwr else print("no such pair");
