# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "SandboxMountConfig",
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


class AuthAwsSandboxesSandboxAwsMountRoleAuthConfig(BaseModel):
    role_arn: str
    """
    IAM role to assume with AssumeRoleWithWebIdentity, using a short-lived OIDC
    token LangSmith signs for this workspace; the role's trust policy must trust
    LangSmith's issuer for the token subject. LangSmith scopes the credentials to
    the configured S3 mounts. Mutually exclusive with static credentials, and cannot
    be changed after creation.
    """

    subject_scope: Optional[str] = None
    """
    SubjectScope picks the token subject the role trusts: "workspace" (the default)
    or "tag:<tag value id>", which must be one of the sandbox's tag_value_ids. Only
    valid with role_arn.
    """


class AuthAwsSandboxesSandboxAwsMountStaticAuthConfigAccessKeyID(BaseModel):
    type: Literal["plaintext", "opaque", "workspace_secret"]

    is_set: Optional[bool] = None

    value: Optional[str] = None


class AuthAwsSandboxesSandboxAwsMountStaticAuthConfigSecretAccessKey(BaseModel):
    type: Literal["plaintext", "opaque", "workspace_secret"]

    is_set: Optional[bool] = None

    value: Optional[str] = None


class AuthAwsSandboxesSandboxAwsMountStaticAuthConfig(BaseModel):
    access_key_id: AuthAwsSandboxesSandboxAwsMountStaticAuthConfigAccessKeyID

    secret_access_key: AuthAwsSandboxesSandboxAwsMountStaticAuthConfigSecretAccessKey

    role_arn: Optional[Literal[""]] = None
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


class AuthAzureSandboxesSandboxAzureMountWorkloadIdentityAuthConfig(BaseModel):
    client_id: str
    """
    ClientID is the application (client) ID, a GUID, of the app registration or
    user-assigned managed identity whose federated identity credential trusts
    LangSmith's issuer. Required with tenant_id.
    """

    tenant_id: str
    """TenantID is the Entra tenant (directory) ID, a GUID.

    Setting it selects workload identity: LangSmith signs an OIDC token for this
    workspace and exchanges it at Entra ID for storage access tokens of client_id.
    Cannot be changed after creation.
    """

    subject_scope: Optional[str] = None
    """
    SubjectScope picks the token subject the federated credential trusts:
    "workspace" (the default) or "tag:<tag value id>", which must be one of the
    sandbox's tag_value_ids. Only valid with tenant_id.
    """


class AuthAzureSandboxesSandboxAzureMountAccountKeyAuthConfigAccountKey(BaseModel):
    type: Literal["plaintext", "opaque", "workspace_secret"]

    is_set: Optional[bool] = None

    value: Optional[str] = None


class AuthAzureSandboxesSandboxAzureMountAccountKeyAuthConfig(BaseModel):
    account_key: AuthAzureSandboxesSandboxAzureMountAccountKeyAuthConfigAccountKey


class AuthAzureSandboxesSandboxAzureMountSasAuthConfigSasToken(BaseModel):
    type: Literal["plaintext", "opaque", "workspace_secret"]

    is_set: Optional[bool] = None

    value: Optional[str] = None


class AuthAzureSandboxesSandboxAzureMountSasAuthConfig(BaseModel):
    sas_token: AuthAzureSandboxesSandboxAzureMountSasAuthConfigSasToken


AuthAzure: TypeAlias = Union[
    AuthAzureSandboxesSandboxAzureMountWorkloadIdentityAuthConfig,
    AuthAzureSandboxesSandboxAzureMountAccountKeyAuthConfig,
    AuthAzureSandboxesSandboxAzureMountSasAuthConfig,
]


class AuthGcpSandboxesSandboxGcpMountWorkloadIdentityAuthConfig(BaseModel):
    workload_identity_provider: str
    """
    WorkloadIdentityProvider federates an OIDC token LangSmith signs for this
    workspace through Workload Identity Federation instead of a service account key:
    //iam.googleapis.com/projects/<number>/locations/global/workloadIdentityPools/<pool>/providers/<provider>.
    Mutually exclusive with service_account_json. Cannot be changed after creation.
    """

    service_account_email: Optional[str] = None
    """
    ServiceAccountEmail is the service account to impersonate with the federated
    token. Omit it to use the federated principal directly. Only valid with
    workload_identity_provider.
    """

    subject_scope: Optional[str] = None
    """
    SubjectScope picks the token subject the provider trusts: "workspace" (the
    default) or "tag:<tag value id>", which must be one of the sandbox's
    tag_value_ids. Only valid with workload_identity_provider.
    """


class AuthGcpSandboxesSandboxGcpMountServiceAccountAuthConfigServiceAccountJson(BaseModel):
    type: Literal["plaintext", "opaque", "workspace_secret"]

    is_set: Optional[bool] = None

    value: Optional[str] = None


