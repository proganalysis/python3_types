from typing import NamedTuple, List, Tuple, Union, Optional, Any

if __name__ == "__main__":
    import sys
    sys.path.append("..")
    del sys

from fenalib.lexical_token import Token

class Node:
    """
    All nodes specified below will inherit from this parent class

    Adds a simple __repr__ method to all of its classes to display its own variables
    """
    pass

class StmtNode(Node):
    """
    General node to be inherited from all specialized statement nodes
    """
    pass

class CmdNode(Node):
    """
    General node to be inherited from all nodes relating to commands
    """
    pass

class MainCmdNode(CmdNode):
    """
    General node to be inherited from all children nodes to the FenaCmdNode
        - Nodes that a command is made up of in the most general context
        - eg. ExecuteCmdNode, SimpleCmdNode
    """
    pass


class FenaCmdNode(NamedTuple, CmdNode):
    """
    Holds all command segments for a command node
    """
    cmd_segment_nodes: List[MainCmdNode]

class ProgramNode(NamedTuple, Node):
    """
    Holds all statements found inside the global scope of the program
    """
    statement_nodes: List[StmtNode]

class McFunctionNode(NamedTuple, StmtNode):
    """
    Holds a single mcfunction with its full path and all fena command nodes
    """
    name: Token
    command_nodes: List[FenaCmdNode]
    debug: bool

class FolderNode(NamedTuple, StmtNode):
    """
    Holds all statements found inside a folder node
    """
    folder: Token
    statement_nodes: List[StmtNode]

class VarSetNode(NamedTuple, StmtNode):
    """
    Holds all variables defined for the file
    """
    variable: Token
    value: Token





class NbtNode(CmdNode):
    pass

class NbtIntegerNode(NamedTuple, NbtNode):
    int_value: Token
    int_type: Optional[Token] = None

class NbtFloatNode(NamedTuple, NbtNode):
    float_value: Token
    float_type: Optional[Token] = None

class NbtObjectNode(NamedTuple, NbtNode):
    # assert_list_types(mappings, NbtMapNode, duplicate_key=lambda x: x.arg.value)
    # mappings: List[NbtMapNode]
    mappings: List[Any]

class NbtArrayNode(NamedTuple, NbtNode):
    # values: List[Token, NbtObjectNode, NbtArrayNode, NbtIntegerNode, NbtFloatNode]
    values: List[Union[Token, NbtObjectNode, NbtIntegerNode, NbtFloatNode]]
    type_specifier: Optional[Token] = None

class NbtMapNode(NamedTuple, NbtNode):
    arg: Token
    value: Union[Token, NbtObjectNode, NbtArrayNode, NbtIntegerNode, NbtFloatNode]


class JsonNode(CmdNode):
    pass

class JsonObjectNode(NamedTuple, JsonNode):
    # assert_list_types(mappings, JsonMapNode, duplicate_key=lambda x: x.arg.value)
    # mappings: List[JsonMapNode]
    mappings: List[Any]

class JsonMapNode(NamedTuple, JsonNode):
    arg: Token
    # value: Union[Token, JsonArrayNode, JsonObjectNode]
    value: Union[Token, JsonObjectNode]

class JsonArrayNode(NamedTuple, JsonNode):
    values: List[Union[Token, JsonObjectNode]]



class IntRangeNode(NamedTuple, CmdNode):
    """
    Note that a range can be a singular number. If so, left_int is the same as right_int

    Attributes:
        min_int (Token or None): The smallest int in the range
        max_int (Token or None): The largest int in the range
        args (tuple of 2 strs or None): Contains the argument for the min int and the max int (eg. (rm, r))

    def __init__(self, min_int, max_int, args=()):
        assert_type(min_int, Token, optional=True)
        assert_type(max_int, Token, optional=True)
        assert not (min_int is None and max_int is None)
        assert_tuple_types(args, str)
        assert len(args) in (0, 2)

        # checks whether the number actually works as a 32 bit signed int
        if min_int is not None:
            assert (-1<<31) <= int(min_int.value) <= ((1<<31)-1)
        if max_int is not None:
            assert (-1<<31) <= int(max_int.value) <= ((1<<31)-1)

        # checks whether the max int is actually greater than or equal to the min int if they both exist
        if min_int is not None and max_int is not None:
            assert int(max_int.value) >= int(min_int.value)

        self.min_int = min_int
        self.max_int = max_int
        self.args = args
    """
    min_int: Optional[Token]
    max_int: Optional[Token]
    args: Union[Tuple[str, str], Tuple[()]]

class NumberRangeNode(NamedTuple, CmdNode):
    """
    Note that a range can be a singular number. If so, min_number is the same as max_number

    def __init__(self, min_number, max_number):
        assert_type(min_number, Token, optional=True)
        assert_type(max_number, Token, optional=True)
        assert not (min_number is None and max_number is None)
        self.min_number = min_number
        self.max_number = max_number
    """
    min_int: Optional[Token]
    max_int: Optional[Token]


class BlockNode(NamedTuple, CmdNode):
    block: Token
    states: Optional[Token] = None
    nbt: Optional[NbtObjectNode] = None

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
    namespace: Optional[Token] = None


class SelectorVarNode(NamedTuple, CmdNode):
    selector_var_specifier: Token

class SelectorScoreArgNode(NamedTuple, CmdNode):
    objective: Token
    value: Union[IntRangeNode, Token]

class SelectorScoreArgsNode(NamedTuple, CmdNode):
    # assert_list_types(score_args, SelectorScoreArgNode, duplicate_key=lambda x: x.objective.value)
    score_args: List[SelectorScoreArgNode]

