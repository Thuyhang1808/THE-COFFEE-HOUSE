import sys
import webbrowser
import pymysql
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from trangchu import Ui_MainWindow  # Import giao diện
from database import Database,connect_db  # Hàm kết nối MySQL


class EditDialog(QDialog):
    """Hộp thoại chỉnh sửa sản phẩm"""
    def __init__(self, parent, row):
        super().__init__(parent)
        self.setWindowTitle("Chỉnh sửa sản phẩm")
        self.setFixedSize(300, 200)

        self.row = row
        self.parent = parent
        self.table = parent.ui.tableWidget  # Lấy bảng từ cửa sổ chính

        # Lấy giá trị hiện tại từ bảng
        self.current_quantity = self.table.item(row, 2).text() if self.table.item(row, 2) else "1"
        self.current_price = self.table.item(row, 3).text() if self.table.item(row, 3) else "0"

        # Tạo giao diện hộp thoại chỉnh sửa
        layout = QVBoxLayout()

        self.label_quantity = QLabel("Số lượng:")
        self.input_quantity = QLineEdit(self.current_quantity)

        self.label_price = QLabel("Đơn giá:")
        self.input_price = QLineEdit(self.current_price)

        self.save_button = QPushButton("Lưu")
        self.save_button.clicked.connect(self.save_changes)

        layout.addWidget(self.label_quantity)
        layout.addWidget(self.input_quantity)
        layout.addWidget(self.label_price)
        layout.addWidget(self.input_price)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def save_changes(self):
        """Lưu thông tin chỉnh sửa vào bảng"""
        new_quantity = self.input_quantity.text()
        new_price = self.input_price.text()

        if new_quantity.isdigit() and new_price.replace(".", "", 1).isdigit():
            new_quantity = int(new_quantity)
            new_price = float(new_price)
            new_total = new_quantity * new_price  # Tính lại thành tiền

            # Cập nhật bảng
            self.table.setItem(self.row, 2, QTableWidgetItem(str(new_quantity)))  # Cập nhật số lượng
            self.table.setItem(self.row, 3, QTableWidgetItem(str(new_price)))  # Cập nhật đơn giá
            self.table.setItem(self.row, 4, QTableWidgetItem(str(new_total)))  # Cập nhật thành tiền

            # Kiểm tra nếu parent có hàm `tinh_tong_thanh_tien`, gọi nó để cập nhật tổng tiền
            if hasattr(self.parent, 'tinh_tong_thanh_tien'):
                self.parent.tinh_tong_thanh_tien()

            self.accept()  # Đóng hộp thoại
        else:
            print("❌ Vui lòng nhập số hợp lệ!")  # Có thể thay bằng QMessageBox để cảnh báo