class AuthGcpSandboxesSandboxGcpMountServiceAccountAuthConfig(BaseModel):
    service_account_json: AuthGcpSandboxesSandboxGcpMountServiceAccountAuthConfigServiceAccountJson


AuthGcp: TypeAlias = Union[
    AuthGcpSandboxesSandboxGcpMountWorkloadIdentityAuthConfig, AuthGcpSandboxesSandboxGcpMountServiceAccountAuthConfig
]


class Auth(BaseModel):
    aws: Optional[AuthAws] = None

    azure: Optional[AuthAzure] = None

    gcp: Optional[AuthGcp] = None


class MountSandboxapiS3BucketMountSpecS3(BaseModel):
    bucket: str

    region: str

    endpoint_url: Optional[str] = None

    path_style: Optional[bool] = None

    prefix: Optional[str] = None


class MountSandboxapiS3BucketMountSpecAzureBlob(BaseModel):
    container: str

    storage_account: str
    """
    StorageAccount is the storage account name: 3 to 24 lowercase letters and
    digits.
    """

    prefix: Optional[str] = None


class MountSandboxapiS3BucketMountSpecCache(BaseModel):
    max_size_bytes: Optional[int] = None

    writeback_seconds: Optional[int] = None


class MountSandboxapiS3BucketMountSpecContexthub(BaseModel):
    repo: str
    """Repo is the Context Hub repository to sync, as "owner/repo" (e.g.

    "-/my-agent", where "-" is the current workspace). The repo's latest commit tree
    is mirrored into the mount path.
    """

    initial_pull_only: Optional[bool] = None
    """
    InitialPullOnly syncs the repo once at startup instead of polling for updates
    for the sandbox's lifetime.
    """


class MountSandboxapiS3BucketMountSpecEncryption(BaseModel):
    kms_key: str
    """KMSKey is the key to encrypt uploads with.

    S3 mounts take a KMS key ARN in the mount's region.
    """


class MountSandboxapiS3BucketMountSpecGcs(BaseModel):
    bucket: str

    prefix: Optional[str] = None


class MountSandboxapiS3BucketMountSpecGitRef(BaseModel):
    name: str

    type: Literal["branch", "tag"]


class MountSandboxapiS3BucketMountSpecGit(BaseModel):
    remote_url: str

    ref: Optional[MountSandboxapiS3BucketMountSpecGitRef] = None

    refresh_interval_seconds: Optional[int] = None


class MountSandboxapiS3BucketMountSpec(BaseModel):
    id: str

    mount_path: str

    s3: MountSandboxapiS3BucketMountSpecS3

    type: Literal["s3", "gcs", "azure_blob", "git", "contexthub"]

    azure_blob: Optional[MountSandboxapiS3BucketMountSpecAzureBlob] = None

    cache: Optional[MountSandboxapiS3BucketMountSpecCache] = None

    contexthub: Optional[MountSandboxapiS3BucketMountSpecContexthub] = None

    encryption: Optional[MountSandboxapiS3BucketMountSpecEncryption] = None

    gcs: Optional[MountSandboxapiS3BucketMountSpecGcs] = None

    git: Optional[MountSandboxapiS3BucketMountSpecGit] = None

    read_only: Optional[bool] = None


class MountSandboxapiGcsBucketMountSpecGcs(BaseModel):
    bucket: str

    prefix: Optional[str] = None


class MountSandboxapiGcsBucketMountSpecAzureBlob(BaseModel):
    container: str

    storage_account: str
    """
    StorageAccount is the storage account name: 3 to 24 lowercase letters and
    digits.
    """

    prefix: Optional[str] = None


class MountSandboxapiGcsBucketMountSpecCache(BaseModel):
    max_size_bytes: Optional[int] = None

    writeback_seconds: Optional[int] = None


class MountSandboxapiGcsBucketMountSpecContexthub(BaseModel):
    repo: str
    """Repo is the Context Hub repository to sync, as "owner/repo" (e.g.

    "-/my-agent", where "-" is the current workspace). The repo's latest commit tree
    is mirrored into the mount path.
    """

    initial_pull_only: Optional[bool] = None
    """
    InitialPullOnly syncs the repo once at startup instead of polling for updates
    for the sandbox's lifetime.
    """


class MountSandboxapiGcsBucketMountSpecEncryption(BaseModel):
    kms_key: str
    """KMSKey is the key to encrypt uploads with.

    S3 mounts take a KMS key ARN in the mount's region.
    """


class MountSandboxapiGcsBucketMountSpecGitRef(BaseModel):
    name: str

    type: Literal["branch", "tag"]


class MountSandboxapiGcsBucketMountSpecGit(BaseModel):
    remote_url: str

    ref: Optional[MountSandboxapiGcsBucketMountSpecGitRef] = None

    refresh_interval_seconds: Optional[int] = None


