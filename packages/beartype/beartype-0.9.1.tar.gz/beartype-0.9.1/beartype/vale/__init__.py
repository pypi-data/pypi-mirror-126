#!/usr/bin/env python3
# --------------------( LICENSE                           )--------------------
# Copyright (c) 2014-2021 Beartype authors.
# See "LICENSE" for further details.

'''
**Beartype validators.**

This submodule publishes a PEP-compliant hierarchy of subscriptable (indexable)
classes enabling callers to validate the internal structure of arbitrarily
complex scalars, data structures, and third-party objects. Like annotation
objects defined by the :mod:`typing` module (e.g., :attr:`typing.Union`), these
classes dynamically generate PEP-compliant type hints when subscripted
(indexed) and are thus intended to annotate callables and variables. Unlike
annotation objects defined by the :mod:`typing` module, these classes are *not*
explicitly covered by existing PEPs and thus *not* directly usable as
annotations.

Instead, callers are expected to (in order):

#. Annotate callable parameters and returns to be validated with
   :pep:`593`_-compliant :attr:`typing.Annotated` type hints.
#. Subscript those hints with (in order):

   #. The type of those parameters and returns.
   #. One or more subscriptions of classes declared by this submodule.
'''

# ....................{ IMPORTS                           }....................
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# WARNING: To avoid polluting the public module namespace, external attributes
# should be locally imported at module scope *ONLY* under alternate private
# names (e.g., "from argparse import ArgumentParser as _ArgumentParser" rather
# than merely "from argparse import ArgumentParser").
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
from beartype.vale._factory._valeis import _IsFactory
from beartype.vale._factory._valeiscls import _IsSubclassFactory
from beartype.vale._factory._valeisobj import _IsAttrFactory
from beartype.vale._factory._valeisoper import _IsEqualFactory

# ....................{ SINGLETONS                        }....................
# Public factory singletons instantiating these private factory classes.
Is = _IsFactory(basename='Is')
IsAttr = _IsAttrFactory(basename='IsAttr')
IsEqual = _IsEqualFactory(basename='IsEqual')
IsSubclass = _IsSubclassFactory(basename='IsSubclass')

# Delete all private factory classes imported above for safety.
del (
    _IsFactory,
    _IsAttrFactory,
    _IsEqualFactory,
    _IsSubclassFactory,
)

# ....................{ TODO                              }....................
#FIXME: As intelligently requested by @Saphyel at #32, add support for
#additional classes support constraints resembling:
#
#* String constraints:
#  * Email.
#  * Uuid.
#  * Choice.
#  * Language.
#  * Locale.
#  * Country.
#  * Currency.
#* Comparison constraints
#  * IdenticalTo.
#  * NotIdenticalTo.
#  * LessThan.
#  * GreaterThan.
#  * Range.
#  * DivisibleBy.

#FIXME: Add a new BeartypeValidator.get_cause_or_none() method with the same
#signature and docstring as the existing CauseSleuth.get_cause_or_none()
#method. This new BeartypeValidator.get_cause_or_none() method should then be
#called by the "_peperrorannotated" submodule to generate human-readable
#exception messages. Note that this implies that:
#* The BeartypeValidator.__init__() method will need to additionally accept a new
#  mandatory "get_cause_or_none: Callable[[], Optional[str]]" parameter, which
#  that method should then localize to "self.get_cause_or_none".
#* Each __class_getitem__() dunder method of each "_BeartypeValidatorFactoryABC" subclass will need
#  to additionally define and pass that callable when creating and returning
#  its "BeartypeValidator" instance.

#FIXME: *BRILLIANT IDEA.* Holyshitballstime. The idea here is that we can
#leverage all of our existing "beartype.is" infrastructure to dynamically
#synthesize PEP-compliant type hints that would then be implicitly supported by
#any runtime type checker. At present, subscriptions of "Is" (e.g.,
#"Annotated[str, Is[lambda text: bool(text)]]") are only supported by beartype
#itself. Of course, does anyone care? I mean, if you're using a runtime type
#checker, you're probably *ONLY* using beartype. Right? That said, this would
#technically improve portability by allowing users to switch between different
#checkers... except not really, since they'd still have to import beartype
#infrastructure to do so. So, this is probably actually useless.
#
#Nonetheless, the idea itself is trivial. We declare a new
#"beartype.is.Portable" singleton accessed in the same way: e.g.,
#    from beartype import beartype
#    from beartype.is import Portable
#    NonEmptyStringTest = Is[lambda text: bool(text)]
#    NonEmptyString = Portable[str, NonEmptyStringTest]
#    @beartype
#    def munge_it(text: NonEmptyString) -> str: ...
#
#So what's the difference between "typing.Annotated" and "beartype.is.Portable"
#then? Simple. The latter dynamically generates one new PEP 3119-compliant
#metaclass and associated class whenever subscripted. Clearly, this gets
#expensive in both space and time consumption fast -- which is why this won't
#be the default approach. For safety, this new class does *NOT* subclass the
#first subscripted class. Instead:
#* This new metaclass of this new class simply defines an __isinstancecheck__()
#  dunder method. For the above example, this would be:
#    class NonEmptyStringMetaclass(object):
#        def __isinstancecheck__(cls, obj) -> bool:
#            return isinstance(obj, str) and NonEmptyStringTest(obj)
#* This new class would then be entirely empty. For the above example, this
#  would be:
#    class NonEmptyStringClass(object, metaclass=NonEmptyStringMetaclass):
#        pass
#
#Well, so much for brilliant. It's slow and big, so it seems doubtful anyone
#would actually do that. Nonetheless, that's food for thought for you.
