# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "SandboxMountConfigParam",
    "Auth",
    "AuthAws",
    "AuthAwsSandboxesSandboxAwsMountRoleAuthConfig",
    "AuthAwsSandboxesSandboxAwsMountStaticAuthConfig",
    "AuthAwsSandboxesSandboxAwsMountStaticAuthConfigAccessKeyID",
    "AuthAwsSandboxesSandboxAwsMountStaticAuthConfigSecretAccessKey",
    "AuthAzure",
    "AuthAzureSandboxesSandboxAzureMountWorkloadIdentityAuthConfig",
    "AuthAzureSandboxesSandboxAzureMountAccountKeyAuthConfig",
    "AuthAzureSandboxesSandboxAzureMountAccountKeyAuthConfigAccountKey",
    "AuthAzureSandboxesSandboxAzureMountSasAuthConfig",
    "AuthAzureSandboxesSandboxAzureMountSasAuthConfigSasToken",
    "AuthGcp",
    "AuthGcpSandboxesSandboxGcpMountWorkloadIdentityAuthConfig",
    "AuthGcpSandboxesSandboxGcpMountServiceAccountAuthConfig",
    "AuthGcpSandboxesSandboxGcpMountServiceAccountAuthConfigServiceAccountJson",
    "Mount",
    "MountSandboxapiS3BucketMountSpec",
    "MountSandboxapiS3BucketMountSpecS3",
    "MountSandboxapiS3BucketMountSpecAzureBlob",
    "MountSandboxapiS3BucketMountSpecCache",
    "MountSandboxapiS3BucketMountSpecContexthub",
    "MountSandboxapiS3BucketMountSpecEncryption",
    "MountSandboxapiS3BucketMountSpecGcs",
    "MountSandboxapiS3BucketMountSpecGit",
    "MountSandboxapiS3BucketMountSpecGitRef",
    "MountSandboxapiGcsBucketMountSpec",
    "MountSandboxapiGcsBucketMountSpecGcs",
    "MountSandboxapiGcsBucketMountSpecAzureBlob",
    "MountSandboxapiGcsBucketMountSpecCache",
    "MountSandboxapiGcsBucketMountSpecContexthub",
    "MountSandboxapiGcsBucketMountSpecEncryption",
    "MountSandboxapiGcsBucketMountSpecGit",
    "MountSandboxapiGcsBucketMountSpecGitRef",
    "MountSandboxapiGcsBucketMountSpecS3",
    "MountSandboxapiGitRepoMountSpec",
    "MountSandboxapiGitRepoMountSpecGit",
    "MountSandboxapiGitRepoMountSpecGitRef",
    "MountSandboxapiGitRepoMountSpecAzureBlob",
    "MountSandboxapiGitRepoMountSpecCache",
    "MountSandboxapiGitRepoMountSpecContexthub",
    "MountSandboxapiGitRepoMountSpecEncryption",
    "MountSandboxapiGitRepoMountSpecGcs",
    "MountSandboxapiGitRepoMountSpecS3",
    "MountSandboxapiContextHubRepoMountSpec",
    "MountSandboxapiContextHubRepoMountSpecContexthub",
    "MountSandboxapiContextHubRepoMountSpecAzureBlob",
    "MountSandboxapiContextHubRepoMountSpecCache",
    "MountSandboxapiContextHubRepoMountSpecEncryption",
    "MountSandboxapiContextHubRepoMountSpecGcs",
    "MountSandboxapiContextHubRepoMountSpecGit",
    "MountSandboxapiContextHubRepoMountSpecGitRef",
    "MountSandboxapiContextHubRepoMountSpecS3",
    "MountSandboxapiAzureBlobContainerMountSpec",
    "MountSandboxapiAzureBlobContainerMountSpecAzureBlob",
    "MountSandboxapiAzureBlobContainerMountSpecCache",
    "MountSandboxapiAzureBlobContainerMountSpecContexthub",
    "MountSandboxapiAzureBlobContainerMountSpecEncryption",
    "MountSandboxapiAzureBlobContainerMountSpecGcs",
    "MountSandboxapiAzureBlobContainerMountSpecGit",
    "MountSandboxapiAzureBlobContainerMountSpecGitRef",
    "MountSandboxapiAzureBlobContainerMountSpecS3",
]


