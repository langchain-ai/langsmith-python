# ProductFeedback

Types:

```python
from langsmith.types import ProductFeedbackCreateResponse, ProductFeedbackRetrieveResponse
```

Methods:

- <code title="post /api/v1/platform/product-feedbacks">client.product_feedback.<a href="./src/langsmith/resources/product_feedback.py">create</a>(\*\*<a href="src/langsmith/types/product_feedback_create_params.py">params</a>) -> <a href="./src/langsmith/types/product_feedback_create_response.py">ProductFeedbackCreateResponse</a></code>
- <code title="get /api/v1/platform/product-feedbacks/{id}">client.product_feedback.<a href="./src/langsmith/resources/product_feedback.py">retrieve</a>(id) -> <a href="./src/langsmith/types/product_feedback_retrieve_response.py">ProductFeedbackRetrieveResponse</a></code>

# Agents

Types:

```python
from langsmith.types import Agent
```

Methods:

- <code title="post /api/v1/agents">client.agents.<a href="./src/langsmith/resources/agents.py">create</a>(\*\*<a href="src/langsmith/types/agent_create_params.py">params</a>) -> <a href="./src/langsmith/types/agent.py">Agent</a></code>
- <code title="get /api/v1/agents/{agent_id}">client.agents.<a href="./src/langsmith/resources/agents.py">retrieve</a>(agent_id, \*\*<a href="src/langsmith/types/agent_retrieve_params.py">params</a>) -> <a href="./src/langsmith/types/agent.py">Agent</a></code>
- <code title="patch /api/v1/agents/{agent_id}">client.agents.<a href="./src/langsmith/resources/agents.py">update</a>(agent_id, \*\*<a href="src/langsmith/types/agent_update_params.py">params</a>) -> <a href="./src/langsmith/types/agent.py">Agent</a></code>
- <code title="get /api/v1/agents">client.agents.<a href="./src/langsmith/resources/agents.py">list</a>(\*\*<a href="src/langsmith/types/agent_list_params.py">params</a>) -> <a href="./src/langsmith/types/agent.py">SyncItemsCursorGetPagination[Agent]</a></code>
- <code title="delete /api/v1/agents/{agent_id}">client.agents.<a href="./src/langsmith/resources/agents.py">delete</a>(agent_id) -> None</code>

# Fleet

## Threads

Types:

```python
from langsmith.types.fleet import ThreadActivateSandboxResponse
```

Methods:

- <code title="post /v1/fleet/threads/{thread_id}/sandbox-activation">client.fleet.threads.<a href="./src/langsmith/resources/fleet/threads.py">activate_sandbox</a>(thread_id) -> <a href="./src/langsmith/types/fleet/thread_activate_sandbox_response.py">ThreadActivateSandboxResponse</a></code>

# Sessions

Types:

```python
from langsmith.types import (
    CustomChartsSection,
    CustomChartsSectionRequest,
    RunStatsGroupBy,
    SessionSortableColumns,
    TimedeltaInput,
    TracerSession,
    TracerSessionWithoutVirtualFields,
    SessionResolveResponse,
)
```

Methods:

- <code title="get /api/v1/sessions/resolutions">client.sessions.<a href="./src/langsmith/resources/sessions.py">resolve</a>(\*\*<a href="src/langsmith/types/session_resolve_params.py">params</a>) -> <a href="./src/langsmith/types/session_resolve_response.py">SessionResolveResponse</a></code>

# Datasets

Types:

```python
from langsmith.types import (
    DataType,
    Dataset,
    DatasetTransformation,
    DatasetVersion,
    FeedbackCreateCoreSchema,
    Missing,
    SortByDatasetColumn,
)
```

## Examples

Methods:

- <code title="delete /api/v1/platform/datasets/{dataset_id}/examples/{example_id}">client.datasets.examples.<a href="./src/langsmith/resources/datasets/examples.py">delete</a>(example_id, \*, dataset_id) -> None</code>

## ExperimentRuns

Types:

```python
from langsmith.types.datasets import ExperimentRunQueryResponse
```

Methods:

- <code title="post /api/v2/datasets/{dataset_id}/experiment-runs">client.datasets.experiment_runs.<a href="./src/langsmith/resources/datasets/experiment_runs.py">query</a>(dataset_id, \*\*<a href="src/langsmith/types/datasets/experiment_run_query_params.py">params</a>) -> <a href="./src/langsmith/types/datasets/experiment_run_query_response.py">SyncItemsCursorPostPagination[ExperimentRunQueryResponse]</a></code>

# Runs

Types:

```python
from langsmith.types import (
    ResponseBodyForRunsGenerateQuery,
    Run,
    RunIngest,
    RunSchema,
    RunSelectField,
    RunStatsQueryParams,
    RunType,
    RunTypeEnum,
    RunsFilterDataSourceTypeEnum,
    RunGetURLResponse,
)
```

Methods:

- <code title="get /api/v2/runs/{run_id}/url">client.runs.<a href="./src/langsmith/resources/runs/runs.py">get_url</a>(run_id, \*\*<a href="src/langsmith/types/run_get_url_params.py">params</a>) -> <a href="./src/langsmith/types/run_get_url_response.py">RunGetURLResponse</a></code>
- <code title="post /api/v2/runs/query">client.runs.<a href="./src/langsmith/resources/runs/runs.py">query_v2</a>(\*\*<a href="src/langsmith/types/run_query_v2_params.py">params</a>) -> <a href="./src/langsmith/types/run.py">SyncItemsCursorPostPagination[Run]</a></code>
- <code title="get /api/v2/runs/{run_id}">client.runs.<a href="./src/langsmith/resources/runs/runs.py">retrieve_v2</a>(run_id, \*\*<a href="src/langsmith/types/run_retrieve_v2_params.py">params</a>) -> <a href="./src/langsmith/types/run.py">Run</a></code>

## Share

Types:

```python
from langsmith.types.runs import ShareCreateResponse
```

Methods:

- <code title="post /api/v2/runs/{run_id}/share">client.runs.share.<a href="./src/langsmith/resources/runs/share.py">create</a>(run_id, \*\*<a href="src/langsmith/types/runs/share_create_params.py">params</a>) -> <a href="./src/langsmith/types/runs/share_create_response.py">ShareCreateResponse</a></code>
- <code title="delete /api/v2/runs/{trace_id}/share">client.runs.share.<a href="./src/langsmith/resources/runs/share.py">delete</a>(trace_id, \*\*<a href="src/langsmith/types/runs/share_delete_params.py">params</a>) -> None</code>

# Threads

Types:

```python
from langsmith.types import Thread, ThreadStats, ThreadTrace, ThreadAggregateStatsResponse
```

Methods:

- <code title="post /api/v2/threads/stats">client.threads.<a href="./src/langsmith/resources/threads/threads.py">aggregate_stats</a>(\*\*<a href="src/langsmith/types/thread_aggregate_stats_params.py">params</a>) -> <a href="./src/langsmith/types/thread_aggregate_stats_response.py">ThreadAggregateStatsResponse</a></code>
- <code title="get /api/v2/threads/{thread_id}/traces">client.threads.<a href="./src/langsmith/resources/threads/threads.py">list_traces</a>(thread_id, \*\*<a href="src/langsmith/types/thread_list_traces_params.py">params</a>) -> <a href="./src/langsmith/types/thread_trace.py">SyncItemsCursorGetPagination[ThreadTrace]</a></code>
- <code title="post /api/v2/threads/query">client.threads.<a href="./src/langsmith/resources/threads/threads.py">query</a>(\*\*<a href="src/langsmith/types/thread_query_params.py">params</a>) -> <a href="./src/langsmith/types/thread.py">SyncItemsCursorPostPagination[Thread]</a></code>
- <code title="get /api/v2/threads/{thread_id}/stats">client.threads.<a href="./src/langsmith/resources/threads/threads.py">stats</a>(thread_id, \*\*<a href="src/langsmith/types/thread_stats_params.py">params</a>) -> <a href="./src/langsmith/types/thread_stats.py">ThreadStats</a></code>

## Share

Types:

```python
from langsmith.types.threads import ShareCreateResponse, ShareRetrieveResponse
```

Methods:

- <code title="post /api/v2/threads/{thread_id}/share">client.threads.share.<a href="./src/langsmith/resources/threads/share.py">create</a>(thread_id, \*\*<a href="src/langsmith/types/threads/share_create_params.py">params</a>) -> <a href="./src/langsmith/types/threads/share_create_response.py">ShareCreateResponse</a></code>
- <code title="get /api/v2/threads/{thread_id}/share">client.threads.share.<a href="./src/langsmith/resources/threads/share.py">retrieve</a>(thread_id, \*\*<a href="src/langsmith/types/threads/share_retrieve_params.py">params</a>) -> <a href="./src/langsmith/types/threads/share_retrieve_response.py">ShareRetrieveResponse</a></code>
- <code title="delete /api/v2/threads/{thread_id}/share">client.threads.share.<a href="./src/langsmith/resources/threads/share.py">delete</a>(thread_id, \*\*<a href="src/langsmith/types/threads/share_delete_params.py">params</a>) -> None</code>

# Traces

Types:

```python
from langsmith.types import Trace, TraceAggregates, TraceListRunsResponse
```

