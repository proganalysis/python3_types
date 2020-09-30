'''
model.pyの機能をチェックするunit testです。
'''

# unit test については https://docs.python.jp/3/library/unittest.html

import unittest
from itertools import product
import model
from openpyxl import Workbook

class TestConversionBetweenQtmodelAndOpenpyxl(unittest.TestCase):

    '''
    openpyxlのワークシート⇔Qtのモデルの変換が正しく行われるかチェックします。
    '''

    def test_convert_openpyxl_to_qtmodel(self):
        '''
        openpyxlのワークシートとして表現された2次元の表をqtのモデルに変換しても表の内容は変化しない。
        '''
        # ダミーの表データを{(row, column): value}形式のPython辞書として作る
        data = create_fruit_price_data()

        # ダミーの表データをopenpyxlのワークシートに変換
        px_worksheet = convert_index_value_pair_to_openpyxl(data)

        # openpyxlのワークシートをQtのモデルに変換
        qt_model = model.convert_openpyxl_to_qtmodel(px_worksheet)

        # Qtのモデルを{(row, column): value}形式のPython辞書に変換
        reversed_data = convert_qtmodel_to_index_value_pair(qt_model)

        # もとのデータと等しくない場合はテストを失敗させる
        self.assertEqual(data, reversed_data)


def convert_qtmodel_to_index_value_pair(qt_model, header=True):
    '''
    Qtのモデルをもとにindexとvalueのペアからなる辞書を作ります。
    現時点ではQtモデルとして2次元の表を想定しており、より深い木構造をもつモデルには対応しません。
    header=True（デフォルト）でQtモデルのヘッダもindex:valueペアに変換します。

    Parameters:
    qt_model -- QAbstractItemModelインタフェースをもつオブジェクト

    Return:
    表のインデックスをキーに、表の値を値にもつPython辞書。
    表のインデックスは(row, column)のtupleで、(0,0)から。
    '''
    rows = qt_model.rowCount()
    columns = qt_model.columnCount()

    ret = {}

    if header:
        for column in range(0, columns):
            header_item = qt_model.horizontalHeaderItem(column)
            if header_item is not None:
                header_string = header_item.text()
                ret[(0, column)] = header_string

    extra_row_index = 1 if header else 0
    for row, column in product(range(0, rows), range(0, columns)):
        index = qt_model.index(row, column)
        value = qt_model.data(index)
        ret[(row + extra_row_index, column)] = value

    return ret

def convert_index_value_pair_to_openpyxl(data):
    '''
    data引数をもとにopenpyxlのワークシートを作ります。

    Parameters:
    data -- セルのインデックスをキーに、セルの値を値にもつ辞書。
            セルのインデックスは(row, column)のtupleで、(0,0)から。

    Return:
    openpyxlのワークシート

    '''
    px_workbook = Workbook()
    px_worksheet = px_workbook.active

    for index, value in data.items():
        row    = index[0] + 1
        column = index[1] + 1
        px_worksheet.cell(row=row, column=column, value=value)

    return px_worksheet

def create_fruit_price_data():
    '''
    ダミーデータを返します。

    果物の値段のテーブルを返します。
    '''
    data = {
        (0,0): 'Fruit', 
        (0,1): 'Price', 
        (1,0): 'Apple', 
        (1,1): '300', 
        (2,0): 'Berry', 
        (2,1): '400'
    }
    return data
if __name__ == '__main__':
    unittest.main()
