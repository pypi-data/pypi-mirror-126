# flake8: noqa
# There's no way to ignore "F401 '...' imported but unused" warnings in this
# module, but to preserve other warnings. So, don't check this module at all.

# Copyright 2020 The HuggingFace Team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import TYPE_CHECKING

from ...file_utils import (
    _LazyModule,
    is_flax_available,
    is_sentencepiece_available,
    is_tf_available,
    is_tokenizers_available,
    is_torch_available,
)


if is_sentencepiece_available():
    from ..t5.tokenization_t5 import T5Tokenizer
else:
    from ...utils.dummy_sentencepiece_objects import T5Tokenizer

MT5Tokenizer = T5Tokenizer

if is_tokenizers_available():
    from ..t5.tokenization_t5_fast import T5TokenizerFast
else:
    from ...utils.dummy_tokenizers_objects import T5TokenizerFast

MT5TokenizerFast = T5TokenizerFast

_import_structure = {
    "configuration_mt5": ["MT5Config"],
}

if is_torch_available():
    _import_structure["modeling_mt5"] = ["MT5EncoderModel", "MT5ForConditionalGeneration", "MT5Model"]

if is_tf_available():
    _import_structure["modeling_tf_mt5"] = ["TFMT5EncoderModel", "TFMT5ForConditionalGeneration", "TFMT5Model"]

if is_flax_available():
    _import_structure["modeling_flax_mt5"] = ["FlaxMT5ForConditionalGeneration", "FlaxMT5Model"]


if TYPE_CHECKING:
    from .configuration_mt5 import MT5Config

    if is_torch_available():
        from .modeling_mt5 import MT5EncoderModel, MT5ForConditionalGeneration, MT5Model

    if is_tf_available():
        from .modeling_tf_mt5 import TFMT5EncoderModel, TFMT5ForConditionalGeneration, TFMT5Model

    if is_flax_available():
        from .modeling_flax_mt5 import FlaxMT5ForConditionalGeneration, FlaxMT5Model

else:
    import sys

    sys.modules[__name__] = _LazyModule(
        __name__,
        globals()["__file__"],
        _import_structure,
        extra_objects={"MT5Tokenizer": MT5Tokenizer, "MT5TokenizerFast": MT5TokenizerFast},
    )
