class Cell:
  def __init__(self, volume_mcm3, weight_ng):
    self.volume_mcm3 = volume_mcm3
    self.weight_ng = weight_ng
    self.is_alive = True

  def density(self):
    return float(self.weight_ng/self.volume_mcm3) * 0.001

  def mitosis(self):
    daughter_volume = self.volume_mcm3/2
    daughter_weight = self.weight_ng/2

    daughter_cell_a = Cell(volume_mcm3=daughter_volume, weight_ng=daughter_weight)
    daughter_cell_b = Cell(volume_mcm3=daughter_volume, weight_ng=daughter_weight)

    self.is_alive = False
    
    return daughter_cell_a, daughter_cell_b

  def consume(self, prey_cell):
    self.volume_mcm3 += prey_cell.volume_mcm3
    self.weight_ng += prey_cell.weight_ng

    prey_cell.volume_mcm3 = 0.0
    prey_cell.weight_ng = 0.0
    prey_cell.is_alive = False