from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.block_status_accounts import BlockStatusAccounts
  from ..models.block_status_hosts import BlockStatusHosts





T = TypeVar("T", bound="BlockStatus")



@_attrs_define
class BlockStatus:
    """ 
        Attributes:
            accounts (Union[Unset, BlockStatusAccounts]):
            hosts (Union[Unset, BlockStatusHosts]):
     """

    accounts: Union[Unset, 'BlockStatusAccounts'] = UNSET
    hosts: Union[Unset, 'BlockStatusHosts'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.block_status_accounts import BlockStatusAccounts
        from ..models.block_status_hosts import BlockStatusHosts
        accounts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.accounts, Unset):
            accounts = self.accounts.to_dict()

        hosts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.hosts, Unset):
            hosts = self.hosts.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if accounts is not UNSET:
            field_dict["accounts"] = accounts
        if hosts is not UNSET:
            field_dict["hosts"] = hosts

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.block_status_accounts import BlockStatusAccounts
        from ..models.block_status_hosts import BlockStatusHosts
        d = dict(src_dict)
        _accounts = d.pop("accounts", UNSET)
        accounts: Union[Unset, BlockStatusAccounts]
        if isinstance(_accounts,  Unset):
            accounts = UNSET
        else:
            accounts = BlockStatusAccounts.from_dict(_accounts)




        _hosts = d.pop("hosts", UNSET)
        hosts: Union[Unset, BlockStatusHosts]
        if isinstance(_hosts,  Unset):
            hosts = UNSET
        else:
            hosts = BlockStatusHosts.from_dict(_hosts)




        block_status = cls(
            accounts=accounts,
            hosts=hosts,
        )


        block_status.additional_properties = d
        return block_status

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
