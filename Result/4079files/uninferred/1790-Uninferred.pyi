from fenalib.lexical_token import Token as Token
from typing import Any, List, NamedTuple, Optional, Tuple, Union

class Node: ...
class StmtNode(Node): ...
class CmdNode(Node): ...
class MainCmdNode(CmdNode): ...

class FenaCmdNode(NamedTuple, CmdNode):
    cmd_segment_nodes: List[MainCmdNode]

class ProgramNode(NamedTuple, Node):
    statement_nodes: List[StmtNode]

class McFunctionNode(NamedTuple, StmtNode):
    name: Token
    command_nodes: List[FenaCmdNode]
    debug: bool

class FolderNode(NamedTuple, StmtNode):
    folder: Token
    statement_nodes: List[StmtNode]

class VarSetNode(NamedTuple, StmtNode):
    variable: Token
    value: Token

class NbtNode(CmdNode): ...

class NbtIntegerNode(NamedTuple, NbtNode):
    int_value: Token
    int_type: Optional[Token] = ...

class NbtFloatNode(NamedTuple, NbtNode):
    float_value: Token
    float_type: Optional[Token] = ...

class NbtObjectNode(NamedTuple, NbtNode):
    mappings: List[Any]

class NbtArrayNode(NamedTuple, NbtNode):
    values: List[Union[Token, NbtObjectNode, NbtIntegerNode, NbtFloatNode]]
    type_specifier: Optional[Token] = ...

class NbtMapNode(NamedTuple, NbtNode):
    arg: Token
    value: Union[Token, NbtObjectNode, NbtArrayNode, NbtIntegerNode, NbtFloatNode]

class JsonNode(CmdNode): ...

class JsonObjectNode(NamedTuple, JsonNode):
    mappings: List[Any]

class JsonMapNode(NamedTuple, JsonNode):
    arg: Token
    value: Union[Token, JsonObjectNode]

class JsonArrayNode(NamedTuple, JsonNode):
    values: List[Union[Token, JsonObjectNode]]

class IntRangeNode(NamedTuple, CmdNode):
    min_int: Optional[Token]
    max_int: Optional[Token]
    args: Union[Tuple[str, str], Tuple]

class NumberRangeNode(NamedTuple, CmdNode):
    min_int: Optional[Token]
    max_int: Optional[Token]

class BlockNode(NamedTuple, CmdNode):
    block: Token
    states: Optional[Token] = ...
    nbt: Optional[NbtObjectNode] = ...

class BlockStateNode(NamedTuple, CmdNode):
    arg: Token
    value: Token

class Vec2Node(NamedTuple, CmdNode):
    coord1: Token
    coord2: Token

class Vec3Node(NamedTuple, CmdNode):
    coord1: Token
    coord2: Token
    coord3: Token

class NamespaceIdNode(NamedTuple, CmdNode):
    id_value: Token
    namespace: Optional[Token] = ...

class SelectorVarNode(NamedTuple, CmdNode):
    selector_var_specifier: Token

class SelectorScoreArgNode(NamedTuple, CmdNode):
    objective: Token
    value: Union[IntRangeNode, Token]

class SelectorScoreArgsNode(NamedTuple, CmdNode):
    score_args: List[SelectorScoreArgNode]

class SelectorDefaultArgValueNode(NamedTuple, CmdNode):
    arg_value: Union[Token, NumberRangeNode, IntRangeNode]
    negated: bool = ...

class SelectorDefaultArgNode(NamedTuple, CmdNode):
    arg: Token
    arg_value: Union[SelectorDefaultArgValueNode]

class SelectorTagArgNode(NamedTuple, CmdNode):
    tag: Token
    negated: bool = ...

class SelectorArgsNode(NamedTuple, CmdNode):
    default_args: List[SelectorDefaultArgNode]
    score_args: SelectorScoreArgsNode
    tag_arg: Optional[SelectorTagArgNode]

class SelectorNode(NamedTuple, CmdNode):
    selector_var: SelectorVarNode
    selector_args: Optional[SelectorArgsNode] = ...

class ExecuteSubIfBlockArg(NamedTuple, CmdNode):
    block: BlockNode
    coords: Optional[Vec3Node] = ...

class ExecuteSubLegacyArg(NamedTuple, MainCmdNode):
    selector: SelectorNode
    coords: Optional[Vec3Node]
    sub_if: List[ExecuteSubIfBlockArg]

