~/archive/typed_project/\(jacobbridges\)veggiecron-server/src/scheduler/parser.py




mypy --show-error-codes --namespace-packages --ignore-missing-imports --show-column-numbers  

pylint -d I,R,C,W,F 

pytype --keep-going 


mypy --show-error-codes --namespace-packages --ignore-missing-imports --show-column-numbers  ~/archive/typed_project/\(jacobbridges\)veggiecron-server/src/scheduler/parser.py

pylint -d I,R,C,W,F ~/archive/typed_project/\(jacobbridges\)veggiecron-server/src/scheduler/parser.py

pytype --keep-going ~/archive/typed_project/\(jacobbridges\)veggiecron-server/src/scheduler/parser.py



mypy -> pylint
str-format 148/200
  [['too-many-format-args', 127], ['too-few-format-args', 12], ['undefined-variable', 9]]
mypy -> pytype
str-format 14/200
  [['name-error', 14]]


(Stiivi)entigen/entigen/writers/python.py:

if prop.type.is_composite and prop.default:
    b += "if {} is None:".format(prop.name)
    b += "    self.{} = {}".format(prop.name, self.default_value(prop))
    b += "else:".format(prop.name)  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<      
    b += "    self.{} = {}".format(prop.name, prop.name)
else:
    b += "self.{} = {}".format(prop.name, prop.name)
...
b = Block()
b += "def __eq__(self, other: object) -> bool:".format(entity.name) <<<<<<<<<<<

mypy
228:18 error: Not all arguments converted during string formatting  [str-format]
277:14 error: Not all arguments converted during string formatting  [str-format]

pytype
NONE

pylint
228:17: E1305: Too many arguments for format string (too-many-format-args)
277:13: E1305: Too many arguments for format string (too-many-format-args)


(REGOVAR)Annso/annso/core/annso/file_manager.py

except Exception as ex:
    raise RegovarException("Error occured when trying to copy/move the file from the provided path : ".format(path), "", ex)

mypy 
205:36: error: Not all arguments converted during string formatting  [str-format]

pytype
line 205, in from_local: Name 'RegovarException' is not defined [name-error]  << Unrelated 

pylint
205:18: E0602: Undefined variable 'RegovarException' (undefined-variable)
205:35: E1305: Too many arguments for format string (too-many-format-args)



mypy -> pytype
type-arg 23/47
  [['not-indexable', 18], ['not-supported-yet', 2], ['invalid-annotation', 2], ['name-error', 1]]
mypy -> pylint
  NONE

(dr-leo)pandaSDMX/pandasdmx/message.py

from pandasdmx.util import BaseModel, DictLike, summarize_dictlike
...
class StructureMessage(Message):
    category_scheme: DictLike[str, CategoryScheme] = DictLike()
    codelist: DictLike[str, Codelist] = DictLike()
    concept_scheme: DictLike[str, ConceptScheme] = DictLike()
    constraint: DictLike[str, ContentConstraint] = DictLike()
    dataflow: DictLike[str, DataflowDefinition] = DictLike()
    structure: DictLike[str, DataStructureDefinition] = DictLike()
    organisation_scheme: DictLike[str, AgencyScheme] = DictLike()
    provisionagreement: DictLike[str, ProvisionAgreement] = DictLike()

mypy
4:1: error: Cannot find implementation or library stub for module named 'pandasdmx.model'  [import]
93:22: error: "DictLike" expects no type arguments, but 2 given  [type-arg]
94:15: error: "DictLike" expects no type arguments, but 2 given  [type-arg]
95:21: error: "DictLike" expects no type arguments, but 2 given  [type-arg]
96:17: error: "DictLike" expects no type arguments, but 2 given  [type-arg]
97:15: error: "DictLike" expects no type arguments, but 2 given  [type-arg]
98:16: error: "DictLike" expects no type arguments, but 2 given  [type-arg]
99:26: error: "DictLike" expects no type arguments, but 2 given  [type-arg]
100:25: error: "DictLike" expects no type arguments, but 2 given  [type-arg]

