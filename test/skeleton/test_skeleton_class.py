from skeleton import SkeletonClass
import pytest


def test__default_name():
    skeleton_class = SkeletonClass()
    skeleton_class.greet()