class AuthAwsSandboxesSandboxAwsMountRoleAuthConfig(TypedDict, total=False):
    role_arn: Required[str]
    """
    IAM role to assume with AssumeRoleWithWebIdentity, using a short-lived OIDC
    token LangSmith signs for this workspace; the role's trust policy must trust
    LangSmith's issuer for the token subject. LangSmith scopes the credentials to
    the configured S3 mounts. Mutually exclusive with static credentials, and cannot
    be changed after creation.
    """

    subject_scope: str
    """
    SubjectScope picks the token subject the role trusts: "workspace" (the default)
    or "tag:<tag value id>", which must be one of the sandbox's tag_value_ids. Only
    valid with role_arn.
    """


class AuthAwsSandboxesSandboxAwsMountStaticAuthConfigAccessKeyID(TypedDict, total=False):
    type: Required[Literal["plaintext", "opaque", "workspace_secret"]]

    is_set: bool

    value: str


class AuthAwsSandboxesSandboxAwsMountStaticAuthConfigSecretAccessKey(TypedDict, total=False):
    type: Required[Literal["plaintext", "opaque", "workspace_secret"]]

    is_set: bool

    value: str


class AuthAwsSandboxesSandboxAwsMountStaticAuthConfig(TypedDict, total=False):
    access_key_id: Required[AuthAwsSandboxesSandboxAwsMountStaticAuthConfigAccessKeyID]

    secret_access_key: Required[AuthAwsSandboxesSandboxAwsMountStaticAuthConfigSecretAccessKey]

    role_arn: Literal[""]
    """
    IAM role to assume with AssumeRoleWithWebIdentity, using a short-lived OIDC
    token LangSmith signs for this workspace; the role's trust policy must trust
    LangSmith's issuer for the token subject. LangSmith scopes the credentials to
    the configured S3 mounts. Mutually exclusive with static credentials, and cannot
    be changed after creation.
    """


AuthAws: TypeAlias = Union[
    AuthAwsSandboxesSandboxAwsMountRoleAuthConfig, AuthAwsSandboxesSandboxAwsMountStaticAuthConfig
]


class AuthAzureSandboxesSandboxAzureMountWorkloadIdentityAuthConfig(TypedDict, total=False):
    client_id: Required[str]
    """
    ClientID is the application (client) ID, a GUID, of the app registration or
    user-assigned managed identity whose federated identity credential trusts
    LangSmith's issuer. Required with tenant_id.
    """

    tenant_id: Required[str]
    """TenantID is the Entra tenant (directory) ID, a GUID.

    Setting it selects workload identity: LangSmith signs an OIDC token for this
    workspace and exchanges it at Entra ID for storage access tokens of client_id.
    Cannot be changed after creation.
    """

    subject_scope: str
    """
    SubjectScope picks the token subject the federated credential trusts:
    "workspace" (the default) or "tag:<tag value id>", which must be one of the
    sandbox's tag_value_ids. Only valid with tenant_id.
    """


class AuthAzureSandboxesSandboxAzureMountAccountKeyAuthConfigAccountKey(TypedDict, total=False):
    type: Required[Literal["plaintext", "opaque", "workspace_secret"]]

    is_set: bool

    value: str


class AuthAzureSandboxesSandboxAzureMountAccountKeyAuthConfig(TypedDict, total=False):
    account_key: Required[AuthAzureSandboxesSandboxAzureMountAccountKeyAuthConfigAccountKey]