class TrangChu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Kết nối CSDL
        self.conn = connect_db()
        if self.conn:
            print("✅ Kết nối cơ sở dữ liệu thành công!")
            self.load_order_details()
        else:
            print("❌ Không thể kết nối CSDL!")
            
        # Danh sách lưu trữ nhiều hóa đơn
        self.all_orders = []  # Lưu tất cả hóa đơn
        self.current_index = -1  # Vị trí của hóa đơn đang xem
        self.current_invoice_number = 1  # 🔹 Khởi tạo số hóa đơn


        # Kết nối các nút chức năng
        self.ui.pushButton_10.clicked.connect(self.dang_xuat)  # Đăng xuất
        self.ui.pushButton_15.clicked.connect(self.them_hoa_don)  # Thêm hóa đơn mới
        self.ui.pushButton_12.clicked.connect(self.lui_hoa_don)  # Lùi <<
        self.ui.pushButton_16.clicked.connect(self.tien_hoa_don)  # Tiến >>
        self.ui.pushButton_13.clicked.connect(self.xoa_san_pham)  # Xóa sản phẩm trong hóa đơn
        self.ui.pushButton_14.clicked.connect(self.sua_san_pham)  # Sửa sản phẩm trong hóa đơn
        self.ui.pushButton_17.clicked.connect(self.in_hoa_don)  # In hóa đơn
        self.ui.pushButton_18.clicked.connect(self.luu_hoa_don_csdl)  # Nút "Lưu hóa đơn"
        self.ui.pushButton_20.clicked.connect(self.thanh_toan)  # Thanh toán
        self.ui.lineEdit_3.returnPressed.connect(self.hien_thi_ma_don_hang)  # Nhấn Enter để tìm mã đơn hàng
        self.ui.pushButton_9.clicked.connect(self.ap_dung_khuyen_mai)
        

        # Gán sự kiện click cho các nút sản phẩm
        self.pushButton4 = QPushButton("Special Tea")
        self.pushButton5 = QPushButton("Coffee")
        self.pushButton2 = QPushButton("Bánh")
        self.pushButton6 = QPushButton("Topping")
        
        self.ui.product_buttons = [
            (self.ui.pushButton_37, "PhinDi Cassia", 55000),
            (self.ui.pushButton_38, "PhinDi Hạnh Nhân", 45000),
            (self.ui.pushButton_24, "PhinDi Choco", 45000),
            (self.ui.pushButton_26, "PhinDi Kem Sữa", 45000),
            (self.ui.pushButton_36, "Classic Phin Freeze", 55000),
            (self.ui.pushButton_35, "Freeze Sô-cô-la", 55000),
            (self.ui.pushButton_34, "Freeze Trà Xanh", 55000),
            (self.ui.pushButton_33, "Latte", 99000),
        ]

        for button, name, price in self.ui.product_buttons:
            button.clicked.connect(lambda _, n=name, p=price: self.chon_san_pham(n, p))

    def load_order_details(self):
        """Lấy dữ liệu từ bảng order_details và hiển thị lên tableWidget."""
        try:
            cursor = self.conn.cursor()
            query = "SELECT order_id, product_id, quantity, price, total FROM order_details"
            cursor.execute(query)
            rows = cursor.fetchall()

            self.ui.tableWidget.setRowCount(len(rows))
            self.ui.tableWidget.setColumnCount(5)
            self.ui.tableWidget.setHorizontalHeaderLabels(["Mã SP", "Tên sản phẩm", "Số lượng", "Đơn giá", "Thành tiền"])

            for row_index, row_data in enumerate(rows):
                for col_index, col_value in enumerate(row_data):
                    item = QTableWidgetItem(str(col_value))
                    self.ui.tableWidget.setItem(row_index, col_index, item)

            cursor.close()
            self.tinh_tong_thanh_tien()
        except pymysql.Error as e:
            print(f"❌ Lỗi khi tải dữ liệu: {e}")

    def chon_san_pham(self, ten_san_pham, don_gia):
        """Thêm sản phẩm vào bảng."""
        table = self.ui.tableWidget
        row_count = table.rowCount()

        for row in range(row_count):
            if table.item(row, 1) and table.item(row, 1).text() == ten_san_pham:
                so_luong = int(table.item(row, 2).text()) + 1
                thanh_tien = so_luong * don_gia
                table.setItem(row, 2, QTableWidgetItem(str(so_luong)))
                table.setItem(row, 4, QTableWidgetItem(str(thanh_tien)))
                self.tinh_tong_thanh_tien()
                return

        table.insertRow(row_count)
        table.setItem(row_count, 0, QTableWidgetItem(str(row_count + 1)))
        table.setItem(row_count, 1, QTableWidgetItem(ten_san_pham))
        table.setItem(row_count, 2, QTableWidgetItem("1"))
        table.setItem(row_count, 3, QTableWidgetItem(str(don_gia)))
        table.setItem(row_count, 4, QTableWidgetItem(str(don_gia)))

        self.tinh_tong_thanh_tien()

    def tinh_tong_thanh_tien(self):
        """Tính tổng thành tiền."""
        total_amount = 0
        for row in range(self.ui.tableWidget.rowCount()):
            item = self.ui.tableWidget.item(row, 4)
            if item and item.text():
                total_amount += float(item.text())

        self.ui.lineEdit_7.setText(str(total_amount))

    def them_hoa_don(self):
        """Thêm hóa đơn mới mà không mất dữ liệu cũ."""
        self.luu_hoa_don_hien_tai()
        self.ui.tableWidget.setRowCount(0)
        self.current_index = len(self.all_orders)  # Chuyển sang hóa đơn mới

    def lui_hoa_don(self):
        """Quay lại hóa đơn trước đó."""
        if self.current_index > 0:
            self.current_index -= 1
            self.khoi_phuc_hoa_don(self.current_index)

    def tien_hoa_don(self):
        """Tiến tới hóa đơn tiếp theo."""
        if self.current_index < len(self.all_orders) - 1:
            self.current_index += 1
            self.khoi_phuc_hoa_don(self.current_index)

    def luu_hoa_don_hien_tai(self):
        """Lưu lại hóa đơn hiện tại vào danh sách."""
        hoa_don = []
        for row in range(self.ui.tableWidget.rowCount()):
            row_data = []
            for col in range(self.ui.tableWidget.columnCount()):
                item = self.ui.tableWidget.item(row, col)
                row_data.append(item.text() if item else "")
            hoa_don.append(row_data)

        self.all_orders.append(hoa_don)

    def khoi_phuc_hoa_don(self, index):
        """Khôi phục hóa đơn từ danh sách."""
        self.ui.tableWidget.setRowCount(len(self.all_orders[index]))
        for row_idx, row_data in enumerate(self.all_orders[index]):
            for col_idx, col_value in enumerate(row_data):
                self.ui.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(col_value))
        self.tinh_tong_thanh_tien()

    def xoa_san_pham(self):
        """Xóa dòng đang chọn."""
        selected_row = self.ui.tableWidget.currentRow()
        if selected_row >= 0:
            self.ui.tableWidget.removeRow(selected_row)
            self.tinh_tong_thanh_tien()

    def sua_san_pham(self):
        """Mở hộp thoại chỉnh sửa sản phẩm"""
        selected_row = self.ui.tableWidget.currentRow()
        if selected_row >= 0:
            dialog = EditDialog(self, selected_row)  # ✅ Truyền self để EditDialog biết parent là TrangChu
            dialog.exec()  # ✅ Hiển thị hộp thoại modal
        else:
            print("❌ Vui lòng chọn một sản phẩm để sửa!")
            
    def in_hoa_don(self):
        """In hóa đơn và lưu lại nhiều hóa đơn"""
        danh_sach_san_pham = []
        for row in range(self.ui.tableWidget.rowCount()):
            ma_sp = self.ui.tableWidget.item(row, 0).text()
            ten_sp = self.ui.tableWidget.item(row, 1).text()
            so_luong = self.ui.tableWidget.item(row, 2).text()
            don_gia = self.ui.tableWidget.item(row, 3).text()
            thanh_tien = self.ui.tableWidget.item(row, 4).text()
            danh_sach_san_pham.append({
                "ma_sp": ma_sp,
                "ten_sp": ten_sp,
                "so_luong": so_luong,
                "don_gia": don_gia,
                "thanh_tien": thanh_tien
            })
        
        tong_tien = sum(float(sp["thanh_tien"]) for sp in danh_sach_san_pham)
        
        danh_sach_html = "".join(
            f"""
            <tr>
                <td>{sp['ma_sp']}</td>
                <td>{sp['ten_sp']}</td>
                <td>{sp['so_luong']}</td>
                <td>{sp['don_gia']}</td>
                <td>{sp['thanh_tien']}</td>
            </tr>
            """ for sp in danh_sach_san_pham
        )
        
        file_name = f"hoadon_{self.current_invoice_number}.html"
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(f"""
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Hóa Đơn Thanh Toán #{self.current_invoice_number}</title>
    <style>
        body {{ font-family: Arial, sans-serif; max-width: 400px; margin: auto; }}
        h2 {{ text-align: center; color: #333; }}
        table {{ width: 100%; border-collapse: collapse; }}
        th, td {{ border: 1px solid #ddd; padding: 10px; text-align: center; }}
        th {{ background-color: #007bff; color: white; }}
        .total {{ text-align: right; font-weight: bold; }}
    </style>
</head>
<body>
    <h2>HÓA ĐƠN #{self.current_invoice_number}</h2>
    <table>
        <tr><th>Mã SP</th><th>Tên SP</th><th>Số lượng</th><th>Đơn giá</th><th>Thành tiền</th></tr>
        {danh_sach_html}
    </table>
    <p class="total">Tổng cộng: {tong_tien} VND</p>
    <p style="text-align: center;">Cảm ơn quý khách! 😊</p>
</body>
</html>
""")
        
        self.current_invoice_number += 1  # Tăng số hóa đơn để lưu tiếp tục

        QMessageBox.information(self, "Thành công", f"Hóa đơn {self.current_invoice_number - 1} đã được lưu!")
        webbrowser.open(f"file://{os.path.abspath(file_name)}")


        
    def luu_hoa_don_csdl(self):
        """Lưu hóa đơn hiện tại vào CSDL"""

        # Kiểm tra kết nối CSDL trước khi thực hiện thao tác
        if not self.conn or not self.conn.open:
            QMessageBox.critical(self, "Lỗi CSDL", "❌ Kết nối CSDL không khả dụng!")
            return
        else:
            print("✅ Kết nối CSDL thành công!")

        try:
            cursor = self.conn.cursor()

            # 🔹 Lấy tổng tiền từ UI và kiểm tra hợp lệ
            total_text = self.ui.lineEdit_7.text().strip()

            if not total_text or not total_text.replace(".", "", 1).isdigit():
                QMessageBox.critical(self, "Lỗi", "❌ Tổng tiền không hợp lệ!")
                return

            total_price = float(total_text)  # Chuyển sang kiểu float
            user_id = 1  # 📝 Giả định user_id = 1 (hoặc thay bằng user thực tế)
            
            # 🔹 Lưu hóa đơn vào bảng `orders` (❌ Không lưu vào `order_details` nữa)
            cursor.execute("INSERT INTO orders (user_id, total_price, order_date) VALUES (%s, %s, NOW())",
                           (user_id, total_price))
            order_id = cursor.lastrowid  # Lấy `order_id` vừa tạo

            # Kiểm tra nếu order_id không hợp lệ
            if order_id is None:
                QMessageBox.critical(self, "Lỗi", "❌ Không thể tạo hóa đơn!")
                return

            print(f"✅ Hóa đơn mới đã tạo: Order ID = {order_id}")

            self.conn.commit()  # ✅ Lưu vào CSDL

            # 🎉 Hiển thị thông báo thành công
            QMessageBox.information(self, "Thành công", "✅ Hóa đơn đã được lưu vào CSDL!")

        except pymysql.Error as e:
            self.conn.rollback()
            QMessageBox.critical(self, "Lỗi CSDL", f"❌ Lỗi khi lưu hóa đơn: {e}")
            print(f"❌ Lỗi khi lưu  hóa đơn: {e}")

        except Exception as ex:
            QMessageBox.critical(self.centralwidget, "Lỗi hệ thống", f"❌ Lỗi không xác định: {ex}")
            print(f"❌ Lỗi không xác định: {ex}")
            

    def hien_thi_ma_don_hang(self, order_id):
            try:
                cursor = self.conn.cursor()
                
                self.ui.lineEdit_3.setText(str(order_id))
                print(f"🔍 Debug: Mã đơn hàng được chọn = {order_id}")
            
                self.ui.tableWidget.setRowCount(0)

                cursor.execute("""
                    SELECT p.name, od.quantity, od.price, (od.quantity * od.price) AS total_price
                    FROM order_details od
                    JOIN products p ON od.product_id = p.product_id
                    WHERE od.order_id = %s
                """, (order_id,))

                rows = cursor.fetchall()
                print(f"📋 Chi tiết đơn hàng lấy được: {rows}")

                if not rows:
                    QMessageBox.warning(self.ui, "Lỗi", f"❌ Đơn hàng {order_id} không có sản phẩm nào!")
                    return

                for row_number, row_data in enumerate(rows):
                    self.ui.tableWidget.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.ui.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

                print(f"✅ Đang hiển thị {len(rows)} sản phẩm trong đơn hàng {order_id}")

                cursor.execute("SELECT total_price FROM orders WHERE order_id = %s", (order_id,))
                total_price = cursor.fetchone()
                total_price = total_price[0] if total_price else 0
                self.ui.lineEdit_7.setText(str(total_price))

                QMessageBox.information(self.ui, "Thành công", f"✅ Đã tải đơn hàng {order_id} thành công!")

            except pymysql.Error as e:
                QMessageBox.critical(self.ui, "Lỗi CSDL", f"❌ Lỗi khi tải đơn hàng: {e}")
                print(f"❌ Lỗi khi tải đơn hàng: {e}")
            except Exception as ex:
                QMessageBox.critical(self.ui, "Lỗi hệ thống", f"❌ Lỗi không xác định: {ex}")
                print(f"❌ Lỗi không xác định: {ex}")

    def ap_dung_khuyen_mai(self):
        ma_khuyen_mai = self.ui.lineEdit_2.text().strip()

        if not ma_khuyen_mai:
            QMessageBox.warning(self.ui, "Lỗi", "❌ Vui lòng nhập mã khuyến mãi!")
            return

        if not self.conn or not self.conn.open:
            QMessageBox.critical(self.ui, "Lỗi CSDL", "❌ Kết nối CSDL không khả dụng!")
            return

        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT discount FROM promotions WHERE code = %s", (ma_khuyen_mai,))
            result = cursor.fetchone()

            if not result:
                QMessageBox.warning(self.ui, "Lỗi", "❌ Mã khuyến mãi không hợp lệ!")
                return

            discount_value = result[0]
            if discount_value is None or discount_value <= 0:
                QMessageBox.warning(self.ui, "Lỗi", "❌ Mã khuyến mãi không hợp lệ hoặc không có giảm giá!")
                return

            print(f"✅ Mã hợp lệ! Giảm giá: {discount_value}")

            total_text = self.ui.lineEdit_7.text().strip()
            try:
                total_price = float(total_text.replace(",", ""))
            except ValueError:
                QMessageBox.critical(self.ui, "Lỗi", "❌ Tổng tiền không hợp lệ!")
                return

            total_price = max(0, total_price - discount_value)
            self.ui.lineEdit_7.setText(str(round(total_price, 2)))

            QMessageBox.information(self.ui, "Thành công", f"✅ Mã khuyến mãi đã áp dụng! Tổng tiền mới: {total_price}")

        except pymysql.Error as e:
            QMessageBox.critical(self.ui, "Lỗi CSDL", f"❌ Lỗi khi áp dụng khuyến mãi: {e}")
        except Exception as ex:
            QMessageBox.critical(self.ui, "Lỗi hệ thống", f"❌ Lỗi không xác định: {ex}")

    def thanh_toan(self):
        """ Lưu hóa đơn vào bảng orders trước, rồi mới thêm vào order_details """

        if not self.conn or not self.conn.open:
            QMessageBox.critical(self, "Lỗi CSDL", "❌ Kết nối CSDL không khả dụng!")
            return

        try:
            cursor = self.conn.cursor()

            # 🔹 Kiểm tra số lượng sản phẩm trong tableWidget
            row_count = self.ui.tableWidget.rowCount()
            if row_count == 0:
                QMessageBox.warning(self, "Cảnh báo", "⚠️ Không có sản phẩm nào để lưu!")
                return

            # 🔹 Lấy tổng tiền từ giao diện
            total_text = self.ui.lineEdit_7.text().strip()
            if not total_text or not total_text.replace(".", "", 1).isdigit():
                QMessageBox.critical(self, "Lỗi", "❌ Tổng tiền không hợp lệ!")
                return

            total_price = float(total_text)
            user_id = 1  # 🔹 Giả sử user_id cố định là 1, có thể lấy từ session đăng nhập

            # 🔥 Bước 1: Chèn vào bảng orders trước
            cursor.execute(
                "INSERT INTO orders (user_id, total_price, order_date) VALUES (%s, %s, NOW())",
                (user_id, total_price)
            )
            order_id = cursor.lastrowid  # 🔹 Lấy order_id vừa tạo
            if not order_id:
                QMessageBox.critical(self, "Lỗi", "❌ Không thể tạo hóa đơn!")
                return

            print(f"✅ Hóa đơn mới đã tạo: Order ID = {order_id}")

            # 🔥 Bước 2: Chèn từng sản phẩm vào bảng order_details
            for row in range(row_count):
                product_id = self.ui.tableWidget.item(row, 0).text()  # 🔹 Cột 1: Mã sản phẩm
                quantity = self.ui.tableWidget.item(row, 2).text()  # 🔹 Cột 3: Số lượng
                price = self.ui.tableWidget.item(row, 3).text()  # 🔹 Cột 4: Đơn giá
                total = self.ui.tableWidget.item(row, 4).text()  # 🔹 Cột 5: Thành tiền

                # Kiểm tra dữ liệu hợp lệ
                if not product_id or not quantity or not price or not total:
                    continue  # 🔹 Bỏ qua dòng rỗng

                cursor.execute(
                    "INSERT INTO order_details (order_id, product_id, quantity, price) VALUES (%s, %s, %s, %s)",
                    (order_id, product_id, quantity, price)
                )

            # 🔥 Bước 3: Xác nhận lưu dữ liệu
            self.conn.commit()
            QMessageBox.information(self, "Thành công", "✅ Hóa đơn đã được lưu vào CSDL!")

        except pymysql.Error as e:
            self.conn.rollback()
            QMessageBox.critical(self, "Lỗi CSDL", f"❌ Lỗi khi lưu hóa đơn: {e}")
            print(f"❌ Lỗi khi lưu hóa đơn: {e}")

        except Exception as ex:
            QMessageBox.critical(self, "Lỗi hệ thống", f"❌ Lỗi không xác định: {ex}")
            print(f"❌ Lỗi không xác định: {ex}")

    def dang_xuat(self):
        self.close()
        from dangnhap1 import DangNhap
        self.login_window = DangNhap()
        self.login_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TrangChu()
    window.show()
    sys.exit(app.exec())