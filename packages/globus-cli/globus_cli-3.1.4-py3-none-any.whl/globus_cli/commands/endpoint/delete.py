from globus_cli.endpointish import Endpointish
from globus_cli.login_manager import LoginManager
from globus_cli.parsing import command, endpoint_id_arg
from globus_cli.services.transfer import get_client
from globus_cli.termio import FORMAT_TEXT_RAW, formatted_print


@command(
    "delete",
    short_help="Delete an endpoint",
    adoc_examples="""[source,bash]
----
$ ep_id=ddb59aef-6d04-11e5-ba46-22000b92c6ec
$ globus endpoint delete $ep_id
----
""",
)
@endpoint_id_arg
@LoginManager.requires_login(LoginManager.TRANSFER_RS)
def endpoint_delete(endpoint_id: str) -> None:
    """Delete a given endpoint.

    WARNING: Deleting an endpoint will permanently disable any existing shared
    endpoints that are hosted on it.
    """
    client = get_client()
    Endpointish(endpoint_id, transfer_client=client).assert_is_traditional_endpoint()

    res = client.delete_endpoint(endpoint_id)
    formatted_print(res, text_format=FORMAT_TEXT_RAW, response_key="message")
