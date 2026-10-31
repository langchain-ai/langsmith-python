# Changelog

## [0.14.17](https://github.com/langchain-ai/langsmith-python/compare/v0.14.16...v0.14.17) (2026-10-31)


### Features

* **cli:** add langsmith evaluators create-decision-model ([534a040](https://github.com/langchain-ai/langsmith-python/commit/534a040cfe964f13a6f18a9dd754e93e0661fed8))
* **sandboxes:** AWS session tags on proxy role rules ([bc15831](https://github.com/langchain-ai/langsmith-python/commit/bc15831e6c47ed6bab97b5494973089ed1df39a7))
* **sdk:** read profile api_key_env in Python, JS and Java SDKs ([ce4946f](https://github.com/langchain-ai/langsmith-python/commit/ce4946f1906f5bef55f10526c24acbfbb4e1202d))


### Bug Fixes

* **evaluators:** show the effective spend limit in the evaluator tables ([b00e161](https://github.com/langchain-ai/langsmith-python/commit/b00e1613f5b5bdb02e8dbfcf4705edf0e8eb1389))
* expose v1 session creation and updates in Python and TypeScript SDKs (LSO-4121, LSO-4130) ([de2293b](https://github.com/langchain-ai/langsmith-python/commit/de2293b2f6e33310bf8fd0f27805df97f0c84ea5))
* restore disposable Engine sandboxes with released SDK ([6529456](https://github.com/langchain-ai/langsmith-python/commit/6529456e7a84290024a635bac12f90efbe8833cf))
* **sdks:** unify shared-profile OAuth refresh locking ([d9c5731](https://github.com/langchain-ai/langsmith-python/commit/d9c5731c770651ab20b89e8d8792f02331e6ac81))


### Documentation

* **sandboxes:** document match_paths on proxy rules ([b764565](https://github.com/langchain-ai/langsmith-python/commit/b76456565e21e4e6db018a1bb3880517a2773fbd))


### Build System

* refresh CA bundles for dev ops ([b202202](https://github.com/langchain-ai/langsmith-python/commit/b2022023baf08720440cf594d6bb7bc540d50053))

## [0.14.16](https://github.com/langchain-ai/langsmith-python/compare/v0.14.15...v0.14.16) (2026-10-29)


### Features

* **py:** trace OpenAI Agents API sessions in wrap_openai ([dac7037](https://github.com/langchain-ai/langsmith-python/commit/dac7037c898ee39ea605ca47c8831d2653c06f0b))
* **sdks:** add create_decision_model to the generated SDKs ([61afde1](https://github.com/langchain-ai/langsmith-python/commit/61afde1097584e69578330b97517b836975b942d))


### Bug Fixes

* **sdk:** drop the base workspace for write replicas on another instance ([1a255bb](https://github.com/langchain-ai/langsmith-python/commit/1a255bb0bbae6cbaba0f6e1a39baabc437929b7e))


### Reverts

* provision disposable Engine sandboxes ([d3a4a2c](https://github.com/langchain-ai/langsmith-python/commit/d3a4a2c4ca6413ffaea91e2d27eee5d32b29e49f))

## [0.14.15](https://github.com/langchain-ai/langsmith-python/compare/v0.14.14...v0.14.15) (2026-10-29)


### Features

* add HTTPS destination rewrite rules for sandboxes ([3e27a3a](https://github.com/langchain-ai/langsmith-python/commit/3e27a3a405300aaca73df109c6fe900bb17a094c))
* **annotation-queues:** rubric item required_if and visible_if conditions ([7af99d4](https://github.com/langchain-ai/langsmith-python/commit/7af99d4f24ba8ba1ed4aea5a184b7d77f7499bc2))
* **feedback:** add allows_multiple_categories flag to categorical feedback configs ([ae2d72f](https://github.com/langchain-ai/langsmith-python/commit/ae2d72fb3b965f97c48865ff2400b485ec9abfe4))
* **sandboxes:** allow non-persistent mode for all tenants ([8ff0144](https://github.com/langchain-ai/langsmith-python/commit/8ff01441a9f07e1ced19451c32b47d962ae16336))
* **sandboxes:** show granular usage instead of dollar estimates ([8b48112](https://github.com/langchain-ai/langsmith-python/commit/8b481128795c22581e1d3612251507ab939376d1))
* **sdk-py:** support CLI profile selection and preferred profile auth ([331fec0](https://github.com/langchain-ai/langsmith-python/commit/331fec0ccdbe7326784d053160ff25f920798d10))


### Bug Fixes

* **ci:** keep Co-authored-by trailers in SDK exports ([1702d37](https://github.com/langchain-ai/langsmith-python/commit/1702d37a9ede32578ea24944596afb9eb2284010))
* **sandboxes:** cap non-persistent sandbox disk at 16 GiB per vCPU ([1171a82](https://github.com/langchain-ai/langsmith-python/commit/1171a82cd3a8bd277f8e72d76d538cdd07c9696f))
* **sandboxes:** retain recorded storage across sampling gaps ([9e81d8e](https://github.com/langchain-ai/langsmith-python/commit/9e81d8ee06f628f191b5fdaf153a47aaace122a1))
* **sdk-py:** show SmithDB migration deprecation warnings by default ([acfb537](https://github.com/langchain-ai/langsmith-python/commit/acfb5376dbfc4849576f0659024b2d23a1773f26))


### Performance Improvements

* provision disposable Engine sandboxes ([037ec1d](https://github.com/langchain-ai/langsmith-python/commit/037ec1d1fc44901aa0a13dcb49ed355459da44a1))


### Chores

* **sdks:** regenerate python.patch for tzdata 2026.6 ([d0678b8](https://github.com/langchain-ai/langsmith-python/commit/d0678b8ac40717266a65d225f54902a6d8ecabfd))


### Documentation

* **api:** describe the annotation queue, example and feedback token CLI flags ([b7ab19b](https://github.com/langchain-ai/langsmith-python/commit/b7ab19b9a6dba917df268149ea380bfc17621b71))

## [0.14.14](https://github.com/langchain-ai/langsmith-python/compare/v0.14.13...v0.14.14) (2026-10-27)


### Features

* include subtree usage in frontend runs queries ([5e8d827](https://github.com/langchain-ai/langsmith-python/commit/5e8d827def1ecacd55760d7c36f86752589feb8c))
* **python:** accept address in agent and voice integrations ([6704dd3](https://github.com/langchain-ai/langsmith-python/commit/6704dd3e954195448c3c3f2a809d8cccd0e70648))
* **python:** accept address in wrapper tracing_extra ([cea48fa](https://github.com/langchain-ai/langsmith-python/commit/cea48fa75f34c8229575bfcf5d0d5e82a4222532))
* **sdks:** stream v2 run, trace and thread queries ([b5e557a](https://github.com/langchain-ai/langsmith-python/commit/b5e557a204cff0f68ed32818f9658c00b9d88d24))

## [0.14.13](https://github.com/langchain-ai/langsmith-python/compare/v0.14.12...v0.14.13) (2026-10-27)


### ⚠ BREAKING CHANGES

* **sandboxes:** add sandbox volumes

### Features

* add agent owner API support ([6854d88](https://github.com/langchain-ai/langsmith-python/commit/6854d8813f18143f8f5ec2af758eade440e6b020))
* **backend:** add support for uploading custom avatars for agents ([f06bffc](https://github.com/langchain-ai/langsmith-python/commit/f06bffceb9233646afcbac98d2e76d478c48b304))
* **engine:** scan and fix GitLab projects through a workspace service account ([19f9076](https://github.com/langchain-ai/langsmith-python/commit/19f90767908aec4a9c6ca11d90c01e913e7df153))
* **engine:** scope GitHub fixes to the instance they were opened on ([fc41248](https://github.com/langchain-ai/langsmith-python/commit/fc4124843e7b20a5e12372a92b051552b9e53c4c))
* **js-sdk:** batch createFeedback through the multipart endpoint ([a6569b5](https://github.com/langchain-ai/langsmith-python/commit/a6569b5fbf212fe58b624faf07003d7def5709ab))
* let Engine boards verify without requesting a preview ([f1c915e](https://github.com/langchain-ai/langsmith-python/commit/f1c915e6a7b249951ed8d9e8aaa5e39212643704))
* **sandboxes:** add sandbox volumes ([f4bef1c](https://github.com/langchain-ai/langsmith-python/commit/f4bef1ccbb20849a121e69a13f86913f4e3bc000))
* **sandboxes:** create non-persistent sandboxes with `persistent: false` (private beta), never billed for storage ([4f8def7](https://github.com/langchain-ai/langsmith-python/commit/4f8def7c176c33813aa1d190ccaf95332d165a94))
* **sandboxes:** embed token-mode service URLs and browser windows with the token kept out of server-visible URLs ([d9188df](https://github.com/langchain-ai/langsmith-python/commit/d9188df1a53b5d3924d0589b45730e90a23e9be1))
* **sandboxes:** relay sandbox egress through a customer's network ([9363303](https://github.com/langchain-ai/langsmith-python/commit/9363303d3788f4fa399067ca60c7c65c920db990))
* **sandboxes:** sandbox functions ([89f7345](https://github.com/langchain-ai/langsmith-python/commit/89f73451e4c0de94c78cb5636011ea60d4058354))
* **sdk:** add select and exclude_default_fields to list_examples in the Python SDK ([bbf5b46](https://github.com/langchain-ai/langsmith-python/commit/bbf5b469559fe95c69f6832e82e2d9bc8cf50ac3))
* **sdks:** add resolve_destination to the Python SDK ([012283c](https://github.com/langchain-ai/langsmith-python/commit/012283cdfa9123b8119e84601355a311c4547464))


### Bug Fixes

* **py:** make Client.flush() wait for buffered run ops ([ccfb6b5](https://github.com/langchain-ai/langsmith-python/commit/ccfb6b5c1df5f839df02684dc121ae4f6dfb9155))
* **sdk-python:** stop AsyncExperimentResults iteration from hanging when processing fails ([ba06e4b](https://github.com/langchain-ai/langsmith-python/commit/ba06e4b29fb3f151cf98ed07d3bffca796b51853))
* **sdk:** default Python agent creation to EXTERNAL ([39fb8af](https://github.com/langchain-ai/langsmith-python/commit/39fb8af8a50c07aab13f634e725b8d4de9818fea))
* **security:** update application certifi bundles ([82a5a67](https://github.com/langchain-ai/langsmith-python/commit/82a5a67f274c0900ea50108f0b00fe903373f6f6))


### Chores

* release 0.14.13 ([19c23cf](https://github.com/langchain-ai/langsmith-python/commit/19c23cfd6a5d1a694efec9c77ecc82f4d4845946))


### Documentation

* remove the beta label from agent addressing ([a19186a](https://github.com/langchain-ai/langsmith-python/commit/a19186ab077b77bf70bef020a6c80d6c2694d98c))
* **threads:** bring POST /api/v2/threads/query into API standards compliance ([5fe228c](https://github.com/langchain-ai/langsmith-python/commit/5fe228cff681c82f0a3da4ca54acf84ff44a2406))


### Refactors

* consolidate SDK tooling under sdks ([c2f0ef2](https://github.com/langchain-ai/langsmith-python/commit/c2f0ef2e1f0d6989ed73030864db679f47c5b6fe))


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