class SelectorDefaultArgValueNode(NamedTuple, CmdNode):
    arg_value: Union[Token, NumberRangeNode, IntRangeNode]
    negated: bool = False

class SelectorDefaultArgNode(NamedTuple, CmdNode):
    arg: Token
    arg_value: Union[SelectorDefaultArgValueNode]

class SelectorTagArgNode(NamedTuple, CmdNode):
    tag: Token
    negated: bool = False

class SelectorArgsNode(NamedTuple, CmdNode):
    # assert_list_types(default_args, SelectorDefaultArgNode, duplicate_key=lambda x: x.arg.value)
    default_args: List[SelectorDefaultArgNode]
    score_args: SelectorScoreArgsNode
    tag_arg: Optional[SelectorTagArgNode]

class SelectorNode(NamedTuple, CmdNode):
    selector_var: SelectorVarNode
    selector_args: Optional[SelectorArgsNode] = None







class ExecuteSubIfBlockArg(NamedTuple, CmdNode):
    block: BlockNode
    coords: Optional[Vec3Node] = None

class ExecuteSubLegacyArg(NamedTuple, MainCmdNode):
    """
    Execute node for all versions under 1.12 inclusive
    """
    selector: SelectorNode
    coords: Optional[Vec3Node]
    sub_if: List[ExecuteSubIfBlockArg]

class ExecuteCmdNode(NamedTuple, MainCmdNode):
    """
    Holds all general execute command nodes
    """
    sub_cmd_nodes: List[ExecuteSubLegacyArg]


class ScoreboardCmdMathNode(NamedTuple, MainCmdNode):
    target: Union[SelectorNode, Token]
    objective: Token
    operator: Token
    target_get: Union[SelectorNode, Token]
    objective_get: Optional[Token] = None

class ScoreboardCmdMathValueNode(NamedTuple, MainCmdNode):
    target: Union[SelectorNode, Token]
    objective: Token
    operator: Token
    value: Token
    nbt: Optional[NbtObjectNode] = None

class ScoreboardCmdSpecialNode(NamedTuple, MainCmdNode):
    target: Union[SelectorNode, Token]
    sub_cmd: Token
    objective: Token

class SimpleCmdNode(NamedTuple, MainCmdNode):
    tokens: List[Union[Token, SelectorNode, JsonObjectNode, NbtObjectNode, NamespaceIdNode]]


class DataCmdNode(MainCmdNode):
    pass

class DataMergeNode(NamedTuple, DataCmdNode):
    entity_vec3: Union[SelectorNode, Vec3Node]
    nbt: NbtObjectNode


class EffectCmdNode(MainCmdNode):
    pass

class EffectClearNode(NamedTuple, EffectCmdNode):
    selector: SelectorNode
    effect_id: Optional[Token] = None

class EffectGiveNode(NamedTuple, EffectCmdNode):
    selector: SelectorNode
    effect_id: Token
    duration: Optional[Token] = None
    level: Optional[Token] = None
    hide_particles: bool = True


class FunctionCmdNode(NamedTuple, MainCmdNode):
    function_id: NamespaceIdNode
    sub_arg: Optional[Token] = None
    selector: Optional[SelectorNode] = None


class ItemNode(NamedTuple, CmdNode):
    item_id: Token
    damage: Optional[Token] = None
    nbt: Optional[NbtObjectNode] = None


class ItemCmdNode(MainCmdNode):
    pass

class ItemGiveNode(NamedTuple, ItemCmdNode):
    selector: SelectorNode
    item: ItemNode
    count: Optional[Token] = None

class ItemClearNode(NamedTuple, ItemCmdNode):
    selector: SelectorNode
    item: Union[ItemNode, Token]
    count: Optional[Token] = None

class ItemReplaceEntityNode(NamedTuple, ItemCmdNode):
    selector: SelectorNode
    slot: Token
    item: ItemNode
    count: Optional[Token] = None

class ItemReplaceBlockNode(NamedTuple, ItemCmdNode):
    vec3: Vec3Node
    slot: Token
    item: ItemNode
    count: Optional[Token] = None


class ObjectiveCmdNode(MainCmdNode):
    pass

class ObjectiveAddNode(NamedTuple, ObjectiveCmdNode):
    objective: Token
    criteria: Token
    display_name: List[Token]

class ObjectiveRemoveNode(NamedTuple, ObjectiveCmdNode):
    objective: Token

class ObjectiveSetdisplayNode(NamedTuple, ObjectiveCmdNode):
    slot: Token
    objective: Optional[Token] = None


class TagCmdNode(MainCmdNode):
    pass

class TagAddNode(NamedTuple, TagCmdNode):
    selector: SelectorNode
    tag: Token
    nbt: Optional[NbtObjectNode] = None

class TagRemoveNode(NamedTuple, TagCmdNode):
    selector: SelectorNode
    tag: Token
    nbt: Optional[NbtObjectNode] = None


class TeamCmdNode(MainCmdNode):
    pass

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


class XpCmdNode(MainCmdNode):
    pass

class XpMathNode(NamedTuple, XpCmdNode):
    selector: SelectorNode
    operator: Token
    value: Token
    sub_cmd: Optional[Token] = None



if __name__ == "__main__":
    # testing random hashes
    # note that it's based on identity, not equality
    class A:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    a = A(1, [2, 3, 4])
    some_dict = {a: 1}
    print(some_dict)

    asdf = ExecuteCmdNode([1, 2, 3])
    print(asdf)



