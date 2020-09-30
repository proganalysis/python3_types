# (generated with --quick)

import __builtin__
import datetime
from typing import Any, List

Article: Any
Factory: Any
JournalType: Any
SolrDocument: Any
dt: module
factory: Any
faker: Any
pysolr: Any
repository: Any

class ArticleFactory(Any):
    Meta: type
    issue: Any
    localidentifier: Any
    with_pdf: Any

class ArticleRef(Any):
    __doc__: str
    issue: Any
    localidentifier: Any
    def __init__(self, issue, localidentifier, from_fixture = ..., title = ..., type = ..., section_titles = ..., publication_allowed = ..., authors = ..., add_to_fedora_issue = ..., with_pdf = ..., external_pdf_url = ..., solr_attrs = ...) -> None: ...
    def _should_use_cache(self) -> bool: ...

class CollectionFactory(Any):
    Meta: type
    code: Any
    localidentifier: Any
    name: Any

class DisciplineFactory(Any):
    Meta: type
    code: Any
    name: Any

class EmbargoedArticleFactory(ArticleFactory):
    issue: Any

class EmbargoedIssueFactory(IssueFactory):
    date_published: datetime.date
    journal: Any
    year: int

class IssueFactory(Any):
    Meta: type
    add_to_fedora_journal: Any
    date_published: datetime.date
    is_published: bool
    journal: Any
    localidentifier: Any
    post: Any
    year: int
    @classmethod
    def create_published_after(cls, other_issue, *args, **kwargs) -> Any: ...

class JournalFactory(Any):
    Meta: __builtin__.type
    Params: __builtin__.type
    code: Any
    collection: Any
    disciplines: Any
    last_publication_year: int
    localidentifier: Any
    members: Any
    name: Any
    post: Any
    publishers: Any
    redirect_to_external_url: bool
    type: Any
    @classmethod
    def create_with_issue(cls, *args, **kwargs) -> Any: ...

class JournalInformationFactory(Any):
    Meta: type
    journal: Any

class JournalTypeFactory(Any):
    Meta: type
    code: Any
    name: Any

class LegacyOrganisationProfileFactory(Any):
    Meta: type
    account_id: Any
    organisation: Any

class NonEmbargoedArticleFactory(ArticleFactory):
    issue: Any

class NonEmbargoedIssueFactory(IssueFactory):
    date_published: datetime.date
    journal: Any
    year: int

class OpenAccessArticleFactory(ArticleFactory):
    issue: Any

class OrganisationFactory(Any):
    Meta: type
    name: Any

class PublisherFactory(Any):
    Meta: type
    name: Any

class SolrDocumentFactory(Any):
    Meta: __builtin__.type
    authors: List[nothing]
    id: Any
    title: Any
    type: str

class ThesisFactory(Any):
    Meta: __builtin__.type
    authors: List[str]
    collection: Any
    date_added: Any
    id: Any
    repository: Any
    title: Any
    type: str
    url: Any
    year: Any

class ThesisRepositoryFactory(Any):
    Meta: type
    code: Any
    name: Any
    solr_name: Any
