import pandas as pd
from PySide2.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QFormLayout,
    QTableView,
    QPushButton,
    QComboBox,
    QHeaderView
)

from rboost.gui.utils.pandasmodel import PandasModel


class ListLabelsWindow(QWidget):

    def __init__(self, rboost):
        super().__init__()
        self.rboost = rboost

        self.layout = QVBoxLayout()
        self._add_form_layout()
        self._add_buttons_layout()
        self.table_view = None
        self._add_table_view_layout()
        self.setLayout(self.layout)

    def _add_form_layout(self):
        labtype_form = self._create_labtype_form()
        self.layout.addLayout(labtype_form)

    def _add_buttons_layout(self):
        self.buttons_layout = QHBoxLayout()
        show_button = QPushButton('Show list')
        show_button.clicked.connect(self.show_table)
        clear_button = QPushButton('Clear list')
        clear_button.clicked.connect(self.clear_table)
        self.buttons_layout.addWidget(show_button)
        self.buttons_layout.addWidget(clear_button)
        self.layout.addLayout(self.buttons_layout)

    def _add_table_view_layout(self, df=None):
        self.table_view_layout = QHBoxLayout()
        if self.table_view is not None:
            self.table_view_layout.removeWidget(self.table_view)
            self.table_view.deleteLater()
        self.table_view = self._create_table_view(df=df)
        self.table_view_layout.addWidget(self.table_view)
        self.layout.addLayout(self.table_view_layout)

    def _create_labtype_form(self):
        labtype_form = QFormLayout()
        items = [None] + sorted(list(self.rboost.labtypes))
        self.labtype_combobox = QComboBox()
        self.labtype_combobox.addItems(items)
        labtype_form.addRow('Label type', self.labtype_combobox)
        return labtype_form

    def _create_table_view(self, df):
        if df is None:
            df = pd.DataFrame()
        model = PandasModel(df)
        table_view = QTableView()
        table_view.setModel(model)
        table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        return table_view

    def _get_labels(self):
        labels = [self.rboost.network.graph.nodes[n]['label']
                  for n in self.rboost.network.graph.nodes]
        labtype = str(self.labtype_combobox.currentText())
        if labtype:
            labels = [label for label in labels if labtype in label.types]
        labels.sort(reverse=True)
        return labels

    def _get_dataframe(self, labels):
        columns = [self.rboost.labels_df_cols[k]
                   for k in ['label', 'types', 'queries', 'uploads']]
        data = [[lab.name, lab.types, lab.queries_count, lab.uploads_count]
                for lab in labels]
        df = pd.DataFrame(data=data, columns=columns)
        return df

    def show_table(self):
        labels = self._get_labels()
        df = self._get_dataframe(labels=labels)
        self._add_table_view_layout(df=df)
        self.setLayout(self.layout)

    def clear_table(self):
        empty_df = pd.DataFrame()
        self._add_table_view_layout(df=empty_df)
        self.setLayout(self.layout)
