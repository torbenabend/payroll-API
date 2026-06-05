from fastapi import APIRouter, Depends, HTTPException

from models import Contract
from dependencies.services import get_contract_service

router = APIRouter(prefix="/contracts", tags=["Contracts"])


@router.get("")
def list_contracts(service = Depends(get_contract_service)):
    return service.list_contracts()


@router.post("")
def create_contract(
        new_contract: Contract,
        service = Depends(get_contract_service)
):
    return service.create_contract(new_contract)


@router.get("/{contract_id}")
def get_contract(
        contract_id: int,
        service = Depends(get_contract_service)
):
    contract = service.get_contract(contract_id)
    if contract is None:
        raise HTTPException(
            status_code=404,
            detail=f"Contract with ID {contract_id} not found"
        )
    return contract


@router.delete("/{contract_id}")
def delete_contract(
        contract_id: int,
        service = Depends(get_contract_service)
):
    deleted_contract = service.delete_contract(contract_id)
    if deleted_contract is None:
        raise HTTPException(
            status_code=404,
            detail=f"Contract with ID {contract_id} not found"
        )
    return deleted_contract


@router.put("/{contract_id}")
def update_contract(
        contract: Contract,
        service = Depends(get_contract_service)
):
    updated_contract = service.update_contract(contract)
    if updated_contract is None:
        raise HTTPException(
            status_code=404,
            detail=f"Contract with ID {contract.id} not found"
        )
    return updated_contract

