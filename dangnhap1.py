import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QInputDialog
from dangnhap import Ui_MainWindow  # Giao diện đăng nhập
from database import Database  # Kết nối Database
from trangchu1 import TrangChu  # Giao diện trang chủ
from dangky1 import DangKy  # Import form đăng ký

class DangNhap(QMainWindow):
    def __init__(self): 
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Kết nối sự kiện các nút
        self.ui.loginButton.clicked.connect(self.dang_nhap)
        self.ui.registerButton.clicked.connect(self.mo_dang_ky)
        self.ui.forgotPasswordButton.clicked.connect(self.quen_mat_khau)  # Nút Quên mật khẩu

    def dang_nhap(self):
        """Xử lý đăng nhập"""
        username = self.ui.lineEdit.text().strip()
        password = self.ui.lineEdit_2.text().strip()

        if not username or not password:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng nhập tên tài khoản và mật khẩu!")
            return

        db = Database()
        cursor = db.conn.cursor(dictionary=True)

        query = "SELECT matkhau FROM users WHERE tendangnhap = %s"
        cursor.execute(query, (username,))
        tendangnhap = cursor.fetchone()

        if tendangnhap and tendangnhap["matkhau"] == password:  # So sánh trực tiếp không mã hóa
            QMessageBox.information(self, "Thành công", "Đăng nhập thành công!")
            self.trang_chu = TrangChu()
            self.trang_chu.show()
            self.close()
        else:
            QMessageBox.warning(self, "Lỗi", "Sai tên đăng nhập hoặc mật khẩu!")

        cursor.close()
        db.close()

    def mo_dang_ky(self):
        """Mở form đăng ký"""
        self.register_window = DangKy(self)
        self.register_window.show()
        self.hide()

    def quen_mat_khau(self):
        """Xử lý quên mật khẩu"""
        username, ok = QInputDialog.getText(self, "Quên mật khẩu", "Nhập tên tài khoản:")
        if not ok or not username.strip():
            return
        
        db = Database()
        cursor = db.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE tendangnhap = %s", (username,))
        user = cursor.fetchone()
        
        if user:
            new_password, ok = QInputDialog.getText(self, "Đặt lại mật khẩu", "Nhập mật khẩu mới:")
            if ok and new_password.strip():
                # Không mã hóa mật khẩu mới
                cursor.execute("UPDATE users SET matkhau = %s WHERE tendangnhap = %s", (new_password, username))
                db.conn.commit()
                QMessageBox.information(self, "Thành công", "Mật khẩu đã được cập nhật!")
            else:
                QMessageBox.warning(self, "Lỗi", "Mật khẩu không được để trống!")
        else:
            QMessageBox.warning(self, "Lỗi", "Tên tài khoản không tồn tại!")
        
        cursor.close()
        db.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DangNhap()
    window.show()
    sys.exit(app.exec())
