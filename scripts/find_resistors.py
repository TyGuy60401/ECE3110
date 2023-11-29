import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("target_resistor", type=float,
                        metavar="target-resistor",
                        help="Target resistor value to be found.")
    parser.add_argument("-r", "--resistor-file", default="./resistors.txt",
                        help="Path for file showing list of resistor values.")
    parser.add_argument("-t", "--tolerance", type=float,
                        help="Target tolerance in percent \
                        for resistor network \
                        to be within target res value.",
                        default=1)
    args = parser.parse_args()

    try:
        res_vals = get_resistors_from_file(args.resistor_file)
    except FileNotFoundError as e:
        print("Error:", e)
        exit()

    get_prime_pair(args.target_resistor, tol=args.tolerance, res_vals=res_vals)


def get_prime_pair(target_val, r1=None, tol=1, count=0, res_vals=[]):
    count += 1
    if count == 40:
        print("Recursive Limit reached")
        return

    vals = []
    for func in [series, parallel, select]:
        val1_potential = res_vals if r1 is None else [r1]

        for val1 in val1_potential:
            for val2 in res_vals:
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
    plural_string = f"resistor{'s' if method != select.__name__ else ''}"
    print(f"Method: {method} with {plural_string}: {resistors}")
    print(f"Resulting resistance: {val:.3f} Ohms | \
            Off by {diff:.3f} Ohms ({diff/target_val*100:.2f}%)\n")
    resulting_val = vals[index]['val']
    if abs(resulting_val-target_val) < target_val * tol/100:
        return
    if method == 'select':
        print("Couldn't obtain desired tolerance.")
        return
    res = get_prime_pair(target_val, vals[index]['val'],
                         count=count, tol=tol,
                         res_vals=res_vals)
    if res is None:
        return


def get_resistors_from_file(resistor_file):
    res_vals = []
    with open(resistor_file) as res_file:
        for val in res_file.readlines():
            try:
                val = val.split('#')[0].translate({ord('\n'): None})
                res_vals.append(float(val))
            except Exception:
                continue
    return res_vals


def series(*rs):
    return sum(rs)


def parallel(*rs):
    total = 0
    for r in rs:
        total += 1 / r
    return 1 / total


def select(*rs):
    return rs[0]


if __name__ == '__main__':
    main()
