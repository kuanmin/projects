from kge.model.ensemble_model import EnsembleModel
from kge import Config, Dataset
import torch


class AverageEnsemble(EnsembleModel):
    def __init__(
        self,
        config: Config,
        dataset: Dataset,
        configuration_key=None,
        init_for_load_only=False,
    ):
        super().__init__(
            config=config,
            dataset=dataset,
            configuration_key=configuration_key,
            init_for_load_only=init_for_load_only,
        )

        if self.num_base < 3:
            self.aggregate_coef = torch.tensor(
                [[1 / self.num_base], [1 / self.num_base],], requires_grad=False,
            ).to(self.device)
        elif self.num_base < 4:
            self.aggregate_coef = torch.tensor(
                [[1 / self.num_base], [1 / self.num_base], [1 / self.num_base],],
                requires_grad=False,
            ).to(self.device)
        else:
            self.aggregate_coef = torch.tensor(
                [
                    [1 / self.num_base],
                    [1 / self.num_base],
                    [1 / self.num_base],
                    [1 / self.num_base],
                ],
                requires_grad=False,
            ).to(self.device)

    def aggregate(self, score_cat, num_row, num_col):
        import torch

        score_cat_t = torch.transpose(score_cat, 0, 1)
        score_mult = torch.mm(score_cat_t, self.aggregate_coef)

        return torch.reshape(score_mult, (num_row, -1))
