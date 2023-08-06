import os
import sys

from rboost.cli.rboost import RBoost
from rboost.source.document.remark import Remark
from rboost.utils.autocomplete import AutoComplete
from rboost.utils.exceptions import Exceptions


@RBoost.subcommand('write-remark')
class WriteRemark (RBoost):
    """
    Write a special remark on RBoost database
    """

    def main(self):

        reference = self.get_reference()
        remark = self.create_document(reference)

        self.upload_file(remark)
        self.update_database(remark)
        self.update_network(remark)

        self.database.push()
        self.network.push()

    def get_reference(self):

        df = self.database.dataframe
        df = df.loc[df['DOCTYPE'].isin(['standard', 'notebook'])]
        documents = set([docname.split('/')[0].split('.')[0]
                        for docname in df['DOCNAME']])

        with AutoComplete(options=documents):
            reference = input('>>> Reference document :\n>>> ')

        if reference not in documents:
            e = Exceptions(state='failure',
                           message=f'The document "{reference}" does not exist in RBoost database')
            e.throw()

        return reference

    def create_document(self, reference):

        path = self.remarks_path + reference + '/'
        os.makedirs(path, exist_ok=True)

        special = input('>>> Remark type : ')
        name = input('>>> Remark name : ')
        date = self.get_date()
        user = self.get_user()
        remark = Remark(date=date, user=user, path=path,
                        name=name, special=special)

        if remark.docname in self.docnames:
            e = Exceptions(state='failure',
                           message=f'The file "{remark.docname}" already exists on RBoost database')
            e.throw()

        return remark

    def upload_file(self, remark):

        print(
            f'>>> Do you want to upload the file "{remark.docname}" on RBoost database?')
        answer = input('>>> (y/n) ')
        if not answer == 'y':
            sys.exit()

        print(f'>>> Uploading "{remark.docname}"')

        filepath = remark.path + remark.name
        folder = remark.docname.split('/')[0]
        self.gdrive.upload_file(filepath=filepath, parent_folder=folder)

    def update_database(self, remark):

        data = [[remark.date, remark.user, remark.docname,
                 remark.doctype, list(remark.keywords.keys())]]
        self.database.append_data(data)

    def update_network(self, remark):

        labs, links = remark.get_data_from_text()
        self.network.update_nodes(labs)
        self.network.update_edges(links)
