# src.py

class Cell:
    def __init__(self, volume_mcm3, mass_ng):
        self.volume_mcm3 = volume_mcm3
        self.mass_ng = mass_ng
        self.is_alive = True

    def density(self):
        return round(self.mass_ng / self.volume_mcm3, 3)

    def mitosis(self):
        self.is_alive = False
        daughter_volume = self.volume_mcm3 / 2.0
        daughter_mass = self.mass_ng / 2.0
        daughter_cell_a = Cell(daughter_volume, daughter_mass)
        daughter_cell_b = Cell(daughter_volume, daughter_mass)
        return (daughter_cell_a, daughter_cell_b)

    def consume(self, prey_cell):
        if prey_cell.is_alive:
            self.volume_mcm3 += prey_cell.volume_mcm3
            self.mass_ng += prey_cell.mass_ng
            prey_cell.is_alive = False
            prey_cell.volume_mcm3 = 0.0
            prey_cell.mass_ng = 0.0