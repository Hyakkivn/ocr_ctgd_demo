from app.infer import run_ocr
from app.template_engine import map_fields_to_excel
from app.corrections_handler import apply_corrections
from app.excel_writer import write_to_excel
import os

INPUT_FOLDER = "datasets/chung_thu_giam_dinh/raw_images"
OUTPUT_FOLDER = "output"
TEMPLATE_PATH = "data/chung_thu_giam_dinh/template.json"
CORRECTIONS_PATH = "data/chung_thu_giam_dinh/corrections.json"


def main():
    print("🔍 Đang quét thư mục ảnh...")
    image_files = [f for f in os.listdir(INPUT_FOLDER) if f.endswith(('.jpg', '.png', '.jpeg'))]

    for image_file in image_files:
        print(f"\n📸 Xử lý ảnh: {image_file}")
        image_path = os.path.join(INPUT_FOLDER, image_file)

        # Step 1: OCR bằng Donut
        ocr_result = run_ocr(image_path)

        # Step 2: Áp corrections theo ngành CTGD
        corrected_result = apply_corrections(ocr_result, CORRECTIONS_PATH)

        # Step 3: Mapping sang Excel template
        excel_data = map_fields_to_excel(corrected_result, TEMPLATE_PATH)

        # Step 4: Xuất ra Excel
        output_file = os.path.join(OUTPUT_FOLDER, f"{os.path.splitext(image_file)[0]}.xlsx")
        write_to_excel(excel_data, output_file)

        print(f"✅ Đã xuất: {output_file}")


if __name__ == "__main__":
    main()
