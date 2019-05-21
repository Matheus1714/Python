from scipy.interpolate import interp1d

T = [0, 8, 16, 24, 32, 40]
O = [14.621, 11.834, 9.870, 8.418, 7.305, 6.413]

f = interp1d(T, O, kind='cubic')

print(f(27))
print(f(5.98))
print(f(17.34))