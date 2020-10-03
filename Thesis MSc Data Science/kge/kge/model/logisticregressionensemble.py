from kge.model.ensemble_model import EnsembleModel
from kge import Config, Dataset
import torch
from torch import nn
from typing import Optional
from kge.model.kge_model import KgeModel
from kge.util import load_checkpoint
from torch import Tensor

from sklearn.utils._testing import ignore_warnings
from sklearn.exceptions import ConvergenceWarning


class LogisticRegressionEnsemble(EnsembleModel):
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

        if len(config.get("logisticregressionensemble.base")) < 3:
            self.aggregate_coef = nn.Parameter(
                torch.tensor([[1.0], [1.0], [0.0]], requires_grad=True)
            )
        elif len(config.get("logisticregressionensemble.base")) < 4:
            self.aggregate_coef = nn.Parameter(
                torch.tensor([[1.0], [1.0], [1.0], [0.0]], requires_grad=True)
            )
        else:
            self.aggregate_coef = nn.Parameter(
                torch.tensor([[1.0], [1.0], [1.0], [1.0], [0.0]], requires_grad=True)
            )
        meta_lr = ""
        if not init_for_load_only:
            # load pretrained meta coefficients
            pretrained_meta_filename = ""

            if self.has_option("meta_optimizer_args.lr"):
                meta_lr = self.get_option("meta_optimizer_args.lr")
            if self.has_option("meta.pretrain.model_filename"):
                pretrained_meta_filename = self.get_option(
                    "meta.pretrain.model_filename"
                )

            def load_pretrained_model(pretrained_filename: str,) -> Optional[KgeModel]:
                if pretrained_filename != "":
                    self.config.log(
                        f"Initializing with meta stored in " f"{pretrained_filename}"
                    )
                    checkpoint = load_checkpoint(pretrained_filename)
                    return KgeModel.create_from(checkpoint)
                return None

            pretrained_meta_model = load_pretrained_model(pretrained_meta_filename)
            if pretrained_meta_model is not None:
                self.aggregate_coef = pretrained_meta_model.aggregate_coef

        from sklearn.linear_model import SGDClassifier

        self.meta_prepared = False
        if self.config.get("freeze_param") == "base":
            if self.num_base != sum(self.aggregate_coef):
                # need to use "warm start" since the meta learner is prepared
                # In this case, use fit, instead of partial_fit
                self.regression = SGDClassifier(warm_start=True, loss="log",)
                self.meta_prepared = True
            else:
                # In this case, use partial fit
                self.regression = SGDClassifier(loss="log",)

    def aggregate(self, score_cat, num_row, num_col):
        # to check if the meta learner is prepared

        one_ = torch.tensor([1.0]).to(self.device)
        if num_col < 0:
            bias = one_.repeat(1, num_row)
        else:
            bias = one_.repeat(1, num_row * num_col)

        scores_predict_manual = torch.cat([score_cat, bias], dim=0)
        score_cat_t = torch.transpose(scores_predict_manual, 0, 1)

        score_mult = torch.mm(score_cat_t, self.aggregate_coef)
        score_sigmoid = torch.sigmoid(score_mult)
        return torch.reshape(score_sigmoid, (num_row, -1))

    def score_sp_po_meta(
        self, s: Tensor, p: Tensor, o: Tensor, entity_subset: Tensor = None
    ) -> Tensor:

        p_long = self.model_base_01.get_p_embedder().embed(p)
        s_long = self.model_base_01.get_s_embedder().embed(s)
        o_long = self.model_base_01.get_o_embedder().embed_all()
        scores_sp = self.model_base_01._scorer.score_emb(
            s_long, p_long, o_long, combine="sp_"
        )
        s_long = self.model_base_01.get_s_embedder().embed_all()
        o_long = self.model_base_01.get_o_embedder().embed(o)
        scores_po = self.model_base_01._scorer.score_emb(
            s_long, p_long, o_long, combine="_po"
        )
        score_1 = torch.reshape(
            torch.cat((self.minmax(scores_sp), self.minmax(scores_po)), dim=1), (1, -1),
        )

        p_long = self.model_base_02.get_p_embedder().embed(p)
        s_long = self.model_base_02.get_s_embedder().embed(s)
        o_long = self.model_base_02.get_o_embedder().embed_all()
        scores_sp = self.model_base_02._scorer.score_emb(
            s_long, p_long, o_long, combine="sp_"
        )
        s_long = self.model_base_02.get_s_embedder().embed_all()
        o_long = self.model_base_02.get_o_embedder().embed(o)
        scores_po = self.model_base_02._scorer.score_emb(
            s_long, p_long, o_long, combine="_po"
        )
        score_2 = torch.reshape(
            torch.cat((self.minmax(scores_sp), self.minmax(scores_po)), dim=1), (1, -1),
        )

        if self.num_base > 2:
            p_long = self.model_base_03.get_p_embedder().embed(p)
            s_long = self.model_base_03.get_s_embedder().embed(s)
            o_long = self.model_base_03.get_o_embedder().embed_all()
            scores_sp = self.model_base_03._scorer.score_emb(
                s_long, p_long, o_long, combine="sp_"
            )
            s_long = self.model_base_03.get_s_embedder().embed_all()
            o_long = self.model_base_03.get_o_embedder().embed(o)
            scores_po = self.model_base_03._scorer.score_emb(
                s_long, p_long, o_long, combine="_po"
            )
            score_3 = torch.reshape(
                torch.cat((self.minmax(scores_sp), self.minmax(scores_po)), dim=1),
                (1, -1),
            )
        if self.num_base > 3:
            p_long = self.model_base_04.get_p_embedder().embed(p)
            s_long = self.model_base_04.get_s_embedder().embed(s)
            o_long = self.model_base_04.get_o_embedder().embed_all()
            scores_sp = self.model_base_04._scorer.score_emb(
                s_long, p_long, o_long, combine="sp_"
            )
            s_long = self.model_base_04.get_s_embedder().embed_all()
            o_long = self.model_base_04.get_o_embedder().embed(o)
            scores_po = self.model_base_04._scorer.score_emb(
                s_long, p_long, o_long, combine="_po"
            )
            score_4 = torch.reshape(
                torch.cat((self.minmax(scores_sp), self.minmax(scores_po)), dim=1),
                (1, -1),
            )
        if self.num_base > 3:
            return torch.cat([score_1, score_2, score_3, score_4], dim=0)
        elif self.num_base > 2:
            return torch.cat([score_1, score_2, score_3], dim=0)
        else:
            return torch.cat([score_1, score_2], dim=0)
