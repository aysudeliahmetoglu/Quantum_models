from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# 1 qubit ve 1 klasik bit içeren bir kuantum devresi oluştur
qc = QuantumCircuit(1, 1)

# Hadamard kapısı ile qubit'i süperpozisyona al
qc.h(0)

# Ölçüm işlemi
qc.measure(0, 0)

# Kuantum devresini çizdir
print(qc.draw())

# Simülatörü başlat
simulator = AerSimulator()
compiled_circuit = transpile(qc, simulator)

# Simülasyonu çalıştır
result = simulator.run(compiled_circuit).result()

# Sonuçları al ve görselleştir
counts = result.get_counts()
histogram = plot_histogram(counts)

# Histogramı ekranda göster
plt.show()
