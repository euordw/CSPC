import time
import decay

N0 = 200000  # 200 min atom
lam = 0.4

print(f"{N0} atom üçün simulyasiya başlayır...\n")

# 1. Adi Python dövrünün (loop) vaxtını ölçürük
start_time = time.perf_counter()
decay.simulate_loop(N0, lam)
end_time = time.perf_counter()
loop_time = end_time - start_time
print(f"Python dövrü (loop) vaxtı: {loop_time:.4f} saniyə")

# 2. NumPy versiyasının vaxtını ölçürük
start_time = time.perf_counter()
decay.simulate(N0, lam)
end_time = time.perf_counter()
numpy_time = end_time - start_time
print(f"NumPy vaxtı: {numpy_time:.4f} saniyə")

# 3. Nəticələri müqayisə edirik
speedup = loop_time / numpy_time
print(f"\nNəticə: NumPy versiyası {speedup:.1f} dəfə daha sürətlidir!")