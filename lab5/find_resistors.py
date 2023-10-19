RES_VALS_SHORT = [1, 1.5, 2.2, 3.3, 4.7, 6.8]
RES_VALS = []
for i in range(0, 6):
    RES_VALS += [x * 10 ** i for x in RES_VALS_SHORT]
# RES_VALS += []
RES_VALS.remove(150e3)
RES_VALS.remove(1500)
METHODS = ['series', 'parallel']


def main():
    target_val = 184.917e3
    get_prime_pair(target_val)
    print("NEW ONE\n\n")
    get_prime_pair(1300, tol=1)
    print("NEW ONE\n\n")
    get_prime_pair(1690, tol=1)

def get_prime_pair(target_val, r1=None, tol=5, count=0):
    count += 1
    if count == 10:
        print("Recursive Limit reached")
        return 

    vals = []
    for func in [series, parallel]:
        val1_potential = RES_VALS if r1 == None else [r1]
        
        for val1 in val1_potential:
            for val2 in RES_VALS:
                final_val = func(val1, val2)
                vals.append({
                    'rs': [val1, val2],
                    'val': final_val,
                    'method': METHODS[[series, parallel].index(func)]
                })
    diffs = [target_val - val['val'] for val in vals]
    diffs_abs = [abs(x) for x in diffs]
    index = diffs_abs.index(min(diffs_abs))
    
    method = vals[index]['method']
    resistors = vals[index]['rs']
    val = vals[index]['val']
    diff = diffs[index]
    print(f"Method: {method} with Resistors: {resistors}")
    print(f"Resulting resistance: {val}\nWith a difference from target of: {diff}")
    print('--')
    resulting_val = vals[index]['val']
    if abs(resulting_val-target_val) < target_val * tol/100:
        return
    res = get_prime_pair(target_val, vals[index]['val'], count=count)
    if res == None:
        return

def series(r1, r2):
    return r1 + r2

def parallel(r1, r2):
    return r1*r2/(r1+r2)

if __name__ == '__main__':
    main()