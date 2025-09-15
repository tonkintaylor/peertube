from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union






T = TypeVar("T", bound="PutApiV1WatchedWordsAccountsAccountNameListsListIdBody")



@_attrs_define
class PutApiV1WatchedWordsAccountsAccountNameListsListIdBody:
    """ 
        Attributes:
            list_name (Union[Unset, str]):
            words (Union[Unset, list[str]]):
     """

    list_name: Union[Unset, str] = UNSET
    words: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        list_name = self.list_name

        words: Union[Unset, list[str]] = UNSET
        if not isinstance(self.words, Unset):
            words = self.words




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if list_name is not UNSET:
            field_dict["listName"] = list_name
        if words is not UNSET:
            field_dict["words"] = words

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        list_name = d.pop("listName", UNSET)

        words = cast(list[str], d.pop("words", UNSET))


        put_api_v1_watched_words_accounts_account_name_lists_list_id_body = cls(
            list_name=list_name,
            words=words,
        )


        put_api_v1_watched_words_accounts_account_name_lists_list_id_body.additional_properties = d
        return put_api_v1_watched_words_accounts_account_name_lists_list_id_body

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
