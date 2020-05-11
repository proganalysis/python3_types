'''
Excel シートをPyQtのモデルとして使うためのモジュールです。
'''

from openpyxl import load_workbook
from PyQt5.QtGui import QStandardItem, QStandardItemModel

class ExcelIOException(Exception):
    pass

class ExcelQtConverter:

    '''
    ExcelのシートとQtモデルの変換を担います。

    Parameters:
    file_name -- Excelファイルのファイル名
    '''
    # IO は Input/Output の略

    def __init__(self, file_name):

        # 特定のシートの書き込む方法は下記を参照。
        # https://stackoverflow.com/a/20221655

        self.file_name = file_name
        self.px_workbook = load_workbook(file_name)

    def to_model(self, name, model_type=QStandardItemModel, header=True):
        '''
        ExcelのシートをQtのモデルに変換します。

        Parameters:
        name -- str型 Excelのシート名
        model_type -- type型 変換後に生成されるQtモデルの型を指定
                      （未指定の場合QStandardItemModel）
        header -- bool型 Trueの場合エクセルの1行目をヘッダとして扱う
                  （未指定の場合True）
        '''
        return convert_openpyxl_to_qtmodel(
            self.px_workbook.get_sheet_by_name(name),
            model_type=model_type,
            header=True
        )

    def from_model(self, qt_model, name):
        raise ExcelIOException('未実装です')

    def save(self):
        self.px_workbook.save(self.file_name)

def convert_openpyxl_to_qtmodel(px_worksheet, model_type=QStandardItemModel, header=True):
    '''
    openpyxl の worksheet を、Qt のモデルに変換します。

    Parameters:
    name -- str型 Excelのシート名
    model_type -- type型 変換後に生成されるQtモデルの型を指定
                    （未指定の場合QStandardItemModel）
    header -- bool型 Trueの場合エクセルの1行目をヘッダとして扱う
                （未指定の場合True）
    '''
    qt_model = model_type()

    rows = px_worksheet.rows

    # 1行目をheaderとして扱う場合の処理
    if header:

        # 1行目のセルたちのタプルを取得
        header_cells = next(rows)

        # セルたちの値を取り出しリストに格納（リスト内包表記を使う）
        header_strings = [header_cell.value for header_cell in header_cells]

        # 取り出した値をqtのモデルのヘッダにする
        qt_model.setHorizontalHeaderLabels(header_strings)

    # すべてのセルを反復して値をqtのモデルに格納
    for row_index, cells in enumerate(rows):
        for column_index, cell in enumerate(cells):
            # cell は openpyxl の worksheet のセル
            # cell.valueはそのセルの値を格納

            # cell を qt の model の item に変換
            # (qt の model の item = エクセルで言うところのセル)
            qt_item = QStandardItem()
            qt_item.setText(str(cell.value))

            # 作成した item を model に登録
            qt_model.setItem(row_index, column_index, qt_item)

    return qt_model