pytype
line 12, in <module>: Cant find module 'pandasdmx.model'. [import-error]
File "/home/bew/archive/typed_project/(dr-leo)pandaSDMX/pandasdmx/message.py", line 93, in StructureMessage: class DictLike is not indexable [not-indexable]
  ('DictLike' does not subclass Generic)
File "/home/bew/archive/typed_project/(dr-leo)pandaSDMX/pandasdmx/message.py", line 94, in StructureMessage: class DictLike is not indexable [not-indexable]
  ('DictLike' does not subclass Generic)
File "/home/bew/archive/typed_project/(dr-leo)pandaSDMX/pandasdmx/message.py", line 95, in StructureMessage: class DictLike is not indexable [not-indexable]
  ('DictLike' does not subclass Generic)
File "/home/bew/archive/typed_project/(dr-leo)pandaSDMX/pandasdmx/message.py", line 96, in StructureMessage: class DictLike is not indexable [not-indexable]
  ('DictLike' does not subclass Generic)
File "/home/bew/archive/typed_project/(dr-leo)pandaSDMX/pandasdmx/message.py", line 97, in StructureMessage: class DictLike is not indexable [not-indexable]
  ('DictLike' does not subclass Generic)
File "/home/bew/archive/typed_project/(dr-leo)pandaSDMX/pandasdmx/message.py", line 98, in StructureMessage: class DictLike is not indexable [not-indexable]
  ('DictLike' does not subclass Generic)
File "/home/bew/archive/typed_project/(dr-leo)pandaSDMX/pandasdmx/message.py", line 99, in StructureMessage: class DictLike is not indexable [not-indexable]
  ('DictLike' does not subclass Generic)
File "/home/bew/archive/typed_project/(dr-leo)pandaSDMX/pandasdmx/message.py", line 100, in StructureMessage: class DictLike is not indexable [not-indexable]
  ('DictLike' does not subclass Generic)



mypy -> pytype
return-value 534/1399
  [['bad-return-type', 534]]
mypy -> pylint
return-value 2/1399
  [['no-member', 2]]

(raiden-network)raiden-token/deploy/utils.py


def check_succesful_tx(web3, txid, timeout=180) -> dict:
    receipt = wait_for_transaction_receipt(web3, txid, timeout=timeout)
    txinfo = web3.eth.getTransaction(txid)
    return receipt, txinfo["gas"] != receipt["gasUsed"]

mypy
34:12: error: Incompatible return value type (got "Tuple[Any, Any]", expected "Dict[Any, Any]")  [return-value]

pytype:
line 34, in check_succesful_tx: bad option in return type [bad-return-type]
           Expected: dict
  Actually returned: Tuple[Any, Any]

pylint:
NONE



(lupoDharkael)flameshot/.travis/services/transferwee.py

def download_url(url: str) -> str:

    if url.startswith('https://we.tl/'):
        r = requests.head(url, allow_redirects=True)
        url = r.url

    recipient_id = None
    params = url.replace('https://wetransfer.com/downloads/', '').split('/')

    if len(params) == 2:
        transfer_id, security_hash = params
    elif len(params) == 3:
        transfer_id, recipient_id, security_hash = params
    else:
        return None

    j = {
        "security_hash": security_hash,
    }
    if recipient_id:
        j["recipient_id"] = recipient_id
    r = requests.post(WETRANSFER_DOWNLOAD_URL.format(transfer_id=transfer_id),
                      json=j)

    j = r.json()
    return j.get('direct_link')


mypy
97:16: error: Incompatible return value type (got "None", expected "str")  [return-value]
108:12: error: Incompatible return value type (got "Optional[str]", expected "str")  [return-value]

pytype
line 97, in download_url: bad option in return type [bad-return-type]
           Expected: str
  Actually returned: None

pylint
NONE



