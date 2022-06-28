x = 16;
epsilon = 0.01;
term = x;
origin = 0;
ans = (term + origin)/2;
num_guesses = 0;
        
# stops if the distance from ans**2 - x to 0 is less than 0.01
while (ans**2 - x) >= 0.01:
    num_guesses += 1;
    
    if ans**2 > x:
        term = ans;
    else:
        origin = ans;
        
    ans = (term + origin)/2;

print(x, ans, ans**2, num_guesses);
