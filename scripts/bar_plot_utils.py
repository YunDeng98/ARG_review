import numpy as np
import os
import matplotlib.pyplot as plt


# Separate function to load arrays from files
def load_array(folder, prefix):
    file_path = os.path.join(folder, f"{prefix}_clades.txt")
    return np.loadtxt(file_path)

def read_and_compare(folder_names, prefixes):
    # Initialize the reference arrays for each prefix in the first folder
    reference_arrays = [load_array(folder_names[0], prefix) for prefix in prefixes]

    # Initialize a list to store average differences for each non-reference folder
    average_differences = []

    # Iterate over each folder, skipping the first one (reference folder)
    for folder in folder_names[1:]:
        differences = []
        print(folder)
        # Compare each prefix file in the current folder to the corresponding reference
        for i, prefix in enumerate(prefixes):
            print(i)
            current_array = load_array(folder, prefix)
            # Count the differences and store them
            differences.append(np.sum(current_array != reference_arrays[i])/np.size(reference_arrays[i]))

        # Calculate the average difference for this folder
        average_diff = np.mean(differences)
        average_differences.append(average_diff)
    
    print(average_differences)
    return average_differences

def plot_bar_plot(results_50, results_300, methods_50, methods_300, colors_50, colors_300, u, filename):
    plt.figure(figsize = [8, 6]);
    x = [0.05, 0.96]
    width=0.12
    i = 0
    for error in results_50:
        bar = plt.bar(x[0] + width * (i - 0.5), error, width=width, label=methods_50[i], color=colors_50[i])
        plt.text(bar[0].get_x() + bar[0].get_width() / 2, error, f'{error:.2f}', ha='center', va='bottom')
        i += 1
    i = 0
    for error in results_300:
        if methods_300[i] not in methods_50:
            bar = plt.bar(x[1] + width * (i - 0.5), error, width=width, label=methods_300[i], color=colors_300[i])
            plt.text(bar[0].get_x() + bar[0].get_width() / 2, error, f'{error:.2f}', ha='center', va='bottom')
            i += 1
        else:
            bar = plt.bar(x[1] + width * (i - 0.5), error, width=width, color=colors_300[i])
            plt.text(bar[0].get_x() + bar[0].get_width() / 2, error, f'{error:.2f}', ha='center', va='bottom')
            i += 1
    plt.xticks(fontsize=0);
    plt.yticks(fontsize=25);
    plt.xlim([-0.2, 1.5]);
    plt.ylim([0, u]);
    plt.legend(fontsize=18);
    plt.savefig(filename, dpi=300);
