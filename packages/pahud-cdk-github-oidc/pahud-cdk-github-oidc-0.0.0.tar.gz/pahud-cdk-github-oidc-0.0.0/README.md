# cdk-github-oidc

Inspired by [aripalo/aws-cdk-github-oidc](https://github.com/aripalo/aws-cdk-github-oidc), this repository allows you to create a `Github OpenID Connect Identity Provider` with the `OpenIdConnectProvider` CDK construct and generate federated IAM roles from this provider used in one or multiple Github repositories.

# Sample

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
from cdk_github_oidc import OpenIdConnectProvider

# create the provider
provider = OpenIdConnectProvider(stack, "GithubOpenIdConnectProvider")
# create an IAM role from this provider
provider.create_role("demo-role", [owner="pahud", repo="gitpod-workspace", owner="pahud", repo="github-codespace", owner="pahud", repo="vscode"
])
```
