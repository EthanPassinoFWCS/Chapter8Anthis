def car(manufacturer, model_name, **car_info):
    car_info["manufacturer"] = manufacturer
    car_info['model_name'] = model_name
    return car_info


print(car("Subaru", "Outback", color="Purple", size="large", cost="30k", date="1995"))

