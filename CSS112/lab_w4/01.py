

def mosteller (weight, height):
    mosteller = ((weight*height)**0.5) / 60
    return mosteller

def du_bois (weight, height):
    du_bois = 0.007184 * (weight**0.425) * (height**0.725)
    return du_bois

def fujimoto (weight, height):
    fujimoto = 0.008883 * (weight**0.444) * (height**0.663)
    return fujimoto

def main ():
    weight = float(input())
    height = float(input())
    mosteller = ((weight*height)**0.5) / 60
    du_bois = 0.007184 * (weight**0.425) * (height**0.725)
    fujimoto = 0.008883 * (weight**0.444) * (height**0.663)
    print("Mosteller =", round(mosteller, 5))
    print("Du Bois =", round(du_bois, 5))
    print("Fujimoto =", round(fujimoto, 5))


exec(input())