class AuthAzureSandboxesSandboxAzureMountSasAuthConfigSasToken(TypedDict, total=False):
    type: Required[Literal["plaintext", "opaque", "workspace_secret"]]

    is_set: bool

    value: str


class AuthAzureSandboxesSandboxAzureMountSasAuthConfig(TypedDict, total=False):
    sas_token: Required[AuthAzureSandboxesSandboxAzureMountSasAuthConfigSasToken]


AuthAzure: TypeAlias = Union[
    AuthAzureSandboxesSandboxAzureMountWorkloadIdentityAuthConfig,
    AuthAzureSandboxesSandboxAzureMountAccountKeyAuthConfig,
    AuthAzureSandboxesSandboxAzureMountSasAuthConfig,
]


class AuthGcpSandboxesSandboxGcpMountWorkloadIdentityAuthConfig(TypedDict, total=False):
    workload_identity_provider: Required[str]
    """
    WorkloadIdentityProvider federates an OIDC token LangSmith signs for this
    workspace through Workload Identity Federation instead of a service account key:
    //iam.googleapis.com/projects/<number>/locations/global/workloadIdentityPools/<pool>/providers/<provider>.
    Mutually exclusive with service_account_json. Cannot be changed after creation.
    """

    service_account_email: str
    """
    ServiceAccountEmail is the service account to impersonate with the federated
    token. Omit it to use the federated principal directly. Only valid with
    workload_identity_provider.
    """

    subject_scope: str
    """
    SubjectScope picks the token subject the provider trusts: "workspace" (the
    default) or "tag:<tag value id>", which must be one of the sandbox's
    tag_value_ids. Only valid with workload_identity_provider.
    """


class AuthGcpSandboxesSandboxGcpMountServiceAccountAuthConfigServiceAccountJson(TypedDict, total=False):
    type: Required[Literal["plaintext", "opaque", "workspace_secret"]]

    is_set: bool

    value: str


class AuthGcpSandboxesSandboxGcpMountServiceAccountAuthConfig(TypedDict, total=False):
    service_account_json: Required[AuthGcpSandboxesSandboxGcpMountServiceAccountAuthConfigServiceAccountJson]


AuthGcp: TypeAlias = Union[
    AuthGcpSandboxesSandboxGcpMountWorkloadIdentityAuthConfig, AuthGcpSandboxesSandboxGcpMountServiceAccountAuthConfig
]


class Auth(TypedDict, total=False):
    aws: AuthAws

    azure: AuthAzure

    gcp: AuthGcp


class MountSandboxapiS3BucketMountSpecS3(TypedDict, total=False):
    bucket: Required[str]

    region: Required[str]

    endpoint_url: str

    path_style: bool

    prefix: str


class MountSandboxapiS3BucketMountSpecAzureBlob(TypedDict, total=False):
    container: Required[str]

    storage_account: Required[str]
    """
    StorageAccount is the storage account name: 3 to 24 lowercase letters and
    digits.
    """

    prefix: str


class MountSandboxapiS3BucketMountSpecCache(TypedDict, total=False):
    max_size_bytes: int

    writeback_seconds: int


class MountSandboxapiS3BucketMountSpecContexthub(TypedDict, total=False):
    repo: Required[str]
    """Repo is the Context Hub repository to sync, as "owner/repo" (e.g.

    "-/my-agent", where "-" is the current workspace). The repo's latest commit tree
    is mirrored into the mount path.
    """

    initial_pull_only: bool
    """
    InitialPullOnly syncs the repo once at startup instead of polling for updates
    for the sandbox's lifetime.
    """


class MountSandboxapiS3BucketMountSpecEncryption(TypedDict, total=False):
    kms_key: Required[str]
    """KMSKey is the key to encrypt uploads with.

    S3 mounts take a KMS key ARN in the mount's region.
    """


class MountSandboxapiS3BucketMountSpecGcs(TypedDict, total=False):
    bucket: Required[str]

    prefix: str


