class BuildingError(Exception):
    def __str__(self):
        return f"With so much material the house cannot be built"
def check_meterial(amout_of_material, limit_value ):
    if amout_of_material > limit_value:
        return "Enough material"
    else:
        raise BuildingError(amout_of_material)

material = 123
check_meterial(material, 300)   