mypy -> pytype
operator 119/617
  [['invalid-typevar', 43], ['unsupported-operands', 32], ['name-error', 15], ['wrong-arg-types', 14]
  , ['not-callable', 11], ['bad-return-type', 3], ['key-error', 1]]

mypy -> pylint
operator 33/617
  [['not-callable', 18], ['no-member', 6], ['invalid-unary-operand-type', 4], 
  ['unsupported-membership-test', 3], ['used-before-assignment', 1], ['undefined-variable', 1]]


(jacobbridges)veggiecron-server/src/scheduler/parser.py

mypy
archive/typed_project/(jacobbridges)veggiecron-server/src/scheduler/parser.py:9:1: error: Relative import climbs too many namespaces  [misc]
archive/typed_project/(jacobbridges)veggiecron-server/src/scheduler/parser.py:72:35: error: Unsupported operand types for + ("float" and "timedelta")  [operator]
archive/typed_project/(jacobbridges)veggiecron-server/src/scheduler/parser.py:72:50: error: Unsupported operand type for unary + ("Optional[int]")  [operator]
archive/typed_project/(jacobbridges)veggiecron-server/src/scheduler/parser.py:80:31: error: Unsupported operand types for + ("float" and "timedelta")  [operator]
archive/typed_project/(jacobbridges)veggiecron-server/src/scheduler/parser.py:80:47: error: Unsupported operand type for unary + ("Optional[int]")  [operator]
archive/typed_project/(jacobbridges)veggiecron-server/src/scheduler/parser.py:83:31: error: Unsupported operand types for + ("float" and "timedelta")  [operator]
archive/typed_project/(jacobbridges)veggiecron-server/src/scheduler/parser.py:83:49: error: Unsupported operand type for unary + ("Optional[int]")  [operator]
archive/typed_project/(jacobbridges)veggiecron-server/src/scheduler/parser.py:86:31: error: Unsupported operand types for + ("float" and "timedelta")  [operator]
archive/typed_project/(jacobbridges)veggiecron-server/src/scheduler/parser.py:86:49: error: Unsupported operand type for unary + ("Optional[int]")  [operator]

pytype

archive/typed_project/(jacobbridges)veggiecron-server/src/scheduler/parser.py:72:49: E1130: bad operand type for unary +: NoneType (invalid-unary-operand-type)
archive/typed_project/(jacobbridges)veggiecron-server/src/scheduler/parser.py:80:46: E1130: bad operand type for unary +: NoneType (invalid-unary-operand-type)
archive/typed_project/(jacobbridges)veggiecron-server/src/scheduler/parser.py:83:48: E1130: bad operand type for unary +: NoneType (invalid-unary-operand-type)
archive/typed_project/(jacobbridges)veggiecron-server/src/scheduler/parser.py:86:48: E1130: bad operand type for unary +: NoneType (invalid-unary-operand-type)

File "/home/bew/archive/typed_project/(jacobbridges)veggiecron-server/src/scheduler/parser.py", line 9, in <module>: Can't find module 'utils.dates'. [import-error]
File "/home/bew/archive/typed_project/(jacobbridges)veggiecron-server/src/scheduler/parser.py", line 72, in parse: unsupported operand type(s) for +: 'None' [unsupported-operands]
  No attribute '__pos__' on None
File "/home/bew/archive/typed_project/(jacobbridges)veggiecron-server/src/scheduler/parser.py", line 80, in parse: unsupported operand type(s) for +: 'None' [unsupported-operands]
  No attribute '__pos__' on None
File "/home/bew/archive/typed_project/(jacobbridges)veggiecron-server/src/scheduler/parser.py", line 83, in parse: unsupported operand type(s) for +: 'None' [unsupported-operands]
  No attribute '__pos__' on None
File "/home/bew/archive/typed_project/(jacobbridges)veggiecron-server/src/scheduler/parser.py", line 86, in parse: unsupported operand type(s) for +: 'None' [unsupported-operands]
  No attribute '__pos__' on None


pylint