class MountSandboxapiS3BucketMountSpecGitRef(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["branch", "tag"]]


class MountSandboxapiS3BucketMountSpecGit(TypedDict, total=False):
    remote_url: Required[str]

    ref: MountSandboxapiS3BucketMountSpecGitRef

    refresh_interval_seconds: int


class MountSandboxapiS3BucketMountSpec(TypedDict, total=False):
    id: Required[str]

    mount_path: Required[str]

    s3: Required[MountSandboxapiS3BucketMountSpecS3]

    type: Required[Literal["s3", "gcs", "azure_blob", "git", "contexthub"]]

    azure_blob: MountSandboxapiS3BucketMountSpecAzureBlob

    cache: MountSandboxapiS3BucketMountSpecCache

    contexthub: MountSandboxapiS3BucketMountSpecContexthub

    encryption: MountSandboxapiS3BucketMountSpecEncryption

    gcs: MountSandboxapiS3BucketMountSpecGcs

    git: MountSandboxapiS3BucketMountSpecGit

    read_only: bool


class MountSandboxapiGcsBucketMountSpecGcs(TypedDict, total=False):
    bucket: Required[str]

    prefix: str


class MountSandboxapiGcsBucketMountSpecAzureBlob(TypedDict, total=False):
    container: Required[str]

    storage_account: Required[str]
    """
    StorageAccount is the storage account name: 3 to 24 lowercase letters and
    digits.
    """

    prefix: str


class MountSandboxapiGcsBucketMountSpecCache(TypedDict, total=False):
    max_size_bytes: int

    writeback_seconds: int


class MountSandboxapiGcsBucketMountSpecContexthub(TypedDict, total=False):
    repo: Required[str]
    """Repo is the Context Hub repository to sync, as "owner/repo" (e.g.

    "-/my-agent", where "-" is the current workspace). The repo's latest commit tree
    is mirrored into the mount path.
    """

    initial_pull_only: bool
    """
    InitialPullOnly syncs the repo once at startup instead of polling for updates
    for the sandbox's lifetime.
    """


class MountSandboxapiGcsBucketMountSpecEncryption(TypedDict, total=False):
    kms_key: Required[str]
    """KMSKey is the key to encrypt uploads with.

    S3 mounts take a KMS key ARN in the mount's region.
    """


class MountSandboxapiGcsBucketMountSpecGitRef(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["branch", "tag"]]


class MountSandboxapiGcsBucketMountSpecGit(TypedDict, total=False):
    remote_url: Required[str]

    ref: MountSandboxapiGcsBucketMountSpecGitRef

    refresh_interval_seconds: int


class MountSandboxapiGcsBucketMountSpecS3(TypedDict, total=False):
    bucket: Required[str]

    region: Required[str]

    endpoint_url: str

    path_style: bool

    prefix: str


class MountSandboxapiGcsBucketMountSpec(TypedDict, total=False):
    id: Required[str]

    gcs: Required[MountSandboxapiGcsBucketMountSpecGcs]

    mount_path: Required[str]

    type: Required[Literal["s3", "gcs", "azure_blob", "git", "contexthub"]]

    azure_blob: MountSandboxapiGcsBucketMountSpecAzureBlob

    cache: MountSandboxapiGcsBucketMountSpecCache

    contexthub: MountSandboxapiGcsBucketMountSpecContexthub

    encryption: MountSandboxapiGcsBucketMountSpecEncryption

    git: MountSandboxapiGcsBucketMountSpecGit

    read_only: bool

    s3: MountSandboxapiGcsBucketMountSpecS3


class MountSandboxapiGitRepoMountSpecGitRef(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["branch", "tag"]]


class MountSandboxapiGitRepoMountSpecGit(TypedDict, total=False):
    remote_url: Required[str]

    ref: MountSandboxapiGitRepoMountSpecGitRef

    refresh_interval_seconds: int


