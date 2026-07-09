import json

with open("plants.ipynb", "r", encoding="utf-8") as f:
    nb = json.load(f)

for idx, cell in enumerate(nb.get("cells", [])):
    if cell.get("cell_type") == "code":
        source = cell.get("source", [])
        if any("plt.subplot(1, 2, 1)" in line for line in source) and any("comparison_plot_path" in line for line in source):
            print(f"Cell Index: {idx}")
            break
