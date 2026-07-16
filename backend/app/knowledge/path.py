from dataclasses import dataclass, field

@dataclass
class KnowledgePath:

    objective: object

    methods: list = field(default_factory=list)

    stimuli: list = field(default_factory=list)

    blocks: list = field(default_factory=list)

    exercises: list = field(default_factory=list)