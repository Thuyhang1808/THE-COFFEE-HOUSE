import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from database import connect_db  # Import hàm kết nối MySQL
from dangky import Ui_MainWindow  # Import giao diện đăng ký


class DangKy(QMainWindow):
    def __init__(self, login_window):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Nhận tham chiếu cửa sổ đăng nhập để quay lại sau khi đăng ký
        self.login_window = login_window

        # Kết nối nút "Đăng ký"
        self.ui.loginButton.clicked.connect(self.dang_ky_tai_khoan)

    def dang_ky_tai_khoan(self):
        """Xử lý đăng ký tài khoản"""
        tendangnhap = self.ui.lineEdit.text().strip()
        matkhau = self.ui.lineEdit_2.text().strip()
        hoten = self.ui.lineEdit_3.text().strip()
        email = self.ui.lineEdit_4.text().strip()
        sodienthoai = self.ui.lineEdit_5.text().strip()

        # Kiểm tra giới tính (Nam = 1, Nữ = 0)
        gioitinh = 1 if self.ui.radioButton_2.isChecked() else 0

        if not all([tendangnhap, matkhau, hoten, email, sodienthoai]):
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng nhập đầy đủ thông tin!")
            return

        conn = connect_db()
        if conn:
            cursor = conn.cursor()

            # Kiểm tra username đã tồn tại chưa
            query_check = "SELECT * FROM users WHERE tendangnhap = %s"
            cursor.execute(query_check, (tendangnhap,))
            if cursor.fetchone():
                QMessageBox.warning(self, "Lỗi", "Tên tài khoản đã tồn tại, vui lòng chọn tên khác.")
                cursor.close()
                conn.close()
                return

            # Thêm tài khoản mới
            query_insert = """
                INSERT INTO users (tendangnhap, matkhau, hoten, gioitinh, email, sodienthoai)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query_insert, (tendangnhap, matkhau, hoten, gioitinh, email, sodienthoai))
            conn.commit()
            cursor.close()
            conn.close()

            QMessageBox.information(self, "Thành công", "Đăng ký thành công! Quay lại màn hình đăng nhập.")

            # Đóng cửa sổ đăng ký và quay lại cửa sổ đăng nhập
            self.close()
            self.login_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    from dangnhap1 import DangNhap  # Import giao diện đăng nhập

    login_window = DangNhap()

    register_window = DangKy(login_window)
    register_window.show()

    sys.exit(app.exec())