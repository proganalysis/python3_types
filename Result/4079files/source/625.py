import os
import os.path as op
import shutil
from collections import namedtuple

from .util import pyref, nspoint, nssize, nsrect

TypeSpec = namedtuple('TypeSpec', 'pytype objctype o2p_code p2o_code')
ArgSpec = namedtuple('ArgSpec', 'argname typespec')
MethodSpec = namedtuple('MethodSpec', 'pyname objcname argspecs returntype is_inherited')
ClassSpec = namedtuple('ClassSpec', 'clsname superclass methodspecs is_protocol follow_protocols')

TYPE_SPECS = [
    TypeSpec(str, 'NSString *', 'ObjP_str_o2p(%s)', 'ObjP_str_p2o(%s)'),
    TypeSpec(int, 'NSInteger', 'ObjP_int_o2p(%s)', 'ObjP_int_p2o(%s)'),
    TypeSpec(float, 'CGFloat', 'ObjP_float_o2p(%s)', 'ObjP_float_p2o(%s)'),
    TypeSpec(bool, 'BOOL', 'ObjP_bool_o2p(%s)', 'ObjP_bool_p2o(%s)'),
    TypeSpec(object, 'id', 'ObjP_obj_o2p(%s)', 'ObjP_obj_p2o(%s)'),
    TypeSpec(list, 'NSArray *', 'ObjP_list_o2p(%s)', 'ObjP_list_p2o(%s)'),
    TypeSpec(dict, 'NSDictionary *', 'ObjP_dict_o2p(%s)', 'ObjP_dict_p2o(%s)'),
    TypeSpec(nspoint, 'NSPoint ', 'ObjP_nspoint_o2p(%s)', 'ObjP_nspoint_p2o(%s)'),
    TypeSpec(nssize, 'NSSize ', 'ObjP_nssize_o2p(%s)', 'ObjP_nssize_p2o(%s)'),
    TypeSpec(nsrect, 'NSRect ', 'ObjP_nsrect_o2p(%s)', 'ObjP_nsrect_p2o(%s)'),
    TypeSpec(pyref, 'PyObject *', 'ObjP_pyref_o2p(%s)', '%s'),
]

PYTYPE2SPEC = {ts.pytype: ts for ts in TYPE_SPECS}
OBJCTYPE2SPEC = {ts.objctype: ts for ts in TYPE_SPECS}

DATA_PATH = op.join(op.dirname(__file__), 'data')

def tmpl_replace(tmpl, **replacments):
    # Because we generate code and that code is likely to contain "{}" braces, it's better if we
    # use more explicit placeholders than the typecal format() method. These placeholders are
    # %%name%%.
    result = tmpl
    for placeholder, replacement in replacments.items():
        result = result.replace('%%{}%%'.format(placeholder), replacement)
    return result

def get_objc_signature(methodspec):
    methodname = methodspec.objcname
    returntype = methodspec.returntype
    name_elems = methodname.split(':')
    assert len(name_elems) == len(methodspec.argspecs) + 1
    returntype = returntype.objctype if returntype is not None else 'void'
    result_elems = ['(%s)' % returntype, name_elems[0]]
    for name_elem, arg in zip(name_elems[1:], methodspec.argspecs):
        result_elems.append(':(%s)%s %s' % (arg.typespec.objctype, arg.argname, name_elem))
    return ''.join(result_elems).strip()

def copy_objp_unit(destfolder):
    if not op.exists(destfolder):
        os.makedirs(destfolder)
    shutil.copy(op.join(DATA_PATH, 'ObjP.h'), destfolder)
    shutil.copy(op.join(DATA_PATH, 'ObjP.m'), destfolder)
