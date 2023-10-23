import argparse

RESISTOR_FILE = './resistors.txt'
RES_VALS = [] # To be filled later

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("target_resistor", type=float, metavar="target-resistor", help="Target resistor value to be found.")
    parser.add_argument("-r", "--resistor-file", help="Path for file showing list of resistor values.")
    parser.add_argument("-t", "--tolerance", type=float, help="Target tolerance in percent for resistor network to be within target resistor value.", default=1)
    args = parser.parse_args()


    if args.resistor_file:
        try:
            RES_VALS = get_resistors_from_file(args.resistor_file)
        except FileNotFoundError as e:
            print("Error:", e)
            exit()
    else:
        RES_VALS = get_resistors_from_file(RESISTOR_FILE)
        
    get_prime_pair(args.target_resistor, tol=args.tolerance)

def get_prime_pair(target_val, r1=None, tol=1, count=0):
    count += 1
    if count == 10:
        print("Recursive Limit reached")
        return 

    vals = []
    for func in [series, parallel, select]:
        val1_potential = RES_VALS if r1 == None else [r1]
        
        for val1 in val1_potential:
            for val2 in RES_VALS:
                final_val = func(val1, val2)
                vals.append({
                    'rs': [val1] if func == select else [val1, val2],
                    'val': final_val,
                    'method': func.__name__
                })
    diffs = [val['val'] - target_val for val in vals]
    diffs_abs = [abs(x) for x in diffs]
    index = diffs_abs.index(min(diffs_abs))
    
    method = vals[index]['method']
    resistors = vals[index]['rs']
    val = vals[index]['val']
    diff = diffs[index]
    print(f"Method: {method} with resistor{'s' if method != select.__name__ else ''}: {resistors}")
    print(f"Resulting resistance: {val:.3f} Ohms | Off by {diff:.3f} Ohms ({diff/target_val*100:.2f}%)\n")
    resulting_val = vals[index]['val']
    if abs(resulting_val-target_val) < target_val * tol/100:
        return
    if method == 'select':
        print("Couldn't obtain desired tolerance.")
        return
    res = get_prime_pair(target_val, vals[index]['val'], count=count, tol=tol)
    if res == None:
        return

def get_resistors_from_file(resistor_file):
    res_vals = []
    with open(resistor_file) as res_file:
        for val in res_file.readlines():
            try:
                RES_VALS.append(float(val.split('#')[0].translate({ord('\n'): None})))
            except Exception as e:
                continue
    return res_vals
    

def series(r1, r2):
    return r1 + r2

def parallel(r1, r2):
    return r1*r2/(r1+r2)

def select(r1, r2):
    return r1

if __name__ == '__main__':
    main()