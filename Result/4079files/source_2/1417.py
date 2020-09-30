'''
Created on 24.07.2017

@author: Peer
'''

from . import aggregation


class AuthorsPerFilePath(aggregation.AbstractAggregator):

    name = 'authors_per_file_path'

    @classmethod
    def provides(cls):
        return 'authors_per_file_path'

    @classmethod
    def requires(cls):
        return 'commit_collection'

    def __init__(self):

        self.output_database = 'result_' + self.provides()
        self.input_database = self.requires()

        unwind = {'$unwind': '$details.modifications'}

        projection = {'$project': {'file_path': '$details.modifications.file_path',
                                   'author': '$author',
                                   'date': '$date',
                                   'additions': '$details.modifications.additions',
                                   'deletions': '$details.modifications.deletions'}}

        group = {'$group': {'_id': '$file_path',
                            'modifications': {'$push': {"author": "$author",
                                                        "date": "$date",
                                                        "additions": "$additions",
                                                        "deletions": "$deletions",
                                                        'lines': {'$add': ['$additions',
                                                                           '$deletions']}}}}}

        out = {'$out': self.output_database}

        self.pipeline = [unwind, projection, group, out]


def main():
    AuthorsPerFilePath().run()


if(__name__ == '__main__'):
    main()
