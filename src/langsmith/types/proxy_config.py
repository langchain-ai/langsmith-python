# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "ProxyConfig",
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


class AccessControl(BaseModel):
    allow_list: Optional[List[str]] = None

    deny_list: Optional[List[str]] = None


class CallbackRequestHeader(BaseModel):
    name: str

    type: Literal["plaintext", "opaque", "workspace_secret"]

    is_set: Optional[bool] = None

    value: Optional[str] = None


class Callback(BaseModel):
    match_hosts: List[str]

    ttl_seconds: int

    url: str

    full_request: Optional[bool] = None

    request_headers: Optional[List[CallbackRequestHeader]] = None


class RuleAwsSandboxesProxyAwsRoleConfig(BaseModel):
    role_arn: str
    """
    IAM role to assume with AssumeRoleWithWebIdentity, using a short-lived OIDC
    token LangSmith signs for this workspace. The role's trust policy must trust
    LangSmith's issuer for the token subject. Credentials renew automatically, and
    access follows the role's effective AWS permissions. Mutually exclusive with
    static keys, and cannot be changed after creation.
    """

    subject_scope: Optional[str] = None
    """
    SubjectScope picks the token subject the role trusts: "workspace" (the default)
    or "tag:<tag value id>", which must be one of the sandbox's tag_value_ids. Only
    valid with role_arn.
    """


class RuleAwsSandboxesProxyAwsStaticConfigAccessKeyID(BaseModel):
    type: Literal["plaintext", "opaque", "workspace_secret"]

    is_set: Optional[bool] = None

    value: Optional[str] = None


class RuleAwsSandboxesProxyAwsStaticConfigSecretAccessKey(BaseModel):
    type: Literal["plaintext", "opaque", "workspace_secret"]

    is_set: Optional[bool] = None

    value: Optional[str] = None


class RuleAwsSandboxesProxyAwsStaticConfig(BaseModel):
    access_key_id: RuleAwsSandboxesProxyAwsStaticConfigAccessKeyID

    secret_access_key: RuleAwsSandboxesProxyAwsStaticConfigSecretAccessKey

    role_arn: Optional[Literal[""]] = None
    """
    IAM role to assume with AssumeRoleWithWebIdentity, using a short-lived OIDC
    token LangSmith signs for this workspace. The role's trust policy must trust
    LangSmith's issuer for the token subject. Credentials renew automatically, and
    access follows the role's effective AWS permissions. Mutually exclusive with
    static keys, and cannot be changed after creation.
    """


RuleAws: TypeAlias = Union[RuleAwsSandboxesProxyAwsRoleConfig, RuleAwsSandboxesProxyAwsStaticConfig]


class RuleAzureSandboxesProxyAzureWorkloadIdentityConfig(BaseModel):
    client_id: str
    """
    ClientID is the application (client) ID, a GUID, of the app registration or
    user-assigned managed identity whose federated identity credential trusts
    LangSmith's issuer. Required with tenant_id.
    """

    tenant_id: str
    """TenantID is the Entra tenant (directory) ID, a GUID.

    Setting it selects workload identity: LangSmith signs an OIDC token for this
    workspace and exchanges it at Entra ID for access tokens of client_id, so no
    secret is stored. Cannot be changed after creation.
    """

    resources: Optional[
        List[
            Literal[
                "https://storage.azure.com",
                "https://vault.azure.net",
                "https://management.azure.com",
                "https://cognitiveservices.azure.com",
            ]
        ]
    ] = None
    """
    Resources narrows the Entra resources access tokens are obtained for, from
    https://storage.azure.com, https://vault.azure.net, https://management.azure.com
    and https://cognitiveservices.azure.com. Defaults to all of them. Only valid
    with tenant_id.
    """

    subject_scope: Optional[str] = None
    """
    SubjectScope picks the token subject the federated credential trusts:
    "workspace" (the default) or "tag:<tag value id>", which must be one of the
    sandbox's tag_value_ids. Only valid with tenant_id.
    """


class RuleAzureSandboxesProxyAzureAccountKeyConfigAccountKey(BaseModel):
    type: Literal["plaintext", "opaque", "workspace_secret"]

    is_set: Optional[bool] = None

    value: Optional[str] = None


class RuleAzureSandboxesProxyAzureAccountKeyConfig(BaseModel):
    account_key: RuleAzureSandboxesProxyAzureAccountKeyConfigAccountKey

    storage_account: str
    """
    StorageAccount is the storage account static credentials authenticate to:
    requests to its blob, dfs, queue, table and file endpoints. Requires exactly one
    of account_key (requests are signed with SharedKey) or sas_token (appended to
    each request).
    """


class RuleAzureSandboxesProxyAzureSasConfigSasToken(BaseModel):
    type: Literal["plaintext", "opaque", "workspace_secret"]

    is_set: Optional[bool] = None

    value: Optional[str] = None


