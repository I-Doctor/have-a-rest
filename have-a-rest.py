from tqdm import tqdm
import time
N = int(1e9)
T = 1e-2
MAX_LEN = 100

def parse_args():
    import argparse
    parser = argparse.ArgumentParser(description='i really wanna have a rest.')
    parser.add_argument('-n', '--iters', type=int, default=N, help='rest iters.')
    parser.add_argument('-f', '--frequency', type=float, default=1/T, help='rest frequency per iter.')
    args = parser.parse_args()
    return args

def have_a_rest():
    args = parse_args()
    str_ = ''
    for idx in tqdm(range(args.iters)):
        str_ = str_ + '  '
        if len(str_) > MAX_LEN:
            str_ = str_[MAX_LEN:]
        str_to_print = str_ + 'kaizhong faker'
        if idx % 10 < 5:
            print(str_to_print)
        else:
            print(str_to_print + str_to_print)
        time.sleep(1.0 / args.frequency)

if __name__ == '__main__':
    have_a_rest()