class ExecuteCmdNode(NamedTuple, MainCmdNode):
    sub_cmd_nodes: List[ExecuteSubLegacyArg]

class ScoreboardCmdMathNode(NamedTuple, MainCmdNode):
    target: Union[SelectorNode, Token]
    objective: Token
    operator: Token
    target_get: Union[SelectorNode, Token]
    objective_get: Optional[Token] = ...

class ScoreboardCmdMathValueNode(NamedTuple, MainCmdNode):
    target: Union[SelectorNode, Token]
    objective: Token
    operator: Token
    value: Token
    nbt: Optional[NbtObjectNode] = ...

class ScoreboardCmdSpecialNode(NamedTuple, MainCmdNode):
    target: Union[SelectorNode, Token]
    sub_cmd: Token
    objective: Token

class SimpleCmdNode(NamedTuple, MainCmdNode):
    tokens: List[Union[Token, SelectorNode, JsonObjectNode, NbtObjectNode, NamespaceIdNode]]

class DataCmdNode(MainCmdNode): ...

class DataMergeNode(NamedTuple, DataCmdNode):
    entity_vec3: Union[SelectorNode, Vec3Node]
    nbt: NbtObjectNode

class EffectCmdNode(MainCmdNode): ...

class EffectClearNode(NamedTuple, EffectCmdNode):
    selector: SelectorNode
    effect_id: Optional[Token] = ...

class EffectGiveNode(NamedTuple, EffectCmdNode):
    selector: SelectorNode
    effect_id: Token
    duration: Optional[Token] = ...
    level: Optional[Token] = ...
    hide_particles: bool = ...

class FunctionCmdNode(NamedTuple, MainCmdNode):
    function_id: NamespaceIdNode
    sub_arg: Optional[Token] = ...
    selector: Optional[SelectorNode] = ...

class ItemNode(NamedTuple, CmdNode):
    item_id: Token
    damage: Optional[Token] = ...
    nbt: Optional[NbtObjectNode] = ...

class ItemCmdNode(MainCmdNode): ...

class ItemGiveNode(NamedTuple, ItemCmdNode):
    selector: SelectorNode
    item: ItemNode
    count: Optional[Token] = ...

class ItemClearNode(NamedTuple, ItemCmdNode):
    selector: SelectorNode
    item: Union[ItemNode, Token]
    count: Optional[Token] = ...

class ItemReplaceEntityNode(NamedTuple, ItemCmdNode):
    selector: SelectorNode
    slot: Token
    item: ItemNode
    count: Optional[Token] = ...

class ItemReplaceBlockNode(NamedTuple, ItemCmdNode):
    vec3: Vec3Node
    slot: Token
    item: ItemNode
    count: Optional[Token] = ...

class ObjectiveCmdNode(MainCmdNode): ...

class ObjectiveAddNode(NamedTuple, ObjectiveCmdNode):
    objective: Token
    criteria: Token
    display_name: List[Token]

class ObjectiveRemoveNode(NamedTuple, ObjectiveCmdNode):
    objective: Token

class ObjectiveSetdisplayNode(NamedTuple, ObjectiveCmdNode):
    slot: Token
    objective: Optional[Token] = ...

class TagCmdNode(MainCmdNode): ...

class TagAddNode(NamedTuple, TagCmdNode):
    selector: SelectorNode
    tag: Token
    nbt: Optional[NbtObjectNode] = ...

class TagRemoveNode(NamedTuple, TagCmdNode):
    selector: SelectorNode
    tag: Token
    nbt: Optional[NbtObjectNode] = ...

class TeamCmdNode(MainCmdNode): ...

class TeamAddNode(NamedTuple, TeamCmdNode):
    team_name: Token
    display_name: List[Token]

class TeamJoinNode(NamedTuple, TeamCmdNode):
    team_name: Token
    target: Union[Token, SelectorNode]

class TeamLeaveNode(NamedTuple, TeamCmdNode):
    target: Union[SelectorNode, Token]

class TeamEmptyNode(NamedTuple, TeamCmdNode):
    team_name: Token

class TeamOptionNode(NamedTuple, TeamCmdNode):
    team_name: Token
    option: Token
    value: Union[Token, JsonObjectNode]

class TeamRemoveNode(NamedTuple, TeamCmdNode):
    team_name: Token

class XpCmdNode(MainCmdNode): ...

class XpMathNode(NamedTuple, XpCmdNode):
    selector: SelectorNode
    operator: Token
    value: Token
    sub_cmd: Optional[Token] = ...
