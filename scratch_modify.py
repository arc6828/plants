import json
import os

notebook_path = "plants.ipynb"

# Read the notebook
with open(notebook_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

modified_cells = 0

for idx, cell in enumerate(nb.get("cells", [])):
    if cell.get("cell_type") != "code":
        continue
    
    source_str = "".join(cell.get("source", []))
    
    # 1. Modify Cell 19 (Fine-Tuning Loop)
    target_1 = 'model = tf.keras.models.load_model(frozen_model_path, compile=False)'
    if target_1 in source_str and "PART 8.2" in source_str:
        replacement_1 = """if name == 'MobileNetV2':
        preprocess_fn = tf.keras.applications.mobilenet_v2.preprocess_input
    elif name == 'EfficientNetB0':
        preprocess_fn = tf.keras.applications.efficientnet.preprocess_input
    elif name == 'ResNet50V2':
        preprocess_fn = tf.keras.applications.resnet_v2.preprocess_input
    else:
        preprocess_fn = None
    model = tf.keras.models.load_model(frozen_model_path, custom_objects={'preprocess_input': preprocess_fn} if preprocess_fn else None, compile=False)"""
        
        source_str = source_str.replace(target_1, replacement_1)
        # Convert back to list of lines with newlines
        cell["source"] = [line + "\n" for line in source_str.split("\n")]
        # Remove trailing newline from the last element if it was split
        if cell["source"] and cell["source"][-1] == "\n":
            cell["source"].pop()
        elif cell["source"]:
            cell["source"][-1] = cell["source"][-1].rstrip("\n")
        
        modified_cells += 1
        print(f"Modified Cell {idx} (Fine-tuning)")
        
    # 2. Modify Cell 23 (verify_plant_identity)
    target_2 = 'model = tf.keras.models.load_model(model_path, compile=False)'
    if target_2 in source_str and "def verify_plant_identity" in source_str:
        replacement_2 = """preprocess_fn = None
    if 'MobileNetV2' in model_path:
        preprocess_fn = tf.keras.applications.mobilenet_v2.preprocess_input
    elif 'EfficientNetB0' in model_path:
        preprocess_fn = tf.keras.applications.efficientnet.preprocess_input
    elif 'ResNet50V2' in model_path:
        preprocess_fn = tf.keras.applications.resnet_v2.preprocess_input

    model = tf.keras.models.load_model(model_path, custom_objects={'preprocess_input': preprocess_fn} if preprocess_fn else None, compile=False)"""
        
        source_str = source_str.replace(target_2, replacement_2)
        cell["source"] = [line + "\n" for line in source_str.split("\n")]
        if cell["source"] and cell["source"][-1] == "\n":
            cell["source"].pop()
        elif cell["source"]:
            cell["source"][-1] = cell["source"][-1].rstrip("\n")
            
        modified_cells += 1
        print(f"Modified Cell {idx} (verify_plant_identity)")

    # 3. Modify Cell 25 (export_to_tflite)
    target_3 = 'keras_model = tf.keras.models.load_model(h5_model_path, compile=False)'
    if target_3 in source_str and "def export_to_tflite" in source_str:
        replacement_3 = """preprocess_fn = None
    if 'MobileNetV2' in h5_model_path:
        preprocess_fn = tf.keras.applications.mobilenet_v2.preprocess_input
    elif 'EfficientNetB0' in h5_model_path:
        preprocess_fn = tf.keras.applications.efficientnet.preprocess_input
    elif 'ResNet50V2' in h5_model_path:
        preprocess_fn = tf.keras.applications.resnet_v2.preprocess_input

    keras_model = tf.keras.models.load_model(h5_model_path, custom_objects={'preprocess_input': preprocess_fn} if preprocess_fn else None, compile=False)"""
        
        source_str = source_str.replace(target_3, replacement_3)
        cell["source"] = [line + "\n" for line in source_str.split("\n")]
        if cell["source"] and cell["source"][-1] == "\n":
            cell["source"].pop()
        elif cell["source"]:
            cell["source"][-1] = cell["source"][-1].rstrip("\n")
            
        modified_cells += 1
        print(f"Modified Cell {idx} (export_to_tflite)")

if modified_cells > 0:
    # Write back the notebook
    with open(notebook_path, "w", encoding="utf-8") as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)
    print(f"Success: {modified_cells} cells modified and saved.")
else:
    print("Error: No cells were modified!")
