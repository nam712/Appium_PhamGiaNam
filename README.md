# Appium Assignment - MSSV: BIT220114

## Ứng dụng được chọn

- **Tên ứng dụng:** Microsoft OneNote  
- **Danh mục con:** Ứng dụng quản lý học tập hoặc ghi chú học thuật
- **Lý do chọn:** Ứng dụng phổ biến, được sử dụng rộng rãi trong học tập và quản lý ghi chú. Phù hợp để kiểm thử các tính năng ghi chú và tìm kiếm.

## Test Cases

### **Test Case 1: Tạo ghi chú mới**

- **Mô tả:** Tạo một ghi chú mới, nhập nội dung `"hello appium"` vào ghi chú.
- **Kết quả mong đợi:** Ghi chú được tạo và nội dung hiển thị chính xác.
- **Kết quả thực tế:** Passed

### **Test Case 2: Chỉnh sửa ghi chú**

- **Mô tả:** Mở ghi chú vừa tạo, thêm 2 mục To-Do có nội dung `"check"` và `"done"`.
- **Kết quả mong đợi:** Các mục To-Do được thêm và hiển thị đúng.
- **Kết quả thực tế:** Passed 

### **Test Case 3: Xoá ghi chú**

- **Mô tả:** Xoá ghi chú vừa tao bằng cách vào menu More Options → Delete.
- **Kết quả mong đợi:** Ghi chú biến mất khỏi danh sách.
- **Kết quả thực tế:** Passed 


## Hướng Dẫn Cài Đặt Môi Trường Kiểm Thử Ứng Dụng Microsoft Onenote

### Giới Thiệu
Hướng dẫn này sẽ giúp bạn cài đặt môi trường để kiểm thử ứng dụng Onenote trên thiết bị ảo Android bằng Appium.

### Yêu Cầu 
- Java Development Kit (JDK)
- Node.js
- Python 3.8+

### Cài đặt 

1. Appium Server
Mở terminal và chạy lệnh sau để cài đặt Appium Server:
```bash
npm install -g appium
```
2. Android Studio
Tải và cài đặt Android Studio.

3. Cài đặt các thư viện cần thiết:
```bash
pip install Appium-Python-Client pytest
```

4. Tải Microsoft OneNote 

## Cách chạy chương trình

1. Chạy Appium Server
Mở terminal và chạy lệnh sau:
```bash
appium
```
2. Chạy Kiểm Thử
```bash
pytest tests/test.py
```

## Video chạy kiểm thử
[Xem video](./videos/demo_appium.mp4)

## Hình ảnh kiểm thử 
<p align="center">
  <img src="screenshots/test1.png" alt="Test Case 1" width="250"/>
  <img src="screenshots/test2.png" alt="Test Case 2" width="250"/>
  <img src="screenshots/test3.png" alt="Test Case 3" width="250"/>
</p>