class MountSandboxapiGitRepoMountSpecAzureBlob(TypedDict, total=False):
    container: Required[str]

    storage_account: Required[str]
    """
    StorageAccount is the storage account name: 3 to 24 lowercase letters and
    digits.
    """

    prefix: str


class MountSandboxapiGitRepoMountSpecCache(TypedDict, total=False):
    max_size_bytes: int

    writeback_seconds: int


class MountSandboxapiGitRepoMountSpecContexthub(TypedDict, total=False):
    repo: Required[str]
    """Repo is the Context Hub repository to sync, as "owner/repo" (e.g.

    "-/my-agent", where "-" is the current workspace). The repo's latest commit tree
    is mirrored into the mount path.
    """

    initial_pull_only: bool
    """
    InitialPullOnly syncs the repo once at startup instead of polling for updates
    for the sandbox's lifetime.
    """


class MountSandboxapiGitRepoMountSpecEncryption(TypedDict, total=False):
    kms_key: Required[str]
    """KMSKey is the key to encrypt uploads with.

    S3 mounts take a KMS key ARN in the mount's region.
    """


class MountSandboxapiGitRepoMountSpecGcs(TypedDict, total=False):
    bucket: Required[str]

    prefix: str


class MountSandboxapiGitRepoMountSpecS3(TypedDict, total=False):
    bucket: Required[str]

    region: Required[str]

    endpoint_url: str

    path_style: bool

    prefix: str


class MountSandboxapiGitRepoMountSpec(TypedDict, total=False):
    id: Required[str]

    git: Required[MountSandboxapiGitRepoMountSpecGit]

    mount_path: Required[str]

    type: Required[Literal["s3", "gcs", "azure_blob", "git", "contexthub"]]

    azure_blob: MountSandboxapiGitRepoMountSpecAzureBlob

    cache: MountSandboxapiGitRepoMountSpecCache

    contexthub: MountSandboxapiGitRepoMountSpecContexthub

    encryption: MountSandboxapiGitRepoMountSpecEncryption

    gcs: MountSandboxapiGitRepoMountSpecGcs

    read_only: bool

    s3: MountSandboxapiGitRepoMountSpecS3


class MountSandboxapiContextHubRepoMountSpecContexthub(TypedDict, total=False):
    repo: Required[str]
    """Repo is the Context Hub repository to sync, as "owner/repo" (e.g.

    "-/my-agent", where "-" is the current workspace). The repo's latest commit tree
    is mirrored into the mount path.
    """

    initial_pull_only: bool
    """
    InitialPullOnly syncs the repo once at startup instead of polling for updates
    for the sandbox's lifetime.
    """


class MountSandboxapiContextHubRepoMountSpecAzureBlob(TypedDict, total=False):
    container: Required[str]

    storage_account: Required[str]
    """
    StorageAccount is the storage account name: 3 to 24 lowercase letters and
    digits.
    """

    prefix: str


class MountSandboxapiContextHubRepoMountSpecCache(TypedDict, total=False):
    max_size_bytes: int

    writeback_seconds: int


class MountSandboxapiContextHubRepoMountSpecEncryption(TypedDict, total=False):
    kms_key: Required[str]
    """KMSKey is the key to encrypt uploads with.

    S3 mounts take a KMS key ARN in the mount's region.
    """


class MountSandboxapiContextHubRepoMountSpecGcs(TypedDict, total=False):
    bucket: Required[str]

    prefix: str


class MountSandboxapiContextHubRepoMountSpecGitRef(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["branch", "tag"]]


class MountSandboxapiContextHubRepoMountSpecGit(TypedDict, total=False):
    remote_url: Required[str]

    ref: MountSandboxapiContextHubRepoMountSpecGitRef

    refresh_interval_seconds: int


class MountSandboxapiContextHubRepoMountSpecS3(TypedDict, total=False):
    bucket: Required[str]

    region: Required[str]

    endpoint_url: str

    path_style: bool

    prefix: str


