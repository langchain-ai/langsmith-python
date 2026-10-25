# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "ProxyConfigParam",
    "AccessControl",
    "Callback",
    "CallbackRequestHeader",
    "Rule",
    "RuleAws",
    "RuleAwsSandboxesProxyAwsRoleConfig",
    "RuleAwsSandboxesProxyAwsStaticConfig",
    "RuleAwsSandboxesProxyAwsStaticConfigAccessKeyID",
    "RuleAwsSandboxesProxyAwsStaticConfigSecretAccessKey",
    "RuleAzure",
    "RuleAzureSandboxesProxyAzureWorkloadIdentityConfig",
    "RuleAzureSandboxesProxyAzureAccountKeyConfig",
    "RuleAzureSandboxesProxyAzureAccountKeyConfigAccountKey",
    "RuleAzureSandboxesProxyAzureSasConfig",
    "RuleAzureSandboxesProxyAzureSasConfigSasToken",
    "RuleGcp",
    "RuleGcpSandboxesProxyGcpWorkloadIdentityConfig",
    "RuleGcpSandboxesProxyGcpServiceAccountConfig",
    "RuleGcpSandboxesProxyGcpServiceAccountConfigServiceAccountJson",
    "RuleHeader",
]


class AccessControl(TypedDict, total=False):
    allow_list: SequenceNotStr[str]

    deny_list: SequenceNotStr[str]


class CallbackRequestHeader(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["plaintext", "opaque", "workspace_secret"]]

    is_set: bool

    value: str


class Callback(TypedDict, total=False):
    match_hosts: Required[SequenceNotStr[str]]

    ttl_seconds: Required[int]

    url: Required[str]

    full_request: bool

    request_headers: Iterable[CallbackRequestHeader]


class RuleAwsSandboxesProxyAwsRoleConfig(TypedDict, total=False):
    role_arn: Required[str]
    """
    IAM role to assume with AssumeRoleWithWebIdentity, using a short-lived OIDC
    token LangSmith signs for this workspace. The role's trust policy must trust
    LangSmith's issuer for the token subject. Credentials renew automatically, and
    access follows the role's effective AWS permissions. Mutually exclusive with
    static keys, and cannot be changed after creation.
    """

    subject_scope: str
    """
    SubjectScope picks the token subject the role trusts: "workspace" (the default)
    or "tag:<tag value id>", which must be one of the sandbox's tag_value_ids. Only
    valid with role_arn.
    """


class RuleAwsSandboxesProxyAwsStaticConfigAccessKeyID(TypedDict, total=False):
    type: Required[Literal["plaintext", "opaque", "workspace_secret"]]

    is_set: bool

    value: str


class RuleAwsSandboxesProxyAwsStaticConfigSecretAccessKey(TypedDict, total=False):
    type: Required[Literal["plaintext", "opaque", "workspace_secret"]]

    is_set: bool

    value: str


class RuleAwsSandboxesProxyAwsStaticConfig(TypedDict, total=False):
    access_key_id: Required[RuleAwsSandboxesProxyAwsStaticConfigAccessKeyID]

    secret_access_key: Required[RuleAwsSandboxesProxyAwsStaticConfigSecretAccessKey]

    role_arn: Literal[""]
    """
    IAM role to assume with AssumeRoleWithWebIdentity, using a short-lived OIDC
    token LangSmith signs for this workspace. The role's trust policy must trust
    LangSmith's issuer for the token subject. Credentials renew automatically, and
    access follows the role's effective AWS permissions. Mutually exclusive with
    static keys, and cannot be changed after creation.
    """


RuleAws: TypeAlias = Union[RuleAwsSandboxesProxyAwsRoleConfig, RuleAwsSandboxesProxyAwsStaticConfig]


class RuleAzureSandboxesProxyAzureWorkloadIdentityConfig(TypedDict, total=False):
    client_id: Required[str]
    """
    ClientID is the application (client) ID, a GUID, of the app registration or
    user-assigned managed identity whose federated identity credential trusts
    LangSmith's issuer. Required with tenant_id.
    """

    tenant_id: Required[str]
    """TenantID is the Entra tenant (directory) ID, a GUID.

    Setting it selects workload identity: LangSmith signs an OIDC token for this
    workspace and exchanges it at Entra ID for access tokens of client_id, so no
    secret is stored. Cannot be changed after creation.
    """

    resources: List[
        Literal[
            "https://storage.azure.com",
            "https://vault.azure.net",
            "https://management.azure.com",
            "https://cognitiveservices.azure.com",
        ]
    ]
    """
    Resources narrows the Entra resources access tokens are obtained for, from
    https://storage.azure.com, https://vault.azure.net, https://management.azure.com
    and https://cognitiveservices.azure.com. Defaults to all of them. Only valid
    with tenant_id.
    """

    subject_scope: str
    """
    SubjectScope picks the token subject the federated credential trusts:
    "workspace" (the default) or "tag:<tag value id>", which must be one of the
    sandbox's tag_value_ids. Only valid with tenant_id.
    """


class RuleAzureSandboxesProxyAzureAccountKeyConfigAccountKey(TypedDict, total=False):
    type: Required[Literal["plaintext", "opaque", "workspace_secret"]]

    is_set: bool

    value: str


