from dataclasses import dataclass, field


@dataclass
class BlockPlan:
    name: str
    volume: int
    zone: str
    objective: str = ""


@dataclass
class SessionPlan:
    total_volume: int
    blocks: list[BlockPlan] = field(default_factory=list)

    @property
    def planned_volume(self) -> int:
        return sum(block.volume for block in self.blocks)