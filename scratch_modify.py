import json

notebook_path = "plants.ipynb"

# Read the notebook
with open(notebook_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

modified = False
for cell in nb.get("cells", []):
    if cell.get("cell_type") == "code":
        source = cell.get("source", [])
        # Check if this cell is the dataset loader block
        if any("โหลดข้อมูลรูปภาพความเร็วสูงมาที่ SSD ของ Colab ชั่วคราว" in line for line in source):
            new_source = [
                "# โหลดข้อมูลรูปภาพความเร็วสูงมาที่ SSD ของ Colab ชั่วคราว (รันทุกครั้งที่เริ่มรัน Session ใหม่)\n",
                "import os\n",
                "if os.path.exists('/content/drive/MyDrive/Colab Notebooks/plants/dataset.zip'):\n",
                "    print(\"📦 กำลังคัดลอกไฟล์ dataset.zip จาก Google Drive มายังเครื่อง Colab ชั่วคราว...\")\n",
                "    !cp \"/content/drive/MyDrive/Colab Notebooks/plants/dataset.zip\" \"/content/dataset.zip\"\n",
                "    \n",
                "    print(\"📂 กำลังสร้างโฟลเดอร์ dataset และแตกไฟล์ dataset.zip ลงบนพื้นที่ Local SSD...\")\n",
                "    os.makedirs('/content/dataset', exist_ok=True)\n",
                "    !unzip -q \"/content/dataset.zip\" -d \"/content/dataset/\"\n",
                "    print(\"✅ โหลดและจัดเตรียมชุดข้อมูลบน Local SSD เรียบร้อยแล้ว! (พร้อมสำหรับเทรนความเร็วสูง)\")\n",
                "else:\n",
                "    print(\"⚠️ ไม่พบไฟล์ dataset.zip บน Google Drive ระบบจะเทรนโดยดึงจาก Drive โดยตรงแทน (ซึ่งจะช้ากว่า)\")\n"
            ]
            cell["source"] = new_source
            modified = True
            print("Cell successfully modified.")
            break

if modified:
    # Write back the notebook
    with open(notebook_path, "w", encoding="utf-8") as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)
    print("Notebook saved.")
else:
    print("Target cell not found!")
