import sys

from PyQt5.QtWidgets import (QAbstractItemView, QApplication, QFrame, 
    QGridLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QStyleFactory,
    QTableView, QTreeView, QWidget)
from PyQt5.QtGui import QIcon

class AbstractWindow(QWidget):

    '''
    このクラスはアプリ内の全ウィンドウに共通の設定を施します。
    （ただし今のところアイコンを設定するのみです）
    ウィンドウを作るときはこのクラスを継承してください。
    '''

    def __init__(self):
        '''
        アイコンを設定します。
        '''
        super().__init__()
        self.setWindowIcon(QIcon('エコエコちゃん icon colored3.jpg'))
        QApplication.setStyle(QStyleFactory.create('Fusion'))
        
class MainWindow(AbstractWindow):

    '''
    アプリのメインウィンドウです。
    新規会計ボタンを持っています。

    Parameters:
    items -- type: model.Items 全商品リスト
    cart  -- type: model.DataframeAsModel 購入済み商品リスト
    '''

    def __init__(self, items, cart):
        super().__init__()
        # super()についての参考：
        # http://www.lifewithpython.com/2014/01/python-super-function.html
        self.accounting_window = None
        self.items_model = items
        self.cart_model = cart

        self.setWindowTitle('Gomipy Accounting')
        self.setGeometry(100, 100, 500, 500)
        self.init_ui()

    def init_ui(self):
        '''
        メインウィンドウ内部にGUIウィジェットを配置します。
        '''
        # はじめに、ウィンドウ全体のレイアウトを設定します。
        # QHBoxLayout は、一個以上の箱が水平に並んだレイアウトを作ります。
        wrapper = QHBoxLayout(self)

        # 新規会計ボタンを作る
        button_start_accounting = QPushButton('新規会計', self)
        button_start_accounting.clicked.connect(self.on_click)
        # wrapperの中に入れる
        wrapper.addWidget(button_start_accounting)

        # 全商品一覧のリストを作る
        items_list = QTreeView(self)
        items_list.setModel(self.items_model)
        # wrapperの中に入れる
        wrapper.addWidget(items_list)


        # ウィンドウを表示します。
        self.show()

    def on_click(self):
        '''
        新規会計ボタンが押されたときに呼び出されます。
        '''
        self.accounting_window = AccountingWindow(self.items_model, self.cart_model)

class AccountingWindow(AbstractWindow):

    '''
    会計処理ウィンドウです。

    Parameters:
    items -- type: model.Items 全商品リスト
    cart  -- type: model.DataframeAsModel 購入済み商品リスト
    '''

    def __init__(self, items, cart):
        super().__init__()
        self.title = '会計'
        self.left = 320
        self.top = 220
        self.width = 500
        self.height = 300
        self.items_model = items
        self.cart_model = cart
        self.init_ui()

    def init_ui(self):
        '''
        会計処理ウィンドウ内部にGUIウィジェットを配置します。
        '''
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # はじめに、会計処理ウィンドウ全体のレイアウトを設定します。
        # QHBoxLayout は、一個以上の箱が水平に並んだレイアウトを作ります。
        self.wrapper = QHBoxLayout(self)

        # wrapper の 中身を作っていきます。
        # QFrameは、内部にレイアウトを持つことができるウィジェットです。
        self.left = QFrame(self)
        # wrapper の左側の箱に入れます。
        self.wrapper.addWidget(self.left)

        # 今作ったQFrameの中に、新たにレイアウトを作ります。
        # GridLayout は、一個以上の箱が格子状に並んだレイアウトです。
        self.item_request_wrapper = QGridLayout(self.left)

        # GridLayoutの中に入れるウィジェットを作っていきます。
        # 「顧客番号」ラベル
        self.customer_id_label = QLabel(self)
        self.customer_id_label.setText('顧客番号')
        # GridLayout に入れます。
        # なお、addWidget() の引数は、(嵌められるウィジェット, 嵌める行, 嵌める列) です。
        self.item_request_wrapper.addWidget(self.customer_id_label, 0, 0)

        # 顧客番号入力欄
        self.customer_id_input = QLineEdit(self)
        # GridLayout に入れます。
        self.item_request_wrapper.addWidget(self.customer_id_input, 0, 1)

        # 「商品番号」ラベル
        self.item_request_id_label = QLabel(self)
        self.item_request_id_label.setText('商品番号')
        # GridLayout に入れます。
        self.item_request_wrapper.addWidget(self.item_request_id_label, 1, 0)

        # 商品番号入力欄
        self.item_request_id_input = QLineEdit(self)
        # GridLayout に入れます。
        self.item_request_wrapper.addWidget(self.item_request_id_input, 1, 1)

        # 「検索」ボタン
        self.item_request_id_search = QPushButton(self)
        self.item_request_id_search.setText('追加')
        self.item_request_id_search.clicked.connect(self.put_item_in_cart)
        # GridLayout に入れます。
        self.item_request_wrapper.addWidget(self.item_request_id_search, 2, 1)

        # wrapper の左から2番目の箱に入れる予定のウィジェットを作ります。
        # カートの中身をあらわす表
        self.right = QTableView(self)
        self.right.setModel(self.cart_model.qt_model)
        # wrapper の左から2番目の箱に入れます。
        self.wrapper.addWidget(self.right)

        # ウィンドウを表示します。
        self.show()

    def put_item_in_cart(self):
        '''
        購入済み商品一覧に追加します。
        '''
        customer_id = self.customer_id_input.text()
        item_id = self.item_request_id_input.text()
        self.cart_model.add_item(customer_id, item_id)


def main(items, cart):
    '''
    GUI を起動します。

    Parameters:
    items -- type: model.Items 全商品リスト
    cart  -- type: model.DataframeAsModel 購入済み商品リスト
    '''

    app = QApplication(sys.argv)
    main_window = MainWindow(items, cart)
    sys.exit(app.exec_())

