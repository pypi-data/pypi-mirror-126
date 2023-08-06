from .activation import (
    activation_requirements_help_text,
    autoactivate,
    supported_activation_methods,
)
from .client import CustomTransferClient, get_client
from .data import assemble_generic_doc, display_name_or_cname, iterable_response_to_dict
from .delegate_proxy import fill_delegate_proxy_activation_requirements

ENDPOINT_LIST_FIELDS = (
    ("ID", "id"),
    ("Owner", "owner_string"),
    ("Display Name", display_name_or_cname),
)


__all__ = (
    "ENDPOINT_LIST_FIELDS",
    "CustomTransferClient",
    "get_client",
    "supported_activation_methods",
    "activation_requirements_help_text",
    "autoactivate",
    "fill_delegate_proxy_activation_requirements",
    "display_name_or_cname",
    "iterable_response_to_dict",
    "assemble_generic_doc",
)
