import re
import matplotlib.pyplot as plt
import numpy as np
import sys
from collections import defaultdict

def parse_file(filename, scaling):
    data = defaultdict(lambda: {"total_time": []})
    
    with open(filename, 'r') as file:
        current_scaling = None
        num_pes = None
        for line in file:
            line = line.strip()
        
            match_num_pes = re.search(r"Number of PEs: (\d+)", line)
            if match_num_pes:
                num_pes = int(match_num_pes.group(1))
                continue
            
            match_scaling_type = re.search(r"(STRONG|WEAK|WEAK_ISOBUCKET) Scaling", line)
            if match_scaling_type:
                current_scaling = match_scaling_type.group(1)
                continue
            
            if current_scaling == scaling and num_pes is not None:
                match_total_time = re.search(r"Average total time \(per PE\): ([\d\.]+)", line)
                
                if match_total_time:
                    data[num_pes]["total_time"].append(float(match_total_time.group(1)))
    
    min_data = {"num_pes": [], "min_total_time": []}
    
    for num_pes, times in sorted(data.items()):
        min_data["num_pes"].append(num_pes)
        min_data["min_total_time"].append(np.min(times["total_time"]))
    
    print(filename)
    for num in min_data["min_total_time"]:
        print(num)
    print(min_data["num_pes"])

    return min_data

def plot_data(datasets, labels, scaling):
    if not any(dataset["num_pes"] for dataset in datasets):
        print(f"No data found for {scaling} scaling.")
        return
    
    plt.figure(figsize=(14, 8), facecolor="white")
    colors = ["#FF0000", "#0000FF", "#FFA500", "#008000", "#800080"]  # Distinct primary colors
    markers = ['o', 's', 'D', 'X', '^']
    linestyles = ['-', '--', '-.', ':', '-']
    
    for dataset, label, color, marker, linestyle in zip(datasets, labels, colors, markers, linestyles):
        if dataset["num_pes"]:
            plt.plot(dataset["num_pes"], dataset["min_total_time"], marker=marker, linestyle=linestyle, 
                     color=color, linewidth=4, label=f'{label} Total Time')
            for x, y in zip(dataset["num_pes"], dataset["min_total_time"]):
                plt.text(x, y, f'{y:.2f}', fontsize=12, ha='right', color=color)
    
    plt.xscale("log", base=2)
    plt.xlabel("Number of cores", fontsize=16, fontweight='bold', color='black')
    plt.ylabel("Execution Time (s)", fontsize=16, fontweight='bold', color='black')
    plt.legend(fontsize=14, facecolor='white', framealpha=1, edgecolor='black')
    plt.grid(True, linestyle='--', alpha=0.7, color='gray')
    plt.tick_params(axis='both', which='major', labelsize=14, colors='black')
    plt.title(f"{scaling} Scaling", fontsize=20, fontweight='bold', color="black")
    
    plt.tight_layout()
    plt.savefig(f"{scaling.lower()}_scaling_comparison.png", dpi=300)
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <scaling_index>")
        print("0: STRONG, 1: WEAK, 2: WEAK_ISOBUCKET")
        sys.exit(1)
    
    scaling_index = int(sys.argv[1])
    scaling_types = ["STRONG", "WEAK", "WEAK_ISOBUCKET"]
    if scaling_index < 0 or scaling_index >= len(scaling_types):
        print("Invalid scaling index. Use 0 for STRONG, 1 for WEAK, or 2 for WEAK_ISOBUCKET.")
        sys.exit(1)
    
    scaling = scaling_types[scaling_index]
    # filenames = [
    #     "Actor/actor_onemsg_isx", "Actor/actor_chunked_isx", "SHMEM/shmem_isx", "MPI/mpi_isx", "MPI-onesided/mpi-one-sided_isx"
    # ]
    filenames = [
        "results/actor_onemsg_isx", "results/actor_chunked_isx", "results/shmem_isx", "results/mpi_isx", "results/mpi-one-sided_isx"
    ]
    
    labels = ["Actor One-Msg", "Actor Chunked Message", "SHMEM", "MPI", "MPI-One-Sided"]
    
    datasets = [parse_file(filename, scaling) for filename in filenames]
    plot_data(datasets, labels, scaling)
