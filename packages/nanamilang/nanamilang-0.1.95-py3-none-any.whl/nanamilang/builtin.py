"""NanamiLang Builtin Class"""

# This file is a part of NanamiLang Project
# This project licensed under GNU GPL version 2
# Initially made by @jedi2light (aka Stoian Minaiev)

import functools
from typing import List
from functools import reduce
from nanamilang import datatypes
from nanamilang.shortcuts import (
    ASSERT_HAS_KEY, ASSERT_LIST_LENGTH_IS,
    ASSERT_LIST_LENGTH_IS_EVEN, ASSERT_NOT_EMPTY_COLLECTION
)


def meta(meta_: dict):
    """
    NanamiLang, apply meta to func
    'name': fn/macro LISP name
    'type': 'macro' or 'function'
    'sample': sample fn/macro usage
    'docstring': what fn/macro does

    :param meta_: function meta data
    """

    def wrapped(fn):
        @functools.wraps(fn)
        def function(*args, **kwargs):
            return fn(*args, **kwargs)

        ASSERT_HAS_KEY(meta_, 'name')
        ASSERT_HAS_KEY(meta_, 'type')
        ASSERT_HAS_KEY(meta_, 'sample')
        ASSERT_HAS_KEY(meta_, 'docstring')
        function.meta = meta_
        return function

    return wrapped