Methods:

- <code title="get /api/v2/traces/{trace_id}/runs">client.traces.<a href="./src/langsmith/resources/traces.py">list_runs</a>(trace_id, \*\*<a href="src/langsmith/types/trace_list_runs_params.py">params</a>) -> <a href="./src/langsmith/types/trace_list_runs_response.py">TraceListRunsResponse</a></code>
- <code title="post /api/v2/traces/query">client.traces.<a href="./src/langsmith/resources/traces.py">query</a>(\*\*<a href="src/langsmith/types/trace_query_params.py">params</a>) -> <a href="./src/langsmith/types/trace.py">SyncItemsCursorPostPagination[Trace]</a></code>

# OnlineEvaluators

Types:

```python
from langsmith.types import (
    BulkDeleteEvaluatorFailedItem,
    BulkDeleteEvaluatorsResponse,
    CreateOnlineCodeEvaluatorRequest,
    CreateOnlineEvaluatorRequest,
    CreateOnlineEvaluatorResponse,
    CreateOnlineLlmEvaluatorRequest,
    GetOnlineEvaluatorSpendResponse,
    OnlineCodeEvaluator,
    OnlineEvaluator,
    OnlineEvaluatorRunRule,
    OnlineEvaluatorSpendDay,
    OnlineEvaluatorSpendGroup,
    OnlineEvaluatorType,
    OnlineLlmEvaluator,
    OnlineSpendLimit,
    UpdateOnlineCodeEvaluatorRequest,
    UpdateOnlineEvaluatorRequest,
    UpdateOnlineEvaluatorResponse,
    UpdateOnlineLlmEvaluatorRequest,
)
```

Methods:

- <code title="post /api/v1/platform/evaluators">client.online_evaluators.<a href="./src/langsmith/resources/online_evaluators.py">create</a>(\*\*<a href="src/langsmith/types/online_evaluator_create_params.py">params</a>) -> <a href="./src/langsmith/types/create_online_evaluator_response.py">CreateOnlineEvaluatorResponse</a></code>
- <code title="get /api/v1/platform/evaluators/{evaluator_id}">client.online_evaluators.<a href="./src/langsmith/resources/online_evaluators.py">retrieve</a>(evaluator_id) -> <a href="./src/langsmith/types/online_evaluator.py">OnlineEvaluator</a></code>
- <code title="patch /api/v1/platform/evaluators/{evaluator_id}">client.online_evaluators.<a href="./src/langsmith/resources/online_evaluators.py">update</a>(evaluator_id, \*\*<a href="src/langsmith/types/online_evaluator_update_params.py">params</a>) -> <a href="./src/langsmith/types/update_online_evaluator_response.py">UpdateOnlineEvaluatorResponse</a></code>
- <code title="get /api/v1/platform/evaluators">client.online_evaluators.<a href="./src/langsmith/resources/online_evaluators.py">list</a>(\*\*<a href="src/langsmith/types/online_evaluator_list_params.py">params</a>) -> <a href="./src/langsmith/types/online_evaluator.py">SyncOffsetPaginationOnlineEvaluators[OnlineEvaluator]</a></code>
- <code title="delete /api/v1/platform/evaluators/{evaluator_id}">client.online_evaluators.<a href="./src/langsmith/resources/online_evaluators.py">delete</a>(evaluator_id, \*\*<a href="src/langsmith/types/online_evaluator_delete_params.py">params</a>) -> None</code>
- <code title="delete /api/v1/platform/evaluators">client.online_evaluators.<a href="./src/langsmith/resources/online_evaluators.py">bulk_delete</a>(\*\*<a href="src/langsmith/types/online_evaluator_bulk_delete_params.py">params</a>) -> <a href="./src/langsmith/types/bulk_delete_evaluators_response.py">BulkDeleteEvaluatorsResponse</a></code>
- <code title="get /api/v1/platform/evaluators/spend">client.online_evaluators.<a href="./src/langsmith/resources/online_evaluators.py">spend</a>(\*\*<a href="src/langsmith/types/online_evaluator_spend_params.py">params</a>) -> <a href="./src/langsmith/types/get_online_evaluator_spend_response.py">GetOnlineEvaluatorSpendResponse</a></code>

# Public

## Runs

Types:

```python
from langsmith.types.public import RunQueryResponse
```

Methods:

