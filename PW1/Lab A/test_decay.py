import numpy as np
import pytest
from decay import simulate

def test_starts_at_N0():
    assert simulate(1000, 0.4)[0] == 1000

def test_rejects_negative_rate():
    with pytest.raises(ValueError):
        simulate(1000, -0.4)

def test_average_decay_matches_theory():
    N0, lam = 1000, 0.4
    runs = [simulate(N0, lam) for _ in range(50)]
    avg_len = np.mean([len(r) for r in runs])
    assert avg_len == pytest.approx(200, abs=50)