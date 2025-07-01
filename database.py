import os
import mysql.connector
from PyQt6.QtWidgets import QLabel, QVBoxLayout, QWidget, QPushButton, QListWidget, QListWidgetItem
from PyQt6.QtGui import QPixmap
import pymysql

def connect_db():
    """Kết nối cơ sở dữ liệu MySQL"""
    try:
        conn = pymysql.connect(
            host="localhost",
            user="root",   # Thay bằng user MySQL của bạn
            password="",   # Thay bằng mật khẩu của bạn
            database="coffeehouse",
            cursorclass=pymysql.cursors.DictCursor
        )
        return conn
    except pymysql.MySQLError as e:
        print(f"Lỗi kết nối MySQL: {e}")
        return None
class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="coffeehouse",
        )
        self.cursor = self.conn.cursor()

    def get_items(self, table_name):
        query = f"SELECT * FROM {table_name}"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.conn.close()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quản Lý Cafe")
        self.setGeometry(100, 100, 800, 600)

        self.db = Database()
        self.layout = QVBoxLayout()
        
        self.listWidget = QListWidget()
        self.layout.addWidget(self.listWidget)
        
        self.buttons = {
            "specialtea": QPushButton("Special Tea"),
            "banh": QPushButton("Bánh"),
            "coffee": QPushButton("Coffee"),
            "topping": QPushButton("Topping")
        }

        for key, btn in self.buttons.items():
            btn.clicked.connect(lambda _, t=key: self.load_items(t))
            self.layout.addWidget(btn)

        self.setLayout(self.layout)

    def get_image_path(self, category, name):
        """
        Trả về đường dẫn ảnh từ thư mục tương ứng với sản phẩm.
        Nếu không tìm thấy ảnh, trả về 'No Image'.
        """
        img_folder = f"image/{category}"
        # Thử với các định dạng ảnh phổ biến
        for ext in ['.jpg', '.png', '.jpeg']:
            img_filename = f"{name.replace(' ', '_')}{ext}"
            img_path = os.path.join(img_folder, img_filename)
            if os.path.exists(img_path):
                return img_path  # Trả về đường dẫn nếu ảnh tồn tại
        return None  # Trả về None nếu không tìm thấy ảnh nào

    def load_items(self, category):
        self.listWidget.clear()
        items = self.db.get_items(category)

        for item in items:
            id, name, price = item[:3]
            
            # Lấy đường dẫn ảnh
            img_path = self.get_image_path(category, name)
            
            widget = QWidget()
            layout = QVBoxLayout()
            
            label = QLabel(name + f" - {price} VND")
            img_label = QLabel()
            
            if img_path:
                pixmap = QPixmap(img_path).scaled(100, 100)
                img_label.setPixmap(pixmap)
            else:
                img_label.setText("No Image")  # Nếu không tìm thấy ảnh
            
            layout.addWidget(img_label)
            layout.addWidget(label)
            widget.setLayout(layout)
            
            item = QListWidgetItem()
            item.setSizeHint(widget.sizeHint())
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, widget)

    def closeEvent(self, event):
        self.db.close()
        event.accept()

if __name__ == "__main__":
    from PyQt6.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())