- <code title="get /api/v2/public/{share_token}/run/{run_id}">client.public.runs.<a href="./src/langsmith/resources/public/runs.py">retrieve</a>(run_id, \*, share_token, \*\*<a href="src/langsmith/types/public/run_retrieve_params.py">params</a>) -> <a href="./src/langsmith/types/run.py">Run</a></code>
- <code title="post /api/v2/public/{share_token}/runs/query">client.public.runs.<a href="./src/langsmith/resources/public/runs.py">query</a>(share_token, \*\*<a href="src/langsmith/types/public/run_query_params.py">params</a>) -> <a href="./src/langsmith/types/public/run_query_response.py">RunQueryResponse</a></code>

# AnnotationQueues

Types:

```python
from langsmith.types import (
    AnnotationQueueRubricItemSchema,
    AnnotationQueueSchema,
    AnnotationQueueSizeSchema,
    RunSchemaWithAnnotationQueueInfo,
    AnnotationQueueRetrieveResponse,
    AnnotationQueueRetrieveAnnotationQueuesResponse,
    AnnotationQueueRetrieveQueuesResponse,
)
```

Methods:

- <code title="get /api/v1/annotation-queues/{queue_id}">client.annotation_queues.<a href="./src/langsmith/resources/annotation_queues/annotation_queues.py">retrieve</a>(queue_id) -> <a href="./src/langsmith/types/annotation_queue_retrieve_response.py">AnnotationQueueRetrieveResponse</a></code>
- <code title="patch /api/v1/annotation-queues/{queue_id}">client.annotation_queues.<a href="./src/langsmith/resources/annotation_queues/annotation_queues.py">update</a>(queue_id, \*\*<a href="src/langsmith/types/annotation_queue_update_params.py">params</a>) -> object</code>
- <code title="delete /api/v1/annotation-queues/{queue_id}">client.annotation_queues.<a href="./src/langsmith/resources/annotation_queues/annotation_queues.py">delete</a>(queue_id) -> object</code>
- <code title="post /api/v1/annotation-queues">client.annotation_queues.<a href="./src/langsmith/resources/annotation_queues/annotation_queues.py">annotation_queues</a>(\*\*<a href="src/langsmith/types/annotation_queue_annotation_queues_params.py">params</a>) -> <a href="./src/langsmith/types/annotation_queue_schema.py">AnnotationQueueSchema</a></code>
- <code title="post /api/v1/annotation-queues/status/{annotation_queue_run_id}">client.annotation_queues.<a href="./src/langsmith/resources/annotation_queues/annotation_queues.py">create_run_status</a>(annotation_queue_run_id, \*\*<a href="src/langsmith/types/annotation_queue_create_run_status_params.py">params</a>) -> object</code>
- <code title="post /api/v1/annotation-queues/{queue_id}/export">client.annotation_queues.<a href="./src/langsmith/resources/annotation_queues/annotation_queues.py">export</a>(queue_id, \*\*<a href="src/langsmith/types/annotation_queue_export_params.py">params</a>) -> object</code>
- <code title="post /api/v1/annotation-queues/populate">client.annotation_queues.<a href="./src/langsmith/resources/annotation_queues/annotation_queues.py">populate</a>(\*\*<a href="src/langsmith/types/annotation_queue_populate_params.py">params</a>) -> object</code>
- <code title="get /api/v1/annotation-queues">client.annotation_queues.<a href="./src/langsmith/resources/annotation_queues/annotation_queues.py">retrieve_annotation_queues</a>(\*\*<a href="src/langsmith/types/annotation_queue_retrieve_annotation_queues_params.py">params</a>) -> <a href="./src/langsmith/types/annotation_queue_retrieve_annotation_queues_response.py">SyncOffsetPaginationTopLevelArray[AnnotationQueueRetrieveAnnotationQueuesResponse]</a></code>
- <code title="get /api/v1/annotation-queues/{run_id}/queues">client.annotation_queues.<a href="./src/langsmith/resources/annotation_queues/annotation_queues.py">retrieve_queues</a>(run_id) -> <a href="./src/langsmith/types/annotation_queue_retrieve_queues_response.py">AnnotationQueueRetrieveQueuesResponse</a></code>
- <code title="get /api/v1/annotation-queues/{queue_id}/run/{index}">client.annotation_queues.<a href="./src/langsmith/resources/annotation_queues/annotation_queues.py">retrieve_run</a>(index, \*, queue_id, \*\*<a href="src/langsmith/types/annotation_queue_retrieve_run_params.py">params</a>) -> <a href="./src/langsmith/types/run_schema_with_annotation_queue_info.py">RunSchemaWithAnnotationQueueInfo</a></code>
- <code title="get /api/v1/annotation-queues/{queue_id}/size">client.annotation_queues.<a href="./src/langsmith/resources/annotation_queues/annotation_queues.py">retrieve_size</a>(queue_id, \*\*<a href="src/langsmith/types/annotation_queue_retrieve_size_params.py">params</a>) -> <a href="./src/langsmith/types/annotation_queue_size_schema.py">AnnotationQueueSizeSchema</a></code>
- <code title="get /api/v1/annotation-queues/{queue_id}/total_archived">client.annotation_queues.<a href="./src/langsmith/resources/annotation_queues/annotation_queues.py">retrieve_total_archived</a>(queue_id, \*\*<a href="src/langsmith/types/annotation_queue_retrieve_total_archived_params.py">params</a>) -> <a href="./src/langsmith/types/annotation_queue_size_schema.py">AnnotationQueueSizeSchema</a></code>
- <code title="get /api/v1/annotation-queues/{queue_id}/total_size">client.annotation_queues.<a href="./src/langsmith/resources/annotation_queues/annotation_queues.py">retrieve_total_size</a>(queue_id) -> <a href="./src/langsmith/types/annotation_queue_size_schema.py">AnnotationQueueSizeSchema</a></code>

