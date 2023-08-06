#!/usr/bin/env python3
# --------------------( LICENSE                           )--------------------
# Copyright (c) 2014-2021 Beartype authors.
# See "LICENSE" for further details.

# ....................{ TODO                              }....................
#FIXME: [FEATURE] Define the following supplementary decorators:
#* @beartype.beartype_O1(), identical to the current @beartype.beartype()
#  decorator but provided for disambiguity. This decorator only type-checks
#  exactly one item from each container for each call rather than all items.
#* @beartype.beartype_Ologn(), type-checking log(n) random items from each
#  container of "n" items for each call.
#* @beartype.beartype_On(), type-checking all items from each container for
#  each call. We have various ideas littered about GitHub on how to optimize
#  this for various conditions, but this is never going to be ideal and should
#  thus never be the default.
#
#To differentiate between these three strategies, consider:
#* Declare an enumeration in "beartype._decor._data" resembling:
#    from enum import Enum
#    BeartypeStrategyKind = Enum('BeartypeStrategyKind ('O1', 'Ologn', 'On',))
#* Define a new "BeartypeData.strategy_kind" instance variable.
#* Set this variable to the corresponding "BeartypeStrategyKind" enumeration
#  member based on which of the three decorators listed above was called.
#* Explicitly pass the value of the "BeartypeData.strategy_kind" instance
#  variable to the beartype._decor._code._pep._pephint.pep_code_check_hint()
#  function as a new memoized "strategy_kind" parameter.
#* Conditionally generate type-checking code throughout that function depending
#  on the value of that parameter.

#FIXME: [SAFETY] @beartype should raise exceptions when decorating callables
#that are actually generators, asynchronous generators, or coroutines whose
#returns are annotated with any type hint whose sign is *NOT*
#"HintSignGenerator", "HintSignAsyncGenerator", or "HintSignCoroutine"
#respectively. Since detecting generator callables, asynchronous generator
#callables, and coroutine callables is trivial, this should be trivial.

#FIXME: Ensure that *ALL* calls to memoized callables throughout the codebase
#are called with purely positional rather than keyword arguments. Currently, we
#suspect the inverse is the case. To do so, we'll probably want to augment the
#wrapper closure returned by the @callable_cached decorator to emit non-fatal
#warnings when called with non-empty keyword arguments.
#
#Alternately, we might simply want to prohibit keyword arguments altogether by
#defining a new @callable_cached_positional decorator restricted to positional
#arguments. Right... That probably makes more sense. Make it so, ensign!
#
#Then, for generality:
#
#* Preserve the existing @callable_cached decorator as is. We won't be using
#  it, but there's little sense in destroying something beautiful.
#* Globally replace all existing "@callable_cached" substrings with
#  "@callable_cached_positional". Voila!

#FIXME: *CRITICAL EDGE CASE:* If the passed "func" is a coroutine, that
#coroutine *MUST* be called preceded by the "await" keyword rather than merely
#called as is. Detecting coroutines is trivial, thanks to our newly defined
#beartype._util.func.utilfunctest.is_func_async_coroutine() tester. Note that
#*ONLY* non-generator callables explicitly declared with "async def" should be
#subject to this logic, which is why we'll intentionally call
#is_func_async_coroutine() rather than is_func_async() to discriminate.
#Asynchronous generator callables are actually factories that only *RETURN* an
#asynchronous generator; they aren't actually asynchronous themselves. So:
#* Modify the "CODE_CALL_CHECKED" and "CODE_CALL_UNCHECKED" snippets to
#  conditionally precede the function call with the substring "await ": e.g.,
#      CODE_CALL_UNCHECKED = '''
#          return {func_await}__beartype_func(*args, **kwargs)
#      '''
#  Note the absence of delimiting space. This is, of course, intentional.
#* Unconditionally format the "func_await" substring into both of those
#  snippets, defined ala:
#      format_await = 'await ' if inspect.iscoroutinefunction(func) else ''
#* Oh, and note that our defined wrapper function must also be preceded by the
#  "async " keyword. So, we'll also need to augment "CODE_SIGNATURE".
#FIXME: Unit test this extensively, please. The only sane way to do so will be
#to generalize the dynamic loop over all type hints declaring a synchronous
#closure iteratively type-hinted by each to *ALSO* declare an asynchronous
#closure. Actually... that sounds like overkill, frankly. We really only need
#to test these notable edge cases:
#* Asynchronous callable with an unannotated return.
#* Asynchronous callable with a return annotated by "typing.NoReturn", which
#  generates different return (and thus awaitable) semantics.
#* Asynchronous callable with a return annotated by *ANY* PEP-compliant type
#  hint other than "typing.NoReturn", which also generates different return
#  (and thus awaitable) semantics.

#FIXME: Non-critical optimization: if the active Python interpreter is already
#performing static type checking (e.g., with Pyre or mypy), @beartype should
#unconditionally reduce to a noop for the current process. Note that:
#
#* Detecting static type checking is trivial, as PEP 563 standardizes the newly
#  declared "typing.TYPE_CHECKING" boolean constant to be true only if static
#  type checking is currently occurring. Note that @beartype supports this now.
#* Detecting whether static type checking just occurred is clearly less
#  trivial and possibly even infeasible. We're unclear what exactly separates
#  the "static type checking" phase from the runtime phase performed by static
#  type checkers, but something clearly does. If all else fails, we can
#  probably attempt to detect whether the basename of the command invoked by
#  the parent process matches "(Pyre|mypy|pyright|pytype)" or... something. Of
#  course, that itself is non-trivial due to Windows, so here we are. *sigh*

#FIXME: Emit one non-fatal warning for each annotated type that is either:
#
#* "beartype.cave.UnavailableType".
#* "beartype.cave.UnavailableTypes".
#
#Both cases imply user-side misconfiguration, but not sufficiently awful enough
#to warrant fatal exceptions. Moreover, emitting warnings rather than
#exceptions enables end users to unconditionally disable all unwanted warnings,
#whereas no such facilities exist for unwanted exceptions.
#FIXME: Validate all tuple annotations to be non-empty *EXCLUDING*
#"beartype.cave.UnavailableTypes", which is intentionally empty.
#FIXME: Unit test the above edge case.

#FIXME: Add support for all possible kinds of parameters. @beartype currently
#supports most but *NOT* all types. Specifically:
#
#* Type-check variadic keyword arguments. Currently, only variadic positional
#  arguments are type-checked. When doing so, remove the
#  "Parameter.VAR_KEYWORD" type from the "_PARAM_KIND_IGNORABLE" set.
#* Type-check positional-only arguments under Python >= 3.8. Note that, since
#  C-based callables have *ALWAYS* supported positional-only arguments, the
#  "Parameter.POSITIONAL_ONLY" type is defined for *ALL* Python versions
#  despite only being usable in actual Python from Python >= 3.8. In other
#  words, support for type-checking positional-only arguments should be added
#  unconditionally without reference to Python version -- we suspect, anyway.
#  When doing so, remove the "Parameter.POSITIONAL_ONLY" type from the
#  "_PARAM_KIND_IGNORABLE" set.
#* Remove the "_PARAM_KIND_IGNORABLE" set entirely.

