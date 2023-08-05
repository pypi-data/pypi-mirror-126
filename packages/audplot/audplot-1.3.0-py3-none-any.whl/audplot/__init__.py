from audplot.core.api import (
    cepstrum,
    confusion_matrix,
    detection_error_tradeoff,
    distribution,
    human_format,
    scatter,
    series,
    signal,
    spectrum,
    waveform,
)


# Disencourage from audfoo import *
__all__ = []


# Dynamically get the version of the installed module
try:
    import pkg_resources
    __version__ = pkg_resources.get_distribution(__name__).version
except Exception:  # pragma: no cover
    pkg_resources = None  # pragma: no cover
finally:
    del pkg_resources
