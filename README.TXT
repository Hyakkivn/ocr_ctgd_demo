# 📄 OCR CTGD DEMO – DONUT OCR SMART ASSISTANT

Ứng dụng nhận diện và xử lý ảnh **Chứng Thư Giám Định** ngành than bằng AI thông minh – sử dụng mô hình **Donut (Document Understanding Transformer)**.

---

## 🧠 CÔNG NGHỆ SỬ DỤNG
- Donut (HuggingFace Transformers – `naver-clova-ix/donut-base`)
- PyTorch, Transformers, Sentencepiece
- Python 3.10+
- Corrections theo ngành nghề
- Tự động mapping dữ liệu OCR → file Excel

---

## 📂 CẤU TRÚC THƯ MỤC
```
ocr_ctgd_demo/
├── main.py                        # Chạy toàn bộ pipeline OCR
├── app/
│   ├── infer.py                  # Donut OCR xử lý ảnh
│   ├── template_engine.py        # Mapping JSON → Excel
│   ├── corrections_handler.py    # Áp lỗi chính tả OCR
│   └── excel_writer.py           # Xuất file Excel
├── data/chung_thu_giam_dinh/
│   ├── template.json
│   ├── corrections.json
│   ├── goods.json
│   ├── vehicle_names.json
│   └── dictionary_vi.json
├── datasets/chung_thu_giam_dinh/raw_images/   # Ảnh đầu vào
├── output/                       # File Excel đầu ra
├── README.md
└── README_HDSD.txt              # Hướng dẫn sử dụng chi tiết
```

---

## 🚀 CÁCH CHẠY DEMO (SAU KHI TẢI VỀ)
```bash
pip install -r requirements.txt
python main.py
```

File kết quả nằm trong: `output/ctgd_output_demo.xlsx`

---

## ✅ MỤC TIÊU DEMO
- OCR toàn bộ ảnh CT giám định
- Tự sửa lỗi phổ biến bằng `corrections.json`
- Mapping chính xác từng trường → vị trí Excel
- Ghi file Excel đúng định dạng (%, số, float)

---

## 🧭 DÀNH CHO DEV
Đây là bản demo, có thể mở rộng cho nhiều ngành khác:
- Chứng thư y tế
- Hóa đơn vận chuyển
- Phiếu giao nhận, hợp đồng PDF scan...

Template, corrections, dictionary... sẽ chia theo từng ngành trong `data/`.

---

*Được phát triển bởi Trì Ca & Team Dev GPT – dưới sự chỉ đạo chiến lược của CEO Tống Thư Hàng.*

