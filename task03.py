import timeit
import random
import string
import matplotlib.pyplot as plt
from task03_alg01 import kmp_search
from task03_alg02 import boyer_moore_search
from task03_alg03 import rabin_karp_search

def draw_graph(x, y, x_label, y_label, title, filename):
    fig, ax = plt.subplots()
    for algo in algorithm_colors:
        ax.plot(x, y[algo], 
                f'{algorithm_colors[algo]}o', 
                label=algo, 
                markersize=5, 
                alpha=0.67)
    
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    ax.legend()
    ax.grid(True)
    plt.savefig(filename)

# Let's read input files
article1 = ""
article2 = ""

with open("./article1.txt","r") as f:
    article1 = "".join(f.readlines())

with open("./article2.txt","r") as f:
    article2 = "".join(f.readlines())

text_length = min(len(article1), len(article2))

REPEATS_PER_TEST = 10
NUMBER_OF_TESTS = 10
pattern_sizes = [10]*NUMBER_OF_TESTS +\
                [50]*NUMBER_OF_TESTS +\
                [100]*NUMBER_OF_TESTS +\
                [150]*NUMBER_OF_TESTS +\
                [200]*NUMBER_OF_TESTS

algorithms = {
    "Knuth-Morris-Pratt": kmp_search,
    "Boyer-Moore": boyer_moore_search,
    "Rabin-Karp": rabin_karp_search
}

algorithm_colors = {
    "Knuth-Morris-Pratt": "k",
    "Boyer-Moore": "r",
    "Rabin-Karp": "b",
}

algo_result_1 = { algo:[] for algo in algorithms }
algo_result_2 = { algo:[] for algo in algorithms }
algo_result_1_random = { algo:[] for algo in algorithms }
algo_result_2_random = { algo:[] for algo in algorithms }
algo_result_1_ab = { algo:[] for algo in algorithms }
algo_result_2_ab = { algo:[] for algo in algorithms }
start_positions = [random.randint(0,text_length-n-1) for n in pattern_sizes]
random_string_1 = []
random_string_2 = []
for i in range(len(pattern_sizes)):
    random_string_1.append("".join([random.choice(string.ascii_letters) for _ in range(pattern_sizes[i])]))
    random_string_2.append("".join([random.choice("ab") for _ in range(pattern_sizes[i])]))

for algo in algorithms:
    for i in range(len(pattern_sizes)):
        n = pattern_sizes[i]
        start = start_positions[i]
        pattern1 = article1[start:start+n]
        pattern2 = article2[start:start+n]
        algo_result_1[algo].append(timeit.timeit('algorithms[algo](article1,pattern1)', number=REPEATS_PER_TEST, globals=globals()))
        algo_result_2[algo].append(timeit.timeit('algorithms[algo](article2,pattern2)', number=REPEATS_PER_TEST, globals=globals()))
        algo_result_1_random[algo].append(timeit.timeit('algorithms[algo](article1,random_string_1[i])', number=REPEATS_PER_TEST, globals=globals()))
        algo_result_2_random[algo].append(timeit.timeit('algorithms[algo](article2,random_string_1[i])', number=REPEATS_PER_TEST, globals=globals()))
        algo_result_1_ab[algo].append(timeit.timeit('algorithms[algo](article1,random_string_2[i])', number=REPEATS_PER_TEST, globals=globals()))
        algo_result_2_ab[algo].append(timeit.timeit('algorithms[algo](article2,random_string_2[i])', number=REPEATS_PER_TEST, globals=globals()))

draw_graph(
    pattern_sizes,
    algo_result_1,
    'Pattern size',
    f'Time for {REPEATS_PER_TEST} experiments, sec',
    'Algorithms performance from pattern size for matching pattern, text 1',
    "./01_matching_pattern_size.png"
)

draw_graph(
    pattern_sizes,
    algo_result_2,
    'Pattern size',
    f'Time for {REPEATS_PER_TEST} experiments, sec',
    'Algorithms performance from pattern size for matching pattern, text 2',
    "./02_matching_pattern_size.png"
)

draw_graph(
    start_positions,
    algo_result_1,
    'matching position',
    f'Time for {REPEATS_PER_TEST} experiments, sec',
    'Algorithms performance from position for matching pattern, text 1',
    "./01_matching_position.png"
)

draw_graph(
    start_positions,
    algo_result_2,
    'matching position',
    f'Time for {REPEATS_PER_TEST} experiments, sec',
    'Algorithms performance from position for matching pattern, text 2',
    "./02_matching_position.png"
)

draw_graph(
    pattern_sizes,
    algo_result_1_random,
    'Pattern size',
    f'Time for {REPEATS_PER_TEST} experiments, sec',
    'Algorithms performance from pattern size for non-matching pattern, text 1',
    "./01_random.png"
)

draw_graph(
    pattern_sizes,
    algo_result_2_random,
    'Pattern size',
    f'Time for {REPEATS_PER_TEST} experiments, sec',
    'Algorithms performance from pattern size for non-matching pattern, text 2',
    "./02_random.png"
)

draw_graph(
    pattern_sizes,
    algo_result_1_ab,
    'Pattern size',
    f'Time for {REPEATS_PER_TEST} experiments, sec',
    'Algorithms performance from pattern size for non-matching pattern, text 1',
    "./01_ab.png"
)

draw_graph(
    pattern_sizes,
    algo_result_2_ab,
    'Pattern size',
    f'Time for {REPEATS_PER_TEST} experiments, sec',
    'Algorithms performance from pattern size for non-matching pattern, text 2',
    "./02_ab.png"
)