## Runs

Types:

```python
from langsmith.types.annotation_queues import (
    RunCreateResponse,
    RunListResponse,
    RunCreateByKeyResponse,
)
```

Methods:

- <code title="post /api/v1/annotation-queues/{queue_id}/runs">client.annotation_queues.runs.<a href="./src/langsmith/resources/annotation_queues/runs.py">create</a>(queue_id, \*\*<a href="src/langsmith/types/annotation_queues/run_create_params.py">params</a>) -> <a href="./src/langsmith/types/annotation_queues/run_create_response.py">RunCreateResponse</a></code>
- <code title="patch /api/v1/annotation-queues/{queue_id}/runs/{queue_run_id}">client.annotation_queues.runs.<a href="./src/langsmith/resources/annotation_queues/runs.py">update</a>(queue_run_id, \*, queue_id, \*\*<a href="src/langsmith/types/annotation_queues/run_update_params.py">params</a>) -> object</code>
- <code title="get /api/v1/annotation-queues/{queue_id}/runs">client.annotation_queues.runs.<a href="./src/langsmith/resources/annotation_queues/runs.py">list</a>(queue_id, \*\*<a href="src/langsmith/types/annotation_queues/run_list_params.py">params</a>) -> <a href="./src/langsmith/types/annotation_queues/run_list_response.py">RunListResponse</a></code>
- <code title="post /api/v1/annotation-queues/{queue_id}/runs/by-key">client.annotation_queues.runs.<a href="./src/langsmith/resources/annotation_queues/runs.py">create_by_key</a>(queue_id, \*\*<a href="src/langsmith/types/annotation_queues/run_create_by_key_params.py">params</a>) -> <a href="./src/langsmith/types/annotation_queues/run_create_by_key_response.py">RunCreateByKeyResponse</a></code>
- <code title="post /api/v1/annotation-queues/{queue_id}/runs/delete">client.annotation_queues.runs.<a href="./src/langsmith/resources/annotation_queues/runs.py">delete_all</a>(queue_id, \*\*<a href="src/langsmith/types/annotation_queues/run_delete_all_params.py">params</a>) -> object</code>
- <code title="delete /api/v1/annotation-queues/{queue_id}/runs/{queue_run_id}">client.annotation_queues.runs.<a href="./src/langsmith/resources/annotation_queues/runs.py">delete_queue</a>(queue_run_id, \*, queue_id) -> object</code>

## Items

Types:

```python
from langsmith.types.annotation_queues import (
    ItemCreateResponse,
    ItemUpdateResponse,
    ItemListResponse,
    ItemCreateStatusResponse,
    ItemDeleteAllResponse,
    ItemRetrieveCountResponse,
    ItemRetrievePlacementResponse,
)
```

Methods:

- <code title="post /api/v1/platform/annotation-queues/{queue_id}/items">client.annotation_queues.items.<a href="./src/langsmith/resources/annotation_queues/items.py">create</a>(queue_id, \*\*<a href="src/langsmith/types/annotation_queues/item_create_params.py">params</a>) -> <a href="./src/langsmith/types/annotation_queues/item_create_response.py">ItemCreateResponse</a></code>
- <code title="patch /api/v1/platform/annotation-queues/{queue_id}/items/{item_id}">client.annotation_queues.items.<a href="./src/langsmith/resources/annotation_queues/items.py">update</a>(item_id, \*, queue_id, \*\*<a href="src/langsmith/types/annotation_queues/item_update_params.py">params</a>) -> <a href="./src/langsmith/types/annotation_queues/item_update_response.py">ItemUpdateResponse</a></code>
- <code title="get /api/v1/platform/annotation-queues/{queue_id}/items">client.annotation_queues.items.<a href="./src/langsmith/resources/annotation_queues/items.py">list</a>(queue_id, \*\*<a href="src/langsmith/types/annotation_queues/item_list_params.py">params</a>) -> <a href="./src/langsmith/types/annotation_queues/item_list_response.py">SyncItemsCursorGetPagination[ItemListResponse]</a></code>
- <code title="post /api/v1/platform/annotation-queues/items/{queue_item_id}/status">client.annotation_queues.items.<a href="./src/langsmith/resources/annotation_queues/items.py">create_status</a>(queue_item_id, \*\*<a href="src/langsmith/types/annotation_queues/item_create_status_params.py">params</a>) -> <a href="./src/langsmith/types/annotation_queues/item_create_status_response.py">ItemCreateStatusResponse</a></code>
- <code title="post /api/v1/platform/annotation-queues/{queue_id}/items/delete">client.annotation_queues.items.<a href="./src/langsmith/resources/annotation_queues/items.py">delete_all</a>(queue_id, \*\*<a href="src/langsmith/types/annotation_queues/item_delete_all_params.py">params</a>) -> <a href="./src/langsmith/types/annotation_queues/item_delete_all_response.py">ItemDeleteAllResponse</a></code>
- <code title="get /api/v1/platform/annotation-queues/{queue_id}/items/count">client.annotation_queues.items.<a href="./src/langsmith/resources/annotation_queues/items.py">retrieve_count</a>(queue_id, \*\*<a href="src/langsmith/types/annotation_queues/item_retrieve_count_params.py">params</a>) -> <a href="./src/langsmith/types/annotation_queues/item_retrieve_count_response.py">ItemRetrieveCountResponse</a></code>
- <code title="get /api/v1/platform/annotation-queues/{queue_id}/items/{item_id}/placement">client.annotation_queues.items.<a href="./src/langsmith/resources/annotation_queues/items.py">retrieve_placement</a>(item_id, \*, queue_id) -> <a href="./src/langsmith/types/annotation_queues/item_retrieve_placement_response.py">ItemRetrievePlacementResponse</a></code>

# PromptWebhooks

Types:

```python
from langsmith.types import PromptWebhook, PromptWebhookListResponse, PromptWebhookTestResponse
```

Methods:

- <code title="post /api/v1/prompt-webhooks">client.prompt_webhooks.<a href="./src/langsmith/resources/prompt_webhooks.py">create</a>(\*\*<a href="src/langsmith/types/prompt_webhook_create_params.py">params</a>) -> <a href="./src/langsmith/types/prompt_webhook.py">PromptWebhook</a></code>
- <code title="get /api/v1/prompt-webhooks/{webhook_id}">client.prompt_webhooks.<a href="./src/langsmith/resources/prompt_webhooks.py">retrieve</a>(webhook_id) -> <a href="./src/langsmith/types/prompt_webhook.py">PromptWebhook</a></code>
- <code title="patch /api/v1/prompt-webhooks/{webhook_id}">client.prompt_webhooks.<a href="./src/langsmith/resources/prompt_webhooks.py">update</a>(webhook_id, \*\*<a href="src/langsmith/types/prompt_webhook_update_params.py">params</a>) -> <a href="./src/langsmith/types/prompt_webhook.py">PromptWebhook</a></code>
- <code title="get /api/v1/prompt-webhooks">client.prompt_webhooks.<a href="./src/langsmith/resources/prompt_webhooks.py">list</a>() -> <a href="./src/langsmith/types/prompt_webhook_list_response.py">PromptWebhookListResponse</a></code>
- <code title="delete /api/v1/prompt-webhooks/{webhook_id}">client.prompt_webhooks.<a href="./src/langsmith/resources/prompt_webhooks.py">delete</a>(webhook_id) -> None</code>
- <code title="post /api/v1/prompt-webhooks/test">client.prompt_webhooks.<a href="./src/langsmith/resources/prompt_webhooks.py">test</a>(\*\*<a href="src/langsmith/types/prompt_webhook_test_params.py">params</a>) -> <a href="./src/langsmith/types/prompt_webhook_test_response.py">PromptWebhookTestResponse</a></code>

# Info

Types:

```python
from langsmith.types import InfoListResponse
```

Methods:

- <code title="get /api/v1/info">client.info.<a href="./src/langsmith/resources/info.py">list</a>() -> <a href="./src/langsmith/types/info_list_response.py">InfoListResponse</a></code>

# Issues

Types:

```python
from langsmith.types import Issue
```

Methods:

- <code title="get /api/v1/platform/issues/{id}">client.issues.<a href="./src/langsmith/resources/issues.py">retrieve</a>(id, \*\*<a href="src/langsmith/types/issue_retrieve_params.py">params</a>) -> <a href="./src/langsmith/types/issue.py">Issue</a></code>
- <code title="get /api/v1/platform/issues">client.issues.<a href="./src/langsmith/resources/issues.py">list</a>(\*\*<a href="src/langsmith/types/issue_list_params.py">params</a>) -> <a href="./src/langsmith/types/issue.py">SyncOffsetPaginationIssues[Issue]</a></code>

# Sandboxes

Types:

```python
from langsmith.types import (
    DownloadURLResponse,
    ProxyConfig,
    SandboxListResponse,
    SandboxMountConfig,
    SandboxResponse,
    SandboxStatusResponse,
    ServiceURLResponse,
    SnapshotListResponse,
    SnapshotResponse,
    SandboxListUsageCostsResponse,
)
```

Methods:

- <code title="get /api/v2/sandboxes/usage/costs">client.sandboxes.<a href="./src/langsmith/resources/sandboxes/sandboxes.py">list_usage_costs</a>(\*\*<a href="src/langsmith/types/sandbox_list_usage_costs_params.py">params</a>) -> <a href="./src/langsmith/types/sandbox_list_usage_costs_response.py">SyncItemsCursorGetPagination[SandboxListUsageCostsResponse]</a></code>

## Boxes

Types:

```python
from langsmith.types.sandboxes import BoxListServiceURLsResponse
```

Methods:

- <code title="post /api/v2/sandboxes/boxes">client.sandboxes.boxes.<a href="./src/langsmith/resources/sandboxes/boxes.py">create</a>(\*\*<a href="src/langsmith/types/sandboxes/box_create_params.py">params</a>) -> <a href="./src/langsmith/types/sandbox_response.py">SandboxResponse</a></code>
- <code title="get /api/v2/sandboxes/boxes/{name}">client.sandboxes.boxes.<a href="./src/langsmith/resources/sandboxes/boxes.py">retrieve</a>(name) -> <a href="./src/langsmith/types/sandbox_response.py">SandboxResponse</a></code>
- <code title="patch /api/v2/sandboxes/boxes/{name}">client.sandboxes.boxes.<a href="./src/langsmith/resources/sandboxes/boxes.py">update</a>(path_name, \*\*<a href="src/langsmith/types/sandboxes/box_update_params.py">params</a>) -> <a href="./src/langsmith/types/sandbox_response.py">SandboxResponse</a></code>
- <code title="get /api/v2/sandboxes/boxes">client.sandboxes.boxes.<a href="./src/langsmith/resources/sandboxes/boxes.py">list</a>(\*\*<a href="src/langsmith/types/sandboxes/box_list_params.py">params</a>) -> <a href="./src/langsmith/types/sandbox_response.py">SyncItemsCursorGetPagination[SandboxResponse]</a></code>
- <code title="delete /api/v2/sandboxes/boxes/{name}">client.sandboxes.boxes.<a href="./src/langsmith/resources/sandboxes/boxes.py">delete</a>(name) -> None</code>
- <code title="post /api/v2/sandboxes/boxes/{name}/snapshot">client.sandboxes.boxes.<a href="./src/langsmith/resources/sandboxes/boxes.py">create_snapshot</a>(path_name, \*\*<a href="src/langsmith/types/sandboxes/box_create_snapshot_params.py">params</a>) -> <a href="./src/langsmith/types/snapshot_response.py">SnapshotResponse</a></code>
- <code title="delete /api/v2/sandboxes/boxes/{name}/service-urls">client.sandboxes.boxes.<a href="./src/langsmith/resources/sandboxes/boxes.py">delete_service_url</a>(name, \*\*<a href="src/langsmith/types/sandboxes/box_delete_service_url_params.py">params</a>) -> None</code>
- <code title="post /api/v2/sandboxes/boxes/{name}/download-url">client.sandboxes.boxes.<a href="./src/langsmith/resources/sandboxes/boxes.py">generate_download_url</a>(name, \*\*<a href="src/langsmith/types/sandboxes/box_generate_download_url_params.py">params</a>) -> <a href="./src/langsmith/types/download_url_response.py">DownloadURLResponse</a></code>
- <code title="post /api/v2/sandboxes/boxes/{name}/service-url">client.sandboxes.boxes.<a href="./src/langsmith/resources/sandboxes/boxes.py">generate_service_url</a>(name, \*\*<a href="src/langsmith/types/sandboxes/box_generate_service_url_params.py">params</a>) -> <a href="./src/langsmith/types/service_url_response.py">ServiceURLResponse</a></code>
- <code title="get /api/v2/sandboxes/boxes/{name}/status">client.sandboxes.boxes.<a href="./src/langsmith/resources/sandboxes/boxes.py">get_status</a>(name) -> <a href="./src/langsmith/types/sandbox_status_response.py">SandboxStatusResponse</a></code>
- <code title="get /api/v2/sandboxes/boxes/{name}/service-urls">client.sandboxes.boxes.<a href="./src/langsmith/resources/sandboxes/boxes.py">list_service_urls</a>(name, \*\*<a href="src/langsmith/types/sandboxes/box_list_service_urls_params.py">params</a>) -> <a href="./src/langsmith/types/sandboxes/box_list_service_urls_response.py">SyncItemsCursorGetPagination[BoxListServiceURLsResponse]</a></code>
- <code title="post /api/v2/sandboxes/boxes/{name}/start">client.sandboxes.boxes.<a href="./src/langsmith/resources/sandboxes/boxes.py">start</a>(name) -> <a href="./src/langsmith/types/sandbox_response.py">SandboxResponse</a></code>
- <code title="post /api/v2/sandboxes/boxes/{name}/stop">client.sandboxes.boxes.<a href="./src/langsmith/resources/sandboxes/boxes.py">stop</a>(name) -> None</code>