class MountSandboxapiGcsBucketMountSpecS3(BaseModel):
    bucket: str

    region: str

    endpoint_url: Optional[str] = None

    path_style: Optional[bool] = None

    prefix: Optional[str] = None


class MountSandboxapiGcsBucketMountSpec(BaseModel):
    id: str

    gcs: MountSandboxapiGcsBucketMountSpecGcs

    mount_path: str

    type: Literal["s3", "gcs", "azure_blob", "git", "contexthub"]

    azure_blob: Optional[MountSandboxapiGcsBucketMountSpecAzureBlob] = None

    cache: Optional[MountSandboxapiGcsBucketMountSpecCache] = None

    contexthub: Optional[MountSandboxapiGcsBucketMountSpecContexthub] = None

    encryption: Optional[MountSandboxapiGcsBucketMountSpecEncryption] = None

    git: Optional[MountSandboxapiGcsBucketMountSpecGit] = None

    read_only: Optional[bool] = None

    s3: Optional[MountSandboxapiGcsBucketMountSpecS3] = None


class MountSandboxapiGitRepoMountSpecGitRef(BaseModel):
    name: str

    type: Literal["branch", "tag"]


class MountSandboxapiGitRepoMountSpecGit(BaseModel):
    remote_url: str

    ref: Optional[MountSandboxapiGitRepoMountSpecGitRef] = None

    refresh_interval_seconds: Optional[int] = None


class MountSandboxapiGitRepoMountSpecAzureBlob(BaseModel):
    container: str

    storage_account: str
    """
    StorageAccount is the storage account name: 3 to 24 lowercase letters and
    digits.
    """

    prefix: Optional[str] = None


class MountSandboxapiGitRepoMountSpecCache(BaseModel):
    max_size_bytes: Optional[int] = None

    writeback_seconds: Optional[int] = None


class MountSandboxapiGitRepoMountSpecContexthub(BaseModel):
    repo: str
    """Repo is the Context Hub repository to sync, as "owner/repo" (e.g.

    "-/my-agent", where "-" is the current workspace). The repo's latest commit tree
    is mirrored into the mount path.
    """

    initial_pull_only: Optional[bool] = None
    """
    InitialPullOnly syncs the repo once at startup instead of polling for updates
    for the sandbox's lifetime.
    """


class MountSandboxapiGitRepoMountSpecEncryption(BaseModel):
    kms_key: str
    """KMSKey is the key to encrypt uploads with.

    S3 mounts take a KMS key ARN in the mount's region.
    """


class MountSandboxapiGitRepoMountSpecGcs(BaseModel):
    bucket: str

    prefix: Optional[str] = None


class MountSandboxapiGitRepoMountSpecS3(BaseModel):
    bucket: str

    region: str

    endpoint_url: Optional[str] = None

    path_style: Optional[bool] = None

    prefix: Optional[str] = None


class MountSandboxapiGitRepoMountSpec(BaseModel):
    id: str

    git: MountSandboxapiGitRepoMountSpecGit

    mount_path: str

    type: Literal["s3", "gcs", "azure_blob", "git", "contexthub"]

    azure_blob: Optional[MountSandboxapiGitRepoMountSpecAzureBlob] = None

    cache: Optional[MountSandboxapiGitRepoMountSpecCache] = None

    contexthub: Optional[MountSandboxapiGitRepoMountSpecContexthub] = None

    encryption: Optional[MountSandboxapiGitRepoMountSpecEncryption] = None

    gcs: Optional[MountSandboxapiGitRepoMountSpecGcs] = None

    read_only: Optional[bool] = None

    s3: Optional[MountSandboxapiGitRepoMountSpecS3] = None


class MountSandboxapiContextHubRepoMountSpecContexthub(BaseModel):
    repo: str
    """Repo is the Context Hub repository to sync, as "owner/repo" (e.g.

    "-/my-agent", where "-" is the current workspace). The repo's latest commit tree
    is mirrored into the mount path.
    """

    initial_pull_only: Optional[bool] = None
    """
    InitialPullOnly syncs the repo once at startup instead of polling for updates
    for the sandbox's lifetime.
    """


class MountSandboxapiContextHubRepoMountSpecAzureBlob(BaseModel):
    container: str

    storage_account: str
    """
    StorageAccount is the storage account name: 3 to 24 lowercase letters and
    digits.
    """

    prefix: Optional[str] = None


class MountSandboxapiContextHubRepoMountSpecCache(BaseModel):
    max_size_bytes: Optional[int] = None

    writeback_seconds: Optional[int] = None


class MountSandboxapiContextHubRepoMountSpecEncryption(BaseModel):
    kms_key: str
    """KMSKey is the key to encrypt uploads with.

    S3 mounts take a KMS key ARN in the mount's region.
    """


