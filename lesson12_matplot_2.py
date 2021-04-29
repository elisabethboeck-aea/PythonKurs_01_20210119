import matplotlib.pyplot as plt
import numpy as np

# Hausübung: Plots erstellen aus API/DB/eigenen Daten, verarbeiten, aufbereiten, plotten

xpoints = np.array([1, 3, 6, 9, 14, 24])
ypoints = np.array([3, 8, 1, 10, 5, 8])

# plt.plot(xpoints, ypoints) # zeichnet die linie
# plt.plot(xpoints, ypoints, 'D-.g') # o markiert punkte, : macht strichlierte linie, m ist die farbe magenta, * macht stern-marker, y ist yellow, - dünne linie, siehe definitionen von matplot https://matplotlib.org/stable/gallery/color/named_colors.html
plt.plot(xpoints, ypoints, 'D', ms=20, mec='g', mfc='#4CAF50') # Langschreibweise, ms= markersize, mec = marker edge colour, ...
# plt.plot(ypoints) # werden keine x-Punkte übergeben, versucht das script, automatisch x-punkte zu vergeben (0, 1, 2, 3 ...)



plt.show()