class RuleAzureSandboxesProxyAzureAccountKeyConfig(TypedDict, total=False):
    account_key: Required[RuleAzureSandboxesProxyAzureAccountKeyConfigAccountKey]

    storage_account: Required[str]
    """
    StorageAccount is the storage account static credentials authenticate to:
    requests to its blob, dfs, queue, table and file endpoints. Requires exactly one
    of account_key (requests are signed with SharedKey) or sas_token (appended to
    each request).
    """


class RuleAzureSandboxesProxyAzureSasConfigSasToken(TypedDict, total=False):
    type: Required[Literal["plaintext", "opaque", "workspace_secret"]]

    is_set: bool

    value: str


class RuleAzureSandboxesProxyAzureSasConfig(TypedDict, total=False):
    sas_token: Required[RuleAzureSandboxesProxyAzureSasConfigSasToken]

    storage_account: Required[str]
    """
    StorageAccount is the storage account static credentials authenticate to:
    requests to its blob, dfs, queue, table and file endpoints. Requires exactly one
    of account_key (requests are signed with SharedKey) or sas_token (appended to
    each request).
    """


RuleAzure: TypeAlias = Union[
    RuleAzureSandboxesProxyAzureWorkloadIdentityConfig,
    RuleAzureSandboxesProxyAzureAccountKeyConfig,
    RuleAzureSandboxesProxyAzureSasConfig,
]


class RuleGcpSandboxesProxyGcpWorkloadIdentityConfig(TypedDict, total=False):
    workload_identity_provider: Required[str]
    """
    WorkloadIdentityProvider federates an OIDC token LangSmith signs for this
    workspace through Workload Identity Federation instead of a service account key.
    Use the full resource name:
    //iam.googleapis.com/projects/<number>/locations/global/workloadIdentityPools/<pool>/providers/<provider>.
    Cannot be changed after creation.
    """

    scopes: SequenceNotStr[str]
    """Scopes are the OAuth scopes requested for the access token.

    Omit them to use https://www.googleapis.com/auth/cloud-platform.
    """

    service_account_email: str
    """
    ServiceAccountEmail is the service account to impersonate with the federated
    token. Omit it to use the federated principal directly.
    """

    subject_scope: str
    """
    SubjectScope picks the token subject the provider trusts: "workspace" (the
    default) or "tag:<tag value id>", which must be one of the sandbox's
    tag_value_ids. Only valid with workload_identity_provider.
    """


class RuleGcpSandboxesProxyGcpServiceAccountConfigServiceAccountJson(TypedDict, total=False):
    type: Required[Literal["plaintext", "opaque", "workspace_secret"]]

    is_set: bool

    value: str


class RuleGcpSandboxesProxyGcpServiceAccountConfig(TypedDict, total=False):
    service_account_json: Required[RuleGcpSandboxesProxyGcpServiceAccountConfigServiceAccountJson]

    scopes: SequenceNotStr[str]
    """Scopes are the OAuth scopes requested for the access token.

    Omit them to use https://www.googleapis.com/auth/cloud-platform.
    """


RuleGcp: TypeAlias = Union[RuleGcpSandboxesProxyGcpWorkloadIdentityConfig, RuleGcpSandboxesProxyGcpServiceAccountConfig]


class RuleHeader(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["plaintext", "opaque", "workspace_secret"]]

    is_set: bool

    value: str


class Rule(TypedDict, total=False):
    name: Required[str]

    aws: RuleAws

    azure: RuleAzure

    description: str
    """
    Description says what this rule lets the sandbox reach, so an agent driving the
    sandbox can be told its capabilities. At most 1024 characters.
    """

    enabled: bool

    env_vars: Dict[str, str]
    """
    EnvVars are plaintext env vars set for every command in the sandbox while this
    rule is enabled. Use them for tools that refuse to run unless a credential env
    var is present (e.g. gh needs GH_TOKEN) even though this rule injects the real
    credential on the wire — set a dummy value here so the command starts. Explicit
    per-sandbox env_vars win over these, and provider-managed (AWS/GCP) vars win
    over both.
    """

    gcp: RuleGcp

    headers: Iterable[RuleHeader]

    match_headers: SequenceNotStr[str]
    """
    MatchHeaders restricts a header injection rule to requests carrying every listed
    header, each written "name: value" with a lowercase name and an exact value.
    Pair with headers of the same name to swap a placeholder the sandbox sends (e.g.
    "authorization: Bearer account-b") for a real credential, so one host can serve
    several accounts. Rules are evaluated in order and the first match wins.
    """

    match_hosts: SequenceNotStr[str]
    """
    MatchHosts is only accepted for header injection and relay rules. Provider auth
    rules use built-in host matching. A relay rule may also list IP addresses and
    CIDR blocks (10.0.0.0/8), which match connections the sandbox makes to an IP
    address rather than a name.
    """

    match_paths: SequenceNotStr[str]

    relay_id: str
    """
    RelayID is the ID of the LangSmith relay (a connection of kind relay) that
    carries connections to match_hosts when type is relay. Those connections leave
    from the relay's connector, and its network and IP, instead of the sandbox host.
    Access control still applies first, the first enabled matching relay rule wins,
    and a matched host never falls back to a direct connection.
    """

    type: str


class ProxyConfigParam(TypedDict, total=False):
    access_control: AccessControl

    callbacks: Iterable[Callback]

    description: str
    """
    Description says what this configuration as a whole lets the sandbox reach,
    complementing the per-rule descriptions. At most 1024 characters.
    """

    no_proxy: SequenceNotStr[str]

    rules: Iterable[Rule]
