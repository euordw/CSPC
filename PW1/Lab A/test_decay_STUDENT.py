"""
Tests for the decay simulation.

One complete test is given as a model. Add the two tests described in the
lab handout (a negative-rate test, and a test against the analytical law).
Run with:  pytest -v
"""
import pytest
import numpy as np
import decay
import numpy as np
import pytest
from decay import simulate, simulate_loop


def test_starts_at_N0():
    # at time zero, no atoms have decayed yet
    assert simulate(1000, 0.4)[0] == 1000


# TODO 1: test_rejects_negative_rate
#   Check that calling simulate(...) with a negative lam raises a ValueError.
#   Which pytest tool checks that an error is raised?


# TODO 2: test_matches_law
#   Check that the simulation's AVERAGE over many seeds is close to the
#   physical law  N0 * exp(-lam * t).
#   Which pytest tool compares floating-point values with a tolerance?
import pytest
import numpy as np
# (Faylın yuxarısında importlar və birinci test onsuz da var, sadəcə aşağıdakıları ən sona əlavə et)

def test_negative_rate_raises_error():
    """Test 2: Mənfi dərəcə ValueError qaytarmalıdır"""
    with pytest.raises(ValueError):
        decay.simulate(1000, -0.4)  # Mənfi lambda veririk

def test_average_close_to_theoretical():
    """Test 3: Ortalama N0 * exp(-lambda * t) düsturuna yaxın olmalıdır"""
    N0 = 1000
    lam = 0.4
    dt = 0.05
    steps = 200
    t = steps * dt
    expected = N0 * np.exp(-lam * t)
    
    # Müxtəlif 'seed'lər (başlanğıclar) ilə 100 dəfə yoxlayırıq
    results = []
    for seed in range(100):
        # simulate funksiyası hər addımdakı atom sayını qaytarır, bizə sonuncu lazımdır ([-1])
        result = decay.simulate(N0, lam, dt=dt, steps=steps, seed=seed)[-1]
        results.append(result)
        
    average_result = np.mean(results)
    # Təxmini yaxınlığı (məsələn, 10% toleransla) yoxlayırıq
    assert average_result == pytest.approx(expected, rel=0.1)