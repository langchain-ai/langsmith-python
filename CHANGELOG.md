# Changelog

## [0.15.0](https://github.com/langchain-ai/langsmith-python/compare/v0.14.12...v0.15.0) (2026-10-24)


### ⚠ BREAKING CHANGES

* **sandboxes:** add sandbox volumes

### Features

* add agent owner API support ([6854d88](https://github.com/langchain-ai/langsmith-python/commit/6854d8813f18143f8f5ec2af758eade440e6b020))
* **engine:** scan and fix GitLab projects through a workspace service account ([19f9076](https://github.com/langchain-ai/langsmith-python/commit/19f90767908aec4a9c6ca11d90c01e913e7df153))
* **js-sdk:** batch createFeedback through the multipart endpoint ([a6569b5](https://github.com/langchain-ai/langsmith-python/commit/a6569b5fbf212fe58b624faf07003d7def5709ab))
* let Engine boards verify without requesting a preview ([f1c915e](https://github.com/langchain-ai/langsmith-python/commit/f1c915e6a7b249951ed8d9e8aaa5e39212643704))
* **sandboxes:** add sandbox volumes ([f4bef1c](https://github.com/langchain-ai/langsmith-python/commit/f4bef1ccbb20849a121e69a13f86913f4e3bc000))
* **sandboxes:** create non-persistent sandboxes with `persistent: false` (private beta), never billed for storage ([4f8def7](https://github.com/langchain-ai/langsmith-python/commit/4f8def7c176c33813aa1d190ccaf95332d165a94))
* **sandboxes:** relay sandbox egress through a customer's network ([9363303](https://github.com/langchain-ai/langsmith-python/commit/9363303d3788f4fa399067ca60c7c65c920db990))
* **sandboxes:** sandbox functions ([89f7345](https://github.com/langchain-ai/langsmith-python/commit/89f73451e4c0de94c78cb5636011ea60d4058354))
* **sdk:** add select and exclude_default_fields to list_examples in the Python SDK ([bbf5b46](https://github.com/langchain-ai/langsmith-python/commit/bbf5b469559fe95c69f6832e82e2d9bc8cf50ac3))
* **sdks:** add resolve_destination to the Python SDK ([012283c](https://github.com/langchain-ai/langsmith-python/commit/012283cdfa9123b8119e84601355a311c4547464))


### Bug Fixes

* **py:** make Client.flush() wait for buffered run ops ([ccfb6b5](https://github.com/langchain-ai/langsmith-python/commit/ccfb6b5c1df5f839df02684dc121ae4f6dfb9155))
* **sdk-python:** stop AsyncExperimentResults iteration from hanging when processing fails ([ba06e4b](https://github.com/langchain-ai/langsmith-python/commit/ba06e4b29fb3f151cf98ed07d3bffca796b51853))
* **sdk:** default Python agent creation to EXTERNAL ([39fb8af](https://github.com/langchain-ai/langsmith-python/commit/39fb8af8a50c07aab13f634e725b8d4de9818fea))
* **security:** update application certifi bundles ([82a5a67](https://github.com/langchain-ai/langsmith-python/commit/82a5a67f274c0900ea50108f0b00fe903373f6f6))


### Build System

* **deps:** consolidate dependency updates and align checkpoint versions ([5cdd396](https://github.com/langchain-ai/langsmith-python/commit/5cdd3965ab971d2766d106f108daea4ffe31dbe5))

## [0.14.12](https://github.com/langchain-ai/langsmith-python/compare/v0.14.11...v0.14.12) (2026-10-21)


### Features

* **agents:** add agent registry CRUD to SDKs and CLI ([d3de1d5](https://github.com/langchain-ai/langsmith-python/commit/d3de1d5e012e92e9f585e43c2ed6bb2bc05703bc))
* **authz:** add root_run_metadata policy conditions and compiled trace_filters ([64684e0](https://github.com/langchain-ai/langsmith-python/commit/64684e058ff7339501fb121920cb8d04a2517a43))
* **cli:** expose runs share and get-url to the CLI ([fcfae7c](https://github.com/langchain-ai/langsmith-python/commit/fcfae7cde308b3962eb324bed7aa2772f116ea87))
* **evaluators:** add trajectory input type for code evaluators ([9b6f6e5](https://github.com/langchain-ai/langsmith-python/commit/9b6f6e540ac7c2f6f9e96d26ab78c546cf15e6af))
* **sandboxes:** let LangSmith login service URLs be embedded by named origins ([dcf7c3e](https://github.com/langchain-ai/langsmith-python/commit/dcf7c3e1e2278756d4528a21ac279be2446db95f))
* **sdk-python:** create enforced feedback configs ([1e3cd15](https://github.com/langchain-ai/langsmith-python/commit/1e3cd1519115b805913c624239323c580fb14e2d))


### Bug Fixes

* **sandboxes:** add cursor pagination to registry listing ([1a44460](https://github.com/langchain-ai/langsmith-python/commit/1a444601f66ef1fe6ac53671b89177a8b2fc2992))
* **sdk-python:** use reference outputs for example creation ([f995f42](https://github.com/langchain-ai/langsmith-python/commit/f995f42b7e7d51ff8f0dcd1acc823573558a482f))
* **sdk-python:** use reference outputs for example creation ([7cbb508](https://github.com/langchain-ai/langsmith-python/commit/7cbb5087ab823fd1f3e97601d76a237a8e09a00b))
* **sdk:** keep wrap_openai Responses stream output when it ends incomplete or failed ([e88c57c](https://github.com/langchain-ai/langsmith-python/commit/e88c57cd3f87ffec9dd6d46027026a6821ea8f03))
* support Standard Units in sandbox cost breakdowns ([e9bee5c](https://github.com/langchain-ai/langsmith-python/commit/e9bee5c23eaf328998430a134318c5161dd02fcf))


### Chores

* remove langsmith-sdk and staging repo leftovers, update SDK docs ([459d4bd](https://github.com/langchain-ai/langsmith-python/commit/459d4bd46205d422b0466227cb431de73973c2ca))


### Documentation

* move sandbox auth options to the bottom of README.md ([#71](https://github.com/langchain-ai/langsmith-python/issues/71)) ([be8a4db](https://github.com/langchain-ai/langsmith-python/commit/be8a4dbd51dab7866d9d7791ae31e8f4d51af400))

## [0.14.11](https://github.com/langchain-ai/langsmith-python/compare/v0.14.10...v0.14.11) (2026-10-16)


### Chores

* drop the release-as pin now that 0.14.10 is out ([#68](https://github.com/langchain-ai/langsmith-python/issues/68)) ([1b41cc8](https://github.com/langchain-ai/langsmith-python/commit/1b41cc8fae1b23bc16f50cd0355dc53092803580))

## [0.14.10](https://github.com/langchain-ai/langsmith-python/compare/v0.14.9-rc.1...v0.14.10) (2026-10-15)


### Chores

* switch release-please to the stable channel, release 0.14.10 ([#52](https://github.com/langchain-ai/langsmith-python/issues/52)) ([9cbdb21](https://github.com/langchain-ai/langsmith-python/commit/9cbdb21b14c666279ae1465fe75b01cb5871a83b))

## [0.14.9-rc.1](https://github.com/langchain-ai/langsmith-python/compare/v0.12.6...v0.14.9-rc.1) (2026-10-15)


### ⚠ BREAKING CHANGES

* **sandboxes:** split ProxyGCPConfig into workload-identity and service-account variants

### Features

* add can_use_teams field to instance info response ([8fa142a](https://github.com/langchain-ai/langsmith-python/commit/8fa142a4050eb4e441f0a8a163f34ec32d593a83))
* **configs:** add deletion/enforcement fields and include_all_configs ([6fe595f](https://github.com/langchain-ai/langsmith-python/commit/6fe595f1807f2c6aeca75035221a0cb26b230a8a))
* ensure that address does not need to be revived, rely on typeddict ([#64](https://github.com/langchain-ai/langsmith-python/issues/64)) ([cd6a3b8](https://github.com/langchain-ai/langsmith-python/commit/cd6a3b8356fbfb451f4debcdc847669bf0ad2709))
* **evaluators:** add code_evaluator_input to code evaluator schemas ([cc4b6dd](https://github.com/langchain-ai/langsmith-python/commit/cc4b6dd6fad0747d2fb22fb1263ac70d4c40cad5))
* **feedback:** add feedback_config_id field and expose id on feedback config ([1b06c46](https://github.com/langchain-ai/langsmith-python/commit/1b06c463d1366645e941d2be47d0e07bf5b69407))
* **runs:** add ai_search field and SSE streaming to query endpoints ([468261e](https://github.com/langchain-ai/langsmith-python/commit/468261e7c706a30b42a148678ea626c1be10467a))
* **runs:** add min/max feedback_modified_at filter fields ([9744532](https://github.com/langchain-ai/langsmith-python/commit/9744532f6abf27893af308a35143920d5eda2259))
* **runs:** add prompt and completion cost detail metric fields ([b57c3ca](https://github.com/langchain-ai/langsmith-python/commit/b57c3caa785be888a7e543b1e1119b533b65def7))
* **runs:** add prompt and completion token detail metric fields ([86c0485](https://github.com/langchain-ai/langsmith-python/commit/86c04855d39c66b23bfa6af2ca6c9e9ae7dfdfef))
* **sandboxes:** add Azure Blob mount and Azure proxy auth config support ([6b4f573](https://github.com/langchain-ai/langsmith-python/commit/6b4f57382bde3f0ca93ffc2919f25795e463d1e4))
* **sandboxes:** add encryption spec and cache/encryption mount variants ([f8b84c7](https://github.com/langchain-ai/langsmith-python/commit/f8b84c7d27be90b55cacf50d69e212ad2823134c))
* **sandboxes:** add subject_scope and workload identity fields to AWS and GCP configs ([90d553c](https://github.com/langchain-ai/langsmith-python/commit/90d553c46e336b53eea2550b7eca9a0cfa136249))
* **sandboxes:** split ProxyGCPConfig into workload-identity and service-account variants ([e3fdc2c](https://github.com/langchain-ai/langsmith-python/commit/e3fdc2c1fb83359ff5ab399b8780fff674e04aa2))
* **sessions:** add resolve endpoint to look up a tracing project by address ([9fc8ab4](https://github.com/langchain-ai/langsmith-python/commit/9fc8ab484263d769c21b154dec3837ed119f6ff2))
* **webhooks:** add test_webhook_destination endpoint ([dd20d24](https://github.com/langchain-ai/langsmith-python/commit/dd20d2444f7277d292d5f2463b2da46705cb1f4f))


### Bug Fixes

* build, lint, and test failures (feat: add upsert and delete Slack app configuration permission scopes) ([ec9d4f0](https://github.com/langchain-ai/langsmith-python/commit/ec9d4f0b4d88def5cdf9cdbcd256c9444a877aae))
* **ci:** let pyperf workers import the bench package ([#60](https://github.com/langchain-ai/langsmith-python/issues/60)) ([8164635](https://github.com/langchain-ai/langsmith-python/commit/81646354e09b36c9c6059f6515613e3b1c235da0))
* prepare Python publishing and repair production sync ([5a1d9c1](https://github.com/langchain-ai/langsmith-python/commit/5a1d9c14c13179168c99c022be8aa8839cbabf50))


### Chores

* cut the python release candidate as 0.14.6-rc.1 ([#62](https://github.com/langchain-ai/langsmith-python/issues/62)) ([2565869](https://github.com/langchain-ai/langsmith-python/commit/2565869bc3cd4e522c9664f514ee4aab2de36f14))
* cut the python release candidate as 0.14.9-rc.1 ([#65](https://github.com/langchain-ai/langsmith-python/issues/65)) ([d4b14c4](https://github.com/langchain-ai/langsmith-python/commit/d4b14c4bde85a7c372ba6eed889c9cbe674fe3ee))


### Documentation

* **py:** document Python staging contributions ([f7e6ea5](https://github.com/langchain-ai/langsmith-python/commit/f7e6ea550bc38759aeda4874d387d7518f223ca9))