class RuleAzureSandboxesProxyAzureSasConfig(BaseModel):
    sas_token: RuleAzureSandboxesProxyAzureSasConfigSasToken

    storage_account: str
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


class RuleGcpSandboxesProxyGcpWorkloadIdentityConfig(BaseModel):
    workload_identity_provider: str
    """
    WorkloadIdentityProvider federates an OIDC token LangSmith signs for this
    workspace through Workload Identity Federation instead of a service account key.
    Use the full resource name:
    //iam.googleapis.com/projects/<number>/locations/global/workloadIdentityPools/<pool>/providers/<provider>.
    Cannot be changed after creation.
    """

    scopes: Optional[List[str]] = None
    """Scopes are the OAuth scopes requested for the access token.

    Omit them to use https://www.googleapis.com/auth/cloud-platform.
    """

    service_account_email: Optional[str] = None
    """
    ServiceAccountEmail is the service account to impersonate with the federated
    token. Omit it to use the federated principal directly.
    """

    subject_scope: Optional[str] = None
    """
    SubjectScope picks the token subject the provider trusts: "workspace" (the
    default) or "tag:<tag value id>", which must be one of the sandbox's
    tag_value_ids. Only valid with workload_identity_provider.
    """


class RuleGcpSandboxesProxyGcpServiceAccountConfigServiceAccountJson(BaseModel):
    type: Literal["plaintext", "opaque", "workspace_secret"]

    is_set: Optional[bool] = None

    value: Optional[str] = None


class RuleGcpSandboxesProxyGcpServiceAccountConfig(BaseModel):
    service_account_json: RuleGcpSandboxesProxyGcpServiceAccountConfigServiceAccountJson

    scopes: Optional[List[str]] = None
    """Scopes are the OAuth scopes requested for the access token.

    Omit them to use https://www.googleapis.com/auth/cloud-platform.
    """


RuleGcp: TypeAlias = Union[RuleGcpSandboxesProxyGcpWorkloadIdentityConfig, RuleGcpSandboxesProxyGcpServiceAccountConfig]


class RuleHeader(BaseModel):
    name: str

    type: Literal["plaintext", "opaque", "workspace_secret"]

    is_set: Optional[bool] = None

    value: Optional[str] = None


class Rule(BaseModel):
    name: str

    aws: Optional[RuleAws] = None

    azure: Optional[RuleAzure] = None

    description: Optional[str] = None
    """
    Description says what this rule lets the sandbox reach, so an agent driving the
    sandbox can be told its capabilities. At most 1024 characters.
    """

    enabled: Optional[bool] = None

    env_vars: Optional[Dict[str, str]] = None
    """
    EnvVars are plaintext env vars set for every command in the sandbox while this
    rule is enabled. Use them for tools that refuse to run unless a credential env
    var is present (e.g. gh needs GH_TOKEN) even though this rule injects the real
    credential on the wire — set a dummy value here so the command starts. Explicit
    per-sandbox env_vars win over these, and provider-managed (AWS/GCP) vars win
    over both.
    """

    gcp: Optional[RuleGcp] = None

    headers: Optional[List[RuleHeader]] = None

    match_headers: Optional[List[str]] = None
    """
    MatchHeaders restricts a header injection rule to requests carrying every listed
    header, each written "name: value" with a lowercase name and an exact value.
    Pair with headers of the same name to swap a placeholder the sandbox sends (e.g.
    "authorization: Bearer account-b") for a real credential, so one host can serve
    several accounts. Rules are evaluated in order and the first match wins.
    """

    match_hosts: Optional[List[str]] = None
    """
    MatchHosts is only accepted for header injection and relay rules. Provider auth
    rules use built-in host matching. A relay rule may also list IP addresses and
    CIDR blocks (10.0.0.0/8), which match connections the sandbox makes to an IP
    address rather than a name.
    """

    match_paths: Optional[List[str]] = None

    relay_id: Optional[str] = None
    """
    RelayID is the ID of the LangSmith relay (a connection of kind relay) that
    carries connections to match_hosts when type is relay. Those connections leave
    from the relay's connector, and its network and IP, instead of the sandbox host.
    Access control still applies first, the first enabled matching relay rule wins,
    and a matched host never falls back to a direct connection.
    """

    type: Optional[str] = None


class ProxyConfig(BaseModel):
    access_control: Optional[AccessControl] = None

    callbacks: Optional[List[Callback]] = None

    description: Optional[str] = None
    """
    Description says what this configuration as a whole lets the sandbox reach,
    complementing the per-rule descriptions. At most 1024 characters.
    """

    no_proxy: Optional[List[str]] = None

    rules: Optional[List[Rule]] = None
