h = int(input("Enter a hour: "))
m = int(input("Enter a minute: "))
s = int(input("Enter a second: "))

h_m = h * 60
h_m_s = h_m * 60

m_s = m * 60

all = h_m_s + m_s + s
print(all)