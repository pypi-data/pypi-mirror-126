"""Slashing module messages types."""

from __future__ import annotations

import attr
from terra_proto.cosmos.slashing.v1beta1 import MsgUnjail as MsgUnjail_pb

from terra_sdk.core import ValAddress
from terra_sdk.core.msg import Msg

__all__ = ["MsgUnjail"]


@attr.s
class MsgUnjail(Msg):
    """Attempt to unjail a jailed validator (must be submitted by same validator).

    Args:
        address: validator address to unjail"""

    type = "slashing/MsgUnjail"
    """"""
    type_url = "/cosmos.slashing.v1beta1.MsgUnjail"
    """"""
    action = "unjail"
    """"""

    address: ValAddress = attr.ib()

    @classmethod
    def from_data(cls, data: dict) -> MsgUnjail:
        return cls(address=data["address"])

    def to_proto(self) -> MsgUnjail_pb:
        return MsgUnjail_pb(validator_addr=self.address)