## Registries

Types:

```python
from langsmith.types.sandboxes import RegistryListResponse, RegistryResponse
```

Methods:

- <code title="post /api/v2/sandboxes/registries">client.sandboxes.registries.<a href="./src/langsmith/resources/sandboxes/registries.py">create</a>(\*\*<a href="src/langsmith/types/sandboxes/registry_create_params.py">params</a>) -> <a href="./src/langsmith/types/sandboxes/registry_response.py">RegistryResponse</a></code>
- <code title="get /api/v2/sandboxes/registries/{name}">client.sandboxes.registries.<a href="./src/langsmith/resources/sandboxes/registries.py">retrieve</a>(name) -> <a href="./src/langsmith/types/sandboxes/registry_response.py">RegistryResponse</a></code>
- <code title="patch /api/v2/sandboxes/registries/{name}">client.sandboxes.registries.<a href="./src/langsmith/resources/sandboxes/registries.py">update</a>(path_name, \*\*<a href="src/langsmith/types/sandboxes/registry_update_params.py">params</a>) -> <a href="./src/langsmith/types/sandboxes/registry_response.py">RegistryResponse</a></code>
- <code title="get /api/v2/sandboxes/registries">client.sandboxes.registries.<a href="./src/langsmith/resources/sandboxes/registries.py">list</a>(\*\*<a href="src/langsmith/types/sandboxes/registry_list_params.py">params</a>) -> <a href="./src/langsmith/types/sandboxes/registry_list_response.py">RegistryListResponse</a></code>
- <code title="delete /api/v2/sandboxes/registries/{name}">client.sandboxes.registries.<a href="./src/langsmith/resources/sandboxes/registries.py">delete</a>(name) -> None</code>

## Snapshots

Types:

```python
from langsmith.types.sandboxes import SnapshotRetrieveByNameResponse
```

Methods:

- <code title="post /api/v2/sandboxes/snapshots">client.sandboxes.snapshots.<a href="./src/langsmith/resources/sandboxes/snapshots.py">create</a>(\*\*<a href="src/langsmith/types/sandboxes/snapshot_create_params.py">params</a>) -> <a href="./src/langsmith/types/snapshot_response.py">SnapshotResponse</a></code>
- <code title="get /api/v2/sandboxes/snapshots/{snapshot_id}">client.sandboxes.snapshots.<a href="./src/langsmith/resources/sandboxes/snapshots.py">retrieve</a>(snapshot_id) -> <a href="./src/langsmith/types/snapshot_response.py">SnapshotResponse</a></code>
- <code title="get /api/v2/sandboxes/snapshots">client.sandboxes.snapshots.<a href="./src/langsmith/resources/sandboxes/snapshots.py">list</a>(\*\*<a href="src/langsmith/types/sandboxes/snapshot_list_params.py">params</a>) -> <a href="./src/langsmith/types/snapshot_response.py">SyncItemsCursorGetPagination[SnapshotResponse]</a></code>
- <code title="delete /api/v2/sandboxes/snapshots/{snapshot_id}">client.sandboxes.snapshots.<a href="./src/langsmith/resources/sandboxes/snapshots.py">delete</a>(snapshot_id) -> None</code>
- <code title="get /api/v2/sandboxes/snapshots-by-name/{name}">client.sandboxes.snapshots.<a href="./src/langsmith/resources/sandboxes/snapshots.py">retrieve_by_name</a>(name) -> <a href="./src/langsmith/types/sandboxes/snapshot_retrieve_by_name_response.py">SnapshotRetrieveByNameResponse</a></code>
