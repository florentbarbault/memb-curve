import numpy as np
import math
import statistics

def calculate_geometry(input_file, output_file):
    """
    Calculates geometric and statistical properties of atoms.

    Args:
        input_file (str): Path to the input file (phosphorus.pdb).
        output_file (str): Path to the output file (radii_vs_time.dat).
    """
    radii = []
    index = 1
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            lines = infile.readlines()[1:]

            points = []
            for line in lines:
                words = line.split()
                if words and words[0] == 'ATOM':
                    try:
                        x = float(words[6])
                        y = float(words[7])
                        z = float(words[8])
                        points.append([x, y, z])
                    except (ValueError, IndexError):
                        print(f"Incorrect line ignored: {line.strip()}")
                elif words and words[0] == 'END' and points:
                    points = np.array(points)

                    # 1. Point B (minimum z coordinate)
                    B_index = np.argmin(points[:, 2])
                    B = points[B_index]

                    # 2. Points A and C (maximum AC distance)
                    max_dist_AC = 0
                    A, C = None, None
                    for i in range(len(points)):
                        for j in range(i + 1, len(points)):
                            dist_AC = np.linalg.norm(points[i] - points[j])
                            if dist_AC > max_dist_AC:
                                max_dist_AC = dist_AC
                                A = points[i]
                                C = points[j]
                    if A is not None and C is not None:
                        # 3. Distances AB and BC
                        AB = np.linalg.norm(A - B)
                        BC = np.linalg.norm(B - C)

                        # 4. Semi-perimeter
                        p = (AB + BC + max_dist_AC) / 2

                        # 5. Area (Heron's formula)
                        S = math.sqrt(p * (p - AB) * (p - BC) * (p - max_dist_AC))

                        # 6. Circumscribed circle radius
                        R = (BC * max_dist_AC * AB) / (4 * S)

                        outfile.write(f"{index} {R:.2f}\n")  # Format to 2 decimal places
                        radii.append(R)
                        index += 1
                        points = []
                    else:
                      print("Could not find A and C. Structure ignored")
                      points = []

            # Calculate mean and standard deviation after processing all structures
            if radii:
                mean_radius = statistics.mean(radii)
                std_dev_radius = statistics.stdev(radii)
                outfile.write(f"\nMean radius: {mean_radius:.2f}\n")  # Format to 2 decimal places
                outfile.write(f"Standard deviation of radii: {std_dev_radius:.2f}\n")  # Format to 2 decimal places
                print(f"Mean radius: {mean_radius:.2f}")
                print(f"Standard deviation of radii: {std_dev_radius:.2f}")
            else:
                outfile.write("No radius calculated.\n")
                print("No radius calculated.")

    except FileNotFoundError:
        print(f"Error: File {input_file} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_file = 'phosphorus.pdb'
output_file = 'radii_vs_time.dat'
calculate_geometry(input_file, output_file)
print(f"Results have been saved to: {output_file}")