class MountSandboxapiContextHubRepoMountSpec(TypedDict, total=False):
    id: Required[str]

    contexthub: Required[MountSandboxapiContextHubRepoMountSpecContexthub]

    mount_path: Required[str]

    type: Required[Literal["s3", "gcs", "azure_blob", "git", "contexthub"]]

    azure_blob: MountSandboxapiContextHubRepoMountSpecAzureBlob

    cache: MountSandboxapiContextHubRepoMountSpecCache

    encryption: MountSandboxapiContextHubRepoMountSpecEncryption

    gcs: MountSandboxapiContextHubRepoMountSpecGcs

    git: MountSandboxapiContextHubRepoMountSpecGit

    read_only: bool

    s3: MountSandboxapiContextHubRepoMountSpecS3


class MountSandboxapiAzureBlobContainerMountSpecAzureBlob(TypedDict, total=False):
    container: Required[str]

    storage_account: Required[str]
    """
    StorageAccount is the storage account name: 3 to 24 lowercase letters and
    digits.
    """

    prefix: str


class MountSandboxapiAzureBlobContainerMountSpecCache(TypedDict, total=False):
    max_size_bytes: int

    writeback_seconds: int


class MountSandboxapiAzureBlobContainerMountSpecContexthub(TypedDict, total=False):
    repo: Required[str]
    """Repo is the Context Hub repository to sync, as "owner/repo" (e.g.

    "-/my-agent", where "-" is the current workspace). The repo's latest commit tree
    is mirrored into the mount path.
    """

    initial_pull_only: bool
    """
    InitialPullOnly syncs the repo once at startup instead of polling for updates
    for the sandbox's lifetime.
    """


class MountSandboxapiAzureBlobContainerMountSpecEncryption(TypedDict, total=False):
    kms_key: Required[str]
    """KMSKey is the key to encrypt uploads with.

    S3 mounts take a KMS key ARN in the mount's region.
    """


class MountSandboxapiAzureBlobContainerMountSpecGcs(TypedDict, total=False):
    bucket: Required[str]

    prefix: str


class MountSandboxapiAzureBlobContainerMountSpecGitRef(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["branch", "tag"]]


class MountSandboxapiAzureBlobContainerMountSpecGit(TypedDict, total=False):
    remote_url: Required[str]

    ref: MountSandboxapiAzureBlobContainerMountSpecGitRef

    refresh_interval_seconds: int


class MountSandboxapiAzureBlobContainerMountSpecS3(TypedDict, total=False):
    bucket: Required[str]

    region: Required[str]

    endpoint_url: str

    path_style: bool

    prefix: str


class MountSandboxapiAzureBlobContainerMountSpec(TypedDict, total=False):
    id: Required[str]

    azure_blob: Required[MountSandboxapiAzureBlobContainerMountSpecAzureBlob]

    mount_path: Required[str]

    type: Required[Literal["s3", "gcs", "azure_blob", "git", "contexthub"]]

    cache: MountSandboxapiAzureBlobContainerMountSpecCache

    contexthub: MountSandboxapiAzureBlobContainerMountSpecContexthub

    encryption: MountSandboxapiAzureBlobContainerMountSpecEncryption

    gcs: MountSandboxapiAzureBlobContainerMountSpecGcs

    git: MountSandboxapiAzureBlobContainerMountSpecGit

    read_only: bool

    s3: MountSandboxapiAzureBlobContainerMountSpecS3


Mount: TypeAlias = Union[
    MountSandboxapiS3BucketMountSpec,
    MountSandboxapiGcsBucketMountSpec,
    MountSandboxapiGitRepoMountSpec,
    MountSandboxapiContextHubRepoMountSpec,
    MountSandboxapiAzureBlobContainerMountSpec,
]


class SandboxMountConfigParam(TypedDict, total=False):
    auth: Auth

    mounts: Iterable[Mount]
