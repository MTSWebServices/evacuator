from __future__ import annotations

import logging

import pytest

from evacuator import NeedEvacuation, evacuator

logger = logging.getLogger(__name__)


def test_core_decorator():
    @evacuator
    def main1():
        """doc"""
        raise NeedEvacuation("abc")

    with pytest.raises(SystemExit, match="125"):
        main1()

    assert main1.__doc__ == "doc"


def test_core_decorator_brackets():
    @evacuator()
    def main2():
        """doc"""
        raise NeedEvacuation("abc")

    with pytest.raises(SystemExit, match="125"):
        main2()

    assert main2.__doc__ == "doc"


def test_core_decorator_args():
    @evacuator()
    def main(arg, *args, kwarg: int | None = None, **kwargs):
        msg = f"arg={arg} kwarg={kwarg} args={args} kwargs={kwargs}"
        raise NeedEvacuation(msg)

    with pytest.raises(SystemExit, match="125"):
        main(1, 2, 3, key=4)


def test_core_decorator_exception():
    @evacuator(exception=RuntimeError)
    def main():
        raise RuntimeError("abc")

    with pytest.raises(SystemExit, match="125"):
        main()


def test_core_decorator_multiple_exceptions():
    @evacuator(exception=(RuntimeError, ValueError))
    def main():
        raise ValueError("abc")

    with pytest.raises(SystemExit, match="125"):
        main()


def test_core_decorator_exit_code():
    @evacuator(exit_code=32)
    def main():
        raise NeedEvacuation("abc")

    with pytest.raises(SystemExit):
        main()


def test_core_decorator_nothing_raised():
    @evacuator(exit_code=32)
    def main():
        logger.debug("abc")

    main()


def test_core_decorator_exception_not_match():
    @evacuator
    def main():
        raise RuntimeError("abc")

    with pytest.raises(RuntimeError, match="abc"):
        main()


def test_core_context():
    with pytest.raises(SystemExit, match="125"), evacuator():
        raise NeedEvacuation("abc")


def test_core_context_exception():
    with pytest.raises(SystemExit, match="125"), evacuator(exception=RuntimeError):
        raise RuntimeError("abc")


def test_core_context_multiple_exceptions():
    with pytest.raises(SystemExit, match="125"), evacuator(exception=(RuntimeError, ValueError)):
        raise ValueError("abc")


def test_core_context_exit_code():
    with pytest.raises(SystemExit), evacuator(exit_code=32):
        raise NeedEvacuation("abc")


def test_core_context_nothing_raised():
    with evacuator():
        logger.debug("abc")


def test_core_context_exception_not_match():
    with pytest.raises(RuntimeError, match="abc"), evacuator():
        raise RuntimeError("abc")