class MountSandboxapiContextHubRepoMountSpecGcs(BaseModel):
    bucket: str

    prefix: Optional[str] = None


class MountSandboxapiContextHubRepoMountSpecGitRef(BaseModel):
    name: str

    type: Literal["branch", "tag"]


class MountSandboxapiContextHubRepoMountSpecGit(BaseModel):
    remote_url: str

    ref: Optional[MountSandboxapiContextHubRepoMountSpecGitRef] = None

    refresh_interval_seconds: Optional[int] = None


class MountSandboxapiContextHubRepoMountSpecS3(BaseModel):
    bucket: str

    region: str

    endpoint_url: Optional[str] = None

    path_style: Optional[bool] = None

    prefix: Optional[str] = None


class MountSandboxapiContextHubRepoMountSpec(BaseModel):
    id: str

    contexthub: MountSandboxapiContextHubRepoMountSpecContexthub

    mount_path: str

    type: Literal["s3", "gcs", "azure_blob", "git", "contexthub"]

    azure_blob: Optional[MountSandboxapiContextHubRepoMountSpecAzureBlob] = None

    cache: Optional[MountSandboxapiContextHubRepoMountSpecCache] = None

    encryption: Optional[MountSandboxapiContextHubRepoMountSpecEncryption] = None

    gcs: Optional[MountSandboxapiContextHubRepoMountSpecGcs] = None

    git: Optional[MountSandboxapiContextHubRepoMountSpecGit] = None

    read_only: Optional[bool] = None

    s3: Optional[MountSandboxapiContextHubRepoMountSpecS3] = None


class MountSandboxapiAzureBlobContainerMountSpecAzureBlob(BaseModel):
    container: str

    storage_account: str
    """
    StorageAccount is the storage account name: 3 to 24 lowercase letters and
    digits.
    """

    prefix: Optional[str] = None


class MountSandboxapiAzureBlobContainerMountSpecCache(BaseModel):
    max_size_bytes: Optional[int] = None

    writeback_seconds: Optional[int] = None


class MountSandboxapiAzureBlobContainerMountSpecContexthub(BaseModel):
    repo: str
    """Repo is the Context Hub repository to sync, as "owner/repo" (e.g.

    "-/my-agent", where "-" is the current workspace). The repo's latest commit tree
    is mirrored into the mount path.
    """

    initial_pull_only: Optional[bool] = None
    """
    InitialPullOnly syncs the repo once at startup instead of polling for updates
    for the sandbox's lifetime.
    """


class MountSandboxapiAzureBlobContainerMountSpecEncryption(BaseModel):
    kms_key: str
    """KMSKey is the key to encrypt uploads with.

    S3 mounts take a KMS key ARN in the mount's region.
    """


class MountSandboxapiAzureBlobContainerMountSpecGcs(BaseModel):
    bucket: str

    prefix: Optional[str] = None


class MountSandboxapiAzureBlobContainerMountSpecGitRef(BaseModel):
    name: str

    type: Literal["branch", "tag"]


class MountSandboxapiAzureBlobContainerMountSpecGit(BaseModel):
    remote_url: str

    ref: Optional[MountSandboxapiAzureBlobContainerMountSpecGitRef] = None

    refresh_interval_seconds: Optional[int] = None


class MountSandboxapiAzureBlobContainerMountSpecS3(BaseModel):
    bucket: str

    region: str

    endpoint_url: Optional[str] = None

    path_style: Optional[bool] = None

    prefix: Optional[str] = None


class MountSandboxapiAzureBlobContainerMountSpec(BaseModel):
    id: str

    azure_blob: MountSandboxapiAzureBlobContainerMountSpecAzureBlob

    mount_path: str

    type: Literal["s3", "gcs", "azure_blob", "git", "contexthub"]

    cache: Optional[MountSandboxapiAzureBlobContainerMountSpecCache] = None

    contexthub: Optional[MountSandboxapiAzureBlobContainerMountSpecContexthub] = None

    encryption: Optional[MountSandboxapiAzureBlobContainerMountSpecEncryption] = None

    gcs: Optional[MountSandboxapiAzureBlobContainerMountSpecGcs] = None

    git: Optional[MountSandboxapiAzureBlobContainerMountSpecGit] = None

    read_only: Optional[bool] = None

    s3: Optional[MountSandboxapiAzureBlobContainerMountSpecS3] = None


Mount: TypeAlias = Union[
    MountSandboxapiS3BucketMountSpec,
    MountSandboxapiGcsBucketMountSpec,
    MountSandboxapiGitRepoMountSpec,
    MountSandboxapiContextHubRepoMountSpec,
    MountSandboxapiAzureBlobContainerMountSpec,
]


class SandboxMountConfig(BaseModel):
    auth: Optional[Auth] = None

    mounts: Optional[List[Mount]] = None
