# -*- coding: utf-8 -*-
r"""
Helper function to assist my orgmode editing
============================================
"""
# Created Tue Sep 15 18:46:42 2015
# Author: Óscar Nájera

from __future__ import division, absolute_import, print_function
import sympy


def platex(*args, environment='equation', **settings):
    """Call sympy latex print over arguments

    Parameters
    ----------
    *args: as many sympy expressions as wanted is the same latex
       equation environment
    environment: wrap expression in an environment block
    **settings: settings for sympy latex
    """

    new_arguments = [sympy.latex(arg, **settings) for arg in args]
    latex_block = r"""\begin{{{environment}}}
{}
\end{{{environment}}}
""".format("\n".join(new_arguments), environment=environment)

    return latex_block


def ket(base, names=[r"\uparrow", r"\downarrow"]):
    r"""Trasforms a binary number into its Ket form

    A binary representation is a number and grows from right to left
    despite reading being from left to right. Names ordering represent
    that order. Thus ket(1)=\downarrow, because that's the first state
    of the two digit entry. ket(2)=\uparrow, because it's the second
    state, and in binary is 10. ket(3)=\uparrow\downarrow, since
    \dwarrow is created first then \uparrow and I keep the fermionic
    sign convention.

    Parameters:
        base (int): number representing the state
        names (list): names of individual basis states
    Returns:
        str : latex string of ket
    """

    binary_base = "{{:0{}b}}".format(len(names)).format(base)
    ketstr = r"|"

    state_vector = [name
                    for state, name in zip(binary_base, names)
                    if int(state)]
    ketstr += " ".join(state_vector)
    if base == 0:
        ketstr += r"\emptyset"

    return ketstr + r"\rangle"
