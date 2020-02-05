# -*- coding: utf-8 -*-
from typing import Dict, List, Tuple
import numpy as np

from yacs.config import CfgNode

import torch
from torch import optim

from videoanalyst.evaluation.got_benchmark.datasets import got10k
from videoanalyst.data.dataset.dataset_base import DatasetBase
from ..optimizer_base import TRACK_OPTIMIZERS, OptimizerBase

@TRACK_OPTIMIZERS.register
class SGD(OptimizerBase):
    r"""
    Tracking data sampler

    Hyper-parameters
    ----------------
    """
    default_hyper_params = dict(
        lr=0.1,
        momentum=0.9,
        weight_decay=0.00005,
    )

    def __init__(self, cfg: CfgNode) -> None:
        super(SGD, self).__init__(cfg)

    def build_optimizer(self):
        super(SGD, self).build_optimizer()
        if self._param_groups_divider is not None:
            params = self._param_groups_divider(self._model)
        else:
            params = self._model.parameters()

        kwargs = self._hyper_params
        self._optimizer = optim.SGD(params, **kwargs)