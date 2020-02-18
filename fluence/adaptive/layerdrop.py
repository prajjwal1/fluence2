# AUTOGENERATED! DO NOT EDIT! File to edit: layerdrop.ipynb (unless otherwise specified).

__all__ = ['LayerDrop']

# Cell
import torch
from torch import nn

# Cell
class LayerDrop(nn.Module):
    """
    Implements Reducing Transformer Depth on Demand with Structured Dropout (https://arxiv.org/abs/1909.11556)

    Arguments:
        module_list (nn.ModuleList): List from which layers are to dropped.
        layers_to_drop (int): number of layers to drop
    """
    def __init__(self, module_list, layers_to_drop):
        super(LayerDrop, self).__init__()
        self.module_list = module_list
        self.layers_to_drop = layers_to_drop
        self.length = len(module_list)

    def forward(self, feats, mask=None):
        x = torch.randint(0, self.length, (self.layers_to_drop,))
        for index, layer in enumerate(self.module_list):
            if index not in x:
                if not mask:
                    feats = layer(feats)
                else:
                    feats = layer(feats, mask)
        return feats