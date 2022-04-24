 # import numpy as np

def emission_factor():
    """ en gco2_eq par km """
    emi = {'car': 259,
           'train': 3.69}
    return emi


def km():
    km = {'car': 5000,
          'train': 20000}
    return km


def update_bc(km, emi):
    """ Cette fonction donne le bilan carbone de nos déplacements cumulés. """
    emi['car'] = 4  # valeur à préciser ; en tco2/km
    emi['train'] = 0.1  # valeur à préciser ; en tco2/km

    co2_car = emi['car']*km['car']
    co2_train = emi['train'] * km['train']

    total_co2 = co2_car + co2_train

    return total_co2


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Notre bilan carbone transport, en gco2 : ", update_bc(km(), emission_factor()))
    print("Nous avons parcouru, en km : ", km())