class BuiltinMacro:
    """NanamiLan Builtin Macro"""

    @staticmethod
    def resolve(mc_name: str) -> dict:
        """Resolve macro by its name"""

        for macro in BuiltinMacro.functions():
            if macro.meta.get('name') == mc_name:
                return {'macro_name': mc_name, 'macro_reference': macro}

    @staticmethod
    def completions() -> List[str]:
        """Return all possible function names (for completion)"""
        return list(map(lambda f: f.meta.get('name'), BuiltinMacro.functions()))

    @staticmethod
    def names() -> List[str]:
        """Return all possible function names"""

        return list(filter(lambda name: '_macro' in name, BuiltinMacro().__dir__()))

    @staticmethod
    def functions() -> list:
        """Return all possible functions"""

        return list(map(lambda n: getattr(BuiltinMacro, n, None), BuiltinMacro.names()))

    @staticmethod
    @meta({'name': 'if',
           'type': 'macro',
           'sample': '(if condition true-branch else-branch)',
           'docstring': 'Return true- or else-branch depending on condition'})
    def if_macro(tree_slice: list, ev_func, token_cls) -> list:
        """
        Builtin 'if' macro implementation

        :param tree_slice: slice of encountered tree
        :param ev_func: reference to recursive evaluation function
        :param token_cls: nanamilang.token.Token class
        :return: converted slice of tree (as this would be expected)
        """

        condition, true_branch, else_branch = tree_slice

        if not isinstance(condition, list):
            condition = [token_cls(token_cls.Identifier, 'identity'), condition]
        if not isinstance(true_branch, list):
            true_branch = [token_cls(token_cls.Identifier, 'identity'), true_branch]
        if not isinstance(else_branch, list):
            else_branch = [token_cls(token_cls.Identifier, 'identity'), else_branch]

        return true_branch if ev_func(condition).reference() is True else else_branch

    @staticmethod
    @meta({'name': 'comment',
           'type': 'macro',
           'sample': '(comment ...)',
           'docstring': 'Turn form into datatypes.Nil'})
    def comment_macro(tree_slice: list, ev_func, token_cls) -> list:
        """
        Builtin 'comment' macro implementation

        :param tree_slice: slice of encountered tree
        :param ev_func: reference to recursive evaluation function
        :param token_cls: nanamilang.token.Token class
        :return: converted slice of tree (as this would be expected)
        """

        return [token_cls(token_cls.Identifier, 'identity'), token_cls(token_cls.Nil, 'nil')]

    @staticmethod
    @meta({'name': 'and',
           'type': 'macro',
           'sample': '(and ...)',
           'docstring': 'Return false if the next cond evaluates to false, otherwise true'})
    def and_macro(tree_slice: list, ev_func, token_cls) -> list:
        """
        Builtin 'and' macro implementation

        :param tree_slice: slice of encountered tree
        :param ev_func: reference to recursive evaluation function
        :param token_cls: nanamilang.token.Token class
        :return: converted slice of tree (as this would be expected)
        """

        for condition in tree_slice:
            if not isinstance(condition, list):
                condition = [token_cls(token_cls.Identifier, 'identity'), condition]
            if ev_func(condition).reference() is False:
                return [token_cls(token_cls.Identifier, 'identity'),
                        token_cls(token_cls.Boolean, False)]
        return [token_cls(token_cls.Identifier, 'identity'), token_cls(token_cls.Boolean, True)]

    @staticmethod
    @meta({'name': 'or',
           'type': 'macro',
           'sample': '(or ...)',
           'docstring': 'Return true if the next cond evaluates to true, otherwise false'})
    def or_macro(tree_slice: list, ev_func, token_cls) -> list:
        """
        Builtin 'or' macro implementation

        :param tree_slice: slice of encountered tree
        :param ev_func: reference to recursive evaluation function
        :param token_cls: nanamilang.token.Token class
        :return: converted slice of tree (as this would be expected)
        """

        for condition in tree_slice:
            if not isinstance(condition, list):
                condition = [token_cls(token_cls.Identifier, 'identity'), condition]
            if ev_func(condition).reference() is True:
                return [token_cls(token_cls.Identifier, 'identity'),
                        token_cls(token_cls.Boolean, True)]
        return [token_cls(token_cls.Identifier, 'identity'), token_cls(token_cls.Boolean, False)]

    @staticmethod
    @meta({'name': '->',
           'type': 'macro',
           'sample': '(-> ...)',
           'docstring': 'Allow you to simplify form'})
    def threading_macro(tree_slice: list, ev_func, token_cls) -> list:
        """
        Builtin '->' macro implementation

        :param tree_slice: slice of encountered tree
        :param ev_func: reference to recursive evaluation function
        :param token_cls: nanamilang.token.Token class
        :return: converted slice of tree (as this would be expected)
        """

        # If we've got MORE than one 'token or forms'
        if len(tree_slice) > 1:

            for idx, tof in enumerate(tree_slice):
                # If we can move next
                if len(tree_slice) - 1 != idx:
                    # If its just a single token, not an actual form, wrap as (identity ...)
                    if not isinstance(tof, list):
                        tof = [token_cls(token_cls.Identifier, 'identity'), tof]
                    # Get the next token or form
                    next_tof = tree_slice[idx + 1]
                    # If its just a single token, not an actual form, create a new expr. form
                    if not isinstance(next_tof, list):
                        tree_slice[idx + 1] = [next_tof, tof]
                    # Otherwise, just insert current 'token or form' as the FIRST form element
                    else:
                        tree_slice[idx + 1].insert(1, tof)

            # And return the LAST form
            return tree_slice[-1]

        # Otherwise, return (identity ...)
        else:

            return [token_cls(token_cls.Identifier, 'identity'), tree_slice[-1]]

    @staticmethod
    @meta({'name': '->>',
           'type': 'macro',
           'sample': '(->> ...)',
           'docstring': 'Allow you so simplify form'})
    def threading_macro_end(tree_slice: list, ev_func, token_cls) -> list:
        """
        Builtin '->>' macro implementation

        :param tree_slice: slice of encountered tree
        :param ev_func: reference to recursive evaluation function
        :param token_cls: nanamilang.token.Token class
        :return: converted slice of tree (as this would be expected)
        """

        # If we've got MORE than one 'token or forms'
        if len(tree_slice) > 1:

            for idx, tof in enumerate(tree_slice):
                # If we can move next
                if len(tree_slice) - 1 != idx:
                    # If its just a single token, not an actual form, wrap as (identity ...)
                    if not isinstance(tof, list):
                        tof = [token_cls(token_cls.Identifier, 'identity'), tof]
                    # Get the next token or form
                    next_tof = tree_slice[idx + 1]
                    # If its just a single token, not an actual form, create a new expr. form
                    if not isinstance(next_tof, list):
                        tree_slice[idx + 1] = [next_tof, tof]
                    # Otherwise, just insert current 'token or form' as the LAST form element
                    else:
                        tree_slice[idx + 1].append(tof)

            # And return the LAST form
            return tree_slice[-1]

        # Otherwise, return (identity ...)
        else:

            return [token_cls(token_cls.Identifier, 'identity'), tree_slice[-1]]

    @staticmethod
    @meta({'name': 'let',
           'type': 'macro',
           'sample': '(let [a 1 b a c (+ a b)] c)',
           'docstring': 'Declare your local bindings'})
    def let_macro(tree_slice: list, ev_func, token_cls) -> list:
        """
        Builtin 'let' macro implementation

        :param tree_slice: slice of encountered tree
        :param ev_func: reference to recursive evaluation function
        :param token_cls: nanamilang.token.Token class
        :return: converted slice of tree (as this would be expected)
        """

        # Why on Earth we need to do something if user do not want to use the results?
        if len(tree_slice) == 1:
            return [token_cls(token_cls.Identifier, 'identity'), token_cls(token_cls.Nil, 'nil')]

        bindings_form, body_form = tree_slice

        def token_type_from_dt_instance(dt_instance: datatypes.Base) -> str:
            """
            Return Token.<Something> based on passed data type instance 'name' value
            If data type instance is a Function or a Macro, we will return 'Identifier'
            """
            return token_cls.Identifier if dt_instance.name in ['Function', 'Macro'] else dt_instance.name

        def replace(tof) -> None:
            """
            It will recursively replace tof._type and tof._dt in case
            token bound data type instance is Undefined and we can find its origins in ours local bindings
            """
            if isinstance(tof, list):
                for part in tof:
                    replace(part)
            else:
                if isinstance(tof.dt(), datatypes.Undefined):
                    key = tof.dt().origin()
                    dt: datatypes.Base = env.get(key)
                    if dt is not None:
                        tof.set_type(token_type_from_dt_instance(dt))
                        tof.set_dt(dt)
                    else:
                        raise MacroEvaluationError(f'let: could not find "{key}" in this scope')

        # Take care of `bindings_form` form first

        env: dict = {}

        class MacroEvaluationError(Exception):
            """NanamiLang: Macro Evaluation Error"""

        lst = bindings_form[1:]

        # Bindings form must be event to continue
        ASSERT_LIST_LENGTH_IS_EVEN(lst)

        partitioned = [lst[i:i + 2] for i in range(0, len(lst), 2)]

        # Starting from the __first__ element to exclude a 'make-vector' Token.Identifier
        for [key_token_or_form, value_token_or_form] in partitioned:
            env_key, env_value = None, None
            # --- take care of environment key ---
            # We expect that the `key_token_or_form`:
            # - just a token (not a form, we don't support any kind of destructuring now)
            # - token type is an Identifier (as we can not assign, for example to number)
            # - data type instance assigned to that token is Undefined (no redefinition!)
            if isinstance(key_token_or_form, token_cls) and \
                    key_token_or_form.type() == token_cls.Identifier and \
                    isinstance(key_token_or_form.dt(), datatypes.Undefined):
                env_key = key_token_or_form.dt().origin()
            else:
                raise MacroEvaluationError(f'let: can\'t assign to: {key_token_or_form}')
            # --- take care of environment value ---
            # If `value_or_token_form` is not a list but just a Token instance, wrap it..
            if not isinstance(value_token_or_form, list):
                value_token_or_form = [token_cls(token_cls.Identifier, 'identity'),
                                       value_token_or_form]
            # Then, we can try to replace `value_or_token_form` with already filled env..
            replace(value_token_or_form)
            # Then try to evaluate it and update an env
            env[env_key] = ev_func(value_token_or_form)

        # Take care of `body_form` form

        replace(body_form)

        return body_form if isinstance(body_form, list) else [token_cls(token_cls.Identifier, 'identity'), body_form]


