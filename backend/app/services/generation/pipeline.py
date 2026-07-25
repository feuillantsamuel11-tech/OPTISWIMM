from .result import GenerationResult


class GenerateSessionPipeline:

    def __init__(
        self,
        decision_engine,
        planner,
        repository,
        ranking_engine,
        selector,
        block_builder,
        validator,
        explanation_engine,
    ):

        self.decision_engine = decision_engine
        self.planner = planner
        self.repository = repository
        self.ranking_engine = ranking_engine
        self.selector = selector
        self.block_builder = block_builder
        self.validator = validator
        self.explanation_engine = explanation_engine

    def generate(
        self,
        athlete,
        context,
    ):

        decision = self._decision(
            athlete,
            context,
        )


        planning = self._planning(
            decision,
        )

        exercises = self._repository(
            planning,
        )

        ranking = self._ranking(
            exercises,
            decision,
        )

        selection = self._selection(
            ranking,
            planning,
        )

        blocks = self._build_blocks(
            selection,
            planning,
        )

        validation = self._validate(
            blocks,
            decision,
        )

        explanation = self._explain(
            blocks,
            validation,
            decision,
        )

        return GenerationResult(
            session=blocks,
            validation=validation,
            explanation=explanation,
            decision=decision,
            planner=planning,
        )
    def _decision(
        self,
        athlete,
        context,
    ):
        return self.decision_engine.decide(
            athlete=athlete,
            context=context,
        )

    def _planning(
        self,
        decision,
    ):
        return self.planner.generate(
            volume=decision.target_volume,
            decision=decision,
        )
    def _repository(
        self,
        planning,
    ):
        return self.repository.find(
            planning,
        )

    def _ranking(
        self,
        exercises,
        decision,
    ):
        return self.ranking_engine.rank(
            exercises,
            decision,
        )
    def _selection(
        self,
        ranking,
        planning,
    ):
        return self.selector.select(
            ranking,
            planning,
        )

    def _build_blocks(
        self,
        selection,
        planning,
    ):
        return self.block_builder.build(
            selection,
            planning,
        )

    def _validate(
        self,
        blocks,
        decision,
    ):
        return self.validator.validate(
            blocks,
            objective=decision.objectives[0],
        )

    def _explain(
        self,
        blocks,
        validation,
        decision,
    ):
        return self.explanation_engine.explain(
            session=blocks,
            validation=validation,
            decision=decision,
        )