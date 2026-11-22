from dataclasses import dataclass

from opentelemetry.sdk.trace.id_generator import IdGenerator  # type: ignore[import]


@dataclass(frozen=True)
class RunIdGenerator(IdGenerator):
    trace_id: int
    span_id: int

    def generate_trace_id(self) -> int:
        return self.trace_id

    def generate_span_id(self) -> int:
        return self.span_id

    def is_trace_id_random(self) -> bool:
        return False