class Builtin:
    """NanamiLang Builtin"""

    @staticmethod
    def install(fn_meta: dict, fn_callback) -> None:
        """
        Allow others to install own functions.
        For example: let the REPL install (exit) function

        :param fn_meta: required function meta information
        :param fn_callback: installed function callback ref
        """

        fn_lisp_name = fn_meta.get('name')
        fn_name = f'{hash(fn_callback)}_func'
        setattr(Builtin, fn_name, fn_callback)
        attribute = getattr(Builtin, fn_name, None)
        attribute.meta = fn_meta

        print(f'[nanamilang.builtin.Builtin.install: installed "{fn_lisp_name}" function]')

    @staticmethod
    def resolve(fn_name: str) -> dict:
        """Resolve function by its name"""

        for func in Builtin.functions():
            if func.meta.get('name') == fn_name:
                return {'function_name': fn_name, 'function_reference': func}

    @staticmethod
    def completions() -> List[str]:
        """Return all possible function names (for completion)"""
        return list(map(lambda f: f.meta.get('name'), Builtin.functions()))

    @staticmethod
    def names() -> List[str]:
        """Return all possible function names"""

        return list(filter(lambda name: '_func' in name, Builtin().__dir__()))

    @staticmethod
    def functions() -> list:
        """Return all possible functions"""

        return list(map(lambda n: getattr(Builtin, n, None), Builtin.names()))

    @staticmethod
    @meta({'name': 'doc',
           'type': 'function',
           'sample': '(doc function-or-macro)',
           'docstring': 'Return Function or Macro doc as a HashMap'})
    def doc_func(args: List[datatypes.Function or datatypes.Macro]) -> datatypes.HashMap:
        """
        Builtin 'doc' function implementation

        :param args: incoming 'doc' function arguments
        :return: datatypes.HashMap
        """

        ASSERT_NOT_EMPTY_COLLECTION(args)
        ASSERT_LIST_LENGTH_IS(args, 1)

        function_or_macro: datatypes.Function or datatypes.Macro = args[0]

        assert (isinstance(function_or_macro, datatypes.Function)
                or isinstance(function_or_macro, datatypes.Macro)), 'Function or Macro was expected'

        _type = function_or_macro.reference().meta.get('type')

        return Builtin.make_hashmap_func([datatypes.Keyword('sample'),
                                          datatypes.String(function_or_macro.reference().meta.get('sample')),
                                          datatypes.Keyword('macro?'), datatypes.Boolean(_type == 'macro'),
                                          datatypes.Keyword('function?'), datatypes.Boolean(_type == 'function'),
                                          datatypes.Keyword('docstring'),
                                          datatypes.String(function_or_macro.reference().meta.get('docstring'))])

    @staticmethod
    @meta({'name': 'get',
           'type': 'function',
           'sample': '(get collection key-or-index)',
           'docstring': 'Collection item by key or index'})
    def get_func(args: List[datatypes.Base]) -> datatypes.Base:
        """
        Builtin 'get' function implementation

        :param args: incoming 'get' function arguments
        :return: datatypes.Base
        """

        ASSERT_NOT_EMPTY_COLLECTION(args)
        ASSERT_LIST_LENGTH_IS(args, 2)

        collection: datatypes.Vector or datatypes.HashMap
        key_or_index: datatypes.Base

        collection, key_or_index = args

        assert (isinstance(collection, datatypes.Vector)
                or isinstance(collection, datatypes.HashMap)), 'HashMap or Vector was expected'

        if isinstance(collection, datatypes.Vector):
            assert isinstance(key_or_index, datatypes.IntegerNumber), 'IntegerNumber was expected'

        return collection.get(key_or_index)

    @staticmethod
    @meta({'name': 'map',
           'type': 'function',
           'sample': '(map function collection)',
           'docstring': 'Vector of mapped collection items'})
    def map_func(args: List[datatypes.Base]) -> datatypes.Vector:
        """
        Builtin 'map' function implementation

        :param args: incoming 'map' function arguments
        :return: datatypes.Vector
        """

        ASSERT_NOT_EMPTY_COLLECTION(args)
        ASSERT_LIST_LENGTH_IS(args, 2)

        function: datatypes.Function
        collection: datatypes.Vector

        function, collection = args

        assert isinstance(function, datatypes.Function), 'Function was expected'
        assert isinstance(collection, datatypes.Vector), 'Vector was expected'

        return datatypes.Vector(
            list(map(lambda e: function.reference()([e]), collection.reference())))

    @staticmethod
    @meta({'name': 'filter',
           'type': 'function',
           'sample': '(filter function collection)',
           'docstring': 'Vector of filtered collection items'})
    def filter_func(args: List[datatypes.Base]) -> datatypes.Vector:
        """
        Builtin 'filter' function implementation

        :param args: incoming 'filter' function arguments
        :return: datatypes.Vector
        """

        ASSERT_NOT_EMPTY_COLLECTION(args)
        ASSERT_LIST_LENGTH_IS(args, 2)

        function: datatypes.Function
        collection: datatypes.Vector

        function, collection = args

        assert isinstance(function, datatypes.Function), 'Function was expected'
        assert isinstance(collection, datatypes.Vector), 'Vector was expected'

        return datatypes.Vector(
            list(filter(lambda e: function.reference()([e]).reference(), collection.reference())))

    @staticmethod
    @meta({'name': 'even?',
           'type': 'function',
           'sample': '(even? number)',
           'docstring': 'Return whether number is even or not'})
    def is_even_func(args: List[datatypes.Base]) -> datatypes.Boolean:
        """
        Builtin 'even?' function implementation

        :param args: incoming 'even?' function arguments
        :return: datatypes.Boolean
        """

        ASSERT_NOT_EMPTY_COLLECTION(args)
        ASSERT_LIST_LENGTH_IS(args, 1)

        number: datatypes.IntegerNumber or datatypes.FloatNumber = args[0]

        assert (isinstance(number, datatypes.IntegerNumber)
                or isinstance(number, datatypes.FloatNumber)), 'IntegerNumber or FloatNumber was expected'

        return datatypes.Boolean(number.reference() % 2 == 0)

    @staticmethod
    @meta({'name': 'nil?',
           'type': 'function',
           'sample': '(nil? something)',
           'docstring': 'Return whether something is nil or not'})
    def is_nil_func(args: List[datatypes.Base]) -> datatypes.Boolean:
        """
        Builtin 'nil?' function implementation

        :param args: incoming 'nil?' function arguments
        :return: datatypes.Boolean
        """

        ASSERT_NOT_EMPTY_COLLECTION(args)
        ASSERT_LIST_LENGTH_IS(args, 1)

        something: datatypes.Base = args[0]

        return datatypes.Boolean(isinstance(something, datatypes.Nil))

    @staticmethod
    @meta({'name': 'make-set',
           'type': 'function',
           'sample': '(make-set ...)',
           'docstring': 'Create Set data structure'})
    def make_set_func(args: List[datatypes.Base]) -> datatypes.Set:
        """
        Builtin 'make-set' function implementation

        :param args: incoming 'make-set' function arguments
        :return: datatypes.Set
        """

        ASSERT_NOT_EMPTY_COLLECTION(args)

        return datatypes.Set(set(args))

    @staticmethod
    @meta({'name': 'make-vector',
           'type': 'function',
           'sample': '(make-vector ...)',
           'docstring': 'Create Vector data structure'})
    def make_vector_func(args: List[datatypes.Base]) -> datatypes.Vector:
        """
        Builtin 'make-vector' function implementation

        :param args: incoming 'make-vector' function arguments
        :return: datatypes.Vector
        """

        ASSERT_NOT_EMPTY_COLLECTION(args)

        return datatypes.Vector(list(args))

    @staticmethod
    @meta({'name': 'make-hashmap',
           'type': 'function',
           'sample': '(make-hashmap ...)',
           'docstring': 'Create HashMap data structure'})
    def make_hashmap_func(args: List[datatypes.Base]) -> datatypes.HashMap:
        """
        Builtin 'make-hashmap' function implementation

        :param args: incoming 'make-hashmap' function arguments
        :return: datatypes.HashMap
        """

        ASSERT_NOT_EMPTY_COLLECTION(args)
        ASSERT_LIST_LENGTH_IS_EVEN(args)

        pythonic = {}
        idx = 0
        while idx < len(args) - 1:
            pythonic[args[idx]] = args[idx + 1]
            idx += 2

        return datatypes.HashMap(dict(pythonic))

    @staticmethod
    @meta({'name': 'inc',
           'type': 'function',
           'sample': '(inc number)',
           'docstring': 'Return incremented number'})
    def inc_func(args: (List[datatypes.IntegerNumber]
                        or List[datatypes.FloatNumber])) -> (datatypes.IntegerNumber
                                                             or datatypes.FloatNumber):
        """
        Builtin 'inc' function implementation

        :param args: incoming 'inc' function arguments
        :return: datatypes.IntegerNumber or datatypes.FloatNumber
        """

        ASSERT_NOT_EMPTY_COLLECTION(args)
        ASSERT_LIST_LENGTH_IS(args, 1)

        number: (datatypes.IntegerNumber or datatypes.FloatNumber) = args[0]
        assert (isinstance(number, datatypes.IntegerNumber)
                or isinstance(number, datatypes.FloatNumber)), 'IntegerNumber or FloatNumber was expected'
        return datatypes.IntegerNumber(number.reference() + 1) if \
            isinstance(number, datatypes.IntegerNumber) else datatypes.FloatNumber(number.reference() + 1)

    @staticmethod
    @meta({'name': 'dec',
           'type': 'function',
           'sample': '(dec number)',
           'docstring': 'Return decremented number'})
    def dec_func(args: (List[datatypes.IntegerNumber]
                        or List[datatypes.FloatNumber])) -> (datatypes.IntegerNumber
                                                             or datatypes.FloatNumber):
        """
        Builtin 'dec' function implementation

        :param args: incoming 'dec' function arguments
        :return: datatypes.IntegerNumber or datatypes.FloatNumber
        """

        ASSERT_NOT_EMPTY_COLLECTION(args)
        ASSERT_LIST_LENGTH_IS(args, 1)

        number: (datatypes.IntegerNumber or datatypes.FloatNumber) = args[0]
        assert (isinstance(number, datatypes.IntegerNumber)
                or isinstance(number, datatypes.FloatNumber)), 'IntegerNumber or FloatNumber was expected'
        return datatypes.IntegerNumber(number.reference() - 1) if \
            isinstance(number, datatypes.IntegerNumber) else datatypes.FloatNumber(number.reference() - 1)

    @staticmethod
    @meta({'name': 'identity',
           'type': 'function',
           'sample': '(identity something)',
           'docstring': 'Just return something'})
    def identity_func(args: List[datatypes.Base]) -> datatypes.Base:
        """
        Builtin 'identity' function implementation

        :param args: incoming 'identity' function arguments
        :return: datatypes.Base
        """

        ASSERT_NOT_EMPTY_COLLECTION(args)
        ASSERT_LIST_LENGTH_IS(args, 1)

        something: datatypes.Base = args[0]

        return something

    @staticmethod
    @meta({'name': 'type',
           'type': 'function',
           'sample': '(type something)',
           'docstring': 'Return something type name as a String'})
    def type_func(args: List[datatypes.Base]) -> datatypes.String:
        """
        Builtin 'type' function implementation

        :param args: incoming 'type' function arguments
        :return: datatypes.String
        """

        ASSERT_NOT_EMPTY_COLLECTION(args)
        ASSERT_LIST_LENGTH_IS(args, 1)

        something: datatypes.Base = args[0]

        return datatypes.String(something.name)

    @staticmethod
    @meta({'name': '=',
           'type': 'function',
           'sample': '(= f s)',
           'docstring': 'Whether f equals to s or not'})
    def eq_func(args: List[datatypes.Base]) -> datatypes.Boolean:
        """
        Builtin '=' function implementation

        :param args: incoming '=' function arguments
        :return: datatypes.Boolean
        """

        ASSERT_NOT_EMPTY_COLLECTION(args)
        ASSERT_LIST_LENGTH_IS(args, 2)

        f: datatypes.Base
        s: datatypes.Base
        f, s = args

        return datatypes.Boolean(f.reference() == s.reference())

    @staticmethod
    @meta({'name': '<',
           'type': 'function',
           'sample': '(< f s)',
           'docstring': 'Whether f lower than s or not'})
    def lower_than_func(args: (List[datatypes.IntegerNumber]
                               or List[datatypes.FloatNumber])) -> datatypes.Boolean:
        """
        Builtin '<' function implementation

        :param args: incoming '<' function arguments
        :return: datatypes.Boolean
        """

        ASSERT_NOT_EMPTY_COLLECTION(args)
        ASSERT_LIST_LENGTH_IS(args, 2)
        for arg in args:
            assert (isinstance(arg, datatypes.IntegerNumber)
                    or isinstance(arg, datatypes.FloatNumber)), 'IntegerNumber or FloatNumber were expected'

        f: datatypes.IntegerNumber or datatypes.FloatNumber
        s: datatypes.IntegerNumber or datatypes.FloatNumber
        f, s = args

        return datatypes.Boolean(f.reference() < s.reference())

    @staticmethod
    @meta({'name': '>',
           'type': 'function',
           'sample': '(> f s)',
           'docstring': 'Whether f greater than s or not'})
    def greater_than_func(args: (List[datatypes.IntegerNumber]
                                 or List[datatypes.FloatNumber])) -> datatypes.Boolean:
        """
        Builtin '>' function implementation

        :param args: incoming '>' function arguments
        :return: datatypes.Boolean
        """

        ASSERT_NOT_EMPTY_COLLECTION(args)
        ASSERT_LIST_LENGTH_IS(args, 2)
        for arg in args:
            assert (isinstance(arg, datatypes.IntegerNumber)
                    or isinstance(arg, datatypes.FloatNumber)), 'IntegerNumber or FloatNumber were expected'

        f: datatypes.IntegerNumber or datatypes.FloatNumber
        s: datatypes.IntegerNumber or datatypes.FloatNumber
        f, s = args

        return datatypes.Boolean(f.reference() > s.reference())

    @staticmethod
    @meta({'name': '<=',
           'type': 'function',
           'sample': '(<= f s)',
           'docstring': 'Whether f lower than or equals to s or not'})
    def lower_than_eq_func(args: (List[datatypes.IntegerNumber]
                                  or List[datatypes.FloatNumber])) -> datatypes.Boolean:
        """
        Builtin '<=' function implementation

        :param args: incoming '>=' function arguments
        :return: datatypes.Boolean
        """

        ASSERT_NOT_EMPTY_COLLECTION(args)
        ASSERT_LIST_LENGTH_IS(args, 2)
        for arg in args:
            assert (isinstance(arg, datatypes.IntegerNumber)
                    or isinstance(arg, datatypes.FloatNumber)), 'IntegerNumber or FloatNumber were expected'

        f: datatypes.IntegerNumber or datatypes.FloatNumber
        s: datatypes.IntegerNumber or datatypes.FloatNumber
        f, s = args

        return datatypes.Boolean(f.reference() <= s.reference())

    @staticmethod
    @meta({'name': '>=',
           'type': 'function',
           'sample': '(>= f s)',
           'docstring': 'Whether f greater than or equals to s or not'})
    def greater_than_eq_func(args: (List[datatypes.IntegerNumber]
                                    or List[datatypes.FloatNumber])) -> datatypes.Boolean:
        """
        Builtin '>=' function implementation

        :param args: incoming '>=' function arguments
        :return: datatypes.Boolean
        """

        ASSERT_NOT_EMPTY_COLLECTION(args)
        ASSERT_LIST_LENGTH_IS(args, 2)
        for arg in args:
            assert (isinstance(arg, datatypes.IntegerNumber)
                    or isinstance(arg, datatypes.FloatNumber)), 'IntegerNumber or FloatNumber were expected'

        f: datatypes.IntegerNumber or datatypes.FloatNumber
        f: datatypes.IntegerNumber or datatypes.FloatNumber
        f, s = args

        return datatypes.Boolean(f.reference() >= s.reference())

    @staticmethod
    @meta({'name': '+',
           'type': 'function',
           'sample': '(+ ...)',
           'docstring': 'All passed numbers summary'})
    def plus_func(args: (List[datatypes.IntegerNumber]
                         or List[datatypes.FloatNumber])) -> (datatypes.IntegerNumber
                                                              or datatypes.FloatNumber):
        """
        Builtin '+' function implementation

        :param args: incoming '+' function arguments
        :return: datatypes.IntegerNumber or datatypes.FloatNumber
        """

        ASSERT_NOT_EMPTY_COLLECTION(args)
        for arg in args:
            assert (isinstance(arg, datatypes.IntegerNumber)
                    or isinstance(arg, datatypes.FloatNumber)), 'IntegerNumber or FloatNumber were expected'

        result = reduce(lambda _, x: _ + x, list(map(lambda n: n.reference(), args)))

        return datatypes.IntegerNumber(result) if isinstance(result, int) else datatypes.FloatNumber(result)

    @staticmethod
    @meta({'name': '-',
           'type': 'function',
           'sample': '(- ...)',
           'docstring': 'All passed numbers difference'})
    def minus_func(args: (List[datatypes.IntegerNumber]
                          or List[datatypes.FloatNumber])) -> (datatypes.IntegerNumber
                                                               or datatypes.FloatNumber):
        """
        Builtin '-' function implementation

        :param args: incoming '-' function arguments
        :return: datatypes.IntegerNumber or datatypes.FloatNumber
        """

        ASSERT_NOT_EMPTY_COLLECTION(args)
        for arg in args:
            assert (isinstance(arg, datatypes.IntegerNumber)
                    or isinstance(arg, datatypes.FloatNumber)), 'IntegerNumber or FloatNumber were expected'

        result = reduce(lambda _, x: _ - x, list(map(lambda n: n.reference(), args)))

        return datatypes.IntegerNumber(result) if isinstance(result, int) else datatypes.FloatNumber(result)

    @staticmethod
    @meta({'name': '/',
           'type': 'function',
           'sample': '(/ ...)',
           'docstring': 'All passed numbers division'})
    def divide_func(args: (List[datatypes.IntegerNumber]
                           or List[datatypes.FloatNumber])) -> (datatypes.IntegerNumber
                                                                or datatypes.FloatNumber):
        """
        Builtin '/' function implementation

        :param args: incoming '/' function arguments
        :return: datatypes.IntegerNumber or datatypes.FloatNumber
        """

        ASSERT_NOT_EMPTY_COLLECTION(args)
        for arg in args:
            assert (isinstance(arg, datatypes.IntegerNumber)
                    or isinstance(arg, datatypes.FloatNumber)), 'IntegerNumber or FloatNumber were expected'

        result = reduce(lambda _, x: _ / x, list(map(lambda n: n.reference(), args)))

        return datatypes.IntegerNumber(result) if isinstance(result, int) else datatypes.FloatNumber(result)

    @staticmethod
    @meta({'name': '*',
           'type': 'function',
           'sample': '(* ...)',
           'docstring': 'All passed numbers production'})
    def multiply_func(args: (List[datatypes.IntegerNumber]
                             or List[datatypes.FloatNumber])) -> (datatypes.IntegerNumber
                                                                  or datatypes.FloatNumber):
        """
        Builtin '*' function implementation

        :param args: incoming '*' function arguments
        :return: datatypes.IntegerNumber or datatypes.FloatNumber
        """

        ASSERT_NOT_EMPTY_COLLECTION(args)
        for arg in args:
            assert (isinstance(arg, datatypes.IntegerNumber)
                    or isinstance(arg, datatypes.FloatNumber)), 'IntegerNumber or FloatNumber were expected'

        result = reduce(lambda _, x: _ * x, list(map(lambda n: n.reference(), args)))

        return datatypes.IntegerNumber(result) if isinstance(result, int) else datatypes.FloatNumber(result)
