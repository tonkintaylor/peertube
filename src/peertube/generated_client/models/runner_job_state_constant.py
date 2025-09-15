from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.runner_job_state import RunnerJobState
from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="RunnerJobStateConstant")



@_attrs_define
class RunnerJobStateConstant:
    """ 
        Attributes:
            id (Union[Unset, RunnerJobState]): The runner job state:
                  - `1` Pending
                  - `2` Processing
                  - `3` Completed
                  - `4` Errored
                  - `5` Waiting for a parent job
                  - `6` Cancelled
                  - `7` Parent had an error
                  - `8` Parent has been cancelled
            label (Union[Unset, str]):  Example: Processing.
     """

    id: Union[Unset, RunnerJobState] = UNSET
    label: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id: Union[Unset, int] = UNSET
        if not isinstance(self.id, Unset):
            id = self.id.value


        label = self.label


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: Union[Unset, RunnerJobState]
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = RunnerJobState(_id)




        label = d.pop("label", UNSET)

        runner_job_state_constant = cls(
            id=id,
            label=label,
        )


        runner_job_state_constant.additional_properties = d
        return runner_job_state_constant

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
