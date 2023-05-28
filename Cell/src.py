
class Cell:
    def __init__(self, volume_mcm3, weight_ng):
        self.volume_mcm3 = volume_mcm3
        self.weight_ng = weight_ng
        self.is_alive = True

    def density(self):
        return self.weight_ng / self.volume_mcm3

    def mitosis(self):
        new_volume = self.volume_mcm3/2
        new_weight = self.weight_ng/2
        new_cell = Cell(volume_mcm3= new_volume,
                        weight_ng= new_weight)
        return new_cell

    def consume(self, prey_cell):
        self.volume_mcm3 += prey_cell.volume_mcm3
        self.weight_ng += prey_cell.weight_ng
        prey_cell.volume_mcm3, prey_cell.weight_ng, prey_cell.is_alive = 0, 0, False
