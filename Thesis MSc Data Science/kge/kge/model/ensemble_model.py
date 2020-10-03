from kge import Config, Dataset
from kge.model.kge_model import KgeModel
from torch import Tensor
import torch
import torch.nn.functional as F


class EnsembleModel(KgeModel):
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
            scorer=None,
            configuration_key=configuration_key,
            init_for_load_only=init_for_load_only,
        )
        # since the droping out from each base learner
        # will cause the highly unstable scores used to train the meta learners,
        # we assign all the dropout rates of base learners to zeros
        def dropout_zero(config):
            try:
                config.set("complex.entity_embedder.dropout", 0.0)
            except:
                pass
            try:
                config.set("complex.relation_embedder.dropout", 0.0)
            except:
                pass

            try:
                config.set("distmult.entity_embedder.dropout", 0.0)
            except:
                pass
            try:
                config.set("distmult.relation_embedder.dropout", 0.0)
            except:
                pass
            try:
                config.set("rescal.entity_embedder.dropout", 0.0)
            except:
                pass
            try:
                config.set("rescal.relation_embedder.dropout", 0.0)
            except:
                pass
            try:
                config.set("conve.entity_embedder.dropout", 0.0)
            except:
                pass
            try:
                config.set("conve.relation_embedder.dropout", 0.0)
            except:
                pass

        if config.get("model") == "averageensemble":
            self.num_base = len(config.get("averageensemble.base"))
            self.device: str = self.config.get("job.device")

            config_01_temp = Config()
            config_01_temp.load(config.get("averageensemble.base")[0])
            if config.get("freeze_param") == "base":
                dropout_zero(config_01_temp)
            self.config_01 = config_01_temp
            config_02_temp = Config()
            config_02_temp.load(config.get("averageensemble.base")[1])
            if config.get("freeze_param") == "base":
                dropout_zero(config_02_temp)
            self.config_02 = config_02_temp
            if self.num_base > 2:
                config_03_temp = Config()
                config_03_temp.load(config.get("averageensemble.base")[2])
                if config.get("freeze_param") == "base":
                    dropout_zero(config_03_temp)
                self.config_03 = config_03_temp
            if self.num_base > 3:
                config_04_temp = Config()
                config_04_temp.load(config.get("averageensemble.base")[3])
                if config.get("freeze_param") == "base":
                    dropout_zero(config_04_temp)
                self.config_04 = config_04_temp
        else:
            self.num_base = len(config.get("logisticregressionensemble.base"))
            self.device: str = self.config.get("job.device")

            config_01_temp = Config()
            config_01_temp.load(config.get("logisticregressionensemble.base")[0])
            if config.get("freeze_param") == "base":
                dropout_zero(config_01_temp)
            self.config_01 = config_01_temp
            config_02_temp = Config()
            config_02_temp.load(config.get("logisticregressionensemble.base")[1])
            if config.get("freeze_param") == "base":
                dropout_zero(config_02_temp)
            self.config_02 = config_02_temp
            if self.num_base > 2:
                config_03_temp = Config()
                config_03_temp.load(config.get("logisticregressionensemble.base")[2])
                if config.get("freeze_param") == "base":
                    dropout_zero(config_03_temp)
                self.config_03 = config_03_temp
            if self.num_base > 3:
                config_04_temp = Config()
                config_04_temp.load(config.get("logisticregressionensemble.base")[3])
                if config.get("freeze_param") == "base":
                    dropout_zero(config_04_temp)
                self.config_04 = config_04_temp

        self.model_base_01: KgeModel = KgeModel.create(self.config_01, dataset)
        self.model_base_02: KgeModel = KgeModel.create(self.config_02, dataset)
        if self.num_base > 2:
            self.model_base_03: KgeModel = KgeModel.create(self.config_03, dataset)
        if self.num_base > 3:
            self.model_base_04: KgeModel = KgeModel.create(self.config_04, dataset)

    def aggregate(self, score_cat, num_row, num_col):

        r"""different calculations for different cases

        """

    def prepare_job(self, job: "Job", **kwargs):
        if self.num_base > 3:
            self.model_base_01.prepare_job(job, **kwargs)
            self.model_base_02.prepare_job(job, **kwargs)
            self.model_base_03.prepare_job(job, **kwargs)
            self.model_base_04.prepare_job(job, **kwargs)
        elif self.num_base > 2:
            self.model_base_01.prepare_job(job, **kwargs)
            self.model_base_02.prepare_job(job, **kwargs)
            self.model_base_03.prepare_job(job, **kwargs)
        else:
            self.model_base_01.prepare_job(job, **kwargs)
            self.model_base_02.prepare_job(job, **kwargs)

    def penalty(self, **kwargs):
        value_1 = []
        value_2 = []
        value_3 = []
        name_1_store = True
        name_2_store = True
        name_3_store = True

        penalty_01 = self.model_base_01.penalty(**kwargs)
        if penalty_01 == []:
            value_1.append(0)
            value_2.append(0)
            value_3.append(0)
        else:
            value_1_temp = 0
            value_2_temp = 0
            value_3_temp = 0

            for index, (penalty_key, penalty_value_torch) in enumerate(penalty_01):
                if index % 3 == 0:
                    if name_1_store:
                        name_1 = penalty_key
                        name_1_store = False
                    value_1_temp += penalty_value_torch
                elif index % 3 == 1:
                    if name_2_store:
                        name_2 = penalty_key
                        name_2_store = False
                    value_2_temp += penalty_value_torch
                else:
                    if name_3_store:
                        name_3 = penalty_key
                        name_3_store = False
                    value_3_temp += penalty_value_torch
            value_1.append(value_1_temp)
            value_2.append(value_2_temp)
            value_3.append(value_3_temp)

        penalty_02 = self.model_base_02.penalty(**kwargs)
        if penalty_02 == []:
            value_1.append(0)
            value_2.append(0)
            value_3.append(0)
        else:
            value_1_temp = 0
            value_2_temp = 0
            value_3_temp = 0

            for index, (penalty_key, penalty_value_torch) in enumerate(penalty_02):
                if index % 3 == 0:
                    if name_1_store:
                        name_1 = penalty_key
                        name_1_store = False
                    value_1_temp += penalty_value_torch
                elif index % 3 == 1:
                    if name_2_store:
                        name_2 = penalty_key
                        name_2_store = False
                    value_2_temp += penalty_value_torch
                else:
                    if name_3_store:
                        name_3 = penalty_key
                        name_3_store = False
                    value_3_temp += penalty_value_torch
            value_1.append(value_1_temp)
            value_2.append(value_2_temp)
            value_3.append(value_3_temp)

        if self.num_base > 2:
            penalty_03 = self.model_base_03.penalty(**kwargs)
            if penalty_03 == []:
                value_1.append(0)
                value_2.append(0)
                value_3.append(0)
            else:
                value_1_temp = 0
                value_2_temp = 0
                value_3_temp = 0

                for index, (penalty_key, penalty_value_torch) in enumerate(penalty_03):
                    if index % 3 == 0:
                        if name_1_store:
                            name_1 = penalty_key
                            name_1_store = False
                        value_1_temp += penalty_value_torch
                    elif index % 3 == 1:
                        if name_2_store:
                            name_2 = penalty_key
                            name_2_store = False
                        value_2_temp += penalty_value_torch
                    else:
                        if name_3_store:
                            name_3 = penalty_key
                            name_3_store = False
                        value_3_temp += penalty_value_torch
                value_1.append(value_1_temp)
                value_2.append(value_2_temp)
                value_3.append(value_3_temp)

        if self.num_base > 3:
            penalty_04 = self.model_base_04.penalty(**kwargs)
            if penalty_04 == []:
                value_1.append(0)
                value_2.append(0)
                value_3.append(0)
            else:
                value_1_temp = 0
                value_2_temp = 0
                value_3_temp = 0

                for index, (penalty_key, penalty_value_torch) in enumerate(penalty_04):
                    if index % 3 == 0:
                        if name_1_store:
                            name_1 = penalty_key
                            name_1_store = False
                        value_1_temp += penalty_value_torch
                    elif index % 3 == 1:
                        if name_2_store:
                            name_2 = penalty_key
                            name_2_store = False
                        value_2_temp += penalty_value_torch
                    else:
                        if name_3_store:
                            name_3 = penalty_key
                            name_3_store = False
                        value_3_temp += penalty_value_torch
                value_1.append(value_1_temp)
                value_2.append(value_2_temp)
                value_3.append(value_3_temp)

        # weighted sum
        index_0 = 0
        for i in range(len(value_1)):
            index_0 += abs(value_1[i])

        if index_0 == 0 or index_0 is None:
            return []
        else:
            value_1_sum = 0
            value_2_sum = 0
            value_3_sum = 0
            if self.config.get("model") == "logisticregressionensemble":
                # weighted summing up
                for i in range(self.num_base):
                    value_1_sum += (
                        value_1[i] * self.aggregate_coef[i] / sum(self.aggregate_coef)
                    )
                    value_2_sum += (
                        value_2[i] * self.aggregate_coef[i] / sum(self.aggregate_coef)
                    )
                    value_3_sum += (
                        value_3[i] * self.aggregate_coef[i] / sum(self.aggregate_coef)
                    )
            else:
                for i in range(self.num_base):
                    value_1_sum += (
                        value_1[i] * self.aggregate_coef[i] / sum(self.aggregate_coef)
                    )
                    value_2_sum += (
                        value_2[i] * self.aggregate_coef[i] / sum(self.aggregate_coef)
                    )
                    value_3_sum += (
                        value_3[i] * self.aggregate_coef[i] / sum(self.aggregate_coef)
                    )

            penalty_agg = [
                (name_1, value_1_sum),
                (name_2, value_2_sum),
                (name_3, value_3_sum),
            ]
            return penalty_agg

    @torch.no_grad()
    def minmax(self, matrix):
        for j in range(len(matrix)):
            from sklearn.preprocessing import MinMaxScaler

            scaler = MinMaxScaler()
            import numpy

            data = numpy.transpose(
                numpy.array(matrix[j].to(torch.device("cpu")))
            ).reshape(-1, 1)
            scaler.fit(data)
            matrix[j] = torch.from_numpy(
                numpy.transpose(scaler.transform(data).reshape(-1))
            )
        return matrix

    def score_spo(self, s: Tensor, p: Tensor, o: Tensor, direction=None) -> Tensor:
        score_1 = self.model_base_01.score_spo(s, p, o, direction)
        num_row = len(score_1)
        num_col = -1
        score_2 = self.model_base_02.score_spo(s, p, o, direction)
        if self.num_base > 2:
            score_3 = self.model_base_03.score_spo(s, p, o, direction)
        if self.num_base > 3:
            score_4 = self.model_base_04.score_spo(s, p, o, direction)
        if self.num_base > 3:
            score_cat_pri = torch.cat(
                [
                    torch.reshape(score_1, (-1, 1)),
                    torch.reshape(score_2, (-1, 1)),
                    torch.reshape(score_3, (-1, 1)),
                    torch.reshape(score_4, (-1, 1)),
                ],
                dim=1,
            )
            score_cat = torch.transpose(score_cat_pri, 0, 1)
            return self.aggregate(score_cat, num_row, num_col)
        elif self.num_base > 2:
            score_cat_pri = torch.cat(
                [
                    torch.reshape(score_1, (-1, 1)),
                    torch.reshape(score_2, (-1, 1)),
                    torch.reshape(score_3, (-1, 1)),
                ],
                dim=1,
            )
            score_cat = torch.transpose(score_cat_pri, 0, 1)
            return self.aggregate(score_cat, num_row, num_col)
        else:
            score_cat_pri = torch.cat(
                [torch.reshape(score_1, (-1, 1)), torch.reshape(score_2, (-1, 1))],
                dim=1,
            )
            score_cat = torch.transpose(score_cat_pri, 0, 1)
            return self.aggregate(score_cat, num_row, num_col)

    def score_sp(self, s: Tensor, p: Tensor, o: Tensor = None) -> Tensor:
        score_1_temp = self.model_base_01.score_sp(s, p, o=None)
        num_row = len(score_1_temp)
        num_col = len(score_1_temp[0])
        score_1 = torch.reshape(self.minmax(score_1_temp), (1, -1))
        score_2 = torch.reshape(
            self.minmax(self.model_base_02.score_sp(s, p, o=None)), (1, -1)
        )
        if self.num_base > 2:
            score_3 = torch.reshape(
                self.minmax(self.model_base_03.score_sp(s, p, o=None)), (1, -1)
            )
        if self.num_base > 3:
            score_4 = torch.reshape(
                self.minmax(self.model_base_04.score_sp(s, p, o=None)), (1, -1)
            )
        if self.num_base > 3:
            score_cat = torch.cat([score_1, score_2, score_3, score_4], dim=0)
            return self.aggregate(score_cat, num_row, num_col)
        elif self.num_base > 2:
            score_cat = torch.cat([score_1, score_2, score_3], dim=0)
            return self.aggregate(score_cat, num_row, num_col)
        else:
            score_cat = torch.cat([score_1, score_2], dim=0)
            return self.aggregate(score_cat, num_row, num_col)

    def score_po(self, p: Tensor, o: Tensor, s: Tensor = None) -> Tensor:
        score_1_temp = self.model_base_01.score_po(p, o, s=None)
        num_row = len(score_1_temp)
        num_col = len(score_1_temp[0])
        score_1 = torch.reshape(self.minmax(score_1_temp), (1, -1))
        score_2 = torch.reshape(
            self.minmax(self.model_base_02.score_po(p, o, s=None)), (1, -1)
        )
        if self.num_base > 2:
            score_3 = torch.reshape(
                self.minmax(self.model_base_03.score_po(p, o, s=None)), (1, -1)
            )
        if self.num_base > 3:
            score_4 = torch.reshape(
                self.minmax(self.model_base_04.score_po(p, o, s=None)), (1, -1)
            )
        if self.num_base > 3:
            score_cat = torch.cat([score_1, score_2, score_3, score_4], dim=0)
            return self.aggregate(score_cat, num_row, num_col)
        elif self.num_base > 2:
            score_cat = torch.cat([score_1, score_2, score_3], dim=0)
            return self.aggregate(score_cat, num_row, num_col)
        else:
            score_cat = torch.cat([score_1, score_2], dim=0)
            return self.aggregate(score_cat, num_row, num_col)

    def score_so(self, s: Tensor, o: Tensor, p: Tensor = None) -> Tensor:

        num_row = len(self.model_base_01.score_so(s, o, p=None))
        num_col = len(self.model_base_01.score_so(s, o, p=None)[0])
        score_1 = torch.reshape(
            self.minmax(self.model_base_01.score_so(s, o, p=None)), (1, -1)
        )
        score_2 = torch.reshape(
            self.minmax(self.model_base_02.score_so(s, o, p=None)), (1, -1)
        )
        if self.num_base > 2:
            score_3 = torch.reshape(
                self.minmax(self.model_base_03.score_so(s, o, p=None)), (1, -1)
            )
        if self.num_base > 3:
            score_4 = torch.reshape(
                self.minmax(self.model_base_04.score_so(s, o, p=None)), (1, -1)
            )
        if self.num_base > 3:
            score_cat = torch.cat([score_1, score_2, score_3, score_4], dim=0)
            return self.aggregate(score_cat, num_row, num_col)
        elif self.num_base > 2:
            score_cat = torch.cat([score_1, score_2, score_3], dim=0)
            return self.aggregate(score_cat, num_row, num_col)
        else:
            score_cat = torch.cat([score_1, score_2], dim=0)
            return self.aggregate(score_cat, num_row, num_col)

    def score_sp_po(
        self, s: Tensor, p: Tensor, o: Tensor, entity_subset: Tensor = None
    ) -> Tensor:

        p_long = self.model_base_01.get_p_embedder().embed(p)
        s_long = self.model_base_01.get_s_embedder().embed(s)
        o_long = self.model_base_01.get_o_embedder().embed_all()
        scores_sp = self.model_base_01._scorer.score_emb(
            s_long, p_long, o_long, combine="sp_"
        )
        num_row = len(scores_sp)
        num_col = len(scores_sp[0]) * 2
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
            score_cat = torch.cat([score_1, score_2, score_3, score_4], dim=0)
            return self.aggregate(score_cat, num_row, num_col)
        elif self.num_base > 2:
            score_cat = torch.cat([score_1, score_2, score_3], dim=0)
            return self.aggregate(score_cat, num_row, num_col)
        else:
            score_cat = torch.cat([score_1, score_2], dim=0)
            return self.aggregate(score_cat, num_row